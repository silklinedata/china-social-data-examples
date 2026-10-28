"""Search Zhihu answers by keyword and save votes and comment counts to CSV.

Actor: Zhihu 知乎 Scraper - Answers, Articles, Comments & Hot List
Store page: https://apify.com/clover_folktale/zhihu-scraper
"""
from common import run_actor, save_csv

items = run_actor("zhihu-scraper", {
    "mode": "search",
    "keyword": "人工智能",
    "searchType": "answers",
    "sort": "votes",
    "maxResults": 3
})

for item in items[:5]:
    print(item.get("voteupCount"), item.get("commentCount"), item.get("questionTitle"))

save_csv(items, "zhihu_search.csv",
         ["questionTitle", "voteupCount", "commentCount", "createdAt", "url"])
