from fastapi import APIRouter, Depends

from app.core.redis import get_redis
from app.schemas.events import EventSchema
from app.services.events import publish_event

router = APIRouter(prefix="/events")


@router.post("")
async def create_event(event: EventSchema, redis=Depends(get_redis)):
    return publish_event(redis, event.model_dump())
