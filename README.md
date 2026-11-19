[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Hellboys87/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Hellboys87/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# 19 November 2026: The World in One Picture

A single 1024×1024 front-page-style image summing up the world news of
Thursday, 19 November 2026 in six stories, each with a headline, a short
factual sub-line, and a small-print wire attribution.

## The six stories

1. **Geopolitics — Shenzhen (SCHEDULED TODAY):** Trump, Xi and Putin set
   for the first-ever trilateral meeting at the APEC summit in Shenzhen,
   with Ukraine, the Iran war, nuclear arms control and AI on the agenda
   (Reuters, 19 Nov 2026).
2. **Markets — AI (DEBUT EXPECTED TODAY):** Anthropic prices a record
   $81.3bn IPO at $83 a share — 980 million shares, valuing the Claude
   maker near $1.5 trillion — ahead of its expected Nasdaq debut as ANT
   (Reuters via BusinessWorld, 19 Nov 2026).
3. **Climate — Pacific:** Fiji declares a national state of disaster over
   the El Nino drought; FJ$20m ($8.5m) is set aside for a one-month
   response, with below-normal rainfall forecast until at least April
   (Reuters, 19 Nov 2026).
4. **Weather — India (FORECAST):** Cyclone Akvan is forecast by IMD to
   cross the Narsapur–Puri coast by noon on Friday 20 Nov as a severe
   cyclonic storm, 90–100 km/h gusting to 110, downgraded from the earlier
   very-severe outlook (IMD National Bulletin No. 27, 02:30, 19 Nov 2026).
5. **Culture — Gaming:** Grand Theft Auto VI launches worldwide after a
   13-year wait, unlocking at midnight local time on 19 Nov for
   PlayStation 5 and Xbox Series X|S, rolling out from New Zealand
   (AP, 19 Nov 2026).
6. **Art market — New York:** Van Gogh's *Chataigniers en fleurs* (1890)
   sells for a record $190.4m at Sotheby's, smashing his $117.2m record
   after a Nazi-era ownership dispute was settled (BBC, 19 Nov 2026).

Stories that had not yet occurred at press time — the trilateral meeting,
the Anthropic trading debut, and the cyclone landfall — are labelled
SCHEDULED, EXPECTED, or FORECAST on the image itself.

## How the image is made

`main.py` is a hand-written Python 3 program using Pillow (PIL). It draws
the masthead, the six story panels, and the footer onto a fixed
1024×1024 canvas with fixed fonts and fixed text. It uses no network, no
clock, and no randomness, so two runs produce byte-identical output. The
rendered image is written to `/output/entry.png` (and to `entry.png`
next to the script).

## Run it

```sh
python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=9xcq3bkm&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
