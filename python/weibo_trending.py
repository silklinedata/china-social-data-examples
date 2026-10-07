"""Fetch Weibo's live trending list (hot search) and save it to CSV."""
from datetime import datetime, timezone

from common import run_actor, save_csv

# Idea: run this hourly with cron or an Apify schedule and append each snapshot
# to one file to see which topics climb or fall over the day.
items = run_actor("weibo-scraper", {"mode": "hot", "maxResults": 50})

captured_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
for item in items:
    item["capturedAt"] = captured_at

for item in items[:10]:
    print(item["rank"], item["keyword"], item["hotness"])

save_csv(items, "weibo_trending.csv", ["capturedAt", "rank", "keyword", "hotness", "label"])
