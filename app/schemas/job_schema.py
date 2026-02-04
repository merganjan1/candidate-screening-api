from pydantic import BaseModel
from typing import List
from datetime import datetime


class JobCreate(BaseModel):
    title: str
    description: str
    required_skills: List[str]
    min_experience_years: int
    is_active: bool = True


class JobResponse(JobCreate):
    id: str
    created_at: datetime
