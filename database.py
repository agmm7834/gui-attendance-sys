import sqlite3

def connect_db():
    return sqlite3.connect("attendance.db")

def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_student(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_students():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM students")
    students = cur.fetchall()
    conn.close()
    return students

def mark_attendance(student_id, date, status):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
        (student_id, date, status)
    )
    conn.commit()
    conn.close()
