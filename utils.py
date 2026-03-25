from datetime import datetime

def log_alert(message):
    with open("logs/alerts.txt", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")