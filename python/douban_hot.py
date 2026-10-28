"""List the hot movies on Douban with rating and rating count.

Actor: Douban 豆瓣 Scraper - Movies, Ratings, Comments & Reviews
Store page: https://apify.com/clover_folktale/douban-scraper
"""
from common import run_actor, save_csv

items = run_actor("douban-scraper", {
    "mode": "hot",
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("rank"), item.get("title"), item.get("rating"), item.get("ratingCount"))

save_csv(items, "douban_hot.csv",
         ["rank", "title", "rating", "ratingCount", "kind", "url"])
