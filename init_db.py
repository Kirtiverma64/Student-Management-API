import sqlite3

conn = sqlite3.connect("students.db")

with open("students.sql", "r", encoding="utf-8") as file:
    conn.executescript(file.read())

conn.commit()
conn.close()

print("Database created successfully!")