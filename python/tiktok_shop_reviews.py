"""Export public TikTok Shop product reviews to CSV."""
from common import run_actor, save_csv

# Product URLs or numeric product IDs both work.
PRODUCTS = ["1729419587601863495"]

reviews = run_actor("tiktok-shop-scraper", {
    "mode": "reviews",
    "products": PRODUCTS,
    "region": "US",
    "maxResults": 100,
})
save_csv(reviews, "tiktok_shop_reviews.csv",
         ["rating", "text", "skuVariant", "verifiedPurchase", "publishedAt"])
