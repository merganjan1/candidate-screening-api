from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)

db = client["candidate_screening"]
resumes_collection = db["resumes"]
screenings_collection = db["screenings"]

