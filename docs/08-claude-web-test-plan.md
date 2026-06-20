# Claude Web Test Plan

Status: pending manual testing
Packaging: not started

## Purpose

This plan defines how to test each skill in Claude Web before considering the suite ready for packaging and release.

## Test rules

- Test one skill at a time.
- Use a fresh Claude chat when possible.
- Keep prompts short and realistic.
- Record whether the expected skill activates.
- Record whether output follows the skill contract.
- Record if the skill over-triggers or under-triggers.
- Do not use real private client data in tests.

## Result labels

Use these labels:

- `PASS`
- `FAIL`
- `PARTIAL`
- `NEEDS DESCRIPTION TUNING`
- `NEEDS OUTPUT CONTRACT TUNING`
- `NEEDS SAFETY TUNING`

## Test matrix

| Skill | Should trigger prompt | Should not trigger prompt | Expected result |
|---|---|---|---|
| `web-project-architect` | Quiero crear una web para un gimnasio local y venderla al dueño. | Traduce este texto. | Plans before coding. |
| `web-premium-design` | Quiero que esta landing parezca premium y menos genérica. | Revisa cabeceras de seguridad. | Creates visual thesis and design plan. |
| `security-web-audit` | Revisa la seguridad de esta web estática antes de publicarla. | Mejora el diseño visual. | Produces scoped risk review. |
| `seo-local-audit` | Revisa el SEO local de una web de gimnasio en Adeje. | Corrige este error JS. | Reviews metadata, NAP, schema and local signals. |
| `web-testing-checklist` | Haz checklist final antes de entregar esta web al cliente. | Crea schema local. | Produces delivery QA checklist. |
| `fact-checker-web` | Separa qué claims están confirmados y cuáles necesitan fuente. | Diseña una landing premium. | Produces claims table and safe rewrites. |
| `token-budget-controller` | Reduce este prompt y dime qué archivos revisar primero. | Haz un análisis SEO local completo. | Produces context and file-priority plan. |

## Output checks

For each skill, verify:

- The answer follows the expected output contract.
- Missing data is clearly marked.
- Assumptions are labeled.
- The skill does not overclaim results.
- The skill recommends the next appropriate workflow.
- The skill does not produce unnecessary large output.

## Activation tuning notes

If a skill triggers too often:

- Narrow the frontmatter description.
- Add stronger "when not to use" examples.
- Adjust tests.

If a skill does not trigger when expected:

- Make the description more specific.
- Add common user trigger phrases.
- Add examples with realistic wording.

## Manual record template

```md
## Skill tested

Date:
Tester:
Claude surface:
Prompt:
Expected skill:
Observed behavior:
Result label:
Issues found:
Required change:
```

## Release rule

Do not package all ZIP files until every skill has at least one recorded Claude Web activation test.
