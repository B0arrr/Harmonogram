from typing import Any, List

from fastapi import APIRouter, Depends
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
    position = crud.employment.create_one(db=db, obj_in=employment_in)
    return position


@router.get("/get_employment_by_id/{id}", response_model=schemas.Employment)
def get_employment_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    positions = crud.employment.get_by_id(db=db, id=id)
    return positions


@router.get("/get_employment_id/{name}")
def get_employment_id_by_name(
        *,
        db: Session = Depends(deps.get_db),
        name: str
) -> Any:
    return crud.employment.get_id(db=db, name=name)


@router.get("/get_employment_name_by_id/{id}")
def get_employment_name_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    return crud.employment.get_name_by_id(db=db, id=id)


@router.get("/get_all_employments", response_model=List[schemas.Employment])
def get_all_employments(
        *,
        db: Session = Depends(deps.get_db)
) -> Any:
    return crud.employment.get_all(db=db)
