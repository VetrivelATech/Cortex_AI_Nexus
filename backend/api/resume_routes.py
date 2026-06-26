from fastapi import APIRouter, UploadFile, File
import os
from engines.resume_analyzer import ResumeAnalyzer

router = APIRouter()


@router.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    analyzer = ResumeAnalyzer()

    result = analyzer.analyze_resume(file_path)

    return result