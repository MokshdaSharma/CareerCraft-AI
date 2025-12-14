import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

st.set_page_config(
    page_title="GenAI Resume & Interview Coach",
    layout="wide"
)

st.title("🤖 GenAI Resume & Interview Coach")

# Sidebar Navigation
page = st.sidebar.radio(
    "Navigate",
    ["Resume Analyzer", "Interview Coach"]
)

# -------------------------------
# Resume Analyzer
# -------------------------------
if page == "Resume Analyzer":
    st.header("📄 Resume Analyzer & ATS Checker")

    resume_file = st.file_uploader(
        "Upload your resume (PDF or DOCX)",
        type=["pdf", "docx"]
    )

    job_description = st.text_area(
        "Paste Job Description",
        height=200
    )

    if st.button("Analyze Resume"):
        if not resume_file or not job_description:
            st.warning("Please upload resume and paste job description")
        else:
            with st.spinner("Analyzing resume..."):
                response = requests.post(
                    f"{BACKEND_URL}/resume/analyze",
                    files={"resume": resume_file},
                    data={"job_description": job_description}
                )

                if response.status_code == 200:
                    data = response.json()

                    ats = data["ats_score"]

                    st.subheader("📊 ATS Score")
                    st.metric("Overall ATS Score", ats["score"])

                    st.subheader("🔍 Score Breakdown")
                    st.json(ats["breakdown"])

                    st.subheader("❌ Missing Keywords")
                    st.write(", ".join(ats["missing_keywords"]))

                    st.subheader("🧠 AI Resume Review")
                    st.markdown(data["feedback"]["resume_review"])

                    st.subheader("🚀 ATS Improvement Suggestions")
                    st.markdown(data["feedback"]["ats_improvement"])
                else:
                    st.error("Error analyzing resume")

# -------------------------------
# Interview Coach
# -------------------------------
if page == "Interview Coach":
    st.header("🎤 Interview Coach")

    role = st.text_input("Target Role", placeholder="e.g. Data Scientist")
    experience = st.selectbox(
        "Experience Level",
        ["fresher", "mid-level", "senior"]
    )

    if st.button("Generate Interview Questions"):
        if not role:
            st.warning("Please enter a role")
        else:
            response = requests.post(
                f"{BACKEND_URL}/interview/questions",
                params={"role": role, "experience_level": experience}
            )

            if response.status_code == 200:
                questions_text = response.json()["questions"]
                st.session_state.questions = questions_text.split("\n")
            else:
                st.error("Failed to generate questions")

    if "questions" in st.session_state:
        st.subheader("📝 Interview Questions")

        for idx, q in enumerate(st.session_state.questions):
            if q.strip():
                st.markdown(f"**Q{idx+1}: {q}**")

                answer = st.text_area(
                    f"Your Answer (Q{idx+1})",
                    key=f"answer_{idx}",
                    height=120
                )

                if st.button(f"Evaluate Answer {idx+1}", key=f"eval_{idx}"):
                    payload = {
                        "role": role,
                        "question": q,
                        "answer": answer
                    }

                    response = requests.post(
                        f"{BACKEND_URL}/interview/evaluate",
                        json=payload
                    )

                    if response.status_code == 200:
                        st.markdown("### 📊 Feedback")
                        st.markdown(response.text)
                    else:
                        st.error("Evaluation failed")
