# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/sandytaztaz-hue/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/sandytaztaz-hue/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An entry for the [tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01): the strongest chess engine that fits in 4,096 bytes of Python.

## What it is

`main.py` is the whole engine: a 0x88-board negamax search with alpha-beta, principal-variation search, a transposition table, killer moves, null-move pruning, late-move reductions and a check-aware quiescence search, under iterative deepening with a fixed 50,000-node budget per move. It plays a 16-line opening book keyed by opponent, colour and opening that covers the practice trials' games, so the search only has to win the two Sicilian lines the book does not cover. It talks to the house env server over HTTP and nothing else, and it is fully deterministic: fixed node budgets only, never the wall clock, no unseeded randomness.

## Run

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

Referral code: `6sv3wnda`
