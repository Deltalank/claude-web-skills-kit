#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "dist", "node_modules", ".venv", "__pycache__"}
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".txt", ".json", ".html", ".css", ".js"}

PATTERNS = [
    ("private-key-marker", re.compile(r"BEGIN (RSA|OPENSSH|EC|DSA)? ?PRIVATE KEY")),
    ("hardcoded-api-key-assignment", re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*=\s*['\"][^'\"]{12,}['\"]")),
    ("unredacted-bearer-token", re.compile(r"(?i)bearer\s+[a-z0-9._\-]{20,}")),
    ("unredacted-email-like-value", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
]

ALLOWLIST = {
    "inteligenciaartificial9401@gmail.com",
    "example.com",
    "schema.org",
}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts) or path.suffix not in TEXT_SUFFIXES


def is_allowed(line: str) -> bool:
    return any(value in line for value in ALLOWLIST)


def main() -> int:
    findings: list[str] = []

    for path in ROOT.rglob("*"):
        if not path.is_file() or should_skip(path.relative_to(ROOT)):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(lines, start=1):
            if is_allowed(line):
                continue
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    findings.append(f"{path.relative_to(ROOT)}:{number}: {label}")

    if findings:
        print("Repository hygiene findings:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Repository hygiene check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
