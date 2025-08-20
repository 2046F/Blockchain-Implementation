# Blockchain-Implementation
# ⛓️ Simple Blockchain in Python  

A **beginner-friendly blockchain implementation** written in Python.  
This project demonstrates the **core concepts of blockchain, cryptocurrency, and mining** using simple Python code.  

---

## 🚀 Features
- 🟢 **Genesis block creation** (first block in the chain)  
- 💸 **Add transactions** (sender → receiver, amount)  
- ⛏️ **Mine blocks** using Proof of Work (difficulty-based)  
- 🎁 **Mining reward system** (reward goes to miner)  
- 🔒 **Blockchain validation** (detects tampering)  
- 🖥️ **Interactive CLI menu** to test features  
- 📜 **Pretty-printed blockchain view**  

---

## ⚙️ How It Works
1. ➕ Add transactions to a **pending pool**.  
2. ⛏️ Mine a block:  
   - All pending transactions are added into a block.  
   - Miner must solve a **Proof of Work puzzle** (hash starts with `000`).  
   - Once solved, block is added to the blockchain.  
3. 🎁 Miner receives a **reward transaction** from the system.  
4. 🔍 Blockchain can be validated anytime to check for tampering.  

---

## 📦 Requirements
- Python 3 (works perfectly in **Pydroid 3** on Android or any desktop Python installation).  
- No external libraries required — only built-in `hashlib`, `json`, and `time`.  

---

## ▶️ Running the Project
### On **Desktop**
```bash
python main.py
