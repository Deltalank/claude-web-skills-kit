# Skill Inventory

Version: `0.1.7`
Status: professional draft

## Implemented skills

| Skill | Purpose | Status |
|---|---|---|
| `web-project-architect` | Plans website projects before design, code or delivery. | Draft |
| `web-premium-design` | Creates premium visual direction and UX structure. | Draft |
| `security-web-audit` | Reviews security, privacy and configuration risks. | Draft |
| `seo-local-audit` | Reviews local SEO and local business search readiness. | Draft |
| `web-testing-checklist` | Validates websites before publishing or client delivery. | Draft |
| `fact-checker-web` | Reviews claims, sources, missing facts and demo-only content. | Draft |
| `token-budget-controller` | Controls context size, output length and phased work. | Draft |

## Required structure

Each skill should include:

```text
SKILL.md
README.md
references/
examples/
tests/
```

## Required tests

Each skill should include:

```text
tests/should-trigger.md
tests/should-not-trigger.md
tests/regression-prompts.md
```

## Next quality level

Before considering a stable release, each skill should be tested in Claude Web with real prompts and adjusted based on activation behavior.
