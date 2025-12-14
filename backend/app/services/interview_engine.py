from pathlib import Path
from app.services.llm_service import call_llm

QUESTION_PROMPT = Path("app/prompts/interview_questions.txt").read_text()
ANSWER_PROMPT = Path("app/prompts/answer_feedback.txt").read_text()


def generate_interview_questions(role: str, experience_level: str):
    prompt = QUESTION_PROMPT.format(
        role=role,
        experience_level=experience_level
    )
    return call_llm(prompt, system_role="You are an expert interviewer.")


def evaluate_answer(question: str, answer: str, role: str):
    prompt = ANSWER_PROMPT.format(
        role=role,
        question=question,
        answer=answer
    )
    return call_llm(prompt, system_role="You are a strict but fair interviewer.")
