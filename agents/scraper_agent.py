import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ScraperAgent:
    def __init__(self):
        self.api_key = os.getenv("SERPER_API_KEY")

        if not self.api_key:
            raise Exception("❌ SERPER_API_KEY is missing. Check your .env file.")

    def scrape(self, query):
        print(f"🔍 Searching for: {query}")
        
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json",
        }
        payload = {"q": query}

        response = requests.post("https://google.serper.dev/search", headers=headers, json=payload)

        if response.status_code == 200:
            search_results = response.json()
            print(f"✅ Search successful: {search_results}")
            return search_results
        else:
            raise Exception(f"❌ Search failed: {response.status_code} - {response.text}")
