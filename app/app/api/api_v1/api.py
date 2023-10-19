from fastapi import APIRouter
from app.api.api_v1.endpoints import dummy

api_router = APIRouter()
api_router.include_router(dummy.router,prefix="/dummy",tags=["dummy"])