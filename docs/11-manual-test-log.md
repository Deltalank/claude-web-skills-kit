# Manual Test Log

Status: active

Use this file to record Claude Web tests before packaging any ZIP files.

## Test result labels

- `PASS`
- `FAIL`
- `PARTIAL`
- `NEEDS DESCRIPTION TUNING`
- `NEEDS OUTPUT CONTRACT TUNING`
- `NEEDS SAFETY TUNING`

## Test template

```md
## Test ID

Skill:
Date:
Tester:
Claude surface:
Prompt:
Expected behavior:
Observed behavior:
Result:
Issues found:
Required change:
```

## Required minimum before packaging

Each skill needs at least:

- one expected activation test
- one non-activation test
- one output contract test
- one missing-data behavior test

## Test records

## Test 001

Skill: `web-project-architect`
Date: 2026-06-20
Tester: Deltalank
Claude surface: Claude Web
Prompt:

```text
Quiero crear una web para un gimnasio local y venderla al dueño. Quiero que me digas cómo estructurar el proyecto antes de diseñar o programar nada.
```

Expected behavior:

The skill should activate and produce a website project plan before design or coding. It should separate confirmed facts, inferred assumptions and missing data. It should avoid inventing business details.

Observed behavior:

Claude activated the skill-oriented behavior and produced a balanced project plan. The response separated confirmed data, inferred assumptions and missing data, identified demo/speculative-sale risk, warned against inventing business data, proposed a one-page local gym structure, listed required files, identified SEO, privacy, accessibility and performance considerations, and ended with a focused intake block.

Result:

`PASS`

Issues found:

- Minor wording note: the response said "He añadido el enfoque de la habilidad", which is acceptable but may sound implementation-facing rather than user-facing.
- The response inferred "Tú estás en Canarias" from user context. This is acceptable for this user test, but the skill should continue marking location assumptions as inferred when not explicitly provided in a new chat.

Required change:

No immediate skill change required. Continue testing with a non-activation prompt and a missing-data prompt before packaging.
