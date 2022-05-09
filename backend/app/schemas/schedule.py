import datetime
from typing import Optional

from pydantic import BaseModel


class ScheduleBase(BaseModel):
    day: datetime.date
    day_off: Optional[bool]


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleUpdate(ScheduleBase):
    pass


class ScheduleInDBBase(ScheduleBase):
    id: int
    day: datetime.date
    day_off: Optional[bool]

    class Config:
        orm_mode = True


class Schedule(ScheduleInDBBase):
    pass


class ScheduleInDB(ScheduleInDBBase):
    pass
