from pydantic import BaseModel


class AnswerEvaluationRequest(BaseModel):
    role: str
    question: str
    answer: str
