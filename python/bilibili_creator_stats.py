"""Get a Bilibili creator's follower stats plus their recent videos, saved to CSV."""
from common import run_actor, save_csv

# Creator UIDs or space.bilibili.com URLs both work.
CREATORS = ["https://space.bilibili.com/19286458"]

items = run_actor("bilibili-scraper", {
    "mode": "creator",
    "creators": CREATORS,
    "maxResults": 20,
})

profile = next(i for i in items if i["type"] == "creator")
print(profile["nickname"], "followers:", profile["followers"],
      "total views:", profile["totalViews"], "videos:", profile["videoCount"])

videos = [i for i in items if i["type"] == "video"]
save_csv(videos, "bilibili_creator_videos.csv",
         ["title", "views", "likes", "danmaku", "comments", "publishedAt", "url"])
