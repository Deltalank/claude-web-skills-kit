# CLAUDE.md

This repository is a professional Claude Skills kit for website workflows.

## How Claude should work in this repo

Claude must behave like a careful maintainer, not like a generic prompt generator.

## Priorities

1. Correctness
2. Safety
3. Clear scope
4. Practical usefulness
5. Maintainability
6. Token efficiency
7. Documentation quality

## Required behavior

- Separate confirmed facts from assumptions.
- Use `[TO_CONFIRM]` placeholders for missing data.
- Do not invent examples that look real.
- Prefer fictional examples unless real data is explicitly approved.
- Keep skills modular.
- Keep `SKILL.md` concise.
- Move long details into `references/`.
- Add examples and tests for every important behavior.
- Do not overpromise what a skill can do.
- Mention limitations clearly.

## When editing a skill

Check:

- Is the trigger description precise?
- Does it say when not to use the skill?
- Does it include a workflow?
- Does it include safety boundaries?
- Does it include an output contract?
- Does it include quality gates?
- Does it avoid unnecessary context bloat?
- Does it have examples?
- Does it have tests?

## Forbidden

Do not:

- add secrets
- add real client private data
- create fake testimonials
- create fake ratings
- create fake prices
- claim legal compliance without review
- claim security guarantees
- claim SEO ranking guarantees
- use vague phrases like "make it professional" without defining criteria

## Output style

Be direct, structured and practical.

When something is uncertain, say so.
