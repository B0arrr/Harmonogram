from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Employment
from app.schemas import EmploymentCreate, EmploymentUpdate


class CRUDEmployment(CRUDBase[Employment, EmploymentCreate, EmploymentUpdate]):
    def create_one(
            self, db: Session, *, obj_in: EmploymentCreate
    ) -> Employment:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_id(
            self, db: Session, *, id: int
    ) -> Employment:
        return db.query(Employment) \
            .filter(Employment.id == id) \
            .first()

    def get_id(
            self, db: Session, *, name: str
    ) -> int:
        return db.query(self.model).filter(Employment.employment == name).first().id

    def get_name_by_id(
            self, db: Session, *, id: int
    ) -> str:
        return db.query(self.model).filter(Employment.id == id).first().employment

    def get_all(
            self, db: Session
    ) -> List[Employment]:
        return db.query(self.model).all()


employment = CRUDEmployment(Employment)
