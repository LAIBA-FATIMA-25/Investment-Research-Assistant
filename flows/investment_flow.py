from dotenv import load_dotenv
import os
from litellm import completion
from crewai.flow.flow import Flow, start, listen
from agents.scraper_agent import ScraperAgent
from agents.sentiment_agent import SentimentAgent
from agents.strategy_agent import StrategyAgent
from agents.analysis_agent import AnalysisAgent

# Load environment variables
load_dotenv()

class InvestmentFlow(Flow):
    model = "gemini-1.5-flash"

    def __init__(self):
        super().__init__()
        self.scraper = ScraperAgent()
        self.sentiment_agent = SentimentAgent()
        self.strategy_agent = StrategyAgent()
        self.analysis_agent = AnalysisAgent()

    @start()
    def fetch_investment_data(self):
        print("📊 Welcome to the Investment Research Assistant!")
        query = input("Enter your investment query: ")
        budget = float(input("Provide your budget: "))
        
        # Store user input
        self.state["query"] = query
        self.state["budget"] = budget

        print(f"🔍 Searching for: {query}")
        
        # Perform web search using Serper API
        search_results = self.scraper.scrape(query)
        
        # Save search results in flow state
        self.state["scraped_data"] = search_results

        return search_results

    @listen(fetch_investment_data)
    def analyze_sentiments(self, scraped_data):
        print("🧠 Analyzing sentiments...")
        sentiment_results = {}
        
        # Analyze sentiment for each search result
        for item in scraped_data["organic"]:
            title = item["title"]
            sentiment = self.sentiment_agent.analyze_sentiment(title)
            sentiment_results[title] = sentiment

        self.state["sentiment_data"] = sentiment_results
        return sentiment_results

    @listen(analyze_sentiments)
    def generate_strategy(self, sentiment_data):
        print("📈 Formulating investment strategy...")
        
        # Get budget and search data
        budget = self.state["budget"]
        scraped_data = self.state["scraped_data"]
        
        # Create recommendations
        recommendations = self.strategy_agent.generate_investment_plan(sentiment_data, scraped_data, budget)
        
        # Store recommendations in the flow state
        self.state["recommendations"] = recommendations
        return recommendations

    @listen(generate_strategy)
    def generate_report(self, recommendations):
        print("📝 Generating report...")
        
        # Create and save the report
        self.analysis_agent.generate_report(recommendations)
        
        print("✅ Investment report created: investment_report.html")


# Start the investment flow
flow = InvestmentFlow()

flow.kickoff()
flow.plot()
