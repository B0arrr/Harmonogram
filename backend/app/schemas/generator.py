import datetime
from typing import List

from pydantic import BaseModel

from app.schemas import employee


class ScheduleForEveryone(BaseModel):
    day: datetime.date
    employees: List[employee.EmployeeDisplay]


class GeneratedSchedule(BaseModel):
    schedules: List[ScheduleForEveryone]


class ScheduleForEmployee(BaseModel):
    day: datetime.date
    employee: employee.EmployeeDisplay
    shift: int


class GeneratedScheduleForEmployee(BaseModel):
    schedules: List[ScheduleForEmployee]
