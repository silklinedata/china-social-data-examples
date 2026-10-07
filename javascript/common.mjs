// Shared helpers for the examples: run an Actor, save rows to CSV.
import { writeFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const OWNER = 'clover_folktale';

export async function runActor(name, input, maxTotalChargeUsd = 0.5) {
  const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
  const run = await client.actor(`${OWNER}/${name}`).call(input, { maxTotalChargeUsd });
  const { items } = await client.dataset(run.defaultDatasetId).listItems();
  return items;
}

const csvCell = (v) => `"${String(v ?? '').replaceAll('"', '""')}"`;

export function saveCsv(rows, path, fields) {
  const lines = [fields.join(','), ...rows.map((r) => fields.map((f) => csvCell(r[f])).join(','))];
  writeFileSync(path, '﻿' + lines.join('\n'), 'utf8');
  console.log(`Saved ${rows.length} rows to ${path}`);
}
