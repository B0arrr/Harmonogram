from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps
from app.api.deps import get_db

router = APIRouter()


@router.post("/create_employment", response_model=schemas.Employment)
def create_employment(
        *,
        db: Session = Depends(get_db),
        employment_in: schemas.EmploymentCreate
) -> Any:
    """
    Create employment
    """
    employment = crud.employment.create(db=db, obj_in=employment_in)
    return employment


@router.get("/get_employment_by_id/{id}", response_model=schemas.Employment)
def get_employment_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Get employment by id
    """
    employments = crud.employment.get(db=db, id=id)
    return employments


@router.get("/get_employment_id/{name}")
def get_employment_id_by_name(
        *,
        db: Session = Depends(deps.get_db),
        name: str
) -> Any:
    """
    Get employment id by employment
    """
    return crud.employment.get_id(db=db, name=name)


@router.get("/get_employment_name_by_id/{id}")
def get_employment_name_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Get employment name by id
    """
    return crud.employment.get_name_by_id(db=db, id=id)


@router.get("/get_all_employments", response_model=List[schemas.Employment])
def get_all_employments(
        *,
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Get all employments
    """
    return crud.employment.get_all(db=db)


@router.put("/update_employment_by_id/{id}/employment/{name}", response_model=schemas.Employment)
def update_employment_name(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        name: str
) -> Any:
    """
    Update employment name
    """
    employment = crud.employment.get(db=db, id=id)
    if not employment:
        raise HTTPException(
            status_code=404,
            detail="Employment with this id don't exist"
        )
    employment_to_update = jsonable_encoder(employment)
    employment_updated = schemas.EmploymentUpdate(**employment_to_update)
    employment_updated.employment = name
    return crud.employment.update(db=db, db_obj=employment, obj_in=employment_updated)


@router.put("/update_employment_by_id/{id}/hours_per_week/{hours}", response_model=schemas.Employment)
def update_employment_name(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        hours: int
) -> Any:
    """
    Update employment name
    """
    employment = crud.employment.get(db=db, id=id)
    if not employment:
        raise HTTPException(
            status_code=404,
            detail="Employment with this id don't exist"
        )
    employment_to_update = jsonable_encoder(employment)
    employment_updated = schemas.EmploymentUpdate(**employment_to_update)
    employment_updated.hours_per_week = hours
    return crud.employment.update(db=db, db_obj=employment, obj_in=employment_updated)


@router.put("/update_employment_by_id/{id}/hours_per_day/{hours}", response_model=schemas.Employment)
def update_employment_name(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        hours: int
) -> Any:
    """
    Update employment name
    """
    employment = crud.employment.get(db=db, id=id)
    if not employment:
        raise HTTPException(
            status_code=404,
            detail="Employment with this id don't exist"
        )
    employment_to_update = jsonable_encoder(employment)
    employment_updated = schemas.EmploymentUpdate(**employment_to_update)
    employment_updated.hours_per_day = hours
    return crud.employment.update(db=db, db_obj=employment, obj_in=employment_updated)


@router.delete("/delete_employment/{id}", response_model=schemas.Employment)
def delete_employment(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Delete employment
    """
    employment = crud.employment.get(db=db, id=id)
    if not employment:
        raise HTTPException(status_code=404, detail="Employment not found")
    employment = crud.employment.remove(db=db, id=id)
    return employment



