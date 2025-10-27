# 🧠 EduAgent — AI Assistant for Schools on Solana

![Solana](https://img.shields.io/badge/Built%20on-Solana-9945FF)
![Hackathon](https://img.shields.io/badge/Event-Cypherpunk%202025-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

<p align="center">
  <img src="assets/banner.png" alt="EduAgent banner" width="800"/>
</p>

> 🏆 Built for **Solana Cypherpunk Hackathon 2025**

---

## 🧩 Table of Contents
- [Overview](#-overview)
- [Architecture](#-architecture)
- [Data Flow](#-data-flow)
- [Backend Logic](#-backend-logic)
- [Frontend Integration](#-frontend-integration)
- [Solana Layer](#-solana-layer)
- [Devnet Deployment](#-devnet-deployment)
- [AI Layer](#-ai-layer)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Deployment](#-deployment)
- [Roadmap](#-roadmap)
- [Team](#-team)
- [Installation](#-installation)
- [Environment Setup](#-environment-setup)
- [License](#-license)

---

## 🌍 Overview

**EduAgent** is an AI-powered assistant and payment system for schools in Kazakhstan, built on **Solana Devnet** with integration of **KZTE stablecoin** and **USDC**.  
The project focuses on transparent tuition payments, on-chain progress tracking, and gamified learning rewards for students and parents.

Built by: **Rakhman Ibragimov 🇰🇿**  
Tracks: Stablecoins / Infrastructure / Consumer Apps

---

## ⚙️ Architecture

```mermaid
flowchart TD
  subgraph Frontend
    Web[Web Dashboard (HTML/JS)]
    TG[Telegram Bot (Telebot)]
  end

  subgraph Backend
    API[REST API endpoints]
    AI[AI Engine (Gemini)]
    Pay[Payment verification]
    RPC[RPC middleware between Frontend and Solana]
  end

  subgraph Solana
    Client[solana-py client]
    Devnet[Devnet RPC Node]
    Token[Token and NFT minting]
    Prog[Smart Program (mock) for receipts]
  end

  Web --> API
  TG --> API
  API --> Pay
  Pay --> RPC
  RPC --> Client
  Client --> Devnet
  Devnet --> Token
  Token --> Prog
🔁 Data Flow
Example: Tuition Payment with KZTE (Devnet)

User runs /pay in Telegram.

Backend calls Solana RPC for balance check.

Transaction is simulated (send_transaction).

Response includes tx_hash and confirmation.

Telegram or Web UI shows blockchain receipt.

NFT “Tuition Verified” badge is minted on-chain.

json
{
  "status": "success",
  "student": "ST-1024",
  "amount": "120.00 KZTE",
  "gateway": "intebix-pilot-mock",
  "tx_hash": "5tR7WbEExHzGNhzFbQdoQPa8CeqvGqEwqZ8L1ENbchQ3"
}
🧱 Backend Logic
All backend logic runs inside /backend/app/main.py (FastAPI).

python
@app.get("/healthz")
def health():
    return {"rpc": "ok", "version": client.get_version()}

@app.post("/api/pay")
def create_payment(payload: PaymentSchema):
    tx = client.send_transaction(payload)
    return {"status": "success", "tx_hash": tx["result"]}

@app.post("/api/ai")
def ask_ai(question: Question):
    resp = gemini.generate(question.text)
    return {"reply": resp.text}
💻 Frontend Integration
Web Example

javascript
async function getBalance(pubkey) {
  const res = await fetch(`/api/solana/balance?pubkey=${pubkey}`);
  const data = await res.json();
  document.getElementById('balance').innerText = `${data.balance} SOL`;
}
Telegram Commands

/balance <pubkey>

/pay

/ask <question>

🔗 Solana Layer
Implemented using solana-py and Web3.js.

python
client = Client("https://api.devnet.solana.com")
balance = client.get_balance(pubkey)
signature = client.send_transaction(tx, signer)
status = client.get_signature_status(signature)
Programs used:

System Program

Token Program (USDC, KZTE)

Metaplex (NFT minting)

🧪 Devnet Deployment
For testing and verification, EduAgent runs on Solana Devnet. All program interactions, token mints, and NFT achievements are testable.

Network Configuration

makefile
RPC_URL=https://api.devnet.solana.com
CLUSTER=devnet
Status: Active
Smart Contract (Program)
Program ID: 8ZC6yb6Vn2wJUZKdrL2oW5pqQFVRFpDYqDb1w8VbyybH
Handles mock tuition payments and triggers NFT minting after verification.
View Program on Explorer

Stablecoin Integration
Token	Mint Address	Description
KZTE (Digital Tenge)	4R4Ve5xHaHzZLJxKcL5UZFXEhCFgC7yUv3xHpoZSnQfL	Mock stablecoin for schools
USDC (Devnet)	7XS1EibDL5ShKRYtRmr7nhJYt6SKCqMKeDRrBQ1iR9rJ	Official Solana Devnet USDC mint

View KZTE Mint

School Wallet & NFT Mint
Component	Devnet Address	Function
School Treasury Wallet	9kR8ZZ9D3RQkWkY8Z1MpvBxTSD7SMF85i4iDqEfeQ6Ef	Receives tuition
Achievement NFT Mint	B71mZqYRi6gqH4mGafSkaoGbTtVfB2ELbKq9bPKRrj6t	Issues student badges

View NFT Example

🤖 AI Layer
EduAgent uses Gemini 1.5 Flash for natural conversation and gamification.
The assistant adapts to each school’s data and supports English, Russian, and Kazakh.

Prompt:

scss
You are EduAgent — an AI assistant for schools in Kazakhstan.
Help parents manage tuition, progress, and attendance.
API Example:

bash
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
Backend	FastAPI, Flask, Python 3.10+
Blockchain	Solana Devnet (solana-py, Web3.js)
AI	Google Gemini (genai SDK)
Payments	Mock Intebix × Eurasian Bank
Database	Supabase / PostgreSQL
NFTs	Metaplex

☁️ Deployment
Local

bash
uvicorn backend.app.main:app --reload --port 8000
python -m http.server 5500
Production Options

Platform	Purpose	Notes
Render	FastAPI hosting	Free tier
Railway	RPC-ready backend	Easy Docker deploy
Fly.io	Secure env	Auto scaling
Vercel	Web dashboard	Static hosting

🛣️ Roadmap
Quarter	Milestone
Q4 2025	Pilot launch with KZTE + mock Intebix
Q1 2026	NFT reward system via Metaplex
Q2 2026	Solana Pay integration
Q3 2026	Wider pilot with partner schools
Q4 2026	Kazakhstan school rollout

👥 Team
Rakhman Ibragimov — Founder & Developer
Expertise: Solana, FastAPI, AI, Education Tech
Community: Superteam KZ × Solana Builders

📦 Installation
bash
git clone https://github.com/abc777-pa/eduagent-solana.git
cd eduagent-solana
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
Frontend:

bash
python -m http.server 5500
⚙️ Environment Setup
ini
RPC_URL=https://api.devnet.solana.com
SECRET_KEY_JSON=[ ... ]
KZTE_MINT=4R4Ve5xHaHzZLJxKcL5UZFXEhCFgC7yUv3xHpoZSnQfL
SCHOOL_WALLET=9kR8ZZ9D3RQkWkY8Z1MpvBxTSD7SMF85i4iDqEfeQ6Ef
GENAI_API_KEY=PASTE_KEY
PORT=8000
📜 License
MIT License © 2025 Rakhman Ibragimov
Built with ❤️ for Solana Cypherpunk Hackathon 2025
