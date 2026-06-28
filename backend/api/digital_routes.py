from fastapi import APIRouter
from pydantic import BaseModel
from engines.digital_twin_engine import DigitalTwinEngine

router = APIRouter()


class DigitalTwinRequest(BaseModel):
    resume_score: int
    github_score: int
    skill_score: int
    consistency: int


@router.post("/digital-twin")
async def digital_twin(data: DigitalTwinRequest):

    engine = DigitalTwinEngine()

    result = engine.analyze(
        data.resume_score,
        data.github_score,
        data.skill_score,
        data.consistency
    )

    return result