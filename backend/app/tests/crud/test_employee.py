import random

from sqlalchemy.orm import Session

from app import crud
from app.core.security import get_password_hash
from app.schemas import EmployeeCreate
from app.tests.utils.utils import random_lower_string, random_email


def test_create_employee(db: Session):
    name = random_lower_string()
    surname = random_lower_string()
    email = random_email()
    employment_id = random.randint(1, 100)
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
    employee = crud.employee.create(db=db, obj_in=employee_in)
    assert employee
    assert employee_in.name == employee.name
    assert employee_in.surname == employee.surname
    assert employee_in.email == employee.email
    assert employee_in.position_id == employee.position_id
    assert employee_in.employment_id == employee.employment_id
    assert employee_in.login == employee.login
    assert employee_in.password == employee.password

