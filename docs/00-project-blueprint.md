# Claude Web Skills Kit — Project Blueprint

Version: `0.1.0`
Status: `experimental / professional draft`
Primary language: Spanish
Target platform: Claude Web first, Claude Code later.

## 1. Purpose

This repository contains a professional suite of Claude Skills designed to help create, audit, improve and deliver websites using AI with a structured, secure and verifiable workflow.

The goal is not to create generic prompts. The goal is to create reusable, documented and testable skills that help Claude work like a disciplined web project assistant.

## 2. Philosophy

1. Small focused skills are better than one oversized skill.
2. Every skill must define when it should and should not be used.
3. Every skill must separate confirmed facts, inferred assumptions and missing data.
4. No skill may invent client data, legal data, reviews, prices, business owners, SEO claims or guaranteed results.
5. Every skill must include quality gates.
6. Every skill must be documented, tested and versioned.
7. Every skill must avoid unnecessary context usage.
8. Security and privacy are not optional.
9. Outputs must be useful for real client work, not just impressive-looking text.
10. A clean report does not prove that a project is safe, finished or legally compliant.

## 3. Skill suite

Initial planned skills:

- `web-project-architect`
- `web-premium-design`
- `security-web-audit`
- `seo-local-audit`
- `web-testing-checklist`
- `fact-checker-web`
- `token-budget-controller`

## 4. First skill

The first skill is `web-project-architect`.

Reason: before Claude designs or codes a website, it must understand the business, audience, conversion path, required pages, risks, missing data, technical stack, legal placeholders, SEO constraints, security boundaries and delivery criteria.

## 5. Repository quality standard

A skill is not considered ready unless it includes:

- `SKILL.md`
- clear trigger description
- clear non-trigger cases
- workflow
- safety boundaries
- output contract
- token policy
- examples
- trigger tests
- non-trigger tests
- changelog entry
- packaging instructions

## 6. Safety rules

This repository must not contain secrets, tokens, real private client data, fake testimonials, fake reviews, fake legal claims, fake SEO guarantees or fake business results.

Use placeholders such as:

- `[CLIENT_NAME]`
- `[BUSINESS_ADDRESS_TO_CONFIRM]`
- `[LEGAL_EMAIL_TO_CONFIRM]`
- `[PRICE_TO_CONFIRM]`
- `[REVIEW_TO_VERIFY]`
- `[CLAIM_REQUIRES_SOURCE]`
