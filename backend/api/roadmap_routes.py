from fastapi import APIRouter
from pydantic import BaseModel
import sys
from pathlib import Path

# root add
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engines.roadmap_generator import RoadmapGenerator

router = APIRouter()


class RoadmapRequest(BaseModel):
    goal: str
    months: int


@router.post("/generate-roadmap")
async def generate_roadmap(data: RoadmapRequest):

    generator = RoadmapGenerator()

    result = generator.generate_roadmap(
        data.goal,
        data.months
    )

    return result