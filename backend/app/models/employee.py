from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Employee(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    login = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    employment_id = Column(Integer, ForeignKey('employment.id'))
    employment = relationship("Employment", back_populates="employee")
    position_id = Column(Integer, ForeignKey('position.id'))
    position = relationship("Position", back_populates="employee")
    schedule = relationship("Schedule_Employee", back_populates="employee")
