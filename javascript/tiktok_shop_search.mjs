// Search TikTok Shop products by keyword and save them to CSV.
import { runActor, saveCsv } from './common.mjs';

const products = await runActor('tiktok-shop-scraper', {
  mode: 'search',
  keyword: 'lipstick',
  region: 'US', // US, SG, MY, TH, PH, VN
  maxResults: 40,
});

products.sort((a, b) => (b.soldCount ?? 0) - (a.soldCount ?? 0));
for (const p of products.slice(0, 5)) console.log(p.soldCount, p.price, p.currency, p.title);

saveCsv(products, 'tiktok_shop_search.csv',
  ['title', 'price', 'currency', 'soldCount', 'rating', 'reviewCount', 'shopName', 'url']);
