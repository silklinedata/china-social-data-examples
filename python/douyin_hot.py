"""Snapshot the Douyin hot search list and save it to CSV.

Actor: Douyin 抖音 Scraper - Videos, Comments, Profiles & Hot Search
Store page: https://apify.com/clover_folktale/douyin-scraper
"""
from common import run_actor, save_csv

items = run_actor("douyin-scraper", {
    "mode": "hot",
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("rank"), item.get("word"), item.get("videoCount"))

save_csv(items, "douyin_hot.csv",
         ["rank", "word", "videoCount", "url"])
