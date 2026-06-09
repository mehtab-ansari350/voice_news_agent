import feedparser

RSS_URL = "https://feeds.bbci.co.uk/news/world/rss.xml"

def get_latest_news(limit=5):
    feed = feedparser.parse(RSS_URL)

    news_list = []

    for entry in feed.entries[:limit]:
        news_list.append({
            "title": entry.title,
            "link": entry.link
        })
    return news_list

if __name__ == "__main__":
    news = get_latest_news()

    for index, item in enumerate(news, start=1 ):
        print(f"{index}. {item['title']}")
        print(item['link'])
        print("_" * 50)