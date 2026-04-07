# SAST GitHub Scan Python

Ce projet permet de scanner un repo GitHub Python pour des vulnérabilités
via l'API Snyk sans avoir besoin de cloner le projet localement.

## Étapes

1. Crée un compte gratuit sur https://snyk.io et génère un API token.
2. Crée un petit repo GitHub contenant `vulnerable.py`.
3. Modifie `scan_snyk.py` :
   - Remplace `TON_API_TOKEN_SYNK` par ton token Snyk.
   - Remplace `ton-username/vulnerable-python` par ton repo GitHub.
4. Installe les dépendances :