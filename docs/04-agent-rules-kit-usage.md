# agent-rules-kit Usage

`agent-rules-kit` is used as an optional local instruction-governance check for files such as `AGENTS.md`, `CLAUDE.md`, Cursor rules, Copilot instructions and Gemini instructions.

It is not a Claude Skill and it is not a web security scanner.

## Purpose in this repository

Use it to detect:

- overly large instruction files
- duplicated rules
- ambiguous instructions
- risky commands or unsafe patterns
- unclear scope
- missing safety boundaries

## Recommended commands

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install agent-rules-kit==0.3.0

agent-rules-kit doctor .
agent-rules-kit check . --format markdown
agent-rules-kit budget .
```

## Reports

Store outputs in:

```text
audits/
```

## Limitations

A clean report does not prove that a repository is safe, complete or professionally finished. It only helps detect instruction-file problems.
