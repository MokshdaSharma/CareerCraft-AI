from fastapi import APIRouter
from app.services.interview_engine import (
    generate_interview_questions,
    evaluate_answer
)
from app.models.interview_models import AnswerEvaluationRequest

router = APIRouter()


@router.post("/questions")
def get_questions(role: str, experience_level: str = "fresher"):
    """
    Generate role-specific interview questions
    """
    questions = generate_interview_questions(role, experience_level)
    return {"questions": questions}


@router.post("/evaluate")
def evaluate(response: AnswerEvaluationRequest):
    """
    Evaluate interview answer
    """
    result = evaluate_answer(
        question=response.question,
        answer=response.answer,
        role=response.role
    )
    return result
