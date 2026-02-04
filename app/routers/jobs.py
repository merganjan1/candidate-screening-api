from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.schemas.job_schema import JobCreate
from app.services.job_service import (
    create_job, get_job, list_jobs, deactivate_job
)

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@router.post("/", status_code=201)
async def create(job: JobCreate):
    job_id = await create_job(job.dict())
    return {"id": job_id}


@router.get("/")
async def list_all():
    jobs_cursor = await list_jobs({})
    jobs = []
    async for job in jobs_cursor:
        job["id"] = str(job["_id"])
        del job["_id"]
        jobs.append(job)
    return jobs


@router.get("/{id}")
async def get(id: str):
    try:
        job = await get_job(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid job id")

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    job["id"] = str(job["_id"])
    del job["_id"]
    return job


@router.patch("/{id}/deactivate")
async def deactivate(id: str):
    await deactivate_job(id)
    return {"message": "Job deactivated"}
