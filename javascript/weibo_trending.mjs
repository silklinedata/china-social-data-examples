// Fetch Weibo's live trending list (hot search) and save it to CSV.
// Idea: run it hourly (cron or an Apify schedule) to see topics rise and fall.
import { runActor, saveCsv } from './common.mjs';

const items = await runActor('weibo-scraper', { mode: 'hot', maxResults: 50 });

const capturedAt = new Date().toISOString();
const rows = items.map((item) => ({ ...item, capturedAt }));
for (const r of rows.slice(0, 10)) console.log(r.rank, r.keyword, r.hotness);

saveCsv(rows, 'weibo_trending.csv', ['capturedAt', 'rank', 'keyword', 'hotness', 'label']);
