# vulnerable.py
import subprocess

def dangerous_command(user_input):
    # Injection possible si user_input n'est pas filtré
    subprocess.call(f"echo {user_input}", shell=True)

dangerous_command("test; rm -rf /tmp")  # Exemple vulnérable