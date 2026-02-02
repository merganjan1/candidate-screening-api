from pydantic import BaseModel
from datetime import datetime
from typing import List

class JobCreate(BaseModel):
    title: str
    description: str
    department: str
    requirements: List[str]

class JobOut(JobCreate):
    id: str
    created_at: datetime
