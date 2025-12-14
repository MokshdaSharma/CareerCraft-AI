from app.utils.keyword_extractor import extract_keywords
from app.utils.text_cleaner import detect_sections
from app.utils.action_verbs import count_action_verbs
from app.services.similarity import calculate_similarity


def calculate_ats_score(resume_text: str, job_description: str) -> dict:
    # --- Keywords ---
    resume_keywords = set(extract_keywords(resume_text))
    jd_keywords = set(extract_keywords(job_description))

    matched_keywords = resume_keywords.intersection(jd_keywords)
    keyword_score = min(40, len(matched_keywords) / max(len(jd_keywords), 1) * 40)

    # --- Sections ---
    sections = detect_sections(resume_text)
    section_score = sum(sections.values()) / len(sections) * 20

    # --- Semantic Similarity ---
    similarity = calculate_similarity(resume_text, job_description)
    similarity_score = min(20, similarity / 100 * 20)

    # --- Action Verbs ---
    action_count = count_action_verbs(resume_text)
    action_score = min(10, action_count)

    # --- Length Heuristic ---
    word_count = len(resume_text.split())
    if 300 <= word_count <= 900:
        length_score = 10
    elif 200 <= word_count <= 1200:
        length_score = 6
    else:
        length_score = 3

    total_score = round(
        keyword_score +
        section_score +
        similarity_score +
        action_score +
        length_score, 2
    )

    return {
        "score": total_score,
        "breakdown": {
            "keyword_match": round(keyword_score, 2),
            "sections": round(section_score, 2),
            "semantic_similarity": round(similarity_score, 2),
            "action_verbs": round(action_score, 2),
            "length_format": length_score
        },
        "matched_keywords": list(matched_keywords),
        "missing_keywords": list(jd_keywords - resume_keywords)
    }
