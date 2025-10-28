# 🧠 EduAgent — AI Assistant for Schools on Solana

<p align="center">
  <img src="assets/banner_dark.png" alt="EduAgent Banner" width="850"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20on-Solana-9945FF?style=for-the-badge&logo=solana" />
  <img src="https://img.shields.io/badge/Event-Cypherpunk%202025-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

> 🏆 Built for **Solana Cypherpunk Hackathon 2025**  
> 🇰🇿 Powered by **AImpact + Superteam KZ**

---

## 🌍 Overview

**EduAgent** is an AI-powered assistant and payment system for schools in Kazakhstan —  
built on **Solana Devnet**, integrated with **KZTE stablecoin** and **USDC**.  

It provides **transparent tuition payments**, **on-chain student progress tracking**, and **gamified NFT rewards** for achievements.

> “EduAgent transforms education into a Web3 experience.”

---

## 🧩 Architecture

FRONTEND (Web + Telegram)
├─ Web Dashboard (HTML/JS)
└─ Telegram Bot (Telebot)
|
| HTTPS / WebSocket
v
BACKEND (FastAPI + Flask)
├─ REST API endpoints
├─ AI Engine (Gemini)
├─ Payment verification
└─ RPC middleware between Frontend and Solana
|
| JSON-RPC
v
SOLANA LAYER (Devnet)
├─ solana-py client
├─ Token & NFT minting
└─ Mock smart program for tuition receipts

yaml


---

## 🔁 Data Flow — Tuition Payment (KZTE)

1. Parent sends `/pay` in Telegram.  
2. Backend verifies balance via Solana RPC.  
3. Transaction executes on **Devnet**.  
4. Backend returns transaction hash.  
5. NFT “Tuition Verified” minted to student wallet.

```json
{
  "status": "success",
  "student": "ST-1024",
  "amount": "120.00 KZTE",
  "tx_hash": "5tR7WbEExHzGNhzFbQdoQPa8CeqvGqEwqZ8L1ENbchQ3"
}
⚙️ Backend Logic (FastAPI)
python
@app.post("/api/pay")
def create_payment(payload: PaymentSchema):
    tx = client.send_transaction(payload)
    return {"status": "success", "tx_hash": tx["result"]}

@app.post("/api/ai")
def ask_ai(question: Question):
    resp = gemini.generate(question.text)
    return {"reply": resp.text}
Healthcheck endpoint:

python
@app.get("/healthz")
def health():
    return {"rpc": "ok", "version": client.get_version()}
💻 Frontend Integration
Web (JavaScript):

js
async function getBalance(pubkey) {
  const res = await fetch(`/api/solana/balance?pubkey=${pubkey}`);
  const data = await res.json();
  document.getElementById('balance').innerText = `${data.balance} SOL`;
}
Telegram commands:
/balance <pubkey> • /pay • /ask <question>

🔗 Solana Layer
Implemented with solana-py + Web3.js.

python
client = Client("https://api.devnet.solana.com")
balance = client.get_balance(pubkey)
signature = client.send_transaction(tx, signer)
status = client.get_signature_status(signature)
Programs: System Program • Token Program (USDC, KZTE) • Metaplex NFT

Component	Address	Function
School Treasury Wallet	9kR8ZZ9D3RQkWkY8Z1MpvBxTSD7SMF85i4iDqEfeQ6Ef	Receives tuition
KZTE Stablecoin	4R4Ve5xHaHzZLJxKcL5UZFXEhCFgC7yUv3xHpoZSnQfL	Digital Tenge
Achievement NFT Mint	B71mZqYRi6gqH4mGafSkaoGbTtVfB2ELbKq9bPKRrj6t	Mints student badges

🤖 AI Layer
EduAgent uses Gemini 1.5 Flash for multilingual, natural interaction and gamification.

Prompt:

You are EduAgent — an AI assistant for schools in Kazakhstan.
Help parents manage tuition, progress, and attendance.

API Example:
POST /api/ai
{
  "question": "When is next math lesson?"
}
Response:

json
{"reply": "Math class starts at 10:30 AM tomorrow."}
🧰 Tech Stack
Layer	Technology
Frontend	HTML, JavaScript, Telegram Bot
Backend	FastAPI, Flask
Blockchain	Solana Devnet (solana-py, Web3.js)
AI	Google Gemini (genai SDK)
Payments	Mock Intebix × Eurasian Bank
Database	Supabase / PostgreSQL
NFTs	Metaplex
Hosting	Railway + Vercel

☁️ Deployment
Local Dev:

git clone https://github.com/abc777-pa/eduagent-solana.git
cd eduagent-solana
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
Frontend:
python -m http.server 5500
Environment (.env):

ini
RPC_URL=https://api.devnet.solana.com
SECRET_KEY_JSON=[ ... ]
KZTE_MINT=4R4Ve5xHaHzZLJxKcL5UZFXEhCFgC7yUv3xHpoZSnQfL
SCHOOL_WALLET=9kR8ZZ9D3RQkWkY8Z1MpvBxTSD7SMF85i4iDqEfeQ6Ef
GENAI_API_KEY=PASTE_KEY
PORT=8000
🗺️ Roadmap
Quarter	Milestone	Status
Q4 2025	Pilot launch with KZTE + Intebix mock	✅
Q1 2026	NFT reward system (Metaplex)	🔄
Q2 2026	Solana Pay integration	🧩
Q3 2026	Multi-school pilot rollout	⏳
Q4 2026	Nationwide EduAgent deployment	🌍

👥 Team
Member	Role	Location
Rakhman Ibragimov	Founder & Developer	Astana, Kazakhstan
AI Co-Pilot (GPT-5)	Tech Advisor	Cyberspace

Community: Superteam KZ × Solana Builders

📜 License
MIT License © 2025 Rakhman Ibragimov

Built with ❤️ for Solana Cypherpunk Hackathon 2025
Powered by Solana × AImpact × Superteam Kazakhstan

<p align="center"> <img src="assets/footer_dark.png" alt="EduAgent Footer" width="700"/> </p> <p align="center"> <b>Built with 💜 on Solana — where AI meets Education</b> </p> ```
