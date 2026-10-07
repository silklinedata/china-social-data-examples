// Search Xiaohongshu (RedNote) notes by keyword and save them to CSV.
import { runActor, saveCsv } from './common.mjs';

// Search in Chinese: "咖啡" (coffee) returns what real users see.
const notes = await runActor('xiaohongshu-scraper', {
  mode: 'search',
  keyword: '咖啡',
  maxResults: 40,
});

notes.sort((a, b) => (b.collects ?? 0) - (a.collects ?? 0));
for (const n of notes.slice(0, 5)) console.log(n.collects, n.likes, n.title);

saveCsv(notes, 'rednote_search.csv',
  ['title', 'authorName', 'likes', 'collects', 'comments', 'shares', 'publishedAt', 'url']);
