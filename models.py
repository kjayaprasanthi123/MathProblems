from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    score = Column(Integer, default=0)
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

class StudentActivity(Base):
    __tablename__ = "student_activities"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, index=True)
    question = Column(String)
    student_answer = Column(Integer)
    correct_answer = Column(Integer)
    is_correct = Column(Boolean)
    timestamp = Column(DateTime, default=datetime.utcnow)
