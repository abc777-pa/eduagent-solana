from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os, hashlib, time

# --- AI: безопасный импорт SDK ---
try:
    from google import genai
except Exception:
    genai = None

app = FastAPI(title="EduAgent Pilot Mock", version="0.1.0")

# Разрешаем запросы с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Оплата (мок)
# -------------------------------
class PayRequest(BaseModel):
    student_id: str
    amount_kzte: float

@app.get("/health")
def health():
    """Показываем статус сервиса и готовность AI."""
    ai_ready = False
    if genai is not None and os.getenv("GENAI_API_KEY"):
        ai_ready = True
    return {"status": "ok", "service": "eduagent-mock", "ai": "ready" if ai_ready else "disabled"}

@app.post("/api/pay")
def pay(req: PayRequest):
    # Генерируем псевдо-хеш "транзакции devnet"
    seed = f"{req.student_id}-{req.amount_kzte}-{time.time()}"
    tx_hash = hashlib.sha256(seed.encode()).hexdigest()[:32]
    return {
        "status": "success",
        "gateway": "intebix-pilot-mock",
        "bank_ref": "EB-PILOT-2025-01",
        "tx_hash": f"DEVNET_TX_{tx_hash}"
    }

# -------------------------------
# NFT mint (мок)
# -------------------------------
class MintRequest(BaseModel):
    student_wallet: str
    badge: str

@app.post("/api/mint")
def mint(req: MintRequest):
    # Заглушка ответа "минта"
    fake_mint = hashlib.md5(f"{req.student_wallet}-{req.badge}".encode()).hexdigest()
    return {
        "status": "queued",
        "badge": req.badge,
        "mint_address": f"FAKE_MINT_{fake_mint[:32]}",
        "note": "Use scripts/mint_nft.ts to mint on Devnet for real."
    }

# -------------------------------
# >>> AI: инициализация клиента
# -------------------------------
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
_ai_client = None
if GENAI_API_KEY and genai is not None:
    try:
        _ai_client = genai.Client(api_key=GENAI_API_KEY)
    except Exception:
        _ai_client = None  # не валим сервис при ошибке SDK/ключа

class AIRequest(BaseModel):
    question: str

@app.post("/api/ai", tags=["ai"])
def ask_ai(req: AIRequest):
    """Простой AI-эндпоинт на Gemini 1.5 Flash."""
    if _ai_client is None:
        raise HTTPException(status_code=503, detail="AI not configured (set GENAI_API_KEY and install google-genai)")
    try:
        resp = _ai_client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[{"role": "user", "parts": [{"text": req.question}]}],
        )
        text = getattr(resp, "text", None) or getattr(resp, "output_text", "")
        return {"reply": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI error: {e}")
