from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import resume, interview

app = FastAPI(
    title="GenAI Resume & Interview Coach",
    version="1.0.0",
    description="LLM-powered resume review and interview coaching system"
)

# CORS (for Streamlit frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(resume.router, prefix="/resume", tags=["Resume"])
app.include_router(interview.router, prefix="/interview", tags=["Interview"])


@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "GenAI Resume & Interview Coach API is live 🚀"
    }
