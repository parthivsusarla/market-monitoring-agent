from langchain.tools import tool
from services.news_fetcher import fetch_news

@tool
def search_market_news(topic: str):
    """
    Fetches recent news related to a market or policy topic.
    """
    articles = fetch_news(topic)

    if not articles:
        return "No relevant news found."

    formatted = ""
    for a in articles[:5]:
        formatted += f"- {a['title']} ({a['source']}): {a['summary']}\n"

    return formatted
