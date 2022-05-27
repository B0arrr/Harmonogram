import random

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas import ScheduleEmployeeCreate


def create_random_schedule_employee(db: Session) -> models.Schedule_Employee:
    schedule_id = random.randint(1, 100)
    employee_id = random.randint(1, 100)
    shift = random.randint(1, 3)
    schedule_employee_in = ScheduleEmployeeCreate(schedule_id=schedule_id,
                                                  employee_id=employee_id,
                                                  shift=shift)
    return crud.schedule_employee.create(db=db, obj_in=schedule_employee_in)
