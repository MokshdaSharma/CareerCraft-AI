import re
from collections import Counter

STOPWORDS = {
    "and", "or", "the", "a", "an", "with", "to", "of", "in", "for", "on"
}

def extract_keywords(text: str, top_n: int = 30):
    words = re.findall(r"[a-zA-Z]{3,}", text.lower())
    filtered = [w for w in words if w not in STOPWORDS]
    return [w for w, _ in Counter(filtered).most_common(top_n)]
