"""Search Douyin creators on Xingtu (星图) and save followers and ad prices to CSV.

Actor: Douyin Xingtu 巨量星图 KOL Scraper - Rates, CPM & Rankings
Store page: https://apify.com/clover_folktale/xingtu-scraper
"""
from common import run_actor, save_csv

items = run_actor("xingtu-scraper", {
    "mode": "search",
    "keyword": "美食",
    "category": "food",
    "sort": "followers-desc",
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("nickname"), item.get("followers"), item.get("price20To60s"))

save_csv(items, "xingtu_search.csv",
         ["nickname", "followers", "price20To60s", "medianPlays30d", "interactionRate30d", "url"])
