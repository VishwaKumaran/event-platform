from contextlib import asynccontextmanager

import redis.asyncio as redis


async def create_redis_client(redis_url: str, **kwargs):
    return redis.from_url(redis_url, decode_responses=True, **kwargs)


async def close_redis_client(client: redis.Redis):
    await client.close()


@asynccontextmanager
async def redis_lifespan(redis_url: str, **kwargs):
    client = await create_redis_client(redis_url, **kwargs)
    try:
        yield client
    finally:
        await close_redis_client(client)
