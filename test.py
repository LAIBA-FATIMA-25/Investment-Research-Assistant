import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SERPER_API_KEY")
print(f"Using SERPER_API_KEY: {api_key}")

headers = {
    "X-API-KEY": api_key,
    "Content-Type": "application/json"
}

response = requests.post("https://google.serper.dev/search", headers=headers, json={"q": "stocks"})

if response.status_code == 200:
    print("✅ API Test Success:", response.json())
else:
    print(f"❌ API Test Failed: {response.status_code} - {response.text}")
