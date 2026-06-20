# Validation Process

Validation exists to reduce errors, not to guarantee correctness.

## Validation layers

1. Structural validation
   - expected folders exist
   - expected files exist
   - `SKILL.md` has valid frontmatter

2. Behavioral validation
   - prompts that should trigger the skill
   - prompts that should not trigger the skill

3. Output validation
   - output follows the expected contract
   - unknown data is marked
   - limitations are visible

4. Instruction governance validation
   - review `AGENTS.md`
   - review `CLAUDE.md`
   - detect duplicated, risky or ambiguous instructions

## Manual checklist

Before publishing a skill:

- [ ] Trigger description is clear.
- [ ] Non-trigger cases are documented.
- [ ] Safety boundaries are explicit.
- [ ] Output contract is stable.
- [ ] Token policy is included.
- [ ] Examples are included.
- [ ] Tests are included.
- [ ] Changelog is updated.

## Recommended local checks

If available, use `agent-rules-kit` to inspect agent instruction files:

```bash
agent-rules-kit doctor .
agent-rules-kit check . --format markdown
agent-rules-kit budget .
```

A clean report does not prove the repository is safe or complete.
