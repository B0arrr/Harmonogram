from fastapi import APIRouter

from app.api.api_v1.endpoints import positions, employments

api_router = APIRouter()

api_router.include_router(positions.router, tags=["position"])
api_router.include_router(employments.router, tags=["employment"])
