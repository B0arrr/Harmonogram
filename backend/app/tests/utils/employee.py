import random

from sqlalchemy.orm import Session

from app import models, crud
from app.core.security import get_password_hash
from app.schemas import EmployeeCreate
from app.tests.utils.utils import random_lower_string, random_email


def create_random_employee(db: Session) -> models.Employee:
    name = random_lower_string()
    surname = random_lower_string()
    email = random_email()
    employment_id = random.randint(1,100)
    position_id = random.randint(1, 100)
    login = random_lower_string()
    password = get_password_hash(random_lower_string())
    employee_in = EmployeeCreate(name=name,
                                 surname=surname,
                                 email=email,
                                 employment_id=employment_id,
                                 position_id=position_id,
                                 login=login,
                                 password=password)
    return crud.employee.create(db=db, obj_in=employee_in)
