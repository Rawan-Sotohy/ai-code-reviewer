from fastapi import APIRouter

from app.core.schemas import EvaluationRequest, EvaluationResponse
from app.evaluation.service import evaluate_submission

router = APIRouter()


@router.post("/evaluate", response_model=EvaluationResponse)
def evaluate(request: EvaluationRequest):
    return evaluate_submission(request)