import json

from app.core.config import settings


async def publish_event(redis, event: dict):
    await redis.xadd(settings.REDIS_STREAM, {"data": json.dumps(event, default=str)})
