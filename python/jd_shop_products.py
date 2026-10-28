"""List the products of a JD.com shop and save them to CSV.

Actor: JD.com 京东 Scraper - Shop Products & Buyer Reviews
Store page: https://apify.com/clover_folktale/jd-scraper
"""
from common import run_actor, save_csv

items = run_actor("jd-scraper", {
    "mode": "shop",
    "shops": [
        "1000000127"
    ],
    "maxResults": 5
})

for item in items[:5]:
    print(item.get("title"), item.get("itemId"))

save_csv(items, "jd_shop_products.csv",
         ["title", "itemId", "shopName", "url"])
