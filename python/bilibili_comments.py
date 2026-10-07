"""Export the public comments of a Bilibili video to CSV."""
from common import run_actor, save_csv

# Video URLs or BV IDs both work.
VIDEOS = ["https://www.bilibili.com/video/BV1M1421t7hT"]

comments = run_actor("bilibili-scraper", {
    "mode": "comments",
    "videos": VIDEOS,
    "maxResults": 100,
})
save_csv(comments, "bilibili_comments.csv",
         ["videoUrl", "text", "likes", "replyCount", "publishedAt", "authorName"])
