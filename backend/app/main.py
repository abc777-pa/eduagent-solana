from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os, hashlib, time

app = FastAPI(title="EduAgent Pilot Mock")

# Разрешаем запросы с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модель запроса для оплаты
class PayRequest(BaseModel):
    student_id: str
    amount_kzte: float

@app.get("/health")
def health():
    return {"status": "ok", "service": "eduagent-mock"}

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

# Модель запроса для NFT
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
