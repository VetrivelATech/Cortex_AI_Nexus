# backend/api/interview_routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from engines.interview_engine import InterviewEngine

router = APIRouter()

class InterviewRequest(BaseModel):
    role: str


@router.post("/generate-interview")

async def generate_interview(data: InterviewRequest):

    engine = InterviewEngine()

    result = engine.generate_questions(data.role)

    return result