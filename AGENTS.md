# AGENTS.md

This repository contains Claude Skills for professional website planning, design, audit, SEO, security, testing and token-efficient AI workflows.

## Scope

These instructions apply to the entire repository.

## Core rules

1. Do not invent facts.
2. Do not add fake reviews, fake clients, fake ratings, fake prices or fake legal data.
3. Do not add secrets, API keys, credentials or private client data.
4. Prefer small, reviewable changes.
5. Do not rewrite large files unless necessary.
6. Keep skills focused. Do not turn one skill into a mega-skill.
7. Use placeholders for unknown data.
8. Document limitations clearly.
9. Add or update tests when changing skill behavior.
10. Update changelog when changing public behavior.

## File conventions

Use this structure for each skill:

```text
skills/<skill-name>/
├── SKILL.md
├── README.md
├── references/
├── examples/
└── tests/
```

## Skill quality standard

Each skill must define:

- purpose
- when to use
- when not to use
- workflow
- safety boundaries
- output contract
- token policy
- quality gates
- examples
- trigger tests
- non-trigger tests

## Safety

Never include:

- real client private information
- unredacted emails
- passwords
- tokens
- API keys
- private phone numbers
- private screenshots
- fake legal claims
- fake SEO guarantees

## Working style

Work in phases:

1. Understand the request.
2. Identify affected files.
3. Make the smallest useful change.
4. Explain what changed.
5. List what remains unverified.

## Validation

Before release, run instruction checks where available and document results in `audits/`.

Do not claim that a clean check proves the repository is safe or complete.
