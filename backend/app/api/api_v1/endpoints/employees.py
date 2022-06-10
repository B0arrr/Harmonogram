from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps
from app.core.security import get_password_hash

router = APIRouter()


@router.post("/create_employee", response_model=schemas.Employee)
def create_employee(
        *,
        db: Session = Depends(deps.get_db),
        employee_in: schemas.EmployeeCreate
) -> Any:
    """
    Create employee
    """
    employee = crud.employee.get_by_email(db=db, email=employee_in.email)
    if employee:
        raise HTTPException(
            status_code=400,
            detail="Email already in use"
        )
    employee = crud.employee.get_by_login(db=db, login=employee_in.login)
    if employee:
        raise HTTPException(
            status_code=400,
            detail="Login already in use"
        )
    employee_in.password = get_password_hash(employee_in.password)
    return crud.employee.create(db=db, obj_in=employee_in)


@router.get("/get_employee_by_id/{id}", response_model=schemas.Employee)
def get_employee_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Get employee by id
    """
    return crud.employee.get(db=db, id=id)


@router.get("/get_employee_by_email/{email}", response_model=schemas.Employee)
def get_employee_by_email(
        *,
        db: Session = Depends(deps.get_db),
        email: str
) -> Any:
    """
    Get employee by email
    """
    return crud.employee.get_by_email(db=db, email=email)


@router.get("/get_employee_by_login/{login}", response_model=schemas.Employee)
def get_employee_by_login(
        *,
        db: Session = Depends(deps.get_db),
        login: str
) -> Any:
    """
    Get employee by login
    """
    return crud.employee.get_by_login(db=db, login=login)


@router.get("/get_all_employees", response_model=List[schemas.Employee])
def get_all_employees(
        *,
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Get all employees
    """
    return crud.employee.get_all_employees(db=db)


@router.put("/create_account/{email}", response_model=schemas.Employee)
def create_account_by_email(
        *,
        db: Session = Depends(deps.get_db),
        email: str,
        login: str,
        password: str
) -> Any:
    """
    Create account for employee
    """
    employee = crud.employee.get_by_email(db=db, email=email)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with this email don't exist"
        )
    if employee.login:
        raise HTTPException(
            status_code=400,
            detail="Account already created"
        )
    employee_2 = crud.employee.get_by_login(db=db, login=login)
    if employee_2:
        raise HTTPException(
            status_code=400,
            detail="Login already in use"
        )
    employee_to_update = jsonable_encoder(employee)
    employee_updated = schemas.EmployeeAccount(**employee_to_update)
    employee_updated.login = login
    employee_updated.password = get_password_hash(password=password)
    return crud.position.update(db=db, db_obj=employee, obj_in=employee_updated)


@router.put("/update_employee_name_by_id/{id}/name/{name}", response_model=schemas.Employee)
def update_employee_name_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        name: str
) -> Any:
    """
    Update employee name by id
    """
    employee = crud.schedule.get(db=db, id=id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with this id don't exist"
        )
    employee_to_update = jsonable_encoder(employee)
    employee_updated = schemas.EmployeeUpdate(**employee_to_update)
    employee_updated.name = name
    return crud.schedule.update(db=db, db_obj=employee, obj_in=employee_updated)


@router.put("/update_employee_surname_by_id/{id}/surname/{surname}", response_model=schemas.Employee)
def update_employee_surname_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        surname: str
) -> Any:
    """
    Update employee surname by id
    """
    employee = crud.schedule.get(db=db, id=id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with this id don't exist"
        )
    employee_to_update = jsonable_encoder(employee)
    employee_updated = schemas.EmployeeUpdate(**employee_to_update)
    employee_updated.surname = surname
    return crud.schedule.update(db=db, db_obj=employee, obj_in=employee_updated)


@router.put("/update_employee_email_by_id/{id}/email/{email}", response_model=schemas.Employee)
def update_employee_email_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        email: EmailStr
) -> Any:
    """
    Update employee email by id
    """
    employee = crud.schedule.get(db=db, id=id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with this id don't exist"
        )
    employee_to_update = jsonable_encoder(employee)
    employee_updated = schemas.EmployeeUpdate(**employee_to_update)
    employee_updated.email = email
    return crud.schedule.update(db=db, db_obj=employee, obj_in=employee_updated)


@router.put("/update_employee_employment_id_by_id/{id}/employment_id/{employment_id}", response_model=schemas.Employee)
def update_employee_employment_id_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        employment_id: int
) -> Any:
    """
    Update employee employment_id by id
    """
    employee = crud.schedule.get(db=db, id=id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with this id don't exist"
        )
    employee_to_update = jsonable_encoder(employee)
    employee_updated = schemas.EmployeeUpdate(**employee_to_update)
    employee_updated.employment_id = employment_id
    return crud.schedule.update(db=db, db_obj=employee, obj_in=employee_updated)


@router.put("/update_employee_position_id_by_id/{id}/position_id/{position_id}", response_model=schemas.Employee)
def update_employee_position_id_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        position_id: int
) -> Any:
    """
    Update employee position_id by id
    """
    employee = crud.schedule.get(db=db, id=id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with this id don't exist"
        )
    employee_to_update = jsonable_encoder(employee)
    employee_updated = schemas.EmployeeUpdate(**employee_to_update)
    employee_updated.position_id = position_id
    return crud.schedule.update(db=db, db_obj=employee, obj_in=employee_updated)


@router.put("/update_employee_login_by_id/{id}/login/{login}", response_model=schemas.Employee)
def update_employee_login_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        login: str
) -> Any:
    """
    Update employee login by id
    """
    employee = crud.schedule.get(db=db, id=id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with this id don't exist"
        )
    employee_to_update = jsonable_encoder(employee)
    employee_updated = schemas.EmployeeUpdate(**employee_to_update)
    employee_updated.login = login
    return crud.schedule.update(db=db, db_obj=employee, obj_in=employee_updated)


@router.put("/update_employee_password_by_id/{id}/password/{password}", response_model=schemas.Employee)
def update_employee_password_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        password: str
) -> Any:
    """
    Update employee password by id
    """
    employee = crud.schedule.get(db=db, id=id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with this id don't exist"
        )
    employee_to_update = jsonable_encoder(employee)
    employee_updated = schemas.EmployeeUpdate(**employee_to_update)
    employee_updated.password = get_password_hash(password)
    return crud.schedule.update(db=db, db_obj=employee, obj_in=employee_updated)


@router.put("/update_employee_department_by_id/{id}/department/{department}", response_model=schemas.Employee)
def update_employee_password_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        department: str
) -> Any:
    """
    Update employee department by id
    """
    employee = crud.schedule.get(db=db, id=id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with this id don't exist"
        )
    employee_to_update = jsonable_encoder(employee)
    employee_updated = schemas.EmployeeUpdate(**employee_to_update)
    employee_updated.department = department
    return crud.schedule.update(db=db, db_obj=employee, obj_in=employee_updated)


@router.delete("/delete_employee/{id}", response_model=schemas.Employee)
def delete_employee(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Delete an employee
    """
    return crud.employee.delete(db=db, id=id)
