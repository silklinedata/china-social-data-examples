"""List top TikTok ads from the Creative Center for a keyword and save them to CSV.

Actor: TikTok Creative Center Scraper - Top Ads, Hashtags & Trends
Store page: https://apify.com/clover_folktale/tiktok-creative-center-scraper
"""
from common import run_actor, save_csv

items = run_actor("tiktok-creative-center-scraper", {
    "mode": "topAds",
    "keywords": [
        "shoes"
    ],
    "maxResults": 3
})

for item in items[:5]:
    print(item.get("title"), item.get("industry"), item.get("likeCount"), item.get("ctr"))

save_csv(items, "tiktok_top_ads.csv",
         ["title", "industry", "objective", "likeCount", "ctr", "durationSeconds", "videoUrl"])
