import os

PART_A = "Your save failed because the disk is full \u2014 your file has nowhere to live. "
PART_B = "Free up some space, then try again before it starts paying rent elsewhere."
LINE = PART_A + PART_B
assert LINE == "Your save failed because the disk is full \u2014 your file has nowhere to live. Free up some space, then try again before it starts paying rent elsewhere."
assert 1 <= len(LINE) <= 200


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
