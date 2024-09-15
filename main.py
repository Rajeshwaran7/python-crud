from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import getDb
import models , schemas

app = FastAPI()


@app.post("/students",response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(getDb)):
    db_student = models.Student(
        name=student.name,
        age=student.age,
        standard=student.standard,
        attendance=student.attendance
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students",response_model=List[schemas.StudentResponse])
def get_students(skik:int = 0,limit:int = 10, db:Session = Depends(getDb)):
    students = db.query(models.Student).offset(skik).limit(limit).all()
    return students

@app.put("/students/{student_id}",response_model=schemas.StudentResponse)
def update_student(student_id:int,student:schemas.StudentUpdate, db:Session = Depends(getDb)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404,detail="Student not found")
    db_student.name = student.name
    db_student.age = student.age
    db_student.attendance = student.attendance
    db_student.standard = student.standard
    db.commit()
    db.refresh(db_student)
    return db_student

@app.delete("/students/delete/{student_id}", response_model=schemas.StudentResponse)
def delete_student(student_id: int, db: Session = Depends(getDb)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return db_student
