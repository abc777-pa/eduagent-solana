🎓 EduAgent — AI Assistant for Schools on Solana

EduAgent connects schools in Kazakhstan to the Digital Tenge (KZTE) pilot via Solana blockchain.
It automates tuition payments and rewards students with NFT achievement badges powered by AI gamification.
Built during the Solana Cypherpunk Hackathon 2025.

🧠 Overview

Goal: Bring together education and Web3 finance.
EduAgent enables schools to accept stablecoin payments (KZTE / USDC) and reward students for attendance, quiz completion, and good performance through AI-tracked NFT achievements.
## 🌐 Demo Screenshot

![Demo Screenshot](assets/screenshot.png)

🔗 [Live Demo (localhost)](http://127.0.0.1:5500)  
🧠 [Backend API Docs](http://127.0.0.1:8000/docs)

Built by: Rakhman Ibragimov 🇰🇿
Location: Kazakhstan
Tracks: Stablecoins / RWAs · Consumer Apps · Infrastructure

⚙️ Tech Stack

Blockchain: Solana Devnet

Backend: FastAPI (Python)

Frontend: HTML + JS (Vanilla, minimal UI)

AI Layer: Scoring logic & gamified events

Database: In-memory / Supabase-ready

Libraries: web3.js · spl-token · dotenv

🚀 Run Locally
# Clone the repo
git clone https://github.com/abc777-pa/eduagent-solana.git
cd eduagent-solana

# Install backend deps
cd backend
pip install -r ../requirements.txt

# Run backend (port 8000)
python -m uvicorn app.main:app --reload --port 8000

# Run frontend (port 5500)
cd frontend
python -m http.server 5500

# Open browser
http://127.0.0.1:5500

🔌 API Reference
Method	Endpoint	Description
GET	/health	Check API status
POST	/api/pay	Simulate tuition payment (mock)
POST	/api/mint	Mint NFT achievement badge (mock)
POST	/api/event	Track user progress / AI score (optional)
GET	/api/score/{student_id}	View accumulated score

📘 Example response:

{
  "status": "success",
  "tx_hash": "FAKE_TX_DEVNET_HASH",
  "gateway": "Intebix × Eurasian Bank"
}

📦 Environment Setup

Create .env file (or copy .env.example):

RPC_URL=https://api.devnet.solana.com
SECRET_KEY_JSON=[ ... ]   # your Devnet Keypair as JSON
KZTE_MINT=PASTE_MINT_ADDRESS_HERE
SCHOOL_WALLET=PASTE_SCHOOL_PUBKEY_HERE

🧩 Roadmap

 FastAPI backend mock (payments + NFT mint)

 Frontend demo with JSON response

 Solana Devnet integration (KZTE token)

 Real NFT mint via Metaplex

 AI gamified scoring system

 Deployment for schools pilot

🪙 Tracks & Impact
Track	Focus
Stablecoins / RWAs	Digital Tenge & Solana stable payments
Consumer Apps	AI gamified assistant for students
Infrastructure	Fintech bridge between banks and Solana

Impact:
EduAgent bridges Kazakhstan’s educational system and blockchain payments — combining real-world finance, AI motivation, and decentralized records for schools.

🎥 Demo Video

▶️ Watch on YouTube (Unlisted)

(replace with your actual link)

📸 Screenshot

🧠 Team

Rakhman Ibragimov — Founder & Developer
🇰🇿 Kazakhstan · @jangoman
 · SuperteamKZ

🔖 License

MIT License © 2025 Rakhman Ibragimov
This project was built as part of the Solana Cypherpunk Hackathon 2025.
