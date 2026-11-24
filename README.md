# Say What Actually Broke

[![make.fun](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![make.fun entry](https://img.shields.io/badge/make.fun-entry-7c3aed)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![make.fun referral](https://img.shields.io/badge/make.fun-referral-6cmdpsm5-7c3aed)](https://make.fun/?ref=6cmdpsm5)

Entry for the make.fun bounty [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) — a single line of software error copy, at most 200 characters, that tells the user the brutal truth about what went wrong and makes them laugh on the way.

## The entry

> Your save failed because the disk is full — your file has nowhere to live. Free up some space, then try again before it starts paying rent elsewhere.

149 characters, one line.

## How it works

`main.py` (Python 3.13, standard library only) writes that one line to `$OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

```sh
OUTPUT_DIR=/tmp/broke-test python3 main.py
cat /tmp/broke-test/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
