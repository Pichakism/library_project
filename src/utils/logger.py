import os
from datetime import datetime

def write_sync_log(message):
    os.makedirs("./data", exist_ok=True)
    with open("./data/sync_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {message}\n")