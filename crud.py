from sqlalchemy.orm import Session
import models, schemas

# Create a new student
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Get all students
def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

# Get student by ID
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

# Update student score
def update_student_score(db: Session, student_id: int, score: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        student.score = score
        db.commit()
        db.refresh(student)
    return student

# Delete student
def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student
def log_activity(db: Session, activity: schemas.ActivityCreate):
    db_activity = models.StudentActivity(
        student_id=activity.student_id,
        question=activity.question,
        student_answer=activity.student_answer,
        correct_answer=activity.correct_answer,
        is_correct=activity.is_correct,
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity
def get_student_activities(db: Session, student_id: int):
    return db.query(models.StudentActivity).filter(
        models.StudentActivity.student_id == student_id
    ).all()
