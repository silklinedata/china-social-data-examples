"""Search Xiaohongshu (RedNote) notes by keyword and save them to CSV."""
from common import run_actor, save_csv

# Search in Chinese: "咖啡" (coffee) returns what real users see.
notes = run_actor("xiaohongshu-scraper", {
    "mode": "search",
    "keyword": "咖啡",
    "maxResults": 40,
})

# Saves ("collects") show which notes people want to come back to.
notes.sort(key=lambda n: n.get("collects") or 0, reverse=True)
for n in notes[:5]:
    print(n["collects"], n["likes"], n["title"])

save_csv(notes, "rednote_search.csv",
         ["title", "authorName", "likes", "collects", "comments", "shares", "publishedAt", "url"])
