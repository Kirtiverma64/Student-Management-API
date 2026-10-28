# Student Management API

##  Project Overview
The Student Management API is a REST API built using Python and FastAPI. It allows users to perform CRUD (Create, Read, Update, Delete) operations on student records stored in an SQLite database.

## Technologies Used
- Python
- FastAPI
- SQLite
- REST API
- Uvicorn

## Features
- Add a new student
- Retrieve all students
- Retrieve a student by ID
- Update student details
- Delete a student record
- Interactive API documentation using Swagger UI

## Project Structure

```text
API/
├── main.py
├── database.py
├── init_db.py
├── students.sql
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kirtiverma64/Student-Management-API.git
```

### 2. Open the project folder

```bash
cd Student-Management-API
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Initialize the database

Run the database initialization script:

```bash
python init_db.py
```

### 7. Start the API server

```bash
uvicorn main:app --reload
```

## API Documentation

After starting the server, open the following URL in your browser:

http://127.0.0.1:8000/docs

Swagger UI allows you to test the API endpoints interactively.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| POST | `/students` | Add a new student |
| PUT | `/students/{student_id}` | Update student details |
| DELETE | `/students/{student_id}` | Delete a student |

## Learning Objectives

- Understand REST API concepts
- Learn how HTTP methods work
- Connect a Python application to an SQLite database
- Implement CRUD operations
- Test API endpoints using Swagger UI

