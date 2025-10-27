# 🧠 EduAgent — AI Assistant for Schools on Solana  

![Solana](https://img.shields.io/badge/Built%20on-Solana-9945FF)
![Hackathon](https://img.shields.io/badge/Event-Cypherpunk%202025-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

<p align="center">
  <img src="assets/banner.png" alt="EduAgent banner" width="700"/>
</p>

> 🏆 Built for **Solana Cypherpunk Hackathon 2025**

---

## Table of Contents
- [Overview](#-overview)
- [Pitch Summary](#-pitch-summary)
- [Features](#-features)
- [Solana Integration](#-solana-integration)
- [Problem & Vision](#-problem--vision)
- [Tech Stack](#-tech-stack)
- [AI & Gamification](#-ai--gamification)
- [Pilot Integration](#-pilot-integration)
- [Roadmap](#️-roadmap)
- [Team](#-team)
- [Extra Module — AI Sales Assistant](#-extra-module--ai-sales-assistant)
- [Installation](#-installation)
- [Environment Setup](#-environment-setup)
- [Submission Links](#-submission-links)
- [License](#-license)
- [Local Description (RU)](#-local-description-ru)

---

## 🌍 Overview  

EduAgent is a pilot project bridging **Kazakhstan’s educational system** and **Solana blockchain**.  
It enables schools to accept **stablecoin (KZTE / USDC)** payments while gamifying student motivation through **AI-generated NFT badges** for attendance, performance, and engagement.  

Built by: **Rakhman Ibragimov 🇰🇿**  
Location: **Kazakhstan**  
Tracks: Stablecoins / RWAs / Consumer Apps / Infrastructure  

---

## 🎯 Pitch Summary  

EduAgent is an AI-powered assistant for schools in Kazakhstan  
that combines tuition payments and student motivation through on-chain NFT achievements on Solana.  
The project solves real transparency and engagement problems  
as part of the **Digital Tenge pilot with Intebix and Eurasian Bank**.  

---

## 🚀 Features  

- 💰 Tuition payments with **Digital Tenge (KZTE)** and **USDC** via Solana Devnet  
- 🧾 Mock integration with **Intebix × Eurasian Bank** pilot gateway  
- 🎓 NFT achievements using **Metaplex Standard**  
- 🤖 AI gamification powered by **FastAPI + Gemini/OpenAI**  
- 🔒 Secure and auditable transactions on **Solana blockchain**  

---

## 🔗 Solana Integration  

EduAgent uses **Solana Devnet** to tokenize payment confirmations and mint achievement NFTs.  
Each transaction is recorded on-chain through a custom Solana program and verified via the RPC API.  

Without Solana, the system would lose transparency and proof-of-ownership —  
on-chain logic ensures every NFT represents a real verified milestone.  

---

## 💡 Problem & Vision  

Kazakhstan is pioneering one of the world’s first **Digital Tenge pilots**,  
yet most schools still rely on cash payments and manual reporting.  

EduAgent creates a transparent digital ecosystem where  
tuition, performance, and achievements are unified on-chain.  

**Vision:**  
AI-driven education meets transparent blockchain finance.  

---

## 🧩 Tech Stack  

| Layer | Technology |  
|--------|-------------|  
| Frontend | HTML + JavaScript |  
| Backend | FastAPI (Python) |  
| Blockchain | Solana Web3.js (Devnet) |  
| Payments | Mock Intebix × Eurasian Bank Gateway |  
| Database | Supabase / PostgreSQL |  
| NFTs | Metaplex NFT Standard |  

---

## 🧠 AI & Gamification  

EduAgent transforms learning into an interactive experience.  
AI tracks progress, analyzes engagement, and suggests goals while rewarding students with NFTs.  

🏅 **Example Badges:**  
- “STEM Explorer” — for winning a science olympiad  
- “Perfect Attendance” — for consistent participation  
- “Kindness Token” — for helping classmates  
- “AI Mentor Badge” — for completing AI-guided courses  

---

## 🧾 Pilot Integration  

EduAgent simulates the **Intebix × Eurasian Bank pilot** for Digital Tenge payments using Solana Devnet.  
Each transaction is mock-verified and returned with a blockchain hash:  

```json
{
  "status": "success",
  "gateway": "intebix-pilot-mock",
  "bank_ref": "EB-PILOT-2025-01",
  "tx_hash": "DEVNET_TX_97260d07d2bcc70342ddca3663eb4fae"
}
```

[🔍 View Example Transaction on Solana Explorer](https://explorer.solana.com/tx/DEVNET_TX_97260d07d2bcc70342ddca3663eb4fae?cluster=devnet)

---

## 🛣️ Roadmap

| Quarter | Milestone |
|----------|------------|
| Q4 2025 | Pilot launch with KZTE + Intebix (mock integration) |
| Q1 2026 | Real NFT minting on Solana Devnet |
| Q2 2026 | Integration with Solana Pay and school CRMs |
| Q3 2026 | Public rollout across Kazakhstan |
| 2027 | Expansion to Central Asia and EduCoin token model |

---

## 👥 Team

**Rakhman Ibragimov** — Founder & Developer  
Expertise: Solana Devnet, FastAPI, AI gamification, education tech.  
Building EduAgent full-time after Cypherpunk Hackathon.  

---

## 🧠 Extra Module — AI Sales Assistant  

Located in `/tools/asketh_bot.py` — a Gemini-powered console bot simulating natural conversations  
for English course sales. It demonstrates EduAgent’s capability for **AI-driven customer interaction** and **personalized learning guidance**.  

🪄 Principle: *“Don’t sell air — guide students toward results.”*  

---

## 📦 Installation

```bash
git clone https://github.com/abc777-pa/eduagent-solana.git
cd eduagent-solana
pip install -r requirements.txt
uvicorn backend.app.main:app --reload --port 8000
```

Then open the frontend:

```bash
python -m http.server 5500
```

---

## 🧩 Environment Setup

```ini
RPC_URL=https://api.devnet.solana.com
SECRET_KEY_JSON=[ ... ]
KZTE_MINT=PASTE_MINT_ADDRESS_HERE
SCHOOL_WALLET=PASTE_SCHOOL_PUBKEY_HERE
PORT=8000
```

---

## 🧭 Submission Links  

- 🔗 **GitHub:** [https://github.com/abc777-pa/eduagent-solana](https://github.com/abc777-pa/eduagent-solana)  
- 🏁 **Colosseum:** [https://arena.colosseum.org/](https://arena.colosseum.org/)  
- 💬 **Superteam KZ:** [https://t.me/Superteamkz_cypherpunk](https://t.me/Superteamkz_cypherpunk)  

---

## 📜 License  

**MIT License © 2025 Rakhman Ibragimov**  
Built with ❤️ for Solana Cypherpunk Hackathon 2025 
