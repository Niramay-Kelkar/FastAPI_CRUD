from fastapi import FastAPI, Depends, HTTPException
import models
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import  Session

#Create Table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_user = models.Student(name=student.name, email=student.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/students/{student_id}", response_model=schemas.StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    else:
        return db_student

@app.get("/students/", response_model=list[schemas.StudentOut])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Student).offset(skip).limit(limit).all()

@app.put("/students/{student_id}", response_model=schemas.StudentOut)
def update_student(student_id: int, student: schemas.StudentUpdate, db:Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.name = student.name if student.name is not None else db_student.name
    db_student.email = student.email if student.email is not None else db_student.email
    db.commit()
    db.refresh(db_student)
    return db_student

