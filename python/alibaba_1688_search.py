"""Search 1688 (China wholesale) products by keyword and save them to CSV.

Actor: 1688.com 阿里巴巴 Wholesale Scraper - MOQ Prices & Suppliers
Store page: https://apify.com/clover_folktale/1688-scraper
"""
from common import run_actor, save_csv

items = run_actor("1688-scraper", {
    "keywords": [
        "phone case"
    ],
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("title"), item.get("price"), item.get("supplierName"), item.get("province"), item.get("url"))

save_csv(items, "alibaba_1688_search.csv",
         ["title", "price", "supplierName", "province", "city", "repurchaseRateBadge", "url"])
