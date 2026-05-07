import re
import sys
from pathlib import Path


FLAG_PATTERNS = [
    r"flag\{.*?\}",
    r"ctf\{.*?\}",
    r"ISCC\{.*?\}",
    r"DASCTF\{.*?\}",
    r"BUUCTF\{.*?\}",
    r"NSSCTF\{.*?\}",
]


def extract_flags(text: str):
    results = []

    for pattern in FLAG_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        results.extend(matches)

    return list(dict.fromkeys(results))


def main():
    if len(sys.argv) < 2:
        print("Usage: python flag_extractor.py <file>")
        return

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"[-] File not found: {file_path}")
        return

    text = file_path.read_text(encoding="utf-8", errors="ignore")
    flags = extract_flags(text)

    if flags:
        print("[+] Possible flags found:")
        for flag in flags:
            print(flag)
    else:
        print("[-] No flag found.")


if __name__ == "__main__":
    main()
