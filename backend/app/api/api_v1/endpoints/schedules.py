import datetime
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core import helper

router = APIRouter()


@router.post("/create_schedule", response_model=schemas.Schedule)
def create_schedule(
        *,
        db: Session = Depends(deps.get_db),
        schedule_in: schemas.ScheduleCreate
) -> Any:
    """
    Create schedule
    """
    schedule = crud.schedule.create(db=db, obj_in=schedule_in)
    return schedule


@router.get("/get_schedule_by_id/{id}", response_model=schemas.Schedule)
def get_schedule_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Get schedule by id
    """
    schedule = crud.schedule.get(db=db, id=id)
    return schedule


@router.get("/get_schedule_id/{day}")
def get_schedule_id_by_name(
        *,
        db: Session = Depends(deps.get_db),
        day: datetime.date
) -> Any:
    """
    Get schedule id by schedule
    """
    return crud.schedule.get_id(db=db, day=day)


@router.get("/get_schedule_day_by_id/{id}")
def get_schedule_day_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Get schedule day by id
    """
    return crud.schedule.get_day_by_id(db=db, id=id)


@router.get("/get_all_schedules", response_model=List[schemas.Schedule])
def get_all_schedules(
        *,
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Get all schedules
    """
    return crud.schedule.get_all(db=db)


@router.put("/update_schedule_by_id/{id}/day/{day}", response_model=schemas.Schedule)
def update_schedule_day(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        day: datetime.date
) -> Any:
    """
    Update schedule day
    """
    schedule = crud.schedule.get(db=db, id=id)
    if not schedule:
        raise HTTPException(
            status_code=404,
            detail="Schedule with this id don't exist"
        )
    schedule_to_update = jsonable_encoder(schedule)
    schedule_updated = schemas.ScheduleUpdate(**schedule_to_update)
    schedule_updated.day = helper.datetime_sqlalchemy(day)
    return crud.schedule.update(db=db, db_obj=schedule, obj_in=schedule_updated)


@router.put("/update_schedule_by_id/{id}/day_off/{day_off}", response_model=schemas.Schedule)
def update_employment_name(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        day_off: bool
) -> Any:
    """
    Update schedule day off
    """
    schedule = crud.employment.get(db=db, id=id)
    if not schedule:
        raise HTTPException(
            status_code=404,
            detail="Schedule with this id don't exist"
        )
    schedule_to_update = jsonable_encoder(schedule)
    schedule_updated = schemas.ScheduleUpdate(**schedule_to_update)
    schedule_updated.day_off = day_off
    return crud.schedule.update(db=db, db_obj=schedule, obj_in=schedule_updated)


@router.delete("/delete_schedule/{id}", response_model=schemas.Schedule)
def delete_employment(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Delete schedule
    """
    schedule = crud.schedule.get(db=db, id=id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    schedule = crud.schedule.remove(db=db, id=id)
    return schedule
