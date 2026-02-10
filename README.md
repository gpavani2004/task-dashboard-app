# Task Dashboard App (Frontend Developer Intern Assignment)

A full-stack web application with user authentication and a task management dashboard.  
Users can register, log in, and perform CRUD operations on tasks using a secure JWT-based authentication system.

---

## Tech Stack

### Frontend
- React.js
- Axios
- HTML / CSS
- JavaScript

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite (can be replaced with PostgreSQL/MySQL)

### Authentication
- JWT (JSON Web Tokens)
- Password hashing using bcrypt

---

## Features Implemented

- User Signup & Login
- JWT-based Authentication
- Protected Routes (Dashboard access only after login)
- Create Tasks
- View Tasks
- Delete Tasks
- Logout functionality
- Frontend ↔ Backend integration
- CORS enabled for frontend-backend communication

---

## Project Structure

task-dashboard-app/
│
├── backend/
│ ├── app.py
│ ├── database.py
│ ├── models.py
│ ├── auth.py
│ ├── dependencies.py
│ ├── routers/
│ │ ├── user.py
│ │ └── task.py
│ └── requirements.txt
│
└── frontend/
├── src/
│ ├── pages/
│ │ ├── Login.js
│ │ ├── Register.js
│ │ └── Dashboard.js
│ ├── api.js
│ ├── App.js
│ └── index.js
├── package.json
└── README.md

---

## How to Run the Project

### 1️ Backend Setup

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload

### Backend will run at:
http://127.0.0.1:8000

### Swagger API docs:
http://127.0.0.1:8000/docs

### 2 Frontend Setup

cd frontend
npm install
npm start

### Frontend will run at:
http://localhost:3000

---

## Authentication Flow (JWT)

User logs in with email & password

Backend validates credentials

JWT token is generated and returned

Token is stored in localStorage

Token is sent in Authorization header for protected API requests

Backend verifies token before allowing access

Authorization: Bearer <JWT_TOKEN>

---

## API Endpoints
### Auth

POST /signup – Register user

POST /login – Login user (returns JWT)

### Tasks (Protected)

GET /tasks – Fetch user tasks

POST /tasks – Create new task

DELETE /tasks/{id} – Delete task

---

## Scalability & Production Considerations

Replace SQLite with PostgreSQL/MySQL

Store JWT secret in environment variables

Add refresh tokens

Add pagination for tasks

Add role-based access control

Deploy frontend and backend separately (e.g., Vercel + AWS)

---
### Screenshots

#### Dashboard
Dashboard screenshot (Screenshorts/Dashboard.png)

Login screenshot (Screenshorts/Login.png)

Swagger screenshot (Screeshorts/Swagger.png)

---

## Author

G Pavani

Frontend Developer Intern Applicant



