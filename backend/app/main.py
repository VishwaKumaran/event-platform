from fastapi import FastAPI
from app.core.redis import init_redis, close_redis

from app.core.config import settings
from app.core.exceptions import setup_exception_handlers
from app.routers.main import api_router



from contextlib import asynccontextmanager
from app.core.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_redis()
    await init_db()
    yield
    await close_redis()

app = FastAPI(
    title=settings.PROJECT_NAME, debug=settings.DEBUG, root_path=settings.API_V1
, lifespan=lifespan)

setup_exception_handlers(app)
app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}!"}
