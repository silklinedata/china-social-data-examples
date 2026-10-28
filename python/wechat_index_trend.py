"""Get the WeChat Index trend of keywords (30 daily values) and save the summary to CSV.

Actor: WeChat Index 微信指数 Scraper - China Keyword Trend Data
Store page: https://apify.com/clover_folktale/wechat-index-scraper
"""
from common import run_actor, save_csv

items = run_actor("wechat-index-scraper", {
    "keywords": [
        "咖啡",
        "瑞幸"
    ],
    "maxResults": 2,
    "mode": "trend"
})

for item in items[:5]:
    print(item.get("keyword"), item.get("averageIndex"), item.get("peakIndex"))

save_csv(items, "wechat_index_trend.csv",
         ["keyword", "averageIndex", "peakIndex", "peakDate", "latestIndex"])
