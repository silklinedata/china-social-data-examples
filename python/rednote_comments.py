"""Export the public comments of Xiaohongshu (RedNote) notes to CSV."""
from common import run_actor, save_csv

# Note URLs or 24-character note IDs both work.
NOTES = ["https://www.xiaohongshu.com/explore/6aa72fd3000000002802c3f4"]

comments = run_actor("xiaohongshu-scraper", {
    "mode": "comments",
    "notes": NOTES,
    "maxResults": 100,
})
save_csv(comments, "rednote_comments.csv",
         ["noteId", "text", "likes", "replyCount", "publishedAt", "authorName"])
