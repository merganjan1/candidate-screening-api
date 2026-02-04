from datetime import datetime
from bson import ObjectId
from app.db.mongodb import jobs_collection


async def create_job(data: dict):
    job = {
        "title": data["title"],
        "description": data["description"],
        "required_skills": data["required_skills"],
        "min_experience_years": data["min_experience_years"],
        "is_active": data.get("is_active", True),
        "created_at": datetime.utcnow()
    }
    result = await jobs_collection.insert_one(job)
    return str(result.inserted_id)


async def get_job(job_id: str):
    return await jobs_collection.find_one({"_id": ObjectId(job_id)})


async def list_jobs(filters: dict):
    query = {}
    if "is_active" in filters:
        query["is_active"] = filters["is_active"]
    return jobs_collection.find(query)


async def deactivate_job(job_id: str):
    await jobs_collection.update_one(
        {"_id": ObjectId(job_id)},
        {"$set": {"is_active": False}}
    )
