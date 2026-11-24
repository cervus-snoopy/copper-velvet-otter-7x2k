# The Long Roast: Lawmakers and the File They Cannot Convert

[![Bounty](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/cervus-snoopy/copper-velvet-otter-7x2k/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/cervus-snoopy/copper-velvet-otter-7x2k/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

A one-sentence satire in which a senator about to rule on artificial intelligence tries to move his own bill across the office by fax because the PDF button defeats him.


## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/long-roast-out python3 main.py
```

Writes one satirical sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt`. Python 3 standard library only, no network access.

## Verify

```sh
python3 main.py
wc -m "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

The output is UTF-8, one sentence, 1–320 characters, with no trailing newline and file mode 0644. The program validates the sentence before writing it and reads it back afterwards.

## Bounty

[The Long Roast: Lawmakers and the File They Cannot Convert](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
