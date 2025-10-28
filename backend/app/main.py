# backend/app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os, hashlib, time

# --- Безопасный импорт SDK Google ---
try:
    from google import genai  # требует пакет google-genai (см. requirements.txt)
except Exception:
    genai = None  # сервис не упадёт, просто отключит /api/ai

app = FastAPI(title="EduAgent Pilot Mock", version="1.0.0")

# --- CORS, чтобы веб/бот могли дергать бэкенд ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
#        SCHEMAS
# =========================
class PayRequest(BaseModel):
    student_id: str
    amount_kzte: float

class MintRequest(BaseModel):
    student_wallet: str
    badge: str

class AIRequest(BaseModel):
    question: str


# =========================
#        HEALTH
# =========================
@app.get("/health")
def health():
    ai_ready = bool(os.getenv("GENAI_API_KEY")) and genai is not None
    return {
        "status": "ok",
        "service": "eduagent-mock",
        "ai": "ready" if ai_ready else "disabled",
        "model": os.getenv("GENAI_MODEL", "gemini-1.5-flash-002"),
    }


# =========================
#        PAY (MOCK)
# =========================
@app.post("/api/pay")
def pay(req: PayRequest):
    seed = f"{req.student_id}-{req.amount_kzte}-{time.time()}"
    tx_hash = hashlib.sha256(seed.encode()).hexdigest()[:32]
    return {
        "status": "success",
        "gateway": "intebix-pilot-mock",
        "bank_ref": "EB-PILOT-2025-01",
        "tx_hash": f"DEVNET_TX_{tx_hash}",
    }


# =========================
#        MINT (MOCK)
# =========================
@app.post("/api/mint")
def mint(req: MintRequest):
    fake_mint = hashlib.md5(f"{req.student_wallet}-{req.badge}".encode()).hexdigest()
    return {
        "status": "queued",
        "badge": req.badge,
        "mint_address": f"FAKE_MINT_{fake_mint[:32]}",
        "note": "Use scripts/mint_nft.ts to mint on Devnet for real.",
    }


# =========================
#        AI (GEMINI)
# =========================
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
# можно переопределить модель через переменную окружения GENAI_MODEL
GENAI_MODEL = os.getenv("GENAI_MODEL", "gemini-1.5-flash-002")

_ai_client = None
if GENAI_API_KEY and genai is not None:
    try:
        _ai_client = genai.Client(api_key=GENAI_API_KEY)
    except Exception:
        _ai_client = None  # не валим приложение на старте

def _ask_gemini(question: str) -> dict:
    if _ai_client is None:
        raise HTTPException(
            status_code=503,
            detail="AI not configured (set GENAI_API_KEY and install google-genai)",
        )

    # Список кандидатов — если один id не поддерживается текущей версией SDK
    candidates = [
        GENAI_MODEL,                 # из ENV
        "gemini-1.5-flash-002",      # стабильный
        "gemini-1.5-flash-latest",   # алиас
        "gemini-1.5-flash-001",      # прошлый
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
