from sqlalchemy.orm import Session

from app import crud, models
from app.schemas import PositionCreate, PositionUpdate
from app.tests.utils.position import create_random_position
from app.tests.utils.utils import random_lower_string


def test_create_position(db: Session):
    name = random_lower_string()
    position_in = PositionCreate(name=name)
    position = crud.position.create(db=db,
                                    obj_in=position_in)
    assert position
    assert position_in.name == position.name


def test_get_position_by_id(db: Session):
    position = create_random_position(db=db)
    get_position = crud.position.get(db=db,
                                     id=position.id)
    assert get_position
    assert position.name == get_position.name


def test_get_position_id(db: Session):
    position = create_random_position(db=db)
    get_position = crud.position.get_id(db=db,
                                        name=position.name)
    assert get_position
    assert position.id == get_position


def test_get_position_name_by_id(db: Session):
    position = create_random_position(db=db)
    get_position = crud.position.get_name_by_id(db=db,
                                                id=position.id)
    assert get_position
    assert position.name == get_position


def test_get_all_positions(db: Session):
    positions = crud.position.get_all(db=db)
    db_positions = db.query(models.Position).all()
    assert db_positions
    assert len(positions) == len(db_positions)


def test_update_position_by_id(db: Session):
    position_new = create_random_position(db=db)
    position_in = PositionUpdate(name=position_new.name)
    position_updated = crud.position.update(db=db,
                                            db_obj=position_new,
                                            obj_in=position_in)
    assert position_new
    assert position_in
    assert position_updated
    assert position_updated.name == position_in.name


def test_delete_position(db: Session):
    position = create_random_position(db=db)
    position_deleted = crud.position.remove(db=db,
                                            id=position.id)
    position_after_delete = crud.position.get(db=db,
                                              id=position.id)
    assert position
    assert position_deleted
    assert position == position_deleted
    assert not position_after_delete
