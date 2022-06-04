import datetime
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps

router = APIRouter()


@router.post("/create_schedule_employee", response_model=schemas.ScheduleEmployee)
def create_schedule_employee(
        *,
        db: Session = Depends(deps.get_db),
        schedule_employee_in: schemas.ScheduleEmployee
) -> Any:
    """
    Create schedule employee
    """
    return crud.schedule_employee.create(db=db, obj_in=schedule_employee_in)


@router.get("/get_schedule/{days}", response_model=List[schemas.ScheduleEmployee])
def get_schedule(
        *,
        db: Session = Depends(deps.get_db),
        days: List[datetime.date]
) -> Any:
    """
    Get schedule
    """
    return crud.schedule_employee.get_schedule(db=db, days=days)


@router.put("/update_schedule_employee_by_ids/schedule_id/{schedule_id/employee_id/{employee_id}/shift",
            response_model=schemas.ScheduleEmployee)
def update_position(
        *,
        db: Session = Depends(deps.get_db),
        schedule_id: int,
        employee_id: int,
        shift: int
) -> Any:
    """
    Update schedule employee by ids
    """
    schedule_employee = crud.schedule_employee.get_by_ids(db=db, schedule_id=schedule_id, employee_id=employee_id)
    if not schedule_employee:
        raise HTTPException(
            status_code=404,
            detail="Schedule employee with this ids don't exist"
        )
    schedule_employee_to_update = jsonable_encoder(schedule_employee)
    schedule_employee_updated = schemas.PositionUpdate(**schedule_employee_to_update)
    schedule_employee_updated.shift = shift
    return crud.position.update(db=db, db_obj=schedule_employee, obj_in=schedule_employee_updated)


@router.delete("/delete_schedule_employee/{schedule_id}/{employee_id}", response_model=schemas.Position)
def delete_position(
    *,
    db: Session = Depends(deps.get_db),
    schedule_id: int,
    employee_id: int
) -> Any:
    """
    Delete a schedule employee
    """
    schedule_employee = crud.schedule_employee.get_by_ids(db=db, schedule_id=schedule_id, employee_id=employee_id)
    if not schedule_employee:
        raise HTTPException(status_code=404, detail="Schedule employee not found")
    schedule_employee = crud.schedule_employee.delete(db=db, schedule_id=schedule_id, employee_id=employee_id)
    return schedule_employee
