from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Schedule_Employee
from app.schemas.schedule_employee import ScheduleEmployeeUpdate, ScheduleEmployeeCreate


class CRUDScheduleEmployee(CRUDBase[Schedule_Employee, ScheduleEmployeeCreate, ScheduleEmployeeUpdate]):
    def get_schedule(
            self, db: Session, *, days: List
    ) -> List[Schedule_Employee]:
        schedule = []
        for i in days:
            schedule.append(db.query(self.model).filter(Schedule_Employee.schedule_id == i).first())
        return schedule

    def get_by_ids(
            self, db: Session, *, schedule_id: int, employee_id: int
    ) -> Schedule_Employee:
        return db.query(self.model) \
            .filter(Schedule_Employee.schedule_id == schedule_id, Schedule_Employee.employee_id == employee_id).first()

    def delete(
            self, db: Session, *, schedule_id: int, employee_id: int
    ) -> Schedule_Employee:
        schedule_employee = db.query(self.model) \
            .filter(Schedule_Employee.schedule_id == schedule_id, Schedule_Employee.employee_id == employee_id).first()
        db.delete(schedule_employee)
        db.commit()
        return schedule_employee


schedule_employee = CRUDScheduleEmployee(Schedule_Employee)
