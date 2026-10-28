# Silkline Apify Actors: code examples and output samples for China and global platform data

Short, runnable Python and JavaScript examples for getting China social, e-commerce and marketing data without an account, cookies or proxies. Use them as a **Xiaohongshu scraper** and **RedNote API**, a **Weibo trending API**, a **Bilibili comments scraper**, a **Douyin**, **WeChat**, **Zhihu**, **Taobao** and **TikTok Shop scraper**, and more: 32 pay-per-result Apify Actors by Silkline in total. Chinese platforms come first, followed by e-commerce, global platforms (TikTok, YouTube, Instagram, Reddit, Threads, Telegram, IMDb) and creator-marketing data. Results come back as flat JSON you can save to CSV.

Every Actor has a real output sample in [`samples/`](samples/): the input that was used and the first two result items. Identity fields of ordinary users (authors, commenters) are replaced with `<redacted>` in the samples. Pay per result, prices on each store page.

## Actors

### Chinese social media and content

| Actor | What you get | Python example | Sample output |
|---|---|---|---|
| [Xiaohongshu 小红书 RedNote Scraper - Notes, Comments & Replies](https://apify.com/clover_folktale/xiaohongshu-scraper) | Notes by keyword with likes, saves and comments; public comments; creator profiles | [rednote_search.py](python/rednote_search.py) | [xiaohongshu.json](samples/xiaohongshu.json) |
| [Douyin 抖音 Scraper - Videos, Comments, Profiles & Hot Search](https://apify.com/clover_folktale/douyin-scraper) | Hot search list, video search, creator videos and profiles, comments, hashtag and sound feeds | [douyin_hot.py](python/douyin_hot.py) | [douyin.json](samples/douyin.json) |
| [Weibo 微博 Scraper - Hot Search, Posts, Comments & Users](https://apify.com/clover_folktale/weibo-scraper) | The live trending list, posts by keyword, public comments, user profiles | [weibo_trending.py](python/weibo_trending.py) | [weibo.json](samples/weibo.json) |
| [Bilibili B站 Scraper - Videos, Comments, Danmaku & Subtitles](https://apify.com/clover_folktale/bilibili-scraper) | Videos by keyword with views and danmaku, public comments, subtitles, creator stats | [bilibili_comments.py](python/bilibili_comments.py) | [bilibili.json](samples/bilibili.json) |
| [WeChat Official Account 公众号 Scraper - Articles & Read Counts](https://apify.com/clover_folktale/wechat-scraper) | Official account articles by keyword or account, full text, read and like counts, Channels video search | [wechat_search.py](python/wechat_search.py) | [wechat.json](samples/wechat.json) |
| [Zhihu 知乎 Scraper - Answers, Articles, Comments & Hot List](https://apify.com/clover_folktale/zhihu-scraper) | Answers, articles and pins by keyword, all answers of a question, comments, the hot list, user profiles | [zhihu_search.py](python/zhihu_search.py) | [zhihu.json](samples/zhihu.json) |
| [Kuaishou 快手 Scraper - Videos, Comments, Users & Hot Lists](https://apify.com/clover_folktale/kuaishou-scraper) | Videos by keyword, a user's videos, video details, comments, users, hot lists | [kuaishou_search.py](python/kuaishou_search.py) | [kuaishou.json](samples/kuaishou.json) |
| [Douban 豆瓣 Scraper - Movies, Ratings, Comments & Reviews](https://apify.com/clover_folktale/douban-scraper) | Hot movie and TV lists with scores, short comments, subject details, full reviews | [douban_hot.py](python/douban_hot.py) | [douban.json](samples/douban.json) |
| [Toutiao 今日头条 Scraper - Articles, Videos & Comments](https://apify.com/clover_folktale/toutiao-scraper) | Articles with full text and read, like and comment counts; videos; comments | [toutiao_article.py](python/toutiao_article.py) | [toutiao.json](samples/toutiao.json) |
| [Youku 优酷 Scraper - Video Search, Video & Channel Details](https://apify.com/clover_folktale/youku-scraper) | Video search by keyword, video details, uploader channel profiles | [youku_search.py](python/youku_search.py) | [youku.json](samples/youku.json) |
| [China Social Media Search - Weibo, WeChat, Douyin & More](https://apify.com/clover_folktale/china-search-scraper) | One keyword searched across Weibo, WeChat, Zhihu, Douyin, Xiaohongshu, Bilibili, Kuaishou and news sites, with a time window | [china_search.py](python/china_search.py) | [china-search.json](samples/china-search.json) |

### E-commerce

| Actor | What you get | Python example | Sample output |
|---|---|---|---|
| [Taobao Tmall 淘宝 Product Scraper - Prices, Sales & Shops](https://apify.com/clover_folktale/taobao-scraper) | Taobao and Tmall products by keyword with price, sales, shop ratings and stock; shop products; product questions | [taobao_search.py](python/taobao_search.py) | [taobao.json](samples/taobao.json) |
| [1688.com 阿里巴巴 Wholesale Scraper - MOQ Prices & Suppliers](https://apify.com/clover_folktale/1688-scraper) | Wholesale products by keyword with price, MOQ tiers, supplier details and location | [alibaba_1688_search.py](python/alibaba_1688_search.py) | [1688.json](samples/1688.json) |
| [JD.com 京东 Scraper - Shop Products & Buyer Reviews](https://apify.com/clover_folktale/jd-scraper) | Every product of a shop; buyer reviews of an item; keyword search | [jd_shop_products.py](python/jd_shop_products.py) | [jd.json](samples/jd.json) |
| [Douyin Shop 抖音商城 Product Scraper - Sales, Commission & Shops](https://apify.com/clover_folktale/douyin-shop-scraper) | Product search with price, 30-day sales, creator commission and shop score; shop catalogues | [douyin_shop_search.py](python/douyin_shop_search.py) | [douyin-shop.json](samples/douyin-shop.json) |
| [TikTok Shop Scraper - Products, Sales, Reviews & Hot Sellers](https://apify.com/clover_folktale/tiktok-shop-scraper) | Products by keyword, details, public reviews, shop products, hot-selling lists | [tiktok_shop_search.py](python/tiktok_shop_search.py) | [tiktok-shop.json](samples/tiktok-shop.json) |
| [AliExpress 速卖通 Scraper - Products, Prices & Sold Counts](https://apify.com/clover_folktale/aliexpress-scraper) | Products by keyword with price, sold count, rating and link; sort, price range and currency options | [aliexpress_search.py](python/aliexpress_search.py) | [aliexpress.json](samples/aliexpress.json) |
| [Amazon Product Scraper - Best Sellers, ASIN, Prices, Ratings](https://apify.com/clover_folktale/amazon-scraper) | Products by keyword, categories and Best Sellers on 24 marketplaces with price, rating and bought-past-month volume | [amazon_search.py](python/amazon_search.py) | [amazon.json](samples/amazon.json) |

### Global platforms

| Actor | What you get | Python example | Sample output |
|---|---|---|---|
| [TikTok Scraper - Video Search, Hashtags, Profiles & Sounds](https://apify.com/clover_folktale/tiktok-scraper) | Videos by keyword, hashtag, profile or sound; creator search; views, likes, shares and captions | [tiktok_search.py](python/tiktok_search.py) | [tiktok.json](samples/tiktok.json) |
| [TikTok Live Scraper - Search, Status, Rankings & Gifters](https://apify.com/clover_folktale/tiktok-live-scraper) | Live rooms by keyword, live status of creators, daily top-creator ranking, top gifters of a room | [tiktok_live_search.py](python/tiktok_live_search.py) | [tiktok-live.json](samples/tiktok-live.json) |
| [YouTube Shorts Scraper - Search, Channel Shorts & Videos](https://apify.com/clover_folktale/youtube-scraper) | Shorts and videos by keyword or channel with views, duration and upload time; channel info and community posts | [youtube_shorts.py](python/youtube_shorts.py) | [youtube.json](samples/youtube.json) |
| [Instagram Scraper - Posts, Reels, Profiles & Followers](https://apify.com/clover_folktale/instagram-scraper) | Public profiles, posts, Reels, comments, followers, hashtag and location feeds, search | [instagram_user_posts.py](python/instagram_user_posts.py) | [instagram.json](samples/instagram.json) |
| [Reddit Scraper - Posts, Comments, Subreddits & Users](https://apify.com/clover_folktale/reddit-scraper) | Posts by keyword, subreddit feeds, comments, user posts and comments | [reddit_search.py](python/reddit_search.py) | [reddit.json](samples/reddit.json) |
| [Threads Scraper (Meta) - Posts, Replies, Profiles & Search](https://apify.com/clover_folktale/threads-scraper) | Posts by keyword, profile posts, replies, profile search | [threads_search.py](python/threads_search.py) | [threads.json](samples/threads.json) |
| [Telegram Channel Scraper - Messages, Search & Subscribers](https://apify.com/clover_folktale/telegram-scraper) | Public channel messages with views and reactions, keyword search, channel info and subscriber counts | [telegram_channel_posts.py](python/telegram_channel_posts.py) | [telegram.json](samples/telegram.json) |
| [IMDb Scraper - Top 250 Movies & TV Shows Chart, Ratings](https://apify.com/clover_folktale/imdb-scraper) | The Top 250 movies and TV charts with rating, vote count and year, in 10 languages; movie news | [imdb_chart.py](python/imdb_chart.py) | [imdb.json](samples/imdb.json) |

### Marketing and creator data

| Actor | What you get | Python example | Sample output |
|---|---|---|---|
| [Douyin Xingtu 巨量星图 KOL Scraper - Rates, CPM & Rankings](https://apify.com/clover_folktale/xingtu-scraper) | Douyin creators from Xingtu: search by keyword and category, video quotes, audience data, ranking lists | [xingtu_search.py](python/xingtu_search.py) | [xingtu.json](samples/xingtu.json) |
| [Xiaohongshu Pugongying 蒲公英 KOL Scraper - Rates & Stats](https://apify.com/clover_folktale/pugongying-scraper) | Xiaohongshu creators from Pugongying: search by keyword and category, note rates, median reads, profiles | [pugongying_search.py](python/pugongying_search.py) | [pugongying.json](samples/pugongying.json) |
| [Bilibili Huahuo 花火 KOL Scraper - Creator Rates & Audience](https://apify.com/clover_folktale/huahuo-scraper) | Bilibili creators from Huahuo: search by keyword and category, quotes, median plays, CPM, audience data | [huahuo_search.py](python/huahuo_search.py) | [huahuo.json](samples/huahuo.json) |
| [Douyin Analytics 抖音数据分析 - Audience, Trends & Keywords](https://apify.com/clover_folktale/douyin-analytics-scraper) | Douyin account and audience insight, video performance, keyword trends, related words, hot topics, category trends | [douyin_account_insight.py](python/douyin_account_insight.py) | [douyin-analytics.json](samples/douyin-analytics.json) |
| [WeChat Index 微信指数 Scraper - China Keyword Trend Data](https://apify.com/clover_folktale/wechat-index-scraper) | WeChat Index: the daily popularity series of a keyword for the last 30 days, with latest, average and peak | [wechat_index_trend.py](python/wechat_index_trend.py) | [wechat-index.json](samples/wechat-index.json) |
| [TikTok Creative Center Scraper - Top Ads, Hashtags & Trends](https://apify.com/clover_folktale/tiktok-creative-center-scraper) | Top ads by keyword, trending hashtags, videos and search words, music charts | [tiktok_top_ads.py](python/tiktok_top_ads.py) | [tiktok-creative-center.json](samples/tiktok-creative-center.json) |

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

Only public content and statistics are returned: public profile fields such as user ID, nickname, avatar and IP location are included where the platform shows them to everyone; no phone numbers bound to accounts, real-name verification data or private messages. In the samples in this repository, identity fields of ordinary users are replaced with `<redacted>`. You are responsible for using the data in line with applicable laws and each platform's terms.

## About

Made by Silkline. Questions or a missing field: open an issue here or on the Actor page. Updates on X: [@silklinedata](https://x.com/silklinedata). Code in this repository is MIT licensed.
