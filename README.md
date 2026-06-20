# Claude Web Skills Kit

Professional Claude Skills kit for web planning, design, SEO, security, testing and token-efficient AI workflows.

## Status

Version: `0.1.5`
Status: `experimental / professional draft`
Primary language: Spanish
Target platform: Claude Web first, Claude Code later.

## Purpose

This repository contains a suite of focused Claude Skills for creating, reviewing and delivering website projects with structured workflows.

The goal is not to collect generic prompts. The goal is to create reusable, documented and testable skills that help Claude work like a disciplined web project assistant.

## Implemented skills

1. `web-project-architect` — plans website projects before design, code, SEO, security or delivery.
2. `web-premium-design` — creates visual direction, UX structure and conversion-focused layouts.
3. `security-web-audit` — reviews website security, privacy and configuration risks.
4. `seo-local-audit` — reviews local SEO, metadata, schema and local business signals.
5. `web-testing-checklist` — validates websites before publishing or client delivery.
6. `fact-checker-web` — separates confirmed facts, assumptions, missing data and source-required claims.
7. `token-budget-controller` — controls context size, output length, file priority and phased workflows.

## Skill folders

```text
skills/web-project-architect/
skills/web-premium-design/
skills/security-web-audit/
skills/seo-local-audit/
skills/web-testing-checklist/
skills/fact-checker-web/
skills/token-budget-controller/
```

## Repository philosophy

- Small focused skills are better than one oversized skill.
- Every skill must define when it should and should not be used.
- Every skill must separate confirmed facts, inferred assumptions and missing data.
- Every skill must include quality gates.
- Every skill must be documented, tested and versioned.
- Every skill must avoid unnecessary context usage.
- Security and privacy are not optional.

## Recommended workflow

1. Plan the website project with `web-project-architect`.
2. Define visual direction with `web-premium-design`.
3. Check facts and claims with `fact-checker-web`.
4. Audit security and privacy with `security-web-audit`.
5. Review SEO with `seo-local-audit`.
6. Validate before delivery with `web-testing-checklist`.
7. Use `token-budget-controller` whenever the context grows too large.

## Claude Web installation

Package a skill as a ZIP file and upload it in Claude Web:

```text
Claude → Personalizar → Skills → + → Cargar una habilidad
```

Each skill follows this structure:

```text
<skill-name>/
├── SKILL.md
├── README.md
├── references/
├── examples/
└── tests/
```

## Validation

Before publishing a skill, review:

- folder structure
- frontmatter in `SKILL.md`
- trigger tests
- non-trigger tests
- examples
- references
- output contract
- changelog entry

## Safety notice

This repository provides structured workflows and review checklists. It does not replace human review before using the output in real client projects.

## License

MIT.
