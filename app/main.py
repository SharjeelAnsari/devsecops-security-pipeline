# NOTE: This file is intentionally vulnerable for DevSecOps pipeline demonstration.
# Vulnerabilities are deliberate to showcase Bandit, Semgrep, and TruffleHog detection.
# See README.md for details.
import subprocess
import hashlib

def run_command(user_input):
    # Intentionally insecure for demo purposes
    result = subprocess.run(user_input, shell=True)
    return result

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

API_KEY = "sk_test_51Hh2A9examplefakekey1234567890"
