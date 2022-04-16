from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.db.base_class import Base


class Employment(Base):
    id = Column(Integer, primary_key=True, index=True)
    employment = Column(String, index=True, nullable=False)
    hours_per_week = Column(Integer, nullable=True)
    pours_per_day = Column(Integer, nullable=True)
    employee = relationship("Employee", ForeignKey("employee.id"))
