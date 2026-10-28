"""Search AliExpress products by keyword and save them to CSV.

Actor: AliExpress 速卖通 Scraper - Products, Prices & Sold Counts
Store page: https://apify.com/clover_folktale/aliexpress-scraper
"""
from common import run_actor, save_csv

items = run_actor("aliexpress-scraper", {
    "mode": "search",
    "keywords": [
        "phone case"
    ],
    "maxResults": 5
})

for item in items[:5]:
    print(item.get("title"), item.get("price"), item.get("currency"))

save_csv(items, "aliexpress_search.csv",
         ["title", "price", "currency", "itemId", "url"])
