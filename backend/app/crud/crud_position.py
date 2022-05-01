from typing import List, Dict, Union, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.position import Position
from app.schemas.position import PositionCreate, PositionUpdate


class CRUDPosition(CRUDBase[Position, PositionCreate, PositionUpdate]):
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


position = CRUDPosition(Position)
