from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, models, crud
from app.api import deps

router = APIRouter()


@router.post("/create_position", response_model=schemas.Position)
def create_item(
        *,
        db: Session = Depends(deps.get_db),
        item_in: schemas.PositionCreate
) -> Any:
    """
    Create new item.
    """
    item = crud.position.create_one(db=db, obj_in=item_in)
    return item


@router.get("/get_position_by_id/{id}", response_model=schemas.Position)
def get_position_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    items = crud.position.get_by_id(db=db, id=id)
    return items


@router.get("/get_position_id/{name}")
def get_position_id_by_name(
        *,
        db: Session = Depends(deps.get_db),
        name: str
) -> Any:
    return crud.position.get_id(db=db, name=name)


@router.get("/get_position_name_by_id")
def get_position_name_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    return crud.position.get_name_by_id(db=db, id=id)


@router.get("/get_all_positions", response_model=List[schemas.Position])
def get_all_positions(
        *,
        db: Session = Depends(deps.get_db)
) -> Any:
    return crud.position.get_all(db=db)
