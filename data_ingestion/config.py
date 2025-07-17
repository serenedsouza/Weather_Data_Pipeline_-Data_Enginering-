import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),      # ✅ Use 'localhost'
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "admin"),
    "database": os.getenv("DB_NAME", "weather_project")
}

API_KEY = os.getenv("bb4ece27bae08d4477fede61690d4afe")
