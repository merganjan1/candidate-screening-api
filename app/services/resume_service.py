from app.db.mongodb import resumes_collection
from bson import ObjectId


async def create_resume(data: dict):
    result = await resumes_collection.insert_one(data)
    return str(result.inserted_id)


async def get_all_resumes():
    resumes = []
    async for r in resumes_collection.find():
        r["_id"] = str(r["_id"])
        resumes.append(r)
    return resumes


async def get_resume(resume_id: str):
    r = await resumes_collection.find_one({"_id": ObjectId(resume_id)})
    if r:
        r["_id"] = str(r["_id"])
    return r
