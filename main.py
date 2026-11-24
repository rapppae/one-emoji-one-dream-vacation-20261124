"""Entry for One Emoji, One Dream Vacation (make.fun).

Writes exactly one emoji for a dream vacation, to /output/entry.txt.
"""
import os

ENTRY = "🏝️"

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
