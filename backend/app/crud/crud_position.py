from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.position import Position
from app.schemas.position import PositionCreate, PositionUpdate


class CRUDItem(CRUDBase[Position, PositionCreate, PositionUpdate]):
    def create_one(
            self, db: Session, *, obj_in: PositionCreate
    ) -> Position:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_id(
            self, db: Session, *, id: int
    ) -> Position:
        return db.query(self.model) \
            .filter(Position.id == id) \
            .first()

    def get_id(
            self, db: Session, *, name: str
    ) -> int:
        return db.query(self.model).filter(Position.name == name).first().id

    def get_name_by_id(
            self, db: Session, *, id: int
    ) -> str:
        return db.query(self.model).filter(Position.id == id).first().name

    def get_all(
            self, db: Session
    ) -> List[Position]:
        return db.query(self.model).all()


position = CRUDItem(Position)
