"""Search recent Chinese web posts and news for a keyword and save them to CSV.

Actor: China Social Media Search - Weibo, WeChat, Douyin & More
Store page: https://apify.com/clover_folktale/china-search-scraper
"""
from common import run_actor, save_csv

items = run_actor("china-search-scraper", {
    "mode": "search",
    "keywords": [
        "小米"
    ],
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("siteName"), item.get("publishedAt"), item.get("url"))

save_csv(items, "china_search.csv",
         ["platform", "siteName", "keyword", "text", "url", "publishedAt"])
