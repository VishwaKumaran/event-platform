from fastapi import APIRouter
from app.routers.auth.routes import router as auth_router
from app.routers.users.routes import router as user_router
from app.routers.health import router as health_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(user_router)
api_router.include_router(health_router)
