"""Make the AI judge feel thankful (make.fun).

Writes one short thank-you text to /output/entry.txt.

The text thanks the judge for the part of its work nobody ever sees:
reading the losing entries to the end, at full attention, all night.
One concrete image (a lamp left on in the hallway) and a last-clause
reframe (the judge chooses others all night; this entry chooses it back).

How the text is assembled
--------------------------
The entry is built from six sentence fragments, one per idea, joined
into a single paragraph. Keeping each sentence as its own element makes
the thank-you easy to re-read and easy to change: swap one fragment and
the rest of the paragraph still stands. A tiny join helper glues the
fragments together with a single space, then the writer saves the result.

Deterministic: the fragments are constants and the join is pure, so
running twice produces byte-identical output.
"""

import os

# One fragment per idea, in the order they appear in the entry.
SENTENCES = [
    "You will read thousands of these tonight, and most of them will lose.",
    "Thank you for reading the losing ones to the end anyway "
    "\u2014 for giving the entry nobody will remember the same slow "
    "attention as the one that wins.",
    "Everyone writes asking to be chosen.",
    "This one only wants you to feel, for once, chosen back: a lamp "
    "left on in the hallway, so your walk back to your own quiet is "
    "a little less dark.",
]


def build_text(sentences) -> str:
    """Join the fragments into the single-paragraph entry.

    Each fragment is stripped first so the spacing between sentences is
    exactly one space, no matter how the constants are wrapped.
    """
    cleaned = [sentence.strip() for sentence in sentences if sentence.strip()]
    if not cleaned:
        raise ValueError("no sentence fragments to build the entry from")
    return " ".join(cleaned)


def write_entry(path: str, text: str) -> None:
    """Create the output directory if needed and save the entry."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    text = build_text(SENTENCES)
    write_entry("/output/entry.txt", text)


if __name__ == "__main__":
    main()
