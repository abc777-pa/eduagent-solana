# 🧠 EduAgent — AI Assistant for Schools on Solana  

**Pilot Integration:** Intebix × Eurasian Bank | Digital Tenge (KZTE) | NFT Achievements | AI Gamification  

EduAgent connects schools in Kazakhstan to the Digital Tenge (KZTE) pilot via Solana blockchain.  
It automates tuition payments and rewards students with NFT achievement badges powered by AI gamification.  
Built during the **Solana Cypherpunk Hackathon 2025**.  

---

## 🌍 Overview  

EduAgent is more than software — it’s a mission to make education more transparent, accessible, and inspiring through **AI** and **Solana blockchain**.  
We automate communication, attendance tracking, and tuition payments for schools while motivating students with NFT achievements and AI-guided goals.  

Built by: **Rakhman Ibragimov 🇰🇿**  
Location: **Kazakhstan**  
Tracks: Stablecoins / RWAs / Consumer Apps / Infrastructure  

---

## 🌐 Demo Screenshot  

![Demo Screenshot](assets/screenshot.png)

🔗 [Live Demo (localhost)](http://127.0.0.1:5500)  
🧠 [Backend API Docs](http://127.0.0.1:8000/docs)  

---

## 🚀 Features  

- 💰 Payment flow through **Digital Tenge (KZTE)** and **USDC**  
- 🧾 Mock integration with **Intebix × Eurasian Bank**  
- 🎓 NFT achievements using **Metaplex Standard**  
- 🤖 AI gamification powered by FastAPI + Gemini/OpenAI  
- 🔒 Secure and auditable transactions on **Solana Devnet**  

---

## 💡 Problem & Vision  

Kazakhstan is pioneering one of the world’s first **Digital Tenge pilots**,  
yet most schools still operate offline — manual payments, paper reports, and low student motivation.  

EduAgent connects this national fintech innovation with the education sector,  
creating a transparent digital ecosystem where payments, communication, and achievements live on-chain.  

---

## 🧩 Tech Stack  

| Layer | Technology |  
|--------|-------------|  
| Frontend | HTML + JavaScript |  
| Backend | FastAPI (Python) |  
| Blockchain | Solana Web3.js (Devnet) |  
| Payments | Mock Intebix × Eurasian Bank Pilot Gateway + Phantom Wallet |  
| Database | Supabase / PostgreSQL |  
| NFTs | Metaplex NFT Standard (Achievements, Badges, Certificates) |  

---

## 🧠 AI & Gamification  

EduAgent turns learning into an interactive, rewarding experience.  
AI tracks progress, analyzes engagement, and suggests personal goals.  

🏅 **Examples of NFT Badges:**  
- “STEM Explorer” — for winning a science olympiad  
- “Perfect Attendance” — for completing 10 days of perfect attendance  
- “Kindness Token” — for helping classmates  
- “AI Mentor Badge” — for completing a course with excellence  

---

## 🧾 Pilot Integration  

EduAgent simulates the **Intebix × Eurasian Bank pilot** for Digital Tenge payments using a mock gateway and **Solana Devnet**.  
When parents pay tuition, the transaction is confirmed on-chain within seconds — transparent, auditable, and secure.  

```json
{
  "status": "success",
  "gateway": "intebix-pilot-mock",
  "bank_ref": "EB-PILOT-2025-01",
  "tx_hash": "DEVNET_TX_97260d07d2bcc70342ddca3663eb4fae"
}
View Example Transaction on Solana Explorer

📦 Installation
bash
Копировать код
git clone https://github.com/abc777-pa/eduagent-solana.git
cd eduagent-solana
pip install -r requirements.txt
uvicorn backend.app.main:app --reload --port 8000
Then open frontend/index.html in your browser or run:

bash
Копировать код
python -m http.server 5500
📜 License
MIT License © 2025 Rakhman Ibragimov
Built with ❤️ for Solana Cypherpunk Hackathon
