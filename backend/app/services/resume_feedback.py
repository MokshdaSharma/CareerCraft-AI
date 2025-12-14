from pathlib import Path
from app.services.llm_service import call_llm

REVIEW_PROMPT = Path("app/prompts/resume_review.txt").read_text()
ATS_PROMPT = Path("app/prompts/ats_improvement.txt").read_text()


def generate_resume_feedback(resume_text, job_description, ats_score):
    review = call_llm(
        REVIEW_PROMPT + f"\n\nJOB DESCRIPTION:\n{job_description}\n\nRESUME:\n{resume_text}",
        system_role="You are an expert resume reviewer."
    )

    ats_feedback = call_llm(
        ATS_PROMPT.format(
            ats_score=ats_score,
            missing_keywords="See ATS breakdown",
            job_description=job_description,
            resume_text=resume_text
        ),
        system_role="You are an ATS optimization expert."
    )

    return {
        "resume_review": review,
        "ats_improvement": ats_feedback
    }
