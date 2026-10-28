"""Search Reddit posts by keyword and save them to CSV.

Actor: Reddit Scraper - Posts, Comments, Subreddits & Users
Store page: https://apify.com/clover_folktale/reddit-scraper
"""
from common import run_actor, save_csv

items = run_actor("reddit-scraper", {
    "mode": "search",
    "keyword": "best budget laptop",
    "maxResults": 10
})

for item in items[:5]:
    print(item.get("subreddit"), item.get("score"), item.get("title"))

save_csv(items, "reddit_search.csv",
         ["title", "subreddit", "score", "commentCount", "createdAt", "url"])
