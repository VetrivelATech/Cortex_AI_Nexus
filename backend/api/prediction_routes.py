from fastapi import APIRouter
from engines.placement_predictor import PlacementPredictor
from database.schemas.prediction_schema import PredictionRequest

router = APIRouter()

@router.post("/predict-placement")
def predict_placement(data: PredictionRequest):

    predictor = PlacementPredictor(
        resume_score=data.resume_score,
        dsa_score=data.dsa_score,
        project_score=data.project_score,
        communication_score=data.communication_score,
        consistency_score=data.consistency_score
    )

    return predictor.generate_prediction_report()