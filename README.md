# 🚨 Alert Triage Assistant

> *A tiny robot that reads a pile of security alerts and taps the scary ones on the shoulder, so a tired human doesn't have to squint at all of them.*

## 🏢 The story

Imagine a security guard at the door of a huge building. A bell rings every time someone walks in. Ding. Ding. Ding. Five hundred times a day.

Most people are harmless: coffee guy, delivery guy, someone checking their email. But every so often, a thief tries to slip in, dressed just like everyone else.

By lunchtime the guard's eyes are fried, and that's exactly when the thief walks past.

This tool is the guard's little robot helper. It looks at every alert, scores how suspicious it is, explains why, and pushes the dangerous ones to the top of the pile, so the human looks there first. 👀

That "look here first" sorting is the daily job of a Tier 1 SOC analyst. This is that job, in about 60 lines of Python.

## 🤖 What it does

- 📥 Reads alerts from a data file (`alerts.json`)
- 🧮 Scores each alert using simple detection rules
- 🏷️ Labels each one 🔴 CRITICAL, 🟡 MEDIUM, or 🟢 LOW
- 💬 Explains the red flags in plain English
- ⬆️ Sorts the scariest alerts to the top
- 📄 Saves a clean report to `report.txt`

## 🧠 How the robot thinks

| 🚩 Red flag | Points |
|---|---|
| 100+ failed logins | +50 |
| 5 to 99 failed logins | +20 |
| Known malicious IP | +40 |
| Odd hour (before 6 AM or after 10 PM) | +15 |
| Login from an unexpected country | +15 |

Verdict: `70+` is 🔴 CRITICAL, `30 to 69` is 🟡 MEDIUM, `under 30` is 🟢 LOW.

## ▶️ Run it

```bash
python3 triage.py
```

The report prints to your screen and saves to `report.txt`.

## 📸 What it looks like

```
================ TRIAGE REPORT ================
Total alerts: 6
CRITICAL: 2   MEDIUM: 1   LOW: 3
===============================================

CRITICAL | score 120 | alert A-2
    500 failed login attempts for user admin
    Why: very many failed logins (500), known bad IP, odd hour (3:00), unexpected country (Russia)
```

Caught the thief. 🎯

## 🔮 What I would build next

- 📂 Read from real log files (CSV or syslog) instead of sample JSON
- 🌐 Pull live known-bad IPs from a threat-intel feed (AbuseIPDB)
- ✈️ Add an "impossible travel" rule (same user, two countries, minutes apart)
- 🖥️ Output the report as a nice HTML page

## 👩‍💻 Author

Astha Patel, M.S. Information Technology (Security), Arizona State University
🔗 [asthaos.vercel.app](https://asthaos.vercel.app)