from fastapi import APIRouter

from backend.app.api.endpoints import items

api_router = APIRouter()

api_router.include_router(items.router, tags=["api"])
