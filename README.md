# 🤖 GenAI Resume & Interview Coach

An **AI-powered Resume Analyzer and Interview Coach** built using **Large Language Models (LLMs)** to help students and job seekers improve their resumes and prepare for interviews.

---

## Features

### Resume Analyzer
- Resume parsing (PDF / DOCX)
- ATS (Applicant Tracking System) score calculation
- ATS score breakdown with explainability
- Missing keyword detection
- AI-generated resume feedback
- ATS optimization suggestions

### Interview Coach
- Role-specific interview question generation
- Technical, behavioral, and scenario-based questions
- AI evaluation of answers
- Score-based feedback with strengths & gaps
- Model answer suggestions

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/your-username/genai-resume-interview-coach.git
cd resume-coach
```
Create .env file:
```bash
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
```

### Backend Setup

```bash
cd backend
python -m venv env
env\Scripts\activate     # Windows
# source env/bin/activate  # Mac/Linux

pip install -r requirements.txt
```

Run backend:
```bash
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
pip install -r requirements.txt
```

Run Streamlit:
```bash
streamlit run streamlit_app.py
```



