from datetime import datetime
from bson import ObjectId

from app.db.mongodb import screenings_collection, resumes_collection
from app.services.ai_service import ai_department_eval


async def process_screening(screening_id: str):
    print("BACKGROUND STARTED", screening_id)
    # pastdagi kodlar o‘z joyida qoladi

    screening = await screenings_collection.find_one(
        {"_id": ObjectId(screening_id)}
    )
    if not screening:
        return

    resume = await resumes_collection.find_one(
        {"_id": ObjectId(screening["resume_id"])}
    )
    if not resume:
        return

    department, score = ai_department_eval(resume["resume_text"])

    await screenings_collection.update_one(
        {"_id": ObjectId(screening_id)},
        {"$set": {
            "status": "scored",
            "ai_department": department,
            "ai_department_score": score,
            "scored_at": datetime.utcnow()
        }}
    )
