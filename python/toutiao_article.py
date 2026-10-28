"""Read a Toutiao (今日头条) article with its read, like and comment counts.

Actor: Toutiao 今日头条 Scraper - Articles, Videos & Comments
Store page: https://apify.com/clover_folktale/toutiao-scraper
"""
from common import run_actor, save_csv

items = run_actor("toutiao-scraper", {
    "mode": "article",
    "posts": [
        "https://www.toutiao.com/article/7700872920532320803/"
    ],
    "maxResults": 3
})

for item in items[:5]:
    print(item.get("title"), item.get("readCount"), item.get("commentCount"))

save_csv(items, "toutiao_article.csv",
         ["title", "readCount", "likeCount", "commentCount", "publishedAt", "url"])
