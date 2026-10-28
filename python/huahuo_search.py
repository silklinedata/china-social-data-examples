"""Search Bilibili creators for brand deals on Huahuo (花火) and save their stats to CSV.

Actor: Bilibili Huahuo 花火 KOL Scraper - Creator Rates & Audience
Store page: https://apify.com/clover_folktale/huahuo-scraper
"""
from common import run_actor, save_csv

items = run_actor("huahuo-scraper", {
    "mode": "search",
    "keyword": "美食",
    "category": "food",
    "sort": "followers",
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("nickname"), item.get("followers"), item.get("averagePlays"))

save_csv(items, "huahuo_search.csv",
         ["nickname", "followers", "averagePlays", "interactionRate", "category", "url"])
