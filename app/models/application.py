from datetime import datetime

application = {
    "job_id": job_id,
    "candidate_name": candidate_name,
    "email": email,
    "resume_text": resume_text,
    "status": "processing",
    "score": None,
    "ai_department": None,
    "ai_department_score": None,
    "created_at": datetime.utcnow(),
    "scored_at": None
}
