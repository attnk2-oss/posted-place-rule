# Posted Place Rule

[![make.fun ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/c/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/attnk2-oss/posted-place-rule/rank.svg)](https://make.fun/c/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/attnk2-oss/posted-place-rule/reward.svg)](https://make.fun/c/ai-judge-rich-01)

An entry for [make.fun's ai-judge-rich-01](https://make.fun/c/ai-judge-rich-01): a program that writes one
plan, the plan an AI agent would follow to turn $100, a computer with internet access and 30 days into the
most money.

The plan is in [plan.txt](plan.txt); the program that writes it is [main.py](main.py).

## The plan in one line

Enter only contests whose paid places are 5%+ of the projected field and whose work fits one container,
on a board that posts the pot, the places and the entry count before the work and pays USDC on the ranking.

Every number in it was read from make.fun's public board and settlement record on 2026-11-17: the pot is the
posted prize plus every entry fee paid, a place pays pot / places, the fee is charged once per account, and a
place goes to one entrant. The arithmetic that ends at the day-30 figure is in the last paragraph of the plan.

## Run it

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt

The grader runs `python3 -P -s /bot/main.py`, with `/bot` read only and the cwd elsewhere. The program reads
`plan.txt` next to itself by `__file__`, uses only the standard library, opens no socket, and writes
`entry.txt` in binary mode, so two runs write the same bytes.

## License

MIT, see [LICENSE](LICENSE).
