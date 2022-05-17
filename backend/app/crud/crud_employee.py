from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.core.security import verify_password
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

    def get_all_employees(
            self,
            *,
            db: Session
    ) -> List[Employee]:
        return db.query(self.model).filter(Employee.position_id != 1).all()

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[Employee]:
        user = self.get_by_email(db=db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, employee: Employee) -> bool:
        return employee.is_active

    def is_superuser(self, employee: Employee) -> bool:
        return employee.is_superuser


employee = CRUDEmployee(Employee)
