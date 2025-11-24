from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    score: int

    class Config:
        orm_mode = True
from datetime import datetime

class ActivityBase(BaseModel):
    student_id: int
    question: str
    student_answer: int
    correct_answer: int
    is_correct: bool

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
