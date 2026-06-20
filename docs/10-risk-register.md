# Risk Register

Status: active
Packaging: not started

This register tracks risks that must be controlled before packaging and uploading skills to Claude Web.

## Risk levels

- `High`: must be fixed before packaging.
- `Medium`: should be fixed before broad use.
- `Low`: track and improve over time.

## Current risks

| Risk | Level | Status | Control |
|---|---:|---|---|
| Skill activates too broadly | Medium | Open | Manual Claude Web activation tests. |
| Skill does not activate when expected | Medium | Open | Trigger prompt tests and description tuning. |
| Output ignores contract | Medium | Open | Manual output checks. |
| Missing data is treated as fact | High | Controlled | Fact-checker rules, placeholders and quality gates. |
| Demo content used as production content | High | Controlled | Demo-only labels and replacement warnings. |
| Context grows too large | Medium | Controlled | Token budget controller and staged workflow. |
| Packaging changes folder structure | Medium | Open | ZIP inspection before upload. |
| Automation passes but manual behavior fails | Medium | Open | Claude Web manual test plan. |
| README and CHANGELOG drift | Low | Controlled | Release consistency check. |
| Sensitive data appears in examples | High | Controlled | Repository hygiene check. |

## Release rule

A risk can be accepted only if it is documented with a reason and a follow-up action.
