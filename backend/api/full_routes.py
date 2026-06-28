from fastapi import APIRouter
from core.orchestrator import CortexOrchestrator

router = APIRouter()

@router.get("/full-analysis")
def full_analysis():

    cortex = CortexOrchestrator()

    result = cortex.run_pipeline()

    return {
        "status": "success",
        "message": "Full Cortex AI Analysis Completed",
        "data": result
    }