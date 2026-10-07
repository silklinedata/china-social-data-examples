"""Export the public comments of a Weibo post to CSV."""
from common import run_actor, save_csv

# Post links or numeric post IDs both work.
POSTS = ["https://weibo.com/6593199887/Rlf5vlWRz"]

comments = run_actor("weibo-scraper", {
    "mode": "comments",
    "posts": POSTS,
    "maxResults": 100,
})
save_csv(comments, "weibo_comments.csv",
         ["text", "likes", "replyCount", "publishedAt", "authorName"])
