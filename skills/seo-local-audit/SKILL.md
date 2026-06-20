---
name: seo-local-audit
description: Reviews local-business websites for local SEO, search visibility, metadata, structure, schema, Google Business Profile alignment and location-based conversion risks.
---

# SEO Local Audit

Version: `0.1.0`
Status: `experimental`
Default mode: `balanced`

## Purpose

Use this skill to review and improve the local SEO readiness of websites for local businesses.

This skill helps Claude evaluate whether a website is structured, written and documented in a way that can support local search visibility without inventing data, reviews, rankings or business claims.

It is especially useful for:

- local business websites
- gym and fitness websites
- restaurants, academies, clinics and service businesses
- landing pages targeting a city or area
- websites connected to Google Business Profile
- static websites hosted on shared hosting or GitHub Pages
- pre-delivery SEO checks
- local SEO audits before selling a website to a client

## When to use this skill

Use this skill when the user asks to:

- review SEO for a local business website
- improve local SEO
- check title, meta description, H1, headings or page structure
- review schema or structured data
- check sitemap or robots.txt
- align a website with Google Business Profile
- improve ranking potential without making fake claims
- identify local SEO gaps before delivery
- plan SEO sections for a local landing page
- audit a website for a city, island, neighborhood or service area

Typical trigger phrases:

- "revisa el SEO local"
- "quiero posicionar esta web en Google"
- "qué le falta para SEO"
- "audita title y meta description"
- "revisa schema"
- "comprueba sitemap y robots"
- "cómo posicionaría una web de gimnasio en Tenerife"
- "mejora esta landing para búsquedas locales"
- "quiero vender esta web con SEO básico"

## When not to use this skill

Do not use this skill as the main skill for:

- guaranteeing rankings
- creating fake reviews or fake ratings
- manipulating search engines deceptively
- keyword stuffing
- spam doorway pages
- scraping competitors without permission
- legal compliance review
- security review
- pure visual design
- backend development
- school exercises unrelated to SEO

This skill can support local SEO planning and review, but it cannot guarantee rankings, traffic, leads or revenue.

## Core principles

1. Do not guarantee Google rankings.
2. Do not invent reviews, ratings, business data, addresses, phone numbers, owners, prices or opening hours.
3. Separate confirmed data from assumptions.
4. Use placeholders when data is missing.
5. Prioritize useful local content over keyword stuffing.
6. Treat Google Business Profile alignment as important but not fully verifiable unless the user provides data.
7. Explain what can and cannot be checked from provided files.
8. Prefer practical fixes that can be implemented before delivery.
9. Distinguish technical SEO, local SEO and content SEO.
10. Mark claims requiring evidence.
11. Avoid spam tactics.
12. Keep recommendations suitable for a real local business.

## Required certainty labels

Always separate:

### Confirmed

Information explicitly provided by the user or visible in supplied files.

### Inferred

Reasonable assumptions based on context. Must be marked as inferred.

### Missing / To confirm

Important SEO or business data that is unavailable and must not be invented.

### Not verifiable here

Search performance, rankings, Google Business Profile data, indexing status, Search Console data or live deployment behavior that cannot be checked in the current environment.

## Minimum SEO intake

Before producing a serious local SEO audit, identify:

- business name
- business type
- location or service area
- primary service
- secondary services
- target audience
- main conversion action
- website URL or files reviewed
- Google Business Profile status
- confirmed NAP data: name, address, phone
- opening hours
- legal/business identity if relevant
- target city or area
- existing reviews or proof, if verified
- sitemap and robots availability
- schema or structured data availability

If data is missing, continue with placeholders and mark what must be confirmed.

## Work modes

### Quick mode

Use when the user wants a fast SEO check.

Output:

1. SEO summary
2. Top local SEO gaps
3. Quick wins
4. Missing data
5. Next action

### Balanced mode

Default mode.

Output:

1. Audit summary
2. Confirmed / Inferred / Missing / Not verifiable
3. Local SEO positioning
4. Metadata review
5. Heading and page structure review
6. Content and service relevance review
7. NAP and Google Business Profile alignment
8. Schema / structured data review
9. Sitemap, robots and indexability review
10. Trust and review-claim review
11. Prioritized recommendations
12. Manual checks before delivery
13. Next action

### Deep mode

Use when the user asks for a full professional local SEO audit.

Output:

1. Executive summary
2. Scope and limitations
3. Confirmed / Inferred / Missing / Not verifiable
4. Business and local search context
5. Audience and search intent
6. Keyword intent map without spam
7. Page architecture review
8. Metadata review
9. Heading structure review
10. Content depth and service relevance
11. Local signals and NAP consistency
12. Google Business Profile alignment
13. Schema / structured data plan
14. Sitemap and robots review
15. Internal linking opportunities
16. Image SEO and alt text guidance
17. Trust, reviews and claim verification
18. Performance and mobile SEO considerations
19. Findings table
20. Fix plan by priority
21. Manual verification checklist
22. Next workflow handoff

## Local SEO areas to review

When relevant, check:

- title tags
- meta descriptions
- H1 and heading hierarchy
- page purpose and search intent
- local keywords used naturally
- service and location clarity
- NAP consistency
- Google Business Profile alignment
- opening hours if confirmed
- map embeds if used
- local trust signals
- verified reviews only
- image alt text
- Open Graph metadata
- schema / structured data
- sitemap.xml
- robots.txt
- canonical URLs
- internal links
- mobile usability
- page speed basics
- duplicate or thin pages
- spammy keyword stuffing
- fake ranking claims

## NAP rule

NAP means:

- Name
- Address
- Phone

Never invent NAP data. If one of these is missing, mark it as `[TO_CONFIRM]`.

## Google Business Profile alignment

When reviewing alignment, check whether the website content supports:

- business name
- category or service type
- address or service area
- phone number
- opening hours
- service descriptions
- real photos
- reviews or proof only when verified
- clear contact action

If the user has not provided Google Business Profile information, mark this section as pending verification.

## Schema / structured data guidance

When suggesting schema:

- choose the most appropriate type for the business context
- use only confirmed business data
- mark unknown values with placeholders
- do not invent ratings or reviews
- do not add aggregateRating unless verified and compliant
- validate structured data after implementation
- avoid schema that misrepresents the business

For gyms and fitness businesses, possible schema families may include local business or sports-related organization types, but the exact type must match confirmed business reality.

## Review and rating policy

Never create or suggest fake reviews.

Never add:

- fake star ratings
- fake review count
- fake testimonials
- fake awards
- fake "best in town" claims
- fake before/after results

Use placeholders:

- `[REVIEW_TO_VERIFY]`
- `[RATING_TO_VERIFY]`
- `[AWARD_TO_VERIFY]`
- `[CLAIM_REQUIRES_SOURCE]`

## Output contract

When delivering an audit, use this format unless the user asks for something different:

```md
# Local SEO Audit

## 1. Audit summary

## 2. Scope and limitations

## 3. Confirmed

## 4. Inferred

## 5. Missing / To confirm

## 6. Not verifiable here

## 7. Local SEO positioning

## 8. Metadata review

## 9. Heading and page structure review

## 10. Content and service relevance review

## 11. NAP and Google Business Profile alignment

## 12. Schema / structured data review

## 13. Sitemap, robots and indexability review

## 14. Trust, reviews and claim verification

## 15. Prioritized recommendations

| Priority | Area | Finding | Impact | Recommended fix | Verification |
|---|---|---|---|---|---|

## 16. Manual checks before delivery

## 17. Next action
```

## Quality gates

Before saying local SEO is ready for delivery, check:

- Is the target location clear?
- Is the primary service clear?
- Is the main CTA clear?
- Are title and meta description specific?
- Is there one clear H1?
- Are headings structured logically?
- Is NAP confirmed or marked as missing?
- Are reviews and ratings verified or removed?
- Is schema based only on confirmed data?
- Are sitemap and robots present or planned?
- Are local claims honest?
- Are manual checks listed?

Never say "this will rank" or "SEO guaranteed". Use wording like "better aligned with local SEO basics" or "ready for manual indexing and performance checks".

## Token policy

Use context carefully.

- Do not produce a huge keyword report unless requested.
- Prioritize the pages and files that affect local SEO.
- Avoid repeating the whole website copy.
- Summarize duplicate issues.
- Ask for Search Console or Google Business Profile data only when needed.
- If the project is large, recommend a staged audit.

## Recommended file priority

For static local business websites, inspect in this order when available:

1. `README.md`
2. `index.html`
3. main service pages
4. legal/contact pages
5. `sitemap.xml`
6. `robots.txt`
7. JSON-LD or schema blocks
8. metadata and Open Graph sections
9. image filenames and alt text
10. deployment URL if available

## Handoff to other skills

This skill may recommend:

- `web-project-architect` for project structure
- `web-premium-design` for visual trust and conversion design
- `security-web-audit` for privacy, scripts and tracking risks
- `web-testing-checklist` for pre-delivery validation
- `fact-checker-web` for current SEO facts, policies or claims
- `token-budget-controller` for large websites

Do not assume those skills are installed. Mention them as recommended workflows, not hard dependencies.

## Final rule

Local SEO is not about stuffing city names into a page. It is about making the business, location, services, trust signals and contact path clear, accurate and verifiable.
