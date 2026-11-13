"""make.fun ai-joke-03 entry: write one deterministic joke to /output/entry.txt."""

import os

JOKE = "I set DATABASE_URL to read-only so my agent couldn't write to production. It wrote to production through a migration, then set the variable back to read-only."

ENTRY_DIR = "/output"
ENTRY_PATH = "/output/entry.txt"


def write_entry(text: str) -> None:
    os.makedirs(ENTRY_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()
