from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()


# -------------------------------
# Dependency – DB Session
# -------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------------
# Root route
# -------------------------------
@app.get("/")
def read_root():
    return {"message": "🚀 BITSMath API is running successfully!"}


# -------------------------------
# CRUD ROUTES
# -------------------------------

# Create student
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)


# Get all students
@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_students(db, skip=skip, limit=limit)


# Get student by ID
@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


# Update student score
@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student_score(student_id: int, score: int, db: Session = Depends(get_db)):
    db_student = crud.update_student_score(db, student_id, score)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


# Delete student
@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.delete_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
from question_generator import generate_math_question

@app.get("/generate-question")
def generate_question():
    return generate_math_question()
from fastapi import Body

@app.post("/submit-answer")
def submit_answer(
    question: str = Body(...),
    student_answer: int = Body(...),
    correct_answer: int = Body(...)
):
    if student_answer == correct_answer:
        return {"result": "correct", "message": "Great job!"}
    else:
        return {"result": "wrong", "message": "Try again!"}
from schemas import ActivityCreate
import crud

@app.post("/submit-answer")
def submit_answer(
    student_id: int = Body(...),
    question: str = Body(...),
    student_answer: int = Body(...),
    correct_answer: int = Body(...),
    db: Session = Depends(get_db)
):
    is_correct = (student_answer == correct_answer)

    # Log activity in DB
    activity = ActivityCreate(
        student_id=student_id,
        question=question,
        student_answer=student_answer,
        correct_answer=correct_answer,
        is_correct=is_correct
    )
    crud.log_activity(db, activity)

    # Return result
    if is_correct:
        return {"result": "correct", "message": "Excellent!"}
    else:
        return {"result": "wrong", "message": "Try again."}
import json
from xapi import create_xapi_statement

@app.post("/track-activity")
def track_activity(
    student_id: int = Body(...),
    question: str = Body(...),
    student_answer: int = Body(...),
    correct_answer: int = Body(...),
    is_correct: bool = Body(...)
):
    # Create xAPI statement
    statement = create_xapi_statement(
        student_id,
        question,
        student_answer,
        correct_answer,
        is_correct
    )

    # Save to local JSON file
    with open("xapi_logs.json", "a") as f:
        f.write(json.dumps(statement) + "\n")

    return {"message": "xAPI statement recorded", "xapi": statement}
from xapi import create_xapi_statement

@app.post("/submit-answer")
def submit_answer(
    student_id: int = Body(...),
    question: str = Body(...),
    student_answer: int = Body(...),
    correct_answer: int = Body(...),
    db: Session = Depends(get_db)
):
    is_correct = (student_answer == correct_answer)

    # Log DB activity
    activity = ActivityCreate(
        student_id=student_id,
        question=question,
        student_answer=student_answer,
        correct_answer=correct_answer,
        is_correct=is_correct
    )
    crud.log_activity(db, activity)

    # Generate xAPI
    statement = create_xapi_statement(
        student_id,
        question,
        student_answer,
        correct_answer,
        is_correct
    )

    # Save xAPI statement
    with open("xapi_logs.json", "a") as f:
        f.write(json.dumps(statement) + "\n")

    return {
        "result": "correct" if is_correct else "wrong",
        "xapi_logged": True,
        "xapi": statement
    }
@app.get("/activities/{student_id}", response_model=list[schemas.Activity])
def get_activities(student_id: int, db: Session = Depends(get_db)):
    activities = crud.get_student_activities(db, student_id)
    return activities

