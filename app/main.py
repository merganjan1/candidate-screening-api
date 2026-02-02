from fastapi import FastAPI
from app.routes.job import router as job_router

app = FastAPI()

app.include_router(job_router)
