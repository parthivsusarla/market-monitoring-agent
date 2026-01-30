import requests
from config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2/everything"

def fetch_news(query, days=1):
    params = {
        "q": query,
        "from": "2026-01-29",
        "sortBy": "relevancy",
        "language": "en",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    articles = []
    for item in data.get("articles", []):
        articles.append({
            "title": item["title"],
            "summary": item["description"],
            "source": item["source"]["name"]
        })

    return articles
