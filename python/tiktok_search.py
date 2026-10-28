"""Search TikTok videos by keyword and save play and like counts to CSV.

Actor: TikTok Scraper - Video Search, Hashtags, Profiles & Sounds
Store page: https://apify.com/clover_folktale/tiktok-scraper
"""
from common import run_actor, save_csv

items = run_actor("tiktok-scraper", {
    "mode": "search",
    "keywords": [
        "air fryer recipes"
    ],
    "sortType": "most-liked",
    "publishTime": "month",
    "maxResults": 3
})

for item in items[:5]:
    print(item.get("playCount"), item.get("likeCount"), item.get("description"))

save_csv(items, "tiktok_search.csv",
         ["description", "playCount", "likeCount", "shareCount", "createdAt", "url"])
