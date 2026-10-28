"""Get a Douyin account insight record (follower change, peer comparison) and save the basics to CSV.

Actor: Douyin Analytics 抖音数据分析 - Audience, Trends & Keywords
Store page: https://apify.com/clover_folktale/douyin-analytics-scraper
"""
from common import run_actor, save_csv

items = run_actor("douyin-analytics-scraper", {
    "mode": "accountInsight",
    "accounts": [
        "https://www.douyin.com/user/MS4wLjABAAAAvcQlQ5vR2pYV04MZ6EzflPQdWTJbVBNnDQTjKiLoH90"
    ],
    "maxResults": 3
})

for item in items[:5]:
    print(item.get("secUid"), item.get("followerChangeAverage"))

save_csv(items, "douyin_account_insight.csv",
         ["secUid", "url", "followerChangeAverage"])
