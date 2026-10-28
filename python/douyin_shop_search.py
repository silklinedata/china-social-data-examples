"""Search Douyin Shop (抖音商城) products by keyword and save sales and commission data to CSV.

Actor: Douyin Shop 抖音商城 Product Scraper - Sales, Commission & Shops
Store page: https://apify.com/clover_folktale/douyin-shop-scraper
"""
from common import run_actor, save_csv

items = run_actor("douyin-shop-scraper", {
    "mode": "search",
    "keywords": [
        "口红"
    ],
    "maxResults": 5
})

for item in items[:5]:
    print(item.get("title"), item.get("price"), item.get("monthlySales"), item.get("shopName"))

save_csv(items, "douyin_shop_search.csv",
         ["title", "price", "monthlySales", "positiveRate", "shopName", "commissionRate", "url"])
