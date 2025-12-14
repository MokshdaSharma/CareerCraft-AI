from fastapi import APIRouter, UploadFile, File, Form
from app.services.resume_parser import parse_resume
from app.services.ats_scorer import calculate_ats_score
from app.services.resume_feedback import generate_resume_feedback

router = APIRouter()


@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Upload resume + job description
    Returns ATS score + AI feedback
    """
    resume_text = await parse_resume(resume)

    ats_result = calculate_ats_score(
        resume_text=resume_text,
        job_description=job_description
    )

    feedback = generate_resume_feedback(
        resume_text=resume_text,
        job_description=job_description,
        ats_score=ats_result["score"]
    )

    return {
        "ats_score": ats_result,
        "feedback": feedback
    }
