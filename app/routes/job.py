from fastapi import APIRouter
from datetime import datetime
from app.schemas.job import JobCreate

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@router.post("/")
def create_job(job: JobCreate):
    return {
        "message": "Job created successfully",
        "job": {
            "title": job.title,
            "description": job.description,
            "department": job.department,
            "requirements": job.requirements,
            "created_at": datetime.utcnow()
        }
    }
