# Skill Quality Standard

Every skill in this repository must be small, focused, testable and honest about its limits.

## Required files

```text
skills/<skill-name>/
├── SKILL.md
├── README.md
├── references/
├── examples/
└── tests/
```

## Required SKILL.md sections

- YAML frontmatter with `name` and `description`
- purpose
- when to use
- when not to use
- core principles
- workflow
- safety boundaries
- output contract
- quality gates
- token policy
- examples or links to examples

## Quality rules

- The description must be specific enough to trigger correctly.
- The skill must not try to do everything.
- The skill must say what it does not do.
- The skill must separate confirmed data from assumptions.
- The skill must use placeholders for missing facts.
- The skill must include test prompts.
- Long detail belongs in `references/`, not in the main skill file.

## Forbidden patterns

- Fake client examples that look real.
- Fake testimonials, fake ratings or fake prices.
- Guaranteed SEO, security, legal or business claims.
- Vague rules like "make it professional" without criteria.
- Huge duplicated instructions across skills.
