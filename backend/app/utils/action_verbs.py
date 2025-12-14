ACTION_VERBS = {
    "developed", "designed", "implemented", "built", "led",
    "optimized", "created", "improved", "analyzed", "deployed"
}

def count_action_verbs(text: str):
    words = set(text.lower().split())
    return len(words.intersection(ACTION_VERBS))
