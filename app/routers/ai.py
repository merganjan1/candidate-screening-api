from fastapi import APIRouter
from app.services.ai_service import score_resume

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/score")
def score(data: dict):
    score = score_resume(
        resume_text=data["resume_text"],
        job_text=data["job_text"]
    )
    return {
        "score": score,
        "status": "success"
    }
