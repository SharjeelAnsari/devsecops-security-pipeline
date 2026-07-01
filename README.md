# 🔐 DevSecOps Automated Security Pipeline

A CI/CD pipeline that automatically scans code for vulnerabilities on every push using GitHub Actions. Simulates a real-world DevSecOps security gate.

---

## 🚀 What This Does

Every time code is pushed, GitHub Actions runs three security tools automatically:

- **Bandit** — Scans Python code for security flaws (shell injection, weak hashing, hardcoded secrets)
- **Semgrep** — Performs static analysis across the codebase using community rule sets
- **TruffleHog** — Scans Git history for leaked API keys, tokens, and credentials

If any critical issue is found, the pipeline **fails the build** — blocking vulnerable code from reaching production.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| GitHub Actions | CI/CD automation |
| Bandit | Python SAST scanning |
| Semgrep | Multi-language static analysis |
| TruffleHog | Secret scanning |
| Python 3.11 | Application language |

---

## 🧪 Intentional Vulnerabilities

The file `app/main.py` contains deliberately planted vulnerabilities to demonstrate detection:

| Vulnerability | Tool That Catches It |
|--------------|----------------------|
| `shell=True` in subprocess (shell injection) | Bandit |
| `hashlib.md5()` (weak hashing) | Bandit |
| Hardcoded API key in source code | Bandit / TruffleHog |

> ⚠️ These vulnerabilities are intentional for demonstration purposes only.

---

## 📂 Project Structure

devsecops-security-pipeline/
├── .github/workflows/security-scan.yml
├── app/main.py
└── README.md

---

## 🔍 Security Concepts Demonstrated

- **Shift Left Security** — Checks happen at commit time, not after deployment
- **SAST** — Analysing source code without executing it
- **Secret Scanning** — Detecting credentials in version control
- **CI/CD Security Gates** — Automated blocking of vulnerable code

---

## 👤 Author

**Sharjeel Ansari** — B.Sc. IT | Cybersecurity | Aspiring SOC Analyst & Penetration Tester

[GitHub](https://github.com/SharjeelAnsari) • [LinkedIn](https://www.linkedin.com/in/sharjeel-ansari-m78/)
