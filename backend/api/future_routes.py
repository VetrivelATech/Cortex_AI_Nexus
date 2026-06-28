from fastapi import APIRouter
from pydantic import BaseModel
from engines.future_simulator import FutureSimulator

router = APIRouter()

class FutureRequest(BaseModel):
    study_hours: int
    projects: int
    consistency: int


@router.post("/simulate-future")
async def simulate_future(data: FutureRequest):

    simulator = FutureSimulator()

    result = simulator.simulate(
        data.study_hours,
        data.projects,
        data.consistency
    )

    return result