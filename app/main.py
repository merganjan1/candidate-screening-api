from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.resumes import router as resumes_router
from app.routers.screenings import router as screenings_router
from app.routers import ai

app = FastAPI()

app.include_router(auth_router)
app.include_router(resumes_router)
app.include_router(screenings_router)
app.include_router(ai.router)
