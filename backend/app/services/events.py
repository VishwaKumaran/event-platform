import json

from app.core.config import settings


def publish_event(redis, event: dict):
    redis.xadd(settings.REDIS_STREAM, {"data": json.dumps(event, defaut=str)})
