from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.core.db import get_session
from app.core.redis import get_redis

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
async def health_check():
    return {"status": "ok"}


@router.get("/db")
async def database_health(session: AsyncSession = Depends(get_session)):
    try:
        await session.execute(text("SELECT 1"))
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database not reachable: {e}")
    return {"status": "ok", "database": "reachable"}


@router.get("/redis")
async def redis_health(redis=Depends(get_redis)):
    return {"status": await redis.ping()}
