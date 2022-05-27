import random

from sqlalchemy.orm import Session

from app import crud
from app.schemas import ScheduleEmployeeCreate
from app.tests.utils.schedule_employee import create_random_schedule_employee


def test_create_schedule_employee(db: Session):
    schedule_id = random.randint(1, 100)
    employee_id = random.randint(1, 100)
    shift = random.randint(1, 3)
    schedule_employee_in = ScheduleEmployeeCreate(schedule_id=schedule_id,
                                                  employee_id=employee_id,
                                                  shift=shift)
    schedule_employee = crud.schedule_employee.create(db=db, obj_in=schedule_employee_in)
    assert schedule_employee
    assert schedule_employee_in.schedule_id == schedule_employee.schedule_id
    assert schedule_employee_in.employee_id == schedule_employee.employee_id
    assert schedule_employee_in.shift == schedule_employee.shift


def test_get_schedule_employee_by_ids(db: Session):
    schedule_employee_new = create_random_schedule_employee(db=db)
    schedule_employee = crud.schedule_employee.get_by_ids(db=db,
                                                          schedule_id=schedule_employee_new.schedule_id,
                                                          employee_id=schedule_employee_new.employee_id)
    assert schedule_employee
    assert schedule_employee_new.schedule_id == schedule_employee.schedule_id
    assert schedule_employee_new.employee_id == schedule_employee.employee_id
    assert schedule_employee_new.shift == schedule_employee.shift
