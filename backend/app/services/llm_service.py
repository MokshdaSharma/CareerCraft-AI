from openai import OpenAI, RateLimitError
from app.config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)


def call_llm(prompt: str, system_role: str = "You are a helpful AI career coach."):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        # Graceful fallback (VERY IMPORTANT)
        return (
            "⚠️ AI response unavailable due to API quota limits.\n\n"
            "This is a fallback response.\n\n"
            "SUGGESTIONS:\n"
            "- Add more role-specific keywords\n"
            "- Improve bullet points with measurable impact\n"
            "- Ensure clear section headings\n"
            "- Optimize resume for ATS parsing\n"
        )

    except Exception as e:
        return f"❌ AI service error: {str(e)}"
