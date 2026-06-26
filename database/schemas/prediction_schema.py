from pydantic import BaseModel

class PredictionRequest(BaseModel):
    resume_score: int
    dsa_score: int
    project_score: int
    communication_score: int
    consistency_score: int