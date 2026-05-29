import redis.asyncio as redis
from fastapi import Request
from lib import close_redis_client, create_redis_client

from app.core.config import settings


async def create_redis():
    return await create_redis_client(settings.REDIS_URL, socket_timeout=10)


async def close_redis(redis_client: redis.Redis):
    await close_redis_client(redis_client)


async def get_redis(request: Request) -> redis.Redis:
    return request.app.state.redis
