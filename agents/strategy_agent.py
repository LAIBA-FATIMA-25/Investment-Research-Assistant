class StrategyAgent:
    def generate_investment_plan(self, sentiment_analysis, scraped_data, user_budget):
        recommendations = []

        for item in scraped_data.get("organic", [])[:5]:  # Consider top 5 search results
            title = item.get("title")
            link = item.get("link")
            sentiment = sentiment_analysis.get(title, "Neutral")

            if "Positive" in sentiment and user_budget >= 100:
                recommendations.append({
                    "title": title,
                    "url": link,
                    "sentiment": sentiment,
                    "strategy": "Recommended for investment due to positive sentiment."
                })
            elif "Neutral" in sentiment and user_budget >= 500:
                recommendations.append({
                    "title": title,
                    "url": link,
                    "sentiment": sentiment,
                    "strategy": "Potential investment, but exercise caution."
                })

        return recommendations
