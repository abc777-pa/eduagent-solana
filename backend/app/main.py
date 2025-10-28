# --- AI (Gemini) логика ---
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
GENAI_MODEL = os.getenv("GENAI_MODEL", "gemini-1.5-flash-002")  # актуальная модель

_ai_client = None
if GENAI_API_KEY and genai is not None:
    try:
        _ai_client = genai.Client(api_key=GENAI_API_KEY)
    except Exception:
        _ai_client = None

class AIRequest(BaseModel):
    question: str

def _ask_gemini(question: str):
    """Пробуем несколько id моделей на случай несовпадений версии SDK."""
    if _ai_client is None:
        raise HTTPException(status_code=503, detail="AI not configured (GENAI_API_KEY / google-genai)")

    candidates = [
        GENAI_MODEL,                      # из ENV
        "gemini-1.5-flash-002",           # текущий стабильный
        "gemini-1.5-flash-latest",        # alias
        "gemini-1.5-flash-001",           # прошлый
    ]
    last_err = None
    for model in candidates:
        try:
            resp = _ai_client.models.generate_content(
                model=model,
                contents=[{"role": "user", "parts": [{"text": question}]}],
            )
            text = getattr(resp, "text", None) or getattr(resp, "output_text", "")
            if text:
                return {"model": model, "reply": text}
            last_err = f"Empty response from {model}"
        except Exception as e:
            last_err = f"{type(e).__name__}: {e}"
            continue
    raise HTTPException(status_code=500, detail=f"AI error: {last_err}")

@app.post("/api/ai", tags=["ai"])
def ask_ai(req: AIRequest):
    return _ask_gemini(req.question)
