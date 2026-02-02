from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)

db = client["candidate_screening"]

users_collection = db["users"]
resumes_collection = db["resumes"]
screenings_collection = db["screenings"]
jobs_collection = db["jobs"]
