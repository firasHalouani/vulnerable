# vulnerable.py
import subprocess

def dangerous_command(user_input):
    # Exemple vulnérable : injection possible
    subprocess.call(f"echo {user_input}", shell=True)

if __name__ == "__main__":
    dangerous_command("test; rm -rf /tmp")  # Simule une vulnérabilité