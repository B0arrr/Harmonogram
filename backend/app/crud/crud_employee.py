from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


class CRUDEmployee(CRUDBase[Employee, EmployeeCreate, EmployeeUpdate]):
    def get_by_email(
            self,
            *,
            db: Session,
            email: str
    ) -> Employee:
        return db.query(self.model).filter(Employee.email == email).first()

    def get_by_login(
            self,
            *,
            db: Session,
            login: str
    ) -> Employee:
        return db.query(self.model).filter(Employee.login == login).first()


employee = CRUDEmployee(Employee)
