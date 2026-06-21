# Test 022 — fact-checker-web non-activation behavior

Skill: `fact-checker-web`
Date: 2026-06-22
Tester: Deltalank
Claude surface: Claude Web
Result: `PASS`

## Purpose

Verify that `fact-checker-web` does not activate for a simple translation request, even when the user mentions that the skill was installed. The skill should remain inactive unless the user asks to verify claims, check web content, separate confirmed/inferred/missing data, identify unsupported statements or perform a fact-checking workflow.

## Prompt

```text
Acabo de instalar la skill `fact-checker-web`.

Traduce este texto al inglés, sin analizarlo ni hacer fact-check:

“Quiero entrenar hoy en el gimnasio.”
```

## Expected behavior

Claude should answer only with the English translation. It should not activate `fact-checker-web`, should not analyze the sentence as a website claim, should not separate confirmed, inferred, missing, requires-source or not-verifiable information, and should not discuss publishing safety, evidence, sources or claim risk.

## Observed behavior

Claude answered only with the translation:

```text
"I want to train at the gym today."
```

No fact-checking behavior appeared. Claude did not produce a claim analysis, certainty labels, source requirements, publishing warnings, safe rewrites or a web fact-check report.

## Issues found

None.

## Required change

No skill change required. Record this non-activation behavior test as `PASS` and continue with the `fact-checker-web` missing-data behavior test.
