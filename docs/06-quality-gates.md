# Quality Gates

This document defines the quality standard before packaging skills for Claude Web.

## Repository gates

- [ ] README lists all implemented skills.
- [ ] CHANGELOG includes the latest skill changes.
- [ ] Each skill has `SKILL.md` and `README.md`.
- [ ] Each skill has `references/`, `examples/` and `tests/`.
- [ ] Each skill has trigger, non-trigger and regression prompts.
- [ ] The validation script passes.
- [ ] The GitHub Actions workflow passes.
- [ ] Examples use safe placeholders when needed.

## Skill gates

- [ ] Purpose is clear.
- [ ] Trigger cases are clear.
- [ ] Non-trigger cases are clear.
- [ ] Output contract exists.
- [ ] Boundaries exist.
- [ ] Token policy exists.
- [ ] Quality gates exist.
- [ ] Examples are practical.
- [ ] Tests are reviewable.

## Claude Web gates

- [ ] ZIP packaging has not changed file structure.
- [ ] Skill uploads successfully.
- [ ] Skill activates on expected prompts.
- [ ] Skill does not activate on unrelated prompts.
- [ ] Output follows the expected contract.
- [ ] Missing data is marked clearly.
- [ ] Limitations are visible.

## Stable release rule

A skill should not be considered stable until it passes local structure validation and a manual Claude Web activation test.
