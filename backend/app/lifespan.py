from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.db import init_db
from app.core.redis import close_redis, create_redis

redis_client = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global redis_client

    redis_client = await create_redis()
    app.state.redis = redis_client

    await init_db()
    yield
    await close_redis(redis_client)
