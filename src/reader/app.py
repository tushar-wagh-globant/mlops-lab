import psycopg2
import os
# Load Config from Environment Variables
# These now come from the .env file passed by Docker
DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "postgres") # Default fallback just in case
DB_PASS = os.getenv("DB_PASS", "password")
DB_NAME = os.getenv("DB_NAME", "postgres")

SHARED_FILE = "/app/shared/data.log"

def connect_db():
    print(f"⏳ Connecting to DB '{DB_NAME}' as user '{DB_USER}'...")
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST, 
                database=DB_NAME, 
                user=DB_USER, 
                password=DB_PASS
            )
            print("✅ DB Connected Successfully!")
            return conn
        except Exception as e:
            print(f"⚠️  DB Waiting... Error: {e}")
            time.sleep(2)

# Main Logic
connect_db()

print("👀 Reader Service Watching...")
last_pos = 0
while True:
    if os.path.exists(SHARED_FILE):
        with open(SHARED_FILE, "r") as f:
            f.seek(last_pos)
            new_lines = f.readlines()
            last_pos = f.tell()
            
            for line in new_lines:
                print(f"📥 Processed: {line.strip()}")
    time.sleep(5)