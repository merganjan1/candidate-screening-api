from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.resume_schema import ResumeCreate
from app.services.resume_service import (
    create_resume,
    get_all_resumes,
    get_resume
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"]
)

# 🔒 CREATE — faqat login qilingan user
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_resume_endpoint(
    resume: ResumeCreate,
    current_user=Depends(get_current_user)
):
    resume_id = await create_resume(resume.dict())
    return {
    "id": str(resume_id),
    **resume.dict()
}



# 🔒 LIST — faqat login qilingan user
@router.get("/")
async def list_all_resumes(
    current_user=Depends(get_current_user)
):
    return await get_all_resumes()


# 🔒 GET BY ID — faqat login qilingan user
@router.get("/{resume_id}")
async def get_resume_by_id(
    resume_id: str,
    current_user=Depends(get_current_user)
):
    resume = await get_resume(resume_id)
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    return resume
