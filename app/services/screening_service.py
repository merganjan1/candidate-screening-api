from datetime import datetime
from app.db.mongodb import screenings_collection


async def create_screening(data: dict):
    screening = {
        "resume_id": data["resume_id"],
        "status": "pending",
        "ai_department": None,
        "ai_department_score": None,
        "created_at": datetime.utcnow(),
        "scored_at": None
    }

    result = await screenings_collection.insert_one(screening)
    return str(result.inserted_id)
