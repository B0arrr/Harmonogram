import datetime
from typing import List

from sqlalchemy.orm import Session

from app import crud
from app.crud.base import CRUDBase
from app.models import Schedule_Employee
from app.schemas import Employee
from app.schemas.schedule_employee import ScheduleEmployeeUpdate, ScheduleEmployeeCreate


class CRUDScheduleEmployee(CRUDBase[Schedule_Employee, ScheduleEmployeeCreate, ScheduleEmployeeUpdate]):
    def get_schedule(
            self, db: Session, *, days: List[datetime.date]
    ) -> List[Schedule_Employee]:
        schedule = []
        for i in days:
            schedule_id = crud.schedule.get_id(db=db, day=i)
            schedule += db.query(self.model).filter(Schedule_Employee.schedule_id == schedule_id).all()
        return schedule

    def get_by_ids(
            self, db: Session, *, schedule_id: int, employee_id: int
    ) -> Schedule_Employee:
        return db.query(self.model) \
            .filter(Schedule_Employee.schedule_id == schedule_id, Schedule_Employee.employee_id == employee_id).first()

    def get_all_employees_from_day(
            self, db: Session, *, day: datetime.date
    ) -> List[Employee]:
        day_id = crud.schedule.get_id(db=db, day=day)
        employees = []
        for i in db.query(self.model).filter(Schedule_Employee.schedule_id == day_id).all():
            employees.append(crud.employee.get(db=db, id=i.employee_id))
        return employees

    def delete(
            self, db: Session, *, schedule_id: int, employee_id: int
    ) -> Schedule_Employee:
        schedule_employee = db.query(self.model) \
            .filter(Schedule_Employee.schedule_id == schedule_id, Schedule_Employee.employee_id == employee_id).first()
        db.delete(schedule_employee)
        db.commit()
        return schedule_employee


schedule_employee = CRUDScheduleEmployee(Schedule_Employee)
