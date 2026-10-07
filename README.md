# Xiaohongshu (RedNote), Weibo, Bilibili and TikTok Shop data: code examples

Short, runnable Python and JavaScript examples for getting China social data without an account, cookies or proxies. Use them as a **Xiaohongshu scraper** and **RedNote API** (search notes, export comments), a **Weibo trending API** (the live hot search list), a **Bilibili comments scraper** and creator-stats tool, and a **TikTok Shop scraper** (products and reviews). Everything runs through four pay-per-result Apify Actors by Silkline, and results come back as flat JSON you can save to CSV.

| Actor | What you get |
|---|---|
| [Xiaohongshu (RedNote) Scraper](https://apify.com/clover_folktale/xiaohongshu-scraper) | Notes by keyword with likes, saves and comments; public comments; creator profiles |
| [Weibo Scraper](https://apify.com/clover_folktale/weibo-scraper) | The live trending list, posts by keyword, public comments, user profiles |
| [Bilibili Scraper](https://apify.com/clover_folktale/bilibili-scraper) | Videos by keyword with views and danmaku, public comments, creator stats |
| [TikTok Shop Scraper](https://apify.com/clover_folktale/tiktok-shop-scraper) | Products by keyword, details, public reviews, shop products, hot-selling lists |

## Quick start

1. Create a free [Apify account](https://apify.com) and copy your API token from **Console → Settings → API & Integrations**.
2. Set it as an environment variable (never commit it):

```bash
export APIFY_TOKEN="your-token-here"
```

3. Python:

```bash
pip install -r requirements.txt   # apify-client
cd python
python rednote_search.py
```

   JavaScript (Node 18+):

```bash
npm install                       # apify-client
node javascript/rednote_search.mjs
```

Each script caps its own spending with `max_total_charge_usd` (default $0.50 per run) and writes a CSV into the current folder. Prices are on each Actor's store page.

## Examples

| Use case | Python | JavaScript |
|---|---|---|
| Search RedNote notes, rank by saves | [rednote_search.py](python/rednote_search.py) | [rednote_search.mjs](javascript/rednote_search.mjs) |
| Export RedNote note comments | [rednote_comments.py](python/rednote_comments.py) | |
| Weibo trending list snapshot | [weibo_trending.py](python/weibo_trending.py) | [weibo_trending.mjs](javascript/weibo_trending.mjs) |
| Export Weibo post comments | [weibo_comments.py](python/weibo_comments.py) | |
| Export Bilibili video comments | [bilibili_comments.py](python/bilibili_comments.py) | |
| Bilibili creator stats and recent videos | [bilibili_creator_stats.py](python/bilibili_creator_stats.py) | |
| Search TikTok Shop products | [tiktok_shop_search.py](python/tiktok_shop_search.py) | [tiktok_shop_search.mjs](javascript/tiktok_shop_search.mjs) |
| Export TikTok Shop reviews | [tiktok_shop_reviews.py](python/tiktok_shop_reviews.py) | |

## Try it without code

These example task pages run the Actors with ready-made inputs:

- RedNote: [search without login](https://apify.com/clover_folktale/xiaohongshu-scraper/examples/rednote-search-without-login) · [trending products](https://apify.com/clover_folktale/xiaohongshu-scraper/examples/rednote-trending-products) · [comments](https://apify.com/clover_folktale/xiaohongshu-scraper/examples/rednote-comments-scraper) · [brand profile](https://apify.com/clover_folktale/xiaohongshu-scraper/examples/rednote-brand-profile-scraper) · [skincare](https://apify.com/clover_folktale/xiaohongshu-scraper/examples/rednote-skincare-posts) · [China travel](https://apify.com/clover_folktale/xiaohongshu-scraper/examples/rednote-china-travel-posts) · [coffee trends](https://apify.com/clover_folktale/xiaohongshu-scraper/examples/rednote-coffee-trends) · [EV car reviews](https://apify.com/clover_folktale/xiaohongshu-scraper/examples/rednote-ev-car-reviews)
- Weibo: [trending topics today](https://apify.com/clover_folktale/weibo-scraper/examples/weibo-hot-search-tracker) · [comments](https://apify.com/clover_folktale/weibo-scraper/examples/weibo-comments-scraper) · [official account posts](https://apify.com/clover_folktale/weibo-scraper/examples/weibo-official-account-posts) · [brand mentions](https://apify.com/clover_folktale/weibo-scraper/examples/weibo-brand-mentions-tesla) · [AI discussion](https://apify.com/clover_folktale/weibo-scraper/examples/weibo-ai-discussion)
- Bilibili: [comments](https://apify.com/clover_folktale/bilibili-scraper/examples/bilibili-comments-scraper) · [creator stats](https://apify.com/clover_folktale/bilibili-scraper/examples/bilibili-creator-stats) · [most-viewed videos](https://apify.com/clover_folktale/bilibili-scraper/examples/bilibili-most-viewed-videos) · [Genshin Impact videos](https://apify.com/clover_folktale/bilibili-scraper/examples/bilibili-genshin-videos) · [phone reviews](https://apify.com/clover_folktale/bilibili-scraper/examples/bilibili-phone-reviews) · [AI tutorials](https://apify.com/clover_folktale/bilibili-scraper/examples/bilibili-ai-tutorials)
- TikTok Shop: [trending products](https://apify.com/clover_folktale/tiktok-shop-scraper/examples/tiktok-shop-trending-products) · [product scraper](https://apify.com/clover_folktale/tiktok-shop-scraper/examples/tiktok-shop-product-scraper) · [review scraper](https://apify.com/clover_folktale/tiktok-shop-scraper/examples/tiktok-shop-review-scraper) · [seller products](https://apify.com/clover_folktale/tiktok-shop-scraper/examples/tiktok-shop-seller-products)

## Fields you get

**Xiaohongshu (RedNote)**: note `title`, `description`, `url`, `authorName`, `publishedAt`, `likes`, `collects` (saves), `comments`, `shares`, `imageCount`, `hashtags` (note details). Comments: `text`, `likes`, `replyCount`, `publishedAt`, `authorName`. Creators: `nickname`, `bio`, `followers`, `noteCount`, `likesReceived`.

**Weibo**: trending entries with `rank`, `keyword`, `hotness`, `label`. Posts with `text`, `authorName`, `publishedAt`, `reposts`, `comments`, `likes`. Comments: `text`, `likes`, `replyCount`. Users: `nickname`, `followers`, `postCount`, `verified`.

**Bilibili**: videos with `title`, `views`, `likes`, `coins`, `favorites`, `shares`, `comments`, `danmaku`, `durationSeconds`, `tags`. Comments: `text`, `likes`, `replyCount`. Creators: `nickname`, `followers`, `videoCount`, `totalViews`, `totalLikes`.

**TikTok Shop**: products with `title`, `price`, `currency`, `soldCount`, `rating`, `reviewCount`, `shopName`; details add SKUs, stock and specifications. Reviews: `rating`, `text`, `skuVariant`, `verifiedPurchase`, `publishedAt`.

Missing values are `null`. Search in the platform's own language for the best results (Chinese for Xiaohongshu, Weibo and Bilibili; English for TikTok Shop).

## Privacy

Only public content and statistics are returned. Commenters appear by public nickname only; no phone numbers, real names, private messages, avatars or commenter IDs. You are responsible for using the data in line with applicable laws and each platform's terms.

## About

Made by Silkline. Questions or a missing field: open an issue here or on the Actor page. Updates on X: [@silklinedata](https://x.com/silklinedata). Code in this repository is MIT licensed.
