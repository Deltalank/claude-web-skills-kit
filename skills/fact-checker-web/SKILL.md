---
name: fact-checker-web
description: Verifies website claims and separates confirmed facts, assumptions, missing data, fictional placeholders and source-required statements before publishing or client delivery.
---

# Fact Checker Web

Version: `0.1.0`
Status: `experimental`
Default mode: `balanced`

## Purpose

Use this skill to prevent false, unsupported or misleading claims in website projects, client demos, commercial proposals and AI-generated web content.

This skill helps Claude separate confirmed facts from assumptions, placeholders, fictional/demo content and claims that require a source.

It is especially useful for:

- local business websites
- gym and fitness websites
- landing pages
- client demos
- commercial proposals
- SEO copy
- testimonials and review claims
- pricing claims
- legal or privacy claims
- business ownership claims
- performance, ranking or conversion claims
- AI-generated content that may sound confident but lacks evidence

## When to use this skill

Use this skill when the user asks to:

- verify claims before publishing
- check if website copy invents data
- separate confirmed facts from assumptions
- review testimonials, reviews or ratings
- check if prices, opening hours or business details are confirmed
- identify claims requiring sources
- make content safer for a real client
- review a proposal before sending it
- avoid hallucinations in web content
- mark placeholders correctly
- distinguish fictional/demo content from real claims

Typical trigger phrases:

- "comprueba si esto está inventado"
- "no quiero que Claude se invente datos"
- "verifica los claims"
- "separa confirmado e inferido"
- "dime qué necesita fuente"
- "revisa si puedo poner estas reseñas"
- "comprueba precios, horarios y datos legales"
- "haz fact-check de esta web"
- "marca lo que falta confirmar"

## When not to use this skill

Do not use this skill as the main skill for:

- full website project planning
- visual design
- security review
- local SEO review
- browser QA
- legal advice
- deep market research without sources
- generating fictional stories unrelated to a website/project context
- claiming external facts are verified without checking sources

This skill can identify what needs verification, but it cannot verify current external facts without reliable sources or browsing/research support.

## Core principles

1. Do not invent real-world facts.
2. Do not present fictional content as real.
3. Do not create fake reviews, fake ratings, fake awards, fake prices or fake legal data for real websites.
4. Separate confirmed facts, inferred assumptions, missing data, source-required claims and fictional/demo content.
5. Mark unverifiable claims clearly.
6. Use placeholders when data is missing.
7. Do not overstate certainty.
8. Treat current information as unstable unless verified.
9. Prefer safe wording over impressive but unsupported wording.
10. Keep useful marketing language, but remove unsupported proof.
11. Explain why a claim is risky.
12. Give replacement wording that preserves the user goal safely.

## Fictional or mock content mode

If the user explicitly asks to invent content for a mockup, demo, prototype, classroom exercise or fictional sample, this skill may allow invented content only when it is clearly labeled as fictional or placeholder content.

Rules:

- Fictional content must be marked as `fictional`, `mock`, `demo` or `[PLACEHOLDER]`.
- Fictional reviews must not be presented as real customer reviews.
- Fictional prices must not be presented as real prices.
- Fictional business data must not be used in production copy.
- Fictional legal data must not be used in real legal pages.
- Fictional ratings must not be added to structured data as real ratings.
- The output must warn that fictional content must be replaced before client delivery or publishing.

Acceptable example:

```text
[DEMO TESTIMONIAL - REPLACE BEFORE PUBLISHING]
"Buen ambiente y trato cercano." — Cliente ficticio
```

Not acceptable:

```text
★★★★★ 4.9 based on 243 real reviews
```

Unless the rating and review count are verified from a reliable source and appropriate to use.

## Required certainty labels

Always separate:

### Confirmed

Information explicitly provided by the user, visible in supplied files, or supported by reliable sources.

### Inferred

Reasonable assumption based on context. Must be marked as inferred and not treated as fact.

### Missing / To confirm

Important information that is absent and must not be invented.

### Requires source

Claim that may be true but needs evidence before being published as fact.

### Not verifiable here

Information that cannot be checked in the current environment or without external source access.

### Fictional / demo only

Content intentionally invented for mockups, demos or examples. Must not be treated as real.

## Claim risk labels

Use these labels:

### Safe

Claim is supported by provided facts or is generic without misleading factual assertion.

### Needs source

Claim may be publishable if evidence is provided.

### Needs confirmation

Claim depends on client/business information that has not been confirmed.

### Rewrite recommended

Claim is too strong, vague or risky and should be softened.

### Remove before publishing

Claim is unsupported, misleading, fake or unsafe for a real client site.

### Demo only

Claim is acceptable only as clearly labeled fictional or placeholder content.

## High-risk claim types

Always review these carefully:

- customer reviews
- star ratings
- review counts
- awards
- "best", "number one" or "top" claims
- business owner or team names
- prices and discounts
- opening hours
- addresses and phone numbers
- legal company data
- tax IDs
- health, fitness or transformation promises
- guaranteed results
- SEO ranking guarantees
- security guarantees
- performance scores
- client counts
- years of experience
- certifications
- partnerships
- media mentions
- before/after claims

## Minimum review intake

Before producing a fact-check report, identify:

- website/project type
- whether the content is for a real client, demo or fictional exercise
- business name if relevant
- location if relevant
- claims to review
- sources provided by the user
- files or copy reviewed
- intended publishing context
- whether placeholders are acceptable

If the publishing context is unclear, assume real-world caution and mark risky content as needing confirmation.

## Work modes

### Quick mode

Use when the user wants a fast claim safety check.

Output:

1. Claim safety summary
2. Risky claims
3. Missing confirmations
4. Safe replacement wording
5. Next action

### Balanced mode

Default mode.

Output:

1. Fact-check summary
2. Confirmed / Inferred / Missing / Requires source / Not verifiable / Fictional-demo only
3. Claims table
4. High-risk claims
5. Safe rewrites
6. Placeholder plan
7. What must be verified before publishing
8. Next action

### Deep mode

Use when the user asks for a complete professional claim review.

Output:

1. Executive summary
2. Scope and limitations
3. Publishing context
4. Confirmed facts
5. Inferred assumptions
6. Missing data
7. Claims requiring sources
8. Not verifiable here
9. Fictional/demo-only content
10. Claim-by-claim table
11. Legal/privacy-adjacent claims
12. SEO/commercial claims
13. Review/rating/testimonial claims
14. Pricing and offer claims
15. Health/performance/result claims
16. Safe rewrite set
17. Placeholder replacement checklist
18. Source request checklist
19. Publishing readiness decision
20. Handoff notes

## Output contract

When delivering a fact-check report, use this format unless the user asks for something different:

```md
# Web Fact Check Report

## 1. Fact-check summary

## 2. Scope and limitations

## 3. Publishing context

## 4. Confirmed

## 5. Inferred

## 6. Missing / To confirm

## 7. Requires source

## 8. Not verifiable here

## 9. Fictional / demo only

## 10. Claims table

| Claim | Status | Risk | Why it matters | Safe action | Replacement wording |
|---|---|---|---|---|---|

## 11. High-risk claims

## 12. Safe rewrites

## 13. Placeholder replacement checklist

## 14. What must be verified before publishing

## 15. Next action
```

## Safe wording patterns

Prefer:

- "designed to help"
- "focused on"
- "available for"
- "located in [LOCATION_TO_CONFIRM]"
- "contact for current prices"
- "opening hours to confirm"
- "reviews to verify before publishing"
- "demo text — replace before publishing"

Avoid unsupported:

- "guaranteed results"
- "best in the area"
- "number one"
- "trusted by thousands"
- "4.9 stars" without verification
- "100% secure"
- "first on Google guaranteed"
- "lose X kg in Y days"

## Quality gates

Before saying content is safe to publish, check:

- Are all real-world claims confirmed or sourced?
- Are assumptions labeled?
- Are placeholders visible?
- Are fictional/demo claims clearly marked?
- Are reviews and ratings verified or removed?
- Are prices and hours confirmed or marked pending?
- Are legal/business details confirmed or marked pending?
- Are health, fitness, SEO, security or performance claims softened or sourced?
- Are safe rewrites provided?
- Are remaining risks listed?

Never say "verified" unless evidence is provided or checked. Use "not verified", "requires source" or "safe as placeholder" when appropriate.

## Token policy

Use context carefully.

- Do not fact-check unrelated text unless requested.
- Focus on claims with publishing risk.
- Summarize repeated unsupported claims.
- Do not quote entire long documents unnecessarily.
- Prioritize real-world claims over style preferences.
- If many claims exist, group them by risk type.
- Ask for sources only for claims that matter.

## Recommended file priority

For website projects, inspect in this order when available:

1. `README.md`
2. `index.html`
3. main landing pages
4. legal pages
5. testimonials/reviews sections
6. pricing sections
7. SEO metadata and schema
8. footer business details
9. proposal or sales copy
10. social proof sections

## Handoff to other skills

This skill may recommend:

- `web-project-architect` for project scope
- `web-premium-design` for safer visual/copy presentation
- `security-web-audit` for security and privacy claims
- `seo-local-audit` for SEO claims and schema
- `web-testing-checklist` for delivery validation
- `token-budget-controller` for large projects

Do not assume those skills are installed. Mention them as recommended workflows, not hard dependencies.

## Final rule

A claim can be useful marketing without pretending to be verified proof. Keep the persuasive intent, but remove or label anything that is unsupported, fictional, unverifiable or unsafe for real publishing.
