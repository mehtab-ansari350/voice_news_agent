# test_db.py

from memory.database import get_all_articles

articles = get_all_articles()

print(f"Articles Found: {len(articles)}")

for article in articles:
    print(article["id"], article["title"])