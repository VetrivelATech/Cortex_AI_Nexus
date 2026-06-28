from fastapi import APIRouter
from pydantic import BaseModel
import sys
from pathlib import Path

# root add
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engines.skill_gap_engine import SkillGapEngine

router = APIRouter()


class SkillRequest(BaseModel):
    target_role: str
    user_skills: list


@router.post("/analyze-skills")
async def analyze_skills(data: SkillRequest):

    analyzer = SkillGapEngine()

    result = analyzer.analyze_skill_gap(
        data.target_role,
        data.user_skills
    )

    return result