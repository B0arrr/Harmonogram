from typing import Optional

from pydantic import BaseModel, EmailStr


class EmployeeBase(BaseModel):
    name: str
    surname: str
    email: EmailStr
    employment_id: int
    position_id: int
    is_active: Optional[bool] = True
    is_superuser: bool = False


class EmployeeCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    employment_id: int
    position_id: int
    login: str
    password: str


class EmployeeUpdate(BaseModel):
    login: Optional[str] = None
    password: Optional[str] = None


class EmployeeInDBBase(EmployeeBase):
    id: int

    class Config:
        orm_mode = True


class Employee(EmployeeInDBBase):
    login: Optional[str] = None
    password: Optional[str] = None
