#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REQUIRED_DIRS = ["references", "examples", "tests"]
REQUIRED_FILES = ["SKILL.md", "README.md"]
REQUIRED_TESTS = ["should-trigger.md", "should-not-trigger.md", "regression-prompts.md"]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
FRONTMATTER_FIELD_RE = re.compile(r"^(name|description):\s*(.+)$", re.MULTILINE)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fields: dict[str, str] = {}
    for key, value in FRONTMATTER_FIELD_RE.findall(match.group(1)):
        fields[key] = value.strip().strip('"').strip("'")
    return fields


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[OK] {message}")


def has_markdown_files(path: Path) -> bool:
    return path.is_dir() and any(child.suffix == ".md" for child in path.iterdir())


def check_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    name = skill_dir.name

    for file_name in REQUIRED_FILES:
        path = skill_dir / file_name
        if not path.exists():
            errors.append(f"{name}: missing {file_name}")

    for dir_name in REQUIRED_DIRS:
        path = skill_dir / dir_name
        if not path.is_dir():
            errors.append(f"{name}: missing {dir_name}/")

    for content_dir in ["references", "examples"]:
        path = skill_dir / content_dir
        if path.exists() and not has_markdown_files(path):
            errors.append(f"{name}: {content_dir}/ has no markdown files")

    skill_file = skill_dir / "SKILL.md"
    if skill_file.exists():
        text = skill_file.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        if frontmatter is None:
            errors.append(f"{name}: missing YAML frontmatter")
        else:
            skill_name = frontmatter.get("name")
            description = frontmatter.get("description")
            if not skill_name:
                errors.append(f"{name}: frontmatter missing name")
            elif skill_name != name:
                errors.append(f"{name}: frontmatter name does not match directory")
            if not description:
                errors.append(f"{name}: frontmatter missing description")
            elif len(description) > 220:
                errors.append(f"{name}: description should stay concise for Claude Web")
        required_sections = [
            "## Purpose",
            "## When to use this skill",
            "## When not to use this skill",
            "## Core principles",
            "## Output contract",
            "## Quality gates",
            "## Token policy",
        ]
        for section in required_sections:
            if section not in text:
                errors.append(f"{name}: missing section {section}")

    tests_dir = skill_dir / "tests"
    if tests_dir.is_dir():
        for file_name in REQUIRED_TESTS:
            if not (tests_dir / file_name).exists():
                errors.append(f"{name}: missing tests/{file_name}")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        fail("missing skills/ directory")
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        fail("no skills found")
        return 1

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
        errors = check_skill(skill_dir)
        if errors:
            all_errors.extend(errors)
        else:
            ok(f"{skill_dir.name}")

    if all_errors:
        print("\nValidation errors:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"\nValidated {len(skill_dirs)} skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
