Candidate Screening Platform API

FastAPI + MongoDB + Local AI (HuggingFace)

📌 Project Overview

This project is a Candidate Screening Platform API built using FastAPI and MongoDB.
It allows recruiters to manage job postings, collect candidate resumes, and automatically evaluate candidates using a local AI model.

The AI runs asynchronously in the background and recommends whether a candidate is more suitable for:

Backend Department

AI / ML Department

No external AI APIs are used — all inference runs locally.

🎯 Key Features

JWT-based Authentication (Register / Login)

Job Management (Create, List, Get, Deactivate)

Resume submission

Screening workflow with async background processing

Local AI inference using Hugging Face transformers

Department recommendation based on semantic similarity 

MongoDB with async driver (Motor)

Swagger/OpenAPI documentation

🛠 Tech Stack
Backend

FastAPI

MongoDB

Motor (Async MongoDB driver)

Pydantic

JWT Authentication (python-jose)

Passlib (password hashing)

AI

Hugging Face Transformers

sentence-transformers/all-MiniLM-L6-v2

Local inference only (no external services)

Async / Background

FastAPI BackgroundTasks

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone <repository-url>
cd candidate-screening-api

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run MongoDB

Make sure MongoDB is running locally:

mongod


Default connection:

mongodb://localhost:27017

5️⃣ Environment Variables

Create a .env file in the root directory:

MONGO_URI=mongodb://localhost:27017
JWT_SECRET_KEY=your_secret_key

6️⃣ Run the server
python -m uvicorn app.main:app --reload


Server URL:

http://127.0.0.1:8000


Swagger documentation:

http://127.0.0.1:8000/docs

🔐 Authentication
Register
POST /auth/register

Login
POST /auth/login


Use the returned JWT token with Authorize in Swagger.

💼 Job Management
Create Job
POST /jobs

{
  "title": "Backend Developer",
  "description": "FastAPI backend developer position",
  "required_skills": ["python", "fastapi", "mongodb"],
  "min_experience_years": 2,
  "is_active": true
}

List Jobs
GET /jobs

Get Job
GET /jobs/{job_id}

Deactivate Job
PATCH /jobs/{job_id}/deactivate

📄 Resume Management
Create Resume
POST /resumes/

{
  "full_name": "John Doe",
  "email": "john@example.com",
  "skills": ["python", "fastapi", "mongodb"],
  "experience": 3,
  "resume_text": "Backend developer with FastAPI and MongoDB experience"
}

🧪 Screening & AI Workflow
Create Screening
POST /screenings/

{
  "resume_id": "RESUME_ID_HERE"
}


What happens next:

Screening is created with status pending

Background task starts automatically

AI model runs locally

Screening is updated with AI results

Status changes to scored

Get Screening Result
GET /screenings/{id}


Example response:

{
  "id": "6982f0c640b8ed3adb1b22a0",
  "resume_id": "6982eff63adc3b59415efaa1",
  "status": "scored",
  "ai_department": "backend",
  "ai_department_score": 0.411,
  "created_at": "2026-02-04T07:09:58.213000",
  "scored_at": "2026-02-04T07:09:58.660000"
}

🤖 AI Department Recommendation
Model

sentence-transformers/all-MiniLM-L6-v2

Reference Profiles

Backend Profile

REST APIs, databases, distributed systems, caching,
microservices, docker, kubernetes, authentication


AI / ML Profile

machine learning, transformers, pytorch,
embeddings, NLP, deep learning, inference

AI Logic

Generate embedding for resume text

Generate embeddings for backend and AI profiles

Compute cosine similarity

Choose the department with higher similarity

⚙️ Design Decisions

AI model is loaded once at startup

Background tasks prevent blocking API requests

MongoDB ObjectId and datetime fields are safely serialized

Clean separation between routers, services, and schemas

🧪 Testing

Manual testing via Swagger UI:

http://127.0.0.1:8000/docs
