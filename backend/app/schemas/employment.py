from typing import Optional

from pydantic import BaseModel


class EmploymentBase(BaseModel):
    employment: str
    hours_per_week: int
    hours_per_day: Optional[int] = 8


class EmploymentCreate(EmploymentBase):
    pass


class EmploymentUpdate(EmploymentBase):
    pass


class EmploymentInDBBase(EmploymentBase):
    id: int
    employment: str
    hours_per_week: int
    hours_per_day: Optional[int] = 8

    class Config:
        orm_mode = True


class Employment(EmploymentInDBBase):
    pass


class EmploymentInDB(EmploymentInDBBase):
    pass
