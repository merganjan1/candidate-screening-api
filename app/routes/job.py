from fastapi import APIRouter
from datetime import datetime
from app.schemas.job import JobCreate
from app.database import jobs_collection

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/")
async def create_job(job: JobCreate):
    job_dict = job.dict()
    job_dict["created_at"] = datetime.utcnow()

    result = await jobs_collection.insert_one(job_dict)
    job_dict["_id"] = str(result.inserted_id)

    return job_dict

@router.get("/")
async def get_jobs():
    jobs = []
    async for job in jobs_collection.find():
        job["_id"] = str(job["_id"])
        jobs.append(job)
    return jobs

from bson import ObjectId
from fastapi import HTTPException

@router.get("/{job_id}")
async def get_job(job_id: str):
    job = await jobs_collection.find_one({"_id": ObjectId(job_id)})

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    job["_id"] = str(job["_id"])
    return job
