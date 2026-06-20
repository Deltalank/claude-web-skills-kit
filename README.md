# Claude Web Skills Kit

Professional Claude Skills kit for web planning, design, SEO, security, testing and token-efficient AI workflows.

## Status

Version: `0.1.0`
Status: `experimental / professional draft`
Primary language: Spanish
Target platform: Claude Web first, Claude Code later.

## Purpose

This repository contains a professional suite of Claude Skills designed to help create, audit, improve and deliver websites using AI with a structured, secure and verifiable workflow.

The goal is not to collect generic prompts. The goal is to create reusable, documented and testable skills that help Claude work like a disciplined web project assistant.

## Initial skill suite

1. `web-project-architect` — plans professional website projects before design, code, SEO, security or delivery.
2. `web-premium-design` — creates visual direction, UX structure and conversion-focused layout for premium websites.
3. `security-web-audit` — reviews static websites and simple web projects for security, privacy and configuration risks.
4. `seo-local-audit` — reviews local SEO, metadata, schema and local conversion signals.
5. `web-testing-checklist` — guides validation before delivering a website.
6. `fact-checker-web` — separates confirmed facts, uncertain assumptions and claims requiring sources.
7. `token-budget-controller` — reduces unnecessary context usage, repeated instructions and large uncontrolled outputs.

## First release focus

The first implemented skill is:

```text
skills/web-project-architect/
```

This skill acts as the project director. It turns vague website requests into structured project plans before visual design, coding, SEO, security, testing or client delivery.

## Repository philosophy

- Small focused skills are better than one oversized skill.
- Every skill must define when it should and should not be used.
- Every skill must separate confirmed facts, inferred assumptions and missing data.
- No skill may invent client data, legal data, reviews, prices, owners, SEO claims or guaranteed results.
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

The ZIP should contain the skill folder as the root folder:

```text
web-project-architect.zip
└── web-project-architect/
    ├── SKILL.md
    ├── README.md
    ├── references/
    ├── examples/
    └── tests/
```

## Safety notice

This repository does not provide legal advice, pentesting, guaranteed SEO rankings, guaranteed sales results or proof that a website is safe. It provides structured workflows and review checklists that still require human judgment.

## License

MIT.
