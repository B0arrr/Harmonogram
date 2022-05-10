from pydantic import BaseModel


class ScheduleEmployeeBase(BaseModel):
    schedule_id: int
    employee_id: int
    shift: int


class ScheduleEmployeeCreate(ScheduleEmployeeBase):
    pass


class ScheduleEmployeeUpdate(ScheduleEmployeeBase):
    pass


class ScheduleEmployeeInDBBase(ScheduleEmployeeBase):
    id: int
    schedule_id: int
    employee_id: int
    shift: int

    class Config:
        orm_mode = True


class ScheduleEmployee(ScheduleEmployeeInDBBase):
    pass


class ScheduleEmployeeInDB(ScheduleEmployeeInDBBase):
    pass
