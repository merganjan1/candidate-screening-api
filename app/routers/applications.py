from fastapi import APIRouter, BackgroundTasks
from app.services.background import process_application
from bson import ObjectId

@router.post("/jobs/{job_id}/apply")
async def apply(
    job_id: str,
    data: dict,
    background_tasks: BackgroundTasks
):
    application = {
        "job_id": job_id,
        "candidate_name": data["candidate_name"],
        "email": data["email"],
        "resume_text": data["resume_text"],
        "status": "processing"
    }

    result = await applications_collection.insert_one(application)

    background_tasks.add_task(
        process_application,
        str(result.inserted_id),
        data["resume_text"]
    )

    return {
        "message": "Application submitted",
        "application_id": str(result.inserted_id)
    }

@router.get("/applications/{id}/ai-evaluation")
async def ai_evaluation(id: str):
    app = await applications_collection.find_one({"_id": ObjectId(id)})
    return {
        "department_recommendation": app["ai_department"],
        "department_score": app["ai_department_score"],
        "status": app["status"]
    }
