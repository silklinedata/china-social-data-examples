"""Search Amazon products by keyword and save price, rating and sales hints to CSV.

Actor: Amazon Product Scraper - Best Sellers, ASIN, Prices, Ratings
Store page: https://apify.com/clover_folktale/amazon-scraper
"""
from common import run_actor, save_csv

items = run_actor("amazon-scraper", {
    "mode": "search",
    "keywords": [
        "wireless earbuds"
    ],
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("title"), item.get("price"), item.get("rating"), item.get("ratingCount"))

save_csv(items, "amazon_search.csv",
         ["title", "price", "rating", "ratingCount", "isPrime", "salesVolumeText", "asin", "url"])
