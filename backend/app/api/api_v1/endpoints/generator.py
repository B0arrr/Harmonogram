import random
from datetime import date
from typing import Any, List

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
        schedule = crud.schedule.create_schedule(db=db, day=i, day_off=day_off)
        employees_temp = employees.copy()
        if not day_off:
            for j in range(shifts):
                for k in range(employee_per_shift):
                    employee = random.choice(employees_temp)
                    schedule_employee_in = schemas.ScheduleEmployeeCreate(
                        schedule_id=schedule.id,
                        employee_id=employee.id,
                        shift=j + 1
                    )
                    employees_temp.remove(employee)
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
    days = helper.get_list_of_days(start=start, end=end)
    list = []
    for i in days:
        try:
            employees = crud.schedule_employee.get_all_employees_from_day(db=db, day=i)
        except:
            continue
        employees_schema = []
        for j in employees:
            employees_schema.append(schemas.EmployeeDisplay(name=j.name, surname=j.surname))
        temp = schemas.ScheduleForEveryone(
            day=i,
            employees=employees_schema
        )
        list.append(temp)
    schedule = schemas.GeneratedSchedule(schedules=list)
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
    list = []
    days = helper.get_list_of_days(start=start, end=end)
    for i in days:
        try:
            employees = crud.schedule_employee.get_all_employees_from_day(db=db, day=i)
        except:
            continue
        ids = []
        for j in employees:
            ids.append(j.id)
        if employee_id in ids:
            employee = crud.employee.get(db=db, id=employee_id)
            employee_display = schemas.EmployeeDisplay(name=employee.name, surname=employee.surname)
            schedule_id = crud.schedule.get_id(db=db, day=i)
            shift = crud.schedule_employee.get_by_ids(db=db, schedule_id=schedule_id, employee_id=employee_id).shift
            temp = schemas.ScheduleForEmployee(
                day=i,
                employee=employee_display,
                shift=shift
            )
            list.append(temp)
    schedule = schemas.GeneratedScheduleForEmployee(schedules=list)
    return schedule
