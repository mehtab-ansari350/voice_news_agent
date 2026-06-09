from newspaper import Article


def extract_article(url):
    try:
        article = Article(url)

        article.download()
        article.parse()

        return {
            "title": article.title,
            "text": article.text
        }

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":

    test_url = "https://www.bbc.com/news/articles/cj6ge150z5go"

    article = extract_article(test_url)

    if article:

        print("\nTITLE:\n")
        print(article["title"])

        print("\nARTICLE:\n")
        print(article["text"][:2000])