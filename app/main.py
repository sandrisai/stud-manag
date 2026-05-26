from fastapi import FastAPI
from db import get_db

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/student")
def add_student(name: str, age: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students(name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Student added"}

@app.get("/students")
def list_students():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"students": data}