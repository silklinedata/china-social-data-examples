"""Search Xiaohongshu creators on Pugongying (蒲公英) and save followers and ad prices to CSV.

Actor: Xiaohongshu Pugongying 蒲公英 KOL Scraper - Rates & Stats
Store page: https://apify.com/clover_folktale/pugongying-scraper
"""
from common import run_actor, save_csv

items = run_actor("pugongying-scraper", {
    "mode": "search",
    "maxResults": 3,
    "keyword": "面膜"
})

for item in items[:5]:
    print(item.get("nickname"), item.get("followers"), item.get("lowestPrice"))

save_csv(items, "pugongying_search.csv",
         ["nickname", "followers", "sponsoredNoteCount", "lowestPrice", "sponsoredMedianReads", "location", "url"])
