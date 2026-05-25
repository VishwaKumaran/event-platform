from contextlib import asynccontextmanager

import redis.asyncio as redis

from core.config import settings


async def create_redis():
    return redis.from_url(settings.REDIS_URL, decode_responses=True)


async def close_redis(client: redis.Redis):
    await client.close()


@asynccontextmanager
async def redis_lifespan():
    client = await create_redis()

    try:
        yield client

    finally:
        await close_redis(client)
