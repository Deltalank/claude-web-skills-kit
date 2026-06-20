#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
SKILLS_DIR = ROOT / "skills"

VERSION_RE = re.compile(r"Version:\s*`([^`]+)`")
CHANGELOG_VERSION_RE = re.compile(r"^## \[([^\]]+)\]", re.MULTILINE)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    if not README.exists():
        errors.append("README.md is missing")
    if not CHANGELOG.exists():
        errors.append("CHANGELOG.md is missing")
    if not SKILLS_DIR.is_dir():
        errors.append("skills/ directory is missing")

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1

    readme = read(README)
    changelog = read(CHANGELOG)

    readme_version_match = VERSION_RE.search(readme)
    changelog_version_match = CHANGELOG_VERSION_RE.search(changelog)

    if not readme_version_match:
        errors.append("README version not found")
    if not changelog_version_match:
        errors.append("latest changelog version not found")

    if readme_version_match and changelog_version_match:
        readme_version = readme_version_match.group(1)
        changelog_version = changelog_version_match.group(1)
        if readme_version != changelog_version:
            errors.append(
                f"README version {readme_version} does not match changelog {changelog_version}"
            )

    skill_names = sorted(path.name for path in SKILLS_DIR.iterdir() if path.is_dir())
    for skill_name in skill_names:
        if skill_name not in readme:
            errors.append(f"README does not mention skill {skill_name}")
        if skill_name not in changelog:
            errors.append(f"CHANGELOG does not mention skill {skill_name}")

    if errors:
        print("Release consistency errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Release consistency OK for {len(skill_names)} skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
