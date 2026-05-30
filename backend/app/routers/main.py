from fastapi import APIRouter

from app.routers.analytics.router import router as analytics_router
from app.routers.auth.routes import router as auth_router
from app.routers.events.routes import router as event_router
from app.routers.health import router as health_router
from app.routers.users.router import router as user_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(user_router)
api_router.include_router(health_router)
api_router.include_router(event_router)
api_router.include_router(analytics_router, tags=["analytics"])
