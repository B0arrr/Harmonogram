import random

from sqlalchemy.orm import Session

from app import crud, models
from app.core.security import get_password_hash
from app.schemas import EmployeeCreate
from app.tests.utils.employee import create_random_employee
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


def test_get_employee_by_id(db: Session):
    employee_new = create_random_employee(db=db)
    employee = crud.employee.get(db=db, id=employee_new.id)
    assert employee
    assert employee_new.name == employee.name
    assert employee_new.surname == employee.surname
    assert employee_new.email == employee.email
    assert employee_new.position_id == employee.position_id
    assert employee_new.employment_id == employee.employment_id
    assert employee_new.login == employee.login
    assert employee_new.password == employee.password


def test_get_employee_by_email(db: Session):
    employee_new = create_random_employee(db=db)
    employee = crud.employee.get_by_email(db=db, email=employee_new.email)
    assert employee
    assert employee_new.name == employee.name
    assert employee_new.surname == employee.surname
    assert employee_new.email == employee.email
    assert employee_new.position_id == employee.position_id
    assert employee_new.employment_id == employee.employment_id
    assert employee_new.login == employee.login
    assert employee_new.password == employee.password


def test_get_employee_by_login(db: Session):
    employee_new = create_random_employee(db=db)
    employee = crud.employee.get_by_login(db=db, login=employee_new.login)
    assert employee
    assert employee_new.name == employee.name
    assert employee_new.surname == employee.surname
    assert employee_new.email == employee.email
    assert employee_new.position_id == employee.position_id
    assert employee_new.employment_id == employee.employment_id
    assert employee_new.login == employee.login
    assert employee_new.password == employee.password


def test_get_all_employees(db: Session):
    employees = crud.employee.get_all_employees(db=db)
    db_employees = db.query(models.Employee).all()
    assert employees
    assert len(employees) + 1 == len(db_employees)


def test_delete_employee(db: Session):
    employee = create_random_employee(db=db)
    employee_deleted = crud.employee.remove(db=db, id=employee.id)
    employee_after_delete = crud.employee.get(db=db, id=employee.id)
    assert employee
    assert employee_deleted
    assert employee == employee_deleted
    assert not employee_after_delete
