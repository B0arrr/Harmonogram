from fastapi import APIRouter

from app.api.api_v1.endpoints import positions

api_router = APIRouter()

api_router.include_router(positions.router, tags=["api"])
