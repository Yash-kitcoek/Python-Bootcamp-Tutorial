import requests

query = input("Enter topic: ")
api = "d676224a7e654dfda899cebb1119eac2"

url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api}"

response = requests.get(url)
data = response.json()

if data["status"] == "ok":
    articles = data["articles"]

    for index, article in enumerate(articles, start=1):
        print(f"\nArticle {index}")
        print("Title :", article.get("title"))
        print("URL   :", article.get("url"))
        print("-" * 60)
else:
    print("Error:", data.get("message"))