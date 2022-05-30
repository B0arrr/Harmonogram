import random

from sqlalchemy.orm import Session

from app import crud
from app.schemas import ScheduleEmployeeCreate, ScheduleEmployeeUpdate
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


def test_update_schedule_employee_by_ids(db: Session):
    schedule_employee_new = create_random_schedule_employee(db=db)
    schedule_employee_in = ScheduleEmployeeUpdate(schedule_id=schedule_employee_new.schedule_id,
                                                  employee_id=schedule_employee_new.employee_id,
                                                  shift=random.randint(1, 10))
    schedule_employee_updated = crud.schedule_employee.update(db=db,
                                                              db_obj=schedule_employee_new,
                                                              obj_in=schedule_employee_in)
    assert schedule_employee_new
    assert schedule_employee_in
    assert schedule_employee_updated
    assert schedule_employee_updated.schedule_id == schedule_employee_in.schedule_id
    assert schedule_employee_updated.employee_id == schedule_employee_in.employee_id
    assert schedule_employee_updated.shift == schedule_employee_in.shift


def test_delete_schedule_employee(db: Session):
    delete_schedule_employee = create_random_schedule_employee(db=db)
    deleted_schedule_employee = crud.schedule_employee.delete(db=db,
                                                              schedule_id=delete_schedule_employee.schedule_id,
                                                              employee_id=delete_schedule_employee.employee_id)
    get_deleted_employee = crud.schedule_employee.get_by_ids(db=db,
                                                             schedule_id=delete_schedule_employee.schedule_id,
                                                             employee_id=delete_schedule_employee.employee_id)
    assert delete_schedule_employee
    assert deleted_schedule_employee
    assert not get_deleted_employee
