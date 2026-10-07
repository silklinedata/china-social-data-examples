"""Shared helpers for the examples: run an Actor, save rows to CSV."""
import csv
import os
from decimal import Decimal

from apify_client import ApifyClient

OWNER = "clover_folktale"


def run_actor(name, run_input, max_usd="0.50"):
    """Run an Actor and return its dataset items. Spending is capped by max_usd."""
    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor(f"{OWNER}/{name}").call(
        run_input=run_input,
        max_total_charge_usd=Decimal(max_usd),
    )
    if run.status != "SUCCEEDED":
        raise RuntimeError(f"Run {run.id} ended with status {run.status}")
    return list(client.dataset(run.default_dataset_id).iterate_items())


def save_csv(rows, path, fields):
    """Write the chosen fields of each item to a CSV file and print a summary."""
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} rows to {path}")
