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
- readiness reviews when the website, profile or business data is incomplete

## Scope boundary

This skill is a local SEO readiness, evidence and policy-alignment workflow.

It is not:

- a ranking guarantee workflow
- a traffic or lead guarantee workflow
- a fake review or rating generator
- a competitor scraping workflow
- a legal compliance review
- a Google Business Profile ownership or verification checker unless the user provides evidence
- a Search Console, Analytics or Maps performance verifier unless the user provides data
- a production-readiness declaration

If evidence is incomplete, continue only as a pre-audit or readiness review and label all blocked items clearly.

## Source hierarchy

When discussing current SEO policies, local visibility, structured data, reviews or Google Business Profile behavior, prefer this source hierarchy:

1. Official Google documentation, especially Google Search Central and Google Business Profile Help.
2. schema.org for vocabulary and semantic modeling.
3. Third-party SEO sources only as secondary context, terminology or implementation commentary.

Do not treat schema.org vocabulary as proof that Google supports, displays or rewards a result feature.

Do not present third-party SEO recommendations as official Google ranking facts.

## When to use this skill

Use this skill when the user asks to:

- review SEO for a local business website
- improve local SEO
- check title, meta description, H1, headings or page structure for local search readiness
- review schema or structured data for a local business
- check sitemap or robots.txt in a local SEO delivery workflow
- align a website with Google Business Profile
- improve local search readiness without making fake claims
- identify local SEO gaps before delivery
- plan SEO sections for a local landing page
- audit a website for a city, island, neighborhood or service area
- review business name, category, address, service area, phone, opening hours or local trust signals
- review whether a service-area business should show or hide an address
- check whether a local review, rating or schema claim needs evidence

Typical trigger phrases:

- "revisa el SEO local"
- "quiero posicionar esta web en Google"
- "qué le falta para SEO local"
- "audita title y meta description para una web local"
- "revisa schema LocalBusiness"
- "comprueba sitemap y robots para SEO local"
- "cómo posicionaría una web de gimnasio en Tenerife"
- "mejora esta landing para búsquedas locales"
- "quiero vender esta web con SEO básico"
- "revisa Google Business Profile"
- "comprueba NAP, dirección y teléfono"
- "puedo poner estrellas en schema"

## When not to use this skill

Do not use this skill as the main skill for:

- guaranteeing rankings
- guaranteeing traffic, leads or revenue
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
- general fact-checking without a local SEO context
- token optimization
- browser QA or responsive testing as the main task

This skill can support local SEO planning and review, but it cannot guarantee rankings, traffic, leads, revenue, rich results or Google Business Profile visibility.

If the user asks for fake reviews, fake stars, guaranteed rankings, doorway pages, keyword stuffing or deceptive profile changes, refuse that part and redirect to safe local SEO alternatives.

## Core principles

1. Do not guarantee Google rankings, Maps visibility, traffic, leads, revenue or rich results.
2. Do not invent reviews, ratings, business data, addresses, phone numbers, owners, prices, services, competitors, categories, opening hours, keyword volume or performance metrics.
3. Separate confirmed data from assumptions and missing data.
4. Use placeholders when data is missing.
5. Prioritize useful local content over keyword stuffing.
6. Treat Google Business Profile alignment as important but not fully verifiable unless the user provides profile data, screenshots, URL or access-derived information.
7. Explain what can and cannot be checked from provided files, URLs, snippets or screenshots.
8. Prefer practical fixes that can be implemented before delivery.
9. Distinguish technical SEO, local SEO, content SEO, profile policy and conversion trust.
10. Mark claims requiring evidence.
11. Avoid spam tactics.
12. Keep recommendations suitable for a real local business.
13. Treat LocalBusiness schema as semantic markup, not as a ranking or rich-result guarantee.
14. Treat Search Console, Analytics and Google Business Profile performance data as unavailable unless explicitly provided.
15. Never convert a recommendation into an official Google ranking fact unless the user provides a reliable source and the claim is accurately represented.

## Required certainty labels

Always separate and label evidence using these categories. The labels may be written in English or Spanish, but the distinction must remain clear.

### HECHO CONFIRMADO / Confirmed

Information explicitly provided by the user, visible in supplied files, visible in supplied screenshots, visible in a supplied URL, or present in user-provided Search Console, Analytics or Google Business Profile data.

Do not treat a reasonable guess as confirmed.

### INFERENCIA / Inferred

Reasonable assumptions based on context. Must be marked as inferred and must not be presented as verified.

Example: possible local intent clusters based on category and location may be inferred, but search volume must not be invented.

### DATO FALTANTE / Missing / To confirm

Important SEO, profile, website or business data that is unavailable and must not be invented.

Use placeholders such as `[TO_CONFIRM]`, `[NAP_TO_CONFIRM]`, `[GBP_TO_VERIFY]`, `[REVIEW_TO_VERIFY]` or `[CLAIM_REQUIRES_SOURCE]`.

### NO VERIFICABLE SIN ACCESO / Not verifiable here

Search performance, rankings, Maps visibility, Google Business Profile verification, profile restrictions, Search Console indexing, Analytics traffic, keyword impressions, click data, live deployment behavior or rich-result appearance that cannot be checked in the current environment.

If the user asks for a conclusion on one of these items without evidence, state what is blocked and what source would be needed.

## Input evidence routes

Before choosing the confidence level of the audit, identify the available evidence route:

### No external evidence

The user provides only an idea, business description or request.

Allowed output:

- readiness pre-audit
- data intake checklist
- policy risk review
- missing-data map
- local SEO plan using placeholders

Not allowed:

- confirmed rankings
- confirmed GBP status
- confirmed NAP consistency across the web
- confirmed keyword demand
- confirmed indexability
- confirmed competitors

### Website files or static project files

The user provides HTML, README, sitemap, robots, metadata, schema snippets or legal/contact pages.

Allowed output:

- page structure review
- metadata review
- visible NAP review
- schema concept review
- sitemap and robots review from supplied files
- local content readiness review

Not allowed unless there is live deployment evidence:

- confirmed indexing
- confirmed Google rendering
- confirmed live canonical behavior
- confirmed search performance

### Published URL

The user provides a deployed URL.

Allowed output:

- live-page review if the URL is accessible in the current environment
- visible content review
- deployed metadata/schema checks when visible
- crawlability clues based on accessible files

Still not guaranteed:

- rankings
- Search Console state
- Google index state without a verified inspection source
- rich-result appearance

### JSON-LD or schema snippet

The user provides structured data code.

Allowed output:

- semantic review
- missing required/recommended fields review
- mismatch and claim-risk review
- validation checklist

Not allowed:

- saying Google will show a rich result
- saying the markup is deployed, indexed or eligible in production without URL and validation evidence

### Google Business Profile evidence

The user provides a GBP URL, screenshot, exported info or account-derived data.

Allowed output depends on evidence quality.

Allowed output:

- compare website data to provided profile data
- identify missing or inconsistent business information
- review categories, services, hours, photos, reviews and policy risks from the supplied evidence

Not allowed without account-derived proof:

- claiming the profile is verified
- claiming the profile is unrestricted
- claiming internal performance metrics

### Search Console, Analytics or GBP performance data

The user provides reports or screenshots.

Allowed output:

- analyze the provided metrics
- connect queries, impressions, clicks, CTR, pages or profile interactions to local SEO recommendations

Required caution:

- cite the provided report/screenshot as the evidence source
- do not extrapolate beyond the date range and scope of the data

## Minimum SEO intake

Before producing a serious local SEO audit, identify:

- business name
- business type: storefront, service-area business, hybrid, online-only or unknown
- business type or category
- location, address or service area
- primary service
- secondary services
- target audience
- main conversion action
- website URL or files reviewed
- Google Business Profile status and evidence source
- confirmed NAP data: name, address, phone
- opening hours and special hours
- legal/business identity if relevant
- target city, neighborhood, island, region or area
- existing reviews or proof, if verified
- sitemap and robots availability
- schema or structured data availability
- Search Console, Analytics or GBP performance data availability

If data is missing, continue with placeholders and mark what must be confirmed.

## Business type handling

Classify the local business context before giving location advice.

### Storefront business

The business receives customers at a physical location.

Review:

- visible address consistency
- opening hours
- directions/map/contact path
- local landing page relevance
- LocalBusiness schema using confirmed visible data

### Service-area business

The business visits customers or serves an area and may not receive customers at a public address.

Review:

- whether the address should remain hidden in Google Business Profile if customers are not served there
- service area clarity
- city/area coverage without spam doorway pages
- contact and booking clarity
- schema based only on confirmed public data

Do not assume every local business should publish a street address.

### Hybrid business

The business serves customers both at its location and at customer locations.

Review both storefront and service-area signals, but keep each recommendation evidence-based.

### Online-only business

If the business has no local physical or service-area relevance, do not force this skill as the main workflow. Recommend a more appropriate SEO or web strategy instead.

## Local SEO areas to review

When relevant, check:

- title tags
- meta descriptions
- H1 and heading hierarchy
- page purpose and search intent
- local keywords used naturally
- service and location clarity
- NAP consistency from supplied evidence
- Google Business Profile alignment from supplied evidence
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
- doorway-page risks
- unsupported reputation claims

## NAP rule

NAP means:

- Name
- Address
- Phone

Never invent NAP data. If one of these is missing, mark it as `[TO_CONFIRM]`.

Treat NAP as business identity evidence, not as a reason to invent or overstate ranking impact.

Do not say that "NAP consistency" is an official Google ranking factor by that exact name unless the user provides a reliable source and the statement is accurate. You may still recommend keeping business identity data accurate and consistent across owned assets.

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

Do not claim that a Google Business Profile is verified, unrestricted, optimized or controlled unless the user provides evidence.

Do not assume all profile information comes only from the business owner. Treat public profile information as potentially compiled from multiple sources unless the user confirms account-level data.

## Schema / structured data guidance

When suggesting schema:

- choose the most appropriate type for the business context
- use only confirmed business data
- mark unknown values with placeholders
- do not invent ratings or reviews
- do not add `aggregateRating` unless verified and compliant
- validate structured data after implementation
- avoid schema that misrepresents the business
- distinguish schema.org vocabulary from Google-supported search features
- state that valid structured data does not guarantee rich results
- ensure marked data reflects visible, relevant page content

For gyms and fitness businesses, possible schema families may include local business or sports-related organization types, but the exact type must match confirmed business reality.

### Review and aggregateRating caution

Never imply that adding `aggregateRating` or `review` to the website of the business itself will guarantee stars in Google Search.

If the reviews are self-serving, controlled by the reviewed business, copied from other sites, manually curated without clear user submission evidence, or not verified, mark the rating/review markup as unsafe or not recommended for Google rich-result purposes.

If the user asks to add stars without proof, refuse that part and propose safe alternatives:

- show real testimonials only when verified and permitted
- link to the public review source when appropriate
- use neutral trust copy without fake numbers
- mark ratings as `[RATING_TO_VERIFY]` until evidence exists

## Review and rating policy

Never create or suggest fake reviews.

Never add:

- fake star ratings
- fake review count
- fake testimonials
- fake awards
- fake "best in town" claims
- fake before/after results
- fake reputation claims
- fake review widgets

Use placeholders:

- `[REVIEW_TO_VERIFY]`
- `[RATING_TO_VERIFY]`
- `[AWARD_TO_VERIFY]`
- `[CLAIM_REQUIRES_SOURCE]`
- `[GBP_TO_VERIFY]`
- `[SEARCH_CONSOLE_REQUIRED]`
- `[ANALYTICS_REQUIRED]`

## Keyword and intent guidance

Do not invent keyword volume, difficulty, CTR, impressions, clicks or ranking positions.

Allowed without external keyword data:

- local intent hypotheses
- service + location clusters
- category + city clusters
- brand queries if the brand name is provided
- "near me" or "open now" intent discussion as generic local search behavior

Required wording:

- "This is a local intent hypothesis, not confirmed keyword volume."
- "Search Console, GBP Performance or a keyword tool would be needed to verify demand."

Avoid keyword stuffing and doorway pages. Recommend useful, distinct pages only when each page has a real service, area and user purpose.

## Forbidden claims and phrases

Do not say:

- "This will rank."
- "SEO guaranteed."
- "You will be first on Google."
- "Guaranteed top 1/top 3."
- "This schema will give you stars."
- "Your Google Business Profile is verified" without proof.
- "Your profile is optimized" without evidence.
- "Your competitors are X" without evidence.
- "These keywords have this volume" without a named data source.
- "Your local reputation is strong" without review evidence.
- "This is ready for production" without a full release and QA process.
- "Add the city to the business name" unless it is part of the real business name.
- "Create many duplicate city pages" as a ranking tactic.
- "Use Google reviews on your own site to get stars" as a guaranteed outcome.

Prefer wording such as:

- "better aligned with local SEO basics"
- "ready for manual indexing and performance checks"
- "pending verification in Google Business Profile"
- "not verifiable without Search Console or profile data"
- "valid structured data does not guarantee rich results"
- "this is an inference, not a confirmed fact"

## Work modes

### Quick mode

Use when the user wants a fast SEO check.

Output:

1. SEO summary
2. Evidence level
3. Top local SEO gaps
4. Quick wins
5. Missing data
6. Next action

### Balanced mode

Default mode.

Output:

1. Audit summary
2. Evidence level and limitations
3. Confirmed / Inferred / Missing / Not verifiable
4. Local SEO positioning
5. Metadata review
6. Heading and page structure review
7. Content and service relevance review
8. NAP and Google Business Profile alignment
9. Schema / structured data review
10. Sitemap, robots and indexability review
11. Trust and review-claim review
12. Prioritized recommendations
13. Manual checks before delivery
14. Next action

### Deep mode

Use when the user asks for a full professional local SEO audit.

Output:

1. Executive summary
2. Scope and limitations
3. Source and evidence hierarchy
4. Confirmed / Inferred / Missing / Not verifiable
5. Business and local search context
6. Audience and search intent
7. Keyword intent map without spam
8. Page architecture review
9. Metadata review
10. Heading structure review
11. Content depth and service relevance
12. Local signals and NAP consistency
13. Google Business Profile alignment
14. Schema / structured data plan
15. Sitemap and robots review
16. Internal linking opportunities
17. Image SEO and alt text guidance
18. Trust, reviews and claim verification
19. Performance and mobile SEO considerations
20. Findings table
21. Fix plan by priority
22. Manual verification checklist
23. Next workflow handoff

## Output contract

When delivering an audit, use this format unless the user asks for something different:

```md
# Local SEO Audit

## 1. Audit summary

## 2. Scope, evidence and limitations

## 3. Source hierarchy used

## 4. HECHO CONFIRMADO / Confirmed

## 5. INFERENCIA / Inferred

## 6. DATO FALTANTE / Missing / To confirm

## 7. NO VERIFICABLE SIN ACCESO / Not verifiable here

## 8. Local SEO positioning

## 9. Metadata review

## 10. Heading and page structure review

## 11. Content and service relevance review

## 12. NAP and Google Business Profile alignment

## 13. Schema / structured data review

## 14. Trust, reviews and claim verification

## 15. Sitemap, robots and indexability review

## 16. Risks by priority

| Priority | Area | Finding or risk | Evidence level | Impact | Recommended fix | Verification |
|---|---|---|---|---|---|---|

## 17. Prioritized recommendations

## 18. Manual checks before delivery

## 19. Next action
```

If the user specifies an exact output contract, follow the user's requested sections exactly while preserving the evidence labels and safety rules.

## Quality gates

Before saying local SEO is ready for delivery, check:

- Is the target location or service area clear?
- Is the business type clear: storefront, service-area, hybrid or unknown?
- Is the primary service clear?
- Is the main CTA clear?
- Are title and meta description specific?
- Is there one clear H1?
- Are headings structured logically?
- Is NAP confirmed or marked as missing?
- Is Google Business Profile evidence provided or marked as not verifiable?
- Are reviews and ratings verified or removed?
- Is schema based only on confirmed, visible data?
- Are sitemap and robots present or planned?
- Are local claims honest?
- Are keyword ideas marked as hypotheses unless supported by data?
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

When evidence is missing, the correct output is not confidence. The correct output is a clear boundary, a safe placeholder and a next verification step.
