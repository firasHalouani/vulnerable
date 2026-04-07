# scan_snyk.py
import requests
import json

# 1️⃣ Ton API Token Snyk (obtenu sur https://snyk.io/account)
API_TOKEN = "snyk_uat.1fcad39e.eyJlIjoxNzgzMzQzNjk0LCJoIjoic255ay5pbyIsImoiOiJBWjFvRmQtRWJiVnNucVJSTVM2Skx3IiwicyI6IndIazF4TWpfUUsyYXV1cjZweEJybmciLCJ0aWQiOiJBQUFBQUFBQUFBQUFBQUFBQUFBQUFBIn0.3sheIAqnvjtftnpac2f83mDeQq6ChIuD5O4KNotxvEluJNziTNtYJGSRv04WCdpyVfVX_Tp_rlOExNWmh4DEBg"

# 2️⃣ Le repo GitHub que tu veux scanner
# Format : "owner/repo"
REPO = ""

# 3️⃣ URL API Snyk pour scanner un repo GitHub
url = f"https://snyk.io/api/v1/org/github/repos/{REPO}/test"

headers = {
    "Authorization": f"token {API_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/vnd.snyk+json"
}

def scan_repo():
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Retour JSON joliment formaté
        print(json.dumps(data, indent=4))
        return data
    else:
        print("Erreur API:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    scan_repo()