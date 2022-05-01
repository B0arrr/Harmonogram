from typing import Any, List

from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps

router = APIRouter()


@router.get("/")
def get():
    return {"name": "Maciek"}


@router.post("/create_position", response_model=schemas.Position)
def create_position(
        *,
        db: Session = Depends(deps.get_db),
        position_in: schemas.PositionCreate
) -> Any:
    """
    Create new position
    """
    position = crud.position.create(db=db, obj_in=position_in)
    return position


@router.get("/get_position_by_id/{id}", response_model=schemas.Position)
def get_position_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Get position by id
    """
    positions = crud.position.get(db=db, id=id)
    return positions


@router.get("/get_position_id/{name}")
def get_position_id_by_name(
        *,
        db: Session = Depends(deps.get_db),
        name: str
) -> Any:
    """
    Get position id by name
    """
    return crud.position.get_id(db=db, name=name)


@router.get("/get_position_name_by_id/{id}")
def get_position_name_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Get position name by id
    """
    return crud.position.get_name_by_id(db=db, id=id)


@router.get("/get_all_positions", response_model=List[schemas.Position])
def get_all_positions(
        *,
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Get all positions
    """
    return crud.position.get_all(db=db)


@router.put("/update_position_by_id/{id}/name/{name}", response_model=schemas.Position)
def update_position(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        name: str
) -> Any:
    """
    Update position by id
    """
    position = crud.position.get(db=db, id=id)
    if not position:
        raise HTTPException(
            status_code=404,
            detail="Position with this id don't exist"
        )
    position_to_update = jsonable_encoder(position)
    position_updated = schemas.PositionUpdate(**position_to_update)
    position_updated.name = name
    return crud.position.update(db=db, db_obj=position, obj_in=position_updated)


@router.delete("/delete_position/{id}", response_model=schemas.Position)
def delete_position(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Delete a position
    """
    position = crud.position.get(db=db, id=id)
    if not position:
        raise HTTPException(status_code=404, detail="Position not found")
    position = crud.position.remove(db=db, id=id)
    return position
