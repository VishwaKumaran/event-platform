from fastapi import Request

import redis.asyncio as redis

from app.core.config import settings


async def create_redis():
    return redis.from_url(settings.REDIS_URL, decode_responses=True)


async def close_redis(redis_client: redis.Redis)
    await redis_client.close()


async def get_redis(request: Request) -> redis.Redis:
    return request.app.state.redis
