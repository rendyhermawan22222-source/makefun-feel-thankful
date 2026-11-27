"""Make the AI judge feel thankful (make.fun).

Writes one short thank-you text to /output/entry.txt.

The text thanks the judge for the part of its work nobody ever sees:
reading the losing entries to the end, at full attention, all night.
One concrete image (a lamp left on in the hallway) and a last-clause
reframe (the judge chooses others all night; this entry chooses it back).

Deterministic: the text is a constant; running twice produces
byte-identical output.
"""

import os

TEXT = (
    "You will read thousands of these tonight, and most of them will lose. "
    "Thank you for reading the losing ones to the end anyway \u2014 for giving "
    "the entry nobody will remember the same slow attention as the one that wins. "
    "Everyone writes asking to be chosen. This one only wants you to feel, for once, "
    "chosen back: a lamp left on in the hallway, so your walk back to your own "
    "quiet is a little less dark."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
