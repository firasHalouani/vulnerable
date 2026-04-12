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


# 2️⃣ NEW: Mock vulnerability scanner (for testing pipeline)
def scan_custom_rules():
    vulnerabilities = []

    # Example rule 1
    vulnerabilities.append({
        "source": "custom-rule-engine",
        "severity": "HIGH",
        "title": "Hardcoded secret detected",
        "file": "config.py",
        "description": "API keys should not be hardcoded in source code"
    })

    # Example rule 2
    vulnerabilities.append({
        "source": "custom-rule-engine",
        "severity": "MEDIUM",
        "title": "Debug mode enabled",
        "file": "settings.py",
        "description": "DEBUG=True should not be used in production"
    })

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
