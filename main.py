"""One funny single-line one-star cat review of its human.

The line is fixed and deterministic: one sharp, concrete incident
(the food bowl filled two minutes late), judged by cat standards,
with the sting in the last few words. No network, stdlib only.
"""

LINE = (
    "One star. He filled my bowl at 6:02 instead of 6:00, "
    "so I am now interviewing his replacement."
)


def main() -> None:
    """Write the review to /output/entry.txt, enforcing the gate."""
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    output_dir = "/output"
    import os

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
