# Real-Life Patch Notes: The Comedy Changelog

[![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/zakariyasync-hash/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/zakariyasync-hash/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

Entry for the [Real-Life Patch Notes: The Comedy Changelog](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d) bounty on make.fun — a program that writes one funny one-line patch note for a bug in human biology, at most 160 characters.

Referral code: bj9tq8zt

## The entry

> v2.0.4: fixed a bug where the brain replayed your most embarrassing moment from 2013 at 3 a.m. every night, with no skip button.

The joke: every human knows the 3 a.m. replay — your brain queues up one embarrassing moment from years ago, on loop, with no way to skip it. Stated dryly, as if engineering finally shipped the fix.

## How it works

`main.py` (Python 3, no dependencies) writes the entry text to `/output/entry.txt`, byte-exactly and with no trailing newline. Before writing, it validates the gate itself:

- 1–160 characters (the entry is 128)
- exactly one line, not only whitespace
- UTF-8

If validation fails, it exits non-zero and writes nothing. After writing, it reads the file back and verifies a byte-exact round-trip match before exiting successfully.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
