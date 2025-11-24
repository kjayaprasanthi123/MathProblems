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
