from app.db.mongodb import screening_collection
from datetime import datetime

async def create_screening(data: dict):
    data["status"] = "pending"
    data["score"] = 0
    data["decision"] = None
    data["created_at"] = datetime.utcnow()
    result = await screening_collection.insert_one(data)
    return str(result.inserted_id)
