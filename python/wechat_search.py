"""Search WeChat official account articles by keyword and save them to CSV.

Actor: WeChat Official Account 公众号 Scraper - Articles & Read Counts
Store page: https://apify.com/clover_folktale/wechat-scraper
"""
from common import run_actor, save_csv

items = run_actor("wechat-scraper", {
    "mode": "search",
    "keyword": "咖啡",
    "sort": "hot",
    "maxResults": 3
})

for item in items[:5]:
    print(item.get("title"), item.get("accountName"), item.get("publishedAt"))

save_csv(items, "wechat_search.csv",
         ["title", "accountName", "publishedAt", "readCount", "url"])
