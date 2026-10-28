"""Read the IMDb Top 250 movie chart and save it to CSV.

Actor: IMDb Scraper - Top 250 Movies & TV Shows Chart, Ratings
Store page: https://apify.com/clover_folktale/imdb-scraper
"""
from common import run_actor, save_csv

items = run_actor("imdb-scraper", {
    "mode": "chart",
    "maxResults": 5
})

for item in items[:5]:
    print(item.get("rank"), item.get("title"), item.get("year"), item.get("rating"))

save_csv(items, "imdb_chart.csv",
         ["rank", "title", "year", "rating", "voteCount", "url"])
