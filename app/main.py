from fastapi import FastAPI
from app.routes.resumes import router as resumes_router
from app.routes.screenings import router as screenings_router

app = FastAPI()

app.include_router(resumes_router)
app.include_router(screenings_router)
