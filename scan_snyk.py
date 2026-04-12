# scan_snyk.py
import requests
import json
import os

# ❗ NEVER hardcode tokens
API_TOKEN = os.getenv("SNYK_TOKEN")

REPO = "owner/repo"

url = f"https://snyk.io/api/v1/org/github/repos/{REPO}/test"

headers = {
    "Authorization": f"token {API_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/vnd.snyk+json"
}

def scan_snyk():
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}


# 2️⃣ Custom vulnerability scanner (mock SAST rules)
def scan_custom_rules():
    vulnerabilities = []

    vulnerabilities.extend([
        {
            "source": "custom-rule-engine",
            "severity": "HIGH",
            "title": "Hardcoded secret detected",
            "file": "config.py",
            "description": "API keys should never be hardcoded"
        },
        {
            "source": "custom-rule-engine",
            "severity": "MEDIUM",
            "title": "Debug mode enabled",
            "file": "settings.py",
            "description": "DEBUG=True should not be used in production"
        },
        {
            "source": "custom-rule-engine",
            "severity": "HIGH",
            "title": "SQL Injection risk",
            "file": "db.py",
            "description": "User input used directly in SQL query"
        },
        {
            "source": "custom-rule-engine",
            "severity": "CRITICAL",
            "title": "Unsafe deserialization",
            "file": "parser.py",
            "description": "Using pickle.loads on untrusted input"
        },
        {
            "source": "custom-rule-engine",
            "severity": "HIGH",
            "title": "Weak password policy",
            "file": "auth.py",
            "description": "Passwords not enforcing minimum complexity"
        },
        {
            "source": "custom-rule-engine",
            "severity": "MEDIUM",
            "title": "Missing input validation",
            "file": "api.py",
            "description": "User input not validated before processing"
        },
        {
            "source": "custom-rule-engine",
            "severity": "HIGH",
            "title": "Insecure HTTP usage",
            "file": "requests_client.py",
            "description": "HTTP used instead of HTTPS for external calls"
        },
        {
            "source": "custom-rule-engine",
            "severity": "MEDIUM",
            "title": "Exposed error messages",
            "file": "app.py",
            "description": "Stack traces returned to end users"
        },
        {
            "source": "custom-rule-engine",
            "severity": "LOW",
            "title": "Outdated dependency usage",
            "file": "requirements.txt",
            "description": "Old version of Flask detected"
        },
        {
            "source": "custom-rule-engine",
            "severity": "CRITICAL",
            "title": "Broken authentication",
            "file": "login.py",
            "description": "Session tokens not properly validated"
        }
    ])

    return {"custom_vulnerabilities": vulnerabilities}


def scan_repo():
    snyk_results = scan_snyk()
    custom_results = scan_custom_rules()

    final_report = {
        "repo": REPO,
        "snyk": snyk_results,
        "custom_scan": custom_results
    }

    print(json.dumps(final_report, indent=4))
    return final_report


if __name__ == "__main__":
    scan_repo()
