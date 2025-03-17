import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not GEMINI_API_KEY or not SERPER_API_KEY:
    raise ValueError("❌ Ensure GEMINI_API_KEY and SERPER_API_KEY are set in the .env file.")
