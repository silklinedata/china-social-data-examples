"""Get the latest posts of an Instagram account and save engagement counts to CSV.

Actor: Instagram Scraper - Posts, Reels, Profiles & Followers
Store page: https://apify.com/clover_folktale/instagram-scraper
"""
from common import run_actor, save_csv

items = run_actor("instagram-scraper", {
    "mode": "userPosts",
    "usernames": [
        "nasa"
    ],
    "maxResults": 3
})

for item in items[:5]:
    print(item.get("createdAt"), item.get("likeCount"), item.get("commentCount"))

save_csv(items, "instagram_user_posts.csv",
         ["createdAt", "caption", "likeCount", "commentCount", "playCount", "url"])
