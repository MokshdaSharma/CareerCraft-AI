def detect_sections(resume_text: str):
    sections = {
        "experience": ["experience", "work history", "employment"],
        "skills": ["skills", "technical skills"],
        "education": ["education", "academic"],
        "projects": ["projects"],
        "summary": ["summary", "profile"]
    }

    found = {}
    lower_text = resume_text.lower()

    for section, keywords in sections.items():
        found[section] = any(k in lower_text for k in keywords)

    return found
