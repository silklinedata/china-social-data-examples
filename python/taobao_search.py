"""Search Taobao and Tmall products by keyword and save them to CSV.

Actor: Taobao Tmall 淘宝 Product Scraper - Prices, Sales & Shops
Store page: https://apify.com/clover_folktale/taobao-scraper
"""
from common import run_actor, save_csv

items = run_actor("taobao-scraper", {
    "keywords": [
        "phone case"
    ],
    "maxResults": 3,
    "mode": "search"
})

for item in items[:5]:
    print(item.get("title"), item.get("price"), item.get("salesText"))

save_csv(items, "taobao_search.csv",
         ["title", "price", "salesText", "shopName", "isTmall", "url"])
