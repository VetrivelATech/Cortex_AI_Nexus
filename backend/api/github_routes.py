from fastapi import APIRouter
import sys
from pathlib import Path

# project root add
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engines.github__analyzer import GitHubAnalyzer

router = APIRouter()

@router.get("/analyze-github/{username}")
async def analyze_github(username: str):
    analyzer = GitHubAnalyzer()
    result = analyzer.analyze_github(username)
    return result