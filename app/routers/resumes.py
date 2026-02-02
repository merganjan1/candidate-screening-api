from fastapi import APIRouter, HTTPException
from app.schemas.resume_schema import ResumeCreate
from app.services.resume_service import (
    create_resume,
    get_all_resumes,
    get_resume
)

router = APIRouter(prefix="/resumes", tags=["Resumes"])

@router.post("/", status_code=201)
async def create(resume: ResumeCreate):
    resume_id = await create_resume(resume.dict())
    return {"id": resume_id, **resume.dict()}

@router.get("/")
async def list_all():
    return await get_all_resumes()

@router.get("/{resume_id}")
async def get(resume_id: str):
    r = await get_resume(resume_id)
    if not r:
        raise HTTPException(404, "Resume not found")
    return r
