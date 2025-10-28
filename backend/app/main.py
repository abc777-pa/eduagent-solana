from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os, hashlib, time

# =============================
#   ИНИЦИАЛИЗАЦИЯ
# =============================
app = FastAPI(title="EduAgent Pilot Mock")

# Разрешаем запросы с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================
#   МОДЕЛИ ЗАПРОСОВ
# =============================
class PayRequest(BaseModel):
    student_id: str
    amount_kzte: float

class MintRequest(BaseModel):
    student_wallet: str
    badge: str

class AIRequest(BaseModel):
    question: str

# =============================
#   ЭНДПОИНТЫ
# =============================
@app.get("/health")
def health():
    ai_ready = bool(os.getenv("GENAI_API_KEY"))
    return {
        "status": "ok",
        "service": "eduagent-mock",
        "ai": "ready" if ai_ready else "disabled",
        "model": "gemini-2.5-flash",
    }

@app.post("/api/pay")
def pay(req: PayRequest):
    seed = f"{req.student_id}-{req.amount_kzte}-{time.time()}"
    tx_hash = hashlib.sha256(seed.encode()).hexdigest()[:32]
    return {
        "status": "success",
        "gateway": "intebix-pilot-mock",
        "bank_ref": "EB-PILOT-2025-01",
        "tx_hash": f"DEVNET_TX_{tx_hash}"
    }

@app.post("/api/mint")
def mint(req: MintRequest):
    fake_mint = hashlib.md5(f"{req.student_wallet}-{req.badge}".encode()).hexdigest()
    return {
        "status": "queued",
        "badge": req.badge,
        "mint_address": f"FAKE_MINT_{fake_mint[:32]}",
        "note": "Use scripts/mint_nft.ts to mint on Devnet for real."
    }

# =============================
#   AI (Gemini 2.5 Flash)
# =============================
try:
    from google import genai
except ImportError:
    genai = None

GENAI_API_KEY = os.getenv("GENAI_API_KEY")
GENAI_MODEL = "gemini-2.5-flash"

_ai_client = None
if GENAI_API_KEY and genai is not None:
    try:
        _ai_client = genai.Client(api_key=GENAI_API_KEY)
    except Exception as e:
        print(f"[AI INIT ERROR] {e}")
        _ai_client = None

@app.post("/api/ai", tags=["ai"])
def ask_ai(req: AIRequest):
    if _ai_client is None:
        raise HTTPException(status_code=503, detail="AI not initialized or GENAI_API_KEY missing.")
    try:
        resp = _ai_client.models.generate_content(
            model=GENAI_MODEL,
            contents=[{"role": "user", "parts": [{"text": req.question}]}],
        )
        text = getattr(resp, "text", None) or getattr(resp, "output_text", "")
        if not text:
            raise ValueError("Empty response")
        return {"model": GENAI_MODEL, "reply": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI error: {str(e)}")

# =============================
#   ФИНАЛ
# =============================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
