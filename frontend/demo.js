const API = "http://127.0.0.1:8000";

document.getElementById("payBtn").onclick = async () => {
  const res = await fetch(`${API}/api/pay`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({ student_id: "stu-001", amount_kzte: 50000 })
  });
  const data = await res.json();
  document.getElementById("payOut").textContent = JSON.stringify(data, null, 2);

  const url = `https://explorer.solana.com/tx/${data.tx_hash}?cluster=devnet`;
  const a = document.getElementById("expl");
  a.href = url; a.textContent = url;
};

document.getElementById("mintBtn").onclick = async () => {
  const wallet = document.getElementById("wallet").value || "DEMO_WALLET_PUBKEY";
  const res = await fetch(`${API}/api/mint`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({ student_wallet: wallet, badge: "Perfect Attendance" })
  });
  const data = await res.json();
  document.getElementById("mintOut").textContent = JSON.stringify(data, null, 2);
};
