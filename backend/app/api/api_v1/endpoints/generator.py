import random
from datetime import date
from typing import Any

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps
from app.core import helper

router = APIRouter()


@router.post("/generate_schedule", response_model=schemas.GeneratedSchedule)
def generate_schedule(
        *,
        db: Session = Depends(deps.get_db),
        start: date,
        end: date,
        employee_per_shift: int,
        shifts: int
) -> Any:
    """
    Generate schedule from start to end day, for different employees on shift, and different amount of shifts
    """
    days = helper.get_list_of_days(start, end)
    employees = crud.employee.get_all_employees(db=db)
    if len(employees) < employee_per_shift * shifts:
        raise HTTPException(
            status_code=400,
            detail="Not enough employees to create schedule",
        )
    for i in days:
        day_off = False
        if i.weekday() == 5 or i.weekday() == 6:
            day_off = True
        schedule = crud.schedule.create_schedule(db=db, day=i, day_off=True)
        employees_temp = employees.copy()
        if not day_off:
            for j in range(shifts):
                for k in range(employee_per_shift):
                    employee = random.choice(employees_temp)
                    employees_temp.remove(employee)
                    schedule_employee_in = schemas.ScheduleEmployeeCreate(
                        schedule_id=schedule.id,
                        employee_id=employee.id,
                        shift=j
                    )
                    crud.schedule_employee.create(db=db, obj_in=schedule_employee_in)
    return get_generated_schedule(db=db, start=start, end=end)


@router.get("/get_generated_schedule/start/{start}/end/{end}", response_model=schemas.GeneratedSchedule)
def get_generated_schedule(
        *,
        db: Session = Depends(deps.get_db),
        start: date,
        end: date
) -> Any:
    """
    Get schedule
    """
    schedule = schemas.GeneratedSchedule()
    days = helper.get_list_of_days(start=start, end=end)
    for i in crud.schedule_employee.get_schedule(db=db, days=days):
        day = crud.schedule.get_day_by_id(db=db, id=i.schedule_id)
        employees = crud.schedule_employee.get_all_employees_from_day(db=db, day=day)
        temp = schemas.ScheduleForEveryone(
            day=day,
            employees=employees
        )
        schedule.schedules.append(temp)
    return schedule


@router.get("/get_generated_schedule/start/{start}/end/{end}/employee_id/{employee_id}",
            response_model=schemas.GeneratedScheduleForEmployee)
def get_generated_schedule_for_employee(
        *,
        db: Session = Depends(deps.get_db),
        start: date,
        end: date,
        employee_id: int
) -> Any:
    """
    Get schedule for concrete employee
    """
    schedule = schemas.GeneratedScheduleForEmployee()
    days = helper.get_list_of_days(start=start, end=end)
    for i in crud.schedule_employee.get_schedule(db=db, days=days):
        day = crud.schedule.get_day_by_id(db=db, id=i.schedule_id)
        employees = crud.schedule_employee.get_all_employees_from_day(db=db, day=day)
        if employee_id in employees["id"]:
            employee = crud.employee.get(db=db, id=employee_id)
            shift = crud.schedule_employee.get_by_ids(db=db, schedule_id=i.id, employee_id=employee_id).shift
            temp = schemas.ScheduleForEmployee(
                day=day,
                employees=employee,
                shift=shift
            )
            schedule.schedules.append(temp)
    return schedule
