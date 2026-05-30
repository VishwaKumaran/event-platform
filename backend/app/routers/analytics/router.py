from fastapi import APIRouter, Depends, Query
from lib.models import Event
from sqlalchemy import distinct, func, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.core.db import get_session

router = APIRouter()


@router.get("/stats/overview")
async def get_overview(session: AsyncSession = Depends(get_session)):
    # total_events
    total_events_query = select(func.count(Event.id))
    total_events = (await session.execute(total_events_query)).scalar() or 0

    # active_users
    active_users_query = select(func.count(distinct(Event.user_id)))
    active_users = (await session.execute(active_users_query)).scalar() or 0

    # top_event_type
    top_event_query = (
        select(Event.event_type, func.count(Event.id).label("count"))
        .group_by(Event.event_type)
        .order_by(func.count(Event.id).desc())
        .limit(1)
    )
    top_event_result = (await session.execute(top_event_query)).first()

    return {
        "total_events": total_events,
        "active_users": active_users,
        "top_event_type": top_event_result[0] if top_event_result else None,
    }


@router.get("/metrics/event-types")
async def get_event_types(session: AsyncSession = Depends(get_session)):
    query = select(Event.event_type, func.count(Event.id).label("count")).group_by(
        Event.event_type
    )
    results = (await session.execute(query)).all()
    return [{"event_type": row[0], "count": row[1]} for row in results]


@router.get("/events")
async def get_events(
    limit: int = Query(default=100, le=1000),
    session: AsyncSession = Depends(get_session),
):
    query = select(Event).order_by(Event.timestamp.desc()).limit(limit)
    events = (await session.execute(query)).scalars().all()
    return events


@router.get("/metrics/events-per-minute")
async def get_events_per_minute(session: AsyncSession = Depends(get_session)):
    # time_bucket is TimescaleDB specific.
    query = text("""
        SELECT
            time_bucket('1 minute', timestamp) AS bucket,
            count(*)
        FROM event
        GROUP BY bucket
        ORDER BY bucket DESC
        LIMIT 60;
    """)
    result = await session.execute(query)
    return [{"bucket": row[0], "count": row[1]} for row in result]
