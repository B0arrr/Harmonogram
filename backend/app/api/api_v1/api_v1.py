from fastapi import APIRouter

from app.api.api_v1.endpoints import positions, employments, employees, schedules, schedule_employees

api_router = APIRouter()

api_router.include_router(positions.router, tags=["position"])
api_router.include_router(employments.router, tags=["employment"])
api_router.include_router(employees.router, tags=["employee"])
api_router.include_router(schedules.router, tags=["schedule"])
api_router.include_router(schedule_employees.router, tags=["schedule_employee"])
