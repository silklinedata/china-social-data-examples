"""Search Threads posts by keyword and save them to CSV.

Actor: Threads Scraper (Meta) - Posts, Replies, Profiles & Search
Store page: https://apify.com/clover_folktale/threads-scraper
"""
from common import run_actor, save_csv

items = run_actor("threads-scraper", {
    "mode": "search",
    "keywords": [
        "coffee"
    ],
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("likeCount"), item.get("replyCount"), item.get("text"))

save_csv(items, "threads_search.csv",
         ["text", "likeCount", "replyCount", "createdAt", "url"])
