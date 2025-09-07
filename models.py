from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    email = Column(String(40), unique=True, index=True, nullable=False)
