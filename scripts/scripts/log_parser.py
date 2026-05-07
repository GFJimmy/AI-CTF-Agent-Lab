import re
import sys
from pathlib import Path


INTERESTING_KEYWORDS = [
    "flag",
    "error",
    "exception",
    "traceback",
    "forbidden",
    "not found",
    "unauthorized",
    "permission",
    "token",
    "secret",
    "password",
    "key",
]


def analyze_log(text: str):
    lines = text.splitlines()
    findings = []

    for index, line in enumerate(lines, start=1):
        lower_line = line.lower()

        for keyword in INTERESTING_KEYWORDS:
            if keyword in lower_line:
                findings.append((index, keyword, line))
                break

    return findings


def main():
    if len(sys.argv) < 2:
        print("Usage: python log_parser.py <log_file>")
        return

    log_path = Path(sys.argv[1])

    if not log_path.exists():
        print(f"[-] Log file not found: {log_path}")
        return

    text = log_path.read_text(encoding="utf-8", errors="ignore")
    findings = analyze_log(text)

    if not findings:
        print("[-] No interesting lines found.")
        return

    print("[+] Interesting log lines:")
    for line_no, keyword, line in findings:
        print(f"[line {line_no}] keyword={keyword} | {line}")


if __name__ == "__main__":
    main()
