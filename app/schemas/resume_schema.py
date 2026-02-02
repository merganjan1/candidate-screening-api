from pydantic import BaseModel
from typing import List

class ResumeCreate(BaseModel):
    full_name: str
    email: str
    skills: List[str]
    experience: int
    resume_text: str

class ResumeResponse(ResumeCreate):
    id: str
