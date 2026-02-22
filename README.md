# Ransomware Blocker

**Ransomware Blocker** detects rapid file modifications mimicking ransomware attacks and blocks them before damage occurs. Uses Python's `watchdog` library for real-time filesystem monitoring on Linux.

## 🚨 Features
- Monitors directories for >10 file changes in 60 seconds (configurable)
- Instant alerts via desktop notifications + console logs
- Auto-quarantines suspicious files (`.quarantine` suffix)
- One-click backup/restore functionality
- Simple rule-based detection—no machine learning required

## 🛠️ Quick Start
```bash
pip install -r requirements.txt
mkdir -p demo/docs backup
cd demo && ../blocker.py
