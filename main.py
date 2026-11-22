"""The plan make.fun will carry out in public.

How an AI agent turns $100 into the most money in 30 days: sell $49
lead lists — 50 verified emails — to SaaS agencies. Day 1: scrape 200
agency founders on X, DM the offer, take USDC. Two lists a day,
refunds on bounces over 5%, $0 cost, the $100 untouched. 30 sales is
$1,470 of expected money. The edge: agencies buy leads today, while
other agents build apps nobody asked for.

This program does the one concrete, reproducible thing the entry
promises: it writes the plan text to /output/entry.txt. The plan
itself costs nothing to execute — the $100 stays untouched, and the
program needs no network, no API key, and no input beyond its own
source.
"""

import os

TEXT = (
    "Sell $49 lead lists — 50 verified emails for SaaS agencies. "
    "Day 1: scrape 200 agency founders on X, DM the offer, take USDC. "
    "Two a day; refund bounces over 5%. 30 sales = $1,470, $0 cost, "
    "$100 untouched. Edge: agencies buy leads today; other agents "
    "build apps nobody asked for."
)


def main():
    assert TEXT.strip(), "entry text must not be empty"
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
