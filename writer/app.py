import time
import os

# Paths
CONFIG_FILE = "/app/config/message.txt"
SHARED_FILE = "/app/shared/data.log"

print("🚀 Writer Service Started...")

while True:
    message = "DEFAULT"
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            message = f.read().strip()
    
    timestamp = time.strftime("%H:%M:%S")
    log_entry = f"{timestamp} - {message}\n"
    
    # Write to shared volume (simulates EFS)
    with open(SHARED_FILE, "a") as f:
        f.write(log_entry)
        print(f"✍️  Wrote: {log_entry.strip()}")
        
    time.sleep(5)