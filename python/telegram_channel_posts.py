"""Read the latest posts of a public Telegram channel and save them to CSV.

Actor: Telegram Channel Scraper - Messages, Search & Subscribers
Store page: https://apify.com/clover_folktale/telegram-scraper
"""
from common import run_actor, save_csv

items = run_actor("telegram-scraper", {
    "mode": "channelPosts",
    "channels": [
        "cointelegraph"
    ],
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("publishedAt"), item.get("viewCount"), item.get("text"))

save_csv(items, "telegram_channel_posts.csv",
         ["channel", "publishedAt", "viewCount", "reactionCount", "text", "url"])
