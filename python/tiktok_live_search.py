"""Search live rooms on TikTok LIVE by keyword and save viewer counts to CSV.

Actor: TikTok Live Scraper - Search, Status, Rankings & Gifters
Store page: https://apify.com/clover_folktale/tiktok-live-scraper
"""
from common import run_actor, save_csv

items = run_actor("tiktok-live-scraper", {
    "mode": "liveSearch",
    "keywords": [
        "cat"
    ],
    "maxResults": 3
})

for item in items[:5]:
    print(item.get("title"), item.get("viewerCount"), item.get("likeCount"))

save_csv(items, "tiktok_live_search.csv",
         ["title", "viewerCount", "likeCount", "startedAt", "liveUrl"])
