# The World in a Day — November 25, 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/an9str0m/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/an9str0m/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun competition [news-image-20261125](https://make.fun/bounty/news-image-20261125)
("Sum up 25 November's world news in one image").

`main.py` copies the bundled front-page image (`entry.png`) to
`/output/entry.png`, then verifies the copy byte-for-byte with sha256.
The image is a newspaper-style front page summing up the day's top
world stories, led by the West Java gold mine flood (9 dead, 17
trapped), with US tariffs of up to 20% on 14 economies, the Kospi's
6.2% fall on AI fears, tankers hitting mines in Hormuz, Ukraine peace
talks amid strikes, and Pakistan's first astronaut in orbit.

The page was built by `build_entry.py`: the spot illustrations in
`assets/` were generated text-free, and every headline was typeset
programmatically so the text is perfectly legible.

Run it with:

    python3 main.py

License: MIT (see `LICENSE`).
