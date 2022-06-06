from sqlalchemy.orm import Session

from app import crud
from app.schemas import PositionCreate
from app.tests.utils.utils import random_lower_string


def create_random_position(db: Session):
    name = random_lower_string()
    position_in = PositionCreate(name=name)
    return crud.position.create(db=db,
                                obj_in=position_in)
