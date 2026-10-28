from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_db_connection

app =FastAPI(title="Student API")

@app.get("/")
def home():
    return {"message":"Student API is running successfully!"}


class Student(BaseModel):
    name: str
    age: int
    email: str


# CREATE
@app.post("/students")
def add_student(student: Student):
    conn =get_db_connection()
    cursor =conn.cursor()

    cursor.execute(
        "INSERT INTO Students (name, age, email) VALUES (?, ?, ?)",
        (student.name, student.age, student.email)
    )

    conn.commit()
    student_id =cursor.lastrowid
    conn.close()

    return {"message":"Student added", "id":student_id}


# READ ALL
@app.get("/students")
def get_students():
    conn =get_db_connection()
    students =conn.execute("SELECT * FROM Students").fetchall()
    conn.close()
    return [dict(student) for student in students]


# READ ONE
@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn =get_db_connection()
    student =conn.execute(
        "SELECT * FROM Students WHERE id =?",
        (student_id,)
    ).fetchone()
    conn.close()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return dict(student)


# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    conn =get_db_connection()

    cursor =conn.execute(
        "UPDATE Students SET name =?, age =?, email =? WHERE id =?",
        (student.name, student.age, student.email, student_id)
    )

    conn.commit()
    updated =cursor.rowcount
    conn.close()

    if updated ==0:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student updated"}


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn =get_db_connection()

    cursor =conn.execute(
        "DELETE FROM Students WHERE id =?",
        (student_id,)
    )

    conn.commit()
    deleted =cursor.rowcount
    conn.close()

    if deleted ==0:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message":"Student deleted"}