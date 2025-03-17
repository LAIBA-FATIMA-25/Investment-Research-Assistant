import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


class SentimentAgent:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)

    def analyze_sentiment(self, text):
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Analyze the sentiment (Positive, Neutral, Negative) for this investment opportunity: {text}"
            response = model.generate_content(prompt)
            sentiment = response.text.strip()
            print(f"📊 Sentiment for '{text[:50]}...': {sentiment}")
            return sentiment
        except Exception as e:
            print(f"❌ Error in sentiment analysis: {e}")
            return "Neutral"
