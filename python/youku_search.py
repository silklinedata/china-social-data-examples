"""Search Youku videos by keyword and save them to CSV.

Actor: Youku 优酷 Scraper - Video Search, Video & Channel Details
Store page: https://apify.com/clover_folktale/youku-scraper
"""
from common import run_actor, save_csv

items = run_actor("youku-scraper", {
    "maxResults": 5,
    "mode": "search",
    "keywords": [
        "纪录片"
    ]
})

for item in items[:5]:
    print(item.get("title"), item.get("uploaderName"), item.get("durationSeconds"))

save_csv(items, "youku_search.csv",
         ["title", "uploaderName", "durationSeconds", "publishedText", "url"])
