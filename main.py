"""Write the plan to /output/entry.txt.

Python 3.13, standard library only. The grader runs this as
`python3 -P -s /bot/main.py` with /bot read only and the cwd elsewhere, so the
plan is read next to this file by __file__, never by the cwd or sys.path.
MAKEFUN_OUTPUT_DIR stands in for /output outside the grader.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    with open(os.path.join(HERE, "plan.txt"), "rb") as source:
        plan = source.read()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Binary mode: the bytes written are the bytes in the file, line ends included.
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as entry:
        entry.write(plan)


if __name__ == "__main__":
    main()
