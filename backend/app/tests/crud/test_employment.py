import random
import string

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas import EmploymentCreate, EmploymentUpdate
from app.tests.utils.employment import create_random_employment
from app.tests.utils.utils import random_lower_string


def test_create_employment(db: Session):
    employment = random_lower_string()
    hours_per_day = random.randint(1, 10)
    hours_per_week = random.randint(1, 10)
    employment_in = EmploymentCreate(employment=employment,
                                     hours_per_week=hours_per_week,
                                     hours_per_day=hours_per_day)
    employment_new = crud.employment.create(db=db,
                                            obj_in=employment_in)
    assert employment_new
    assert employment_in
    assert employment_new.employment == employment_in.employment
    assert employment_new.hours_per_day == employment_in.hours_per_day
    assert employment_new.hours_per_week == employment_in.hours_per_week


def test_get_employment_by_id(db: Session):
    employment = create_random_employment(db=db)
    get_employment = crud.employment.get(db=db,
                                         id=employment.id)
    assert get_employment
    assert employment.id == get_employment.id
    assert employment.hours_per_week == get_employment.hours_per_week
    assert employment.hours_per_day == get_employment.hours_per_day


def test_employment_id(db: Session):
    employment = create_random_employment(db=db)
    get_employment = crud.employment.get_id(db=db,
                                            name=employment.employment)

    assert get_employment
    assert employment.id == get_employment


def test_get_employment_name_by_id(db: Session):
    employment = create_random_employment(db=db)
    get_employment = crud.employment.get_name_by_id(db=db,
                                                    id=employment.id)
    assert get_employment
    assert employment.employment == get_employment


def test_get_all_employments(db: Session):
    employment = crud.employment.get_all(db=db)
    db_employment = db.query(models.Employee).all()
    assert employment
    assert len(employment) == len(db_employment)


def test_update_employments_by_id_name(db: Session):
    employments_new = create_random_employment(db=db)
    employments_in = EmploymentUpdate(employment=random_lower_string(),
                                      hours_per_week=employments_new.hours_per_week,
                                      hours_per_day=employments_new.hours_per_day)
    employments_updated = crud.employment.update(db=db,
                                                 db_obj=employments_new,
                                                 obj_in=employments_in)
    assert employments_new
    assert employments_in
    assert employments_updated
    assert employments_updated.employment == employments_in.employment


def test_update_employments_by_id_hpw(db: Session):
    employments_new = create_random_employment(db=db)
    employments_in = EmploymentUpdate(employment=employments_new.employment,
                                      hours_per_week=random.randint(1, 10),
                                      hours_per_day=employments_new.hours_per_day)
    employments_updated = crud.employment.update(db=db,
                                                 db_obj=employments_new,
                                                 obj_in=employments_in)
    assert employments_new
    assert employments_in
    assert employments_updated
    assert employments_updated.hours_per_week == employments_in.hours_per_week


def test_update_employments_by_id_hpd(db: Session):
    employments_new = create_random_employment(db=db)
    employments_in = EmploymentUpdate(employment=employments_new.employment,
                                      hours_per_week=employments_new.hours_per_week,
                                      hours_per_day=random.randint(1, 10))
    employments_updated = crud.employment.update(db=db,
                                                 db_obj=employments_new,
                                                 obj_in=employments_in)
    assert employments_new
    assert employments_in
    assert employments_updated
    assert employments_updated.hours_per_day == employments_in.hours_per_day


def test_delete_employee(db: Session):
    employment = create_random_employment(db=db)
    employment_deleted = crud.employment.remove(db=db, id=employment.id)
    employment_after_delete = crud.employment.get(db=db, id=employment.id)
    assert employment
    assert employment_deleted
    assert employment == employment_deleted
    assert not employment_after_delete
