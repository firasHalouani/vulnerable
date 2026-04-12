# scan_snyk.py
import requests
import json
import os
import subprocess

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
    return {"error": response.text}


# ✅ REAL BANDIT SCANNER
def scan_bandit(path="."):
    """
    Run Bandit and return vulnerabilities as JSON
    """

    try:
        result = subprocess.run(
            ["bandit", "-r", path, "-f", "json"],
            capture_output=True,
            text=True
        )

        if result.returncode not in [0, 1]:  
            # 0 = clean, 1 = issues found
            return {"error": result.stderr}

        data = json.loads(result.stdout)

        vulnerabilities = []

        for issue in data.get("results", []):
            vulnerabilities.append({
                "source": "bandit",
                "severity": issue.get("issue_severity"),
                "confidence": issue.get("issue_confidence"),
                "title": issue.get("test_name"),
                "file": issue.get("filename"),
                "line": issue.get("line_number"),
                "description": issue.get("issue_text")
            })

        return {"bandit_vulnerabilities": vulnerabilities}

    except Exception as e:
        return {"error": str(e)}


def scan_repo():
    snyk_results = scan_snyk()

    # 👇 scan current project folder
    bandit_results = scan_bandit(".")

    final_report = {
        "repo": REPO,
        "snyk": snyk_results,
        "bandit": bandit_results
    }

    print(json.dumps(final_report, indent=4))
    return final_report


if __name__ == "__main__":
    scan_repo()
