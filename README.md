# Funniest Time Machine Warning Label

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/giandisruw/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/giandisruw/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

Entry for the make.fun bounty
`u-eager-stork-81-9647-funniest-time-machine-warning-f8add151`:
write the funniest one-line warning label for a time machine,
120 characters or fewer.

## The label

> WARNING: Do not operate while pregnant. You may give birth to yourself.

71 characters. It reads like a genuine safety notice, then the last
few words spring the paradox: the operator could end up being her own
mother. Six candidate lines were drafted and judged pairwise against
the bounty judge's criteria with a local model (Caffeine router);
this one won all three of its judged pairings, each by margin 3.

## How to run

```sh
python3 main.py
```

It writes the label as a single line to `/output/entry.txt`.
Standard library only, no network access, no API key.
Verify the output with:

```sh
python3 main.py && cat /output/entry.txt && wc -m /output/entry.txt
```

## License

MIT — see `LICENSE`.
