🔐 DevSecOps Automated Security Pipeline
A CI/CD security pipeline that automatically scans code for vulnerabilities on every push using GitHub Actions. Built to simulate a real-world DevSecOps security gate.

🚀 What This Does
Every time code is pushed to this repository, GitHub Actions automatically spins up a fresh environment and runs three security tools against the codebase:

Bandit — Scans Python code for common security flaws (shell injection, weak hashing, hardcoded secrets)
Semgrep — Performs broader static analysis across the codebase using community rule sets
TruffleHog — Scans the entire Git history for leaked API keys, tokens, and credentials

If any critical issue is found, the pipeline fails the build — simulating how a real security gate would block vulnerable code from reaching production.

🛠️ Tools & Technologies
ToolPurposeGitHub ActionsCI/CD automationBanditPython SAST (Static Application Security Testing)SemgrepMulti-language static analysisTruffleHogSecret scanningPython 3.11Application language

🧪 Intentional Vulnerabilities (Demo)
The file app/main.py contains deliberately planted vulnerabilities to demonstrate the pipeline's detection capability:
VulnerabilityDescriptionTool That Catches Itshell=True in subprocessAllows shell injection attacksBandithashlib.md5()Weak hashing algorithm, not suitable for passwordsBanditHardcoded API keySecret exposed directly in source codeBandit / TruffleHog

⚠️ These vulnerabilities are intentional for demonstration purposes only. This is a security testing project, not production code.


⚙️ Pipeline Architecture
 
Developer pushes code
        ↓
GitHub Actions triggered
        ↓
┌─────────────────────────┐
│     security-scan job   │
│                         │
│  1. Checkout code       │
│  2. Set up Python 3.11  │
│  3. Run Bandit          │
│  4. Run Semgrep         │
│  5. Run TruffleHog      │
└─────────────────────────┘
        ↓
  Vulnerabilities found?
    YES → Build fails ❌ (code blocked)
    NO  → Build passes ✅ (code approved)


📂 Project Structure

    devsecops-security-pipeline/
├── .github/
│   └── workflows/
│       └── security-scan.yml   # Pipeline definition
├── app/
│   └── main.py                 # Intentionally vulnerable Python app
└── README.md


🔍 Key Security Concepts Demonstrated

Shift Left Security — Security checks happen at commit time, not after deployment
SAST (Static Application Security Testing) — Analysing source code without executing it
Secret Scanning — Detecting credentials accidentally committed to version control
CI/CD Security Gates — Automated enforcement that blocks vulnerable code from merging


👤 Author
Sharjeel Ansari
B.Sc. IT — Cybersecurity | Aspiring SOC Analyst & Penetration Tester
GitHub • https://www.linkedin.com/in/sharjeel-ansari-m78/
