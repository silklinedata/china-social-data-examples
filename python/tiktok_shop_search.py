"""Search TikTok Shop products by keyword and save them to CSV."""
from common import run_actor, save_csv

products = run_actor("tiktok-shop-scraper", {
    "mode": "search",
    "keyword": "lipstick",
    "region": "US",  # US, SG, MY, TH, PH, VN
    "maxResults": 40,
})

products.sort(key=lambda p: p.get("soldCount") or 0, reverse=True)
for p in products[:5]:
    print(p["soldCount"], p["price"], p["currency"], p["title"])

save_csv(products, "tiktok_shop_search.csv",
         ["title", "price", "currency", "soldCount", "rating", "reviewCount", "shopName", "url"])
