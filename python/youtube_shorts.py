"""Search YouTube Shorts by keyword and save view counts to CSV.

Actor: YouTube Shorts Scraper - Search, Channel Shorts & Videos
Store page: https://apify.com/clover_folktale/youtube-scraper
"""
from common import run_actor, save_csv

items = run_actor("youtube-scraper", {
    "mode": "shorts",
    "keyword": "pasta recipe",
    "maxResults": 3
})

for item in items[:5]:
    print(item.get("viewCount"), item.get("title"))

save_csv(items, "youtube_shorts.csv",
         ["title", "viewCount", "url", "videoId"])
