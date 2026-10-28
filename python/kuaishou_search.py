"""Search Kuaishou videos by keyword and save play and like counts to CSV.

Actor: Kuaishou 快手 Scraper - Videos, Comments, Users & Hot Lists
Store page: https://apify.com/clover_folktale/kuaishou-scraper
"""
from common import run_actor, save_csv

items = run_actor("kuaishou-scraper", {
    "mode": "search",
    "keywords": [
        "美食"
    ],
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("playCount"), item.get("likeCount"), item.get("description"))

save_csv(items, "kuaishou_search.csv",
         ["description", "playCount", "likeCount", "commentCount", "createdAt", "url"])
