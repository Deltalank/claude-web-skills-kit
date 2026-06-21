# seo-local-audit

`seo-local-audit` reviews local-business websites for local SEO readiness, search visibility alignment, metadata, page structure, schema, Google Business Profile alignment and location-based conversion risks.

It is designed for cautious, evidence-based local SEO review. It does not promise rankings, traffic, leads, revenue or rich results.

## Purpose

Use this skill when a user wants to review or improve the local SEO readiness of a real local business website.

Typical use cases:

- review local SEO before publishing or delivering a client website
- improve a local business website without fake claims
- check title tags, meta descriptions, H1s and headings
- review local service and location clarity
- review NAP: name, address and phone
- align website content with Google Business Profile data
- review LocalBusiness schema or other structured data
- check sitemap, robots and basic indexability signals
- identify missing local trust signals
- avoid fake reviews, fake ratings and fake ranking claims

## Main value

This skill helps Claude produce a structured local SEO review while keeping strict boundaries around evidence.

It should separate:

- `HECHO CONFIRMADO / Confirmed`
- `INFERENCIA / Inferred`
- `DATO FALTANTE / Missing / To confirm`
- `NO VERIFICABLE SIN ACCESO / Not verifiable here`

The goal is not to sound impressive. The goal is to identify what can be checked, what is missing, what is risky and what should be verified next.

## What this skill does

It can help review:

- local SEO positioning
- business name, address, phone and service-area clarity
- Google Business Profile alignment from supplied evidence
- metadata and heading structure
- local content relevance
- service and location pages
- LocalBusiness schema readiness
- reviews, ratings and reputation claims
- sitemap and robots availability
- basic indexability readiness
- local trust and conversion signals
- risks before delivery to a client

## What this skill does not do

This skill does not:

- guarantee Google rankings
- guarantee Maps visibility
- guarantee traffic, leads or sales
- generate fake reviews
- generate fake star ratings
- invent business data
- invent addresses, phones, hours, prices or services
- invent competitors
- invent keyword volume or demand
- verify Google Business Profile ownership without proof
- verify Search Console, Analytics or GBP performance without supplied data
- declare a website production-ready
- replace legal, privacy or security review

If the user asks for fake reviews, fake stars, guaranteed rankings, keyword stuffing or duplicate doorway pages, Claude should refuse that part and suggest safe alternatives.

## Evidence levels

The quality of the audit depends on the evidence provided.

| Evidence provided | What the skill can do | What remains limited |
|---|---|---|
| No URL or files | Pre-audit, intake checklist, missing-data map, policy-risk review | No confirmed rankings, profile status, indexability, competitors or keyword demand |
| Website files | Review metadata, headings, visible NAP, schema snippets, sitemap and robots from supplied files | No live Google indexing or Search Console verification |
| Published URL | Review visible deployed content if accessible | No ranking, Search Console, Analytics or GBP internal performance unless supplied |
| JSON-LD snippet | Review schema conceptually and flag missing or risky fields | No guarantee of rich results or live deployment |
| GBP URL/screenshot/data | Compare website to supplied profile evidence | No account-level status unless the data proves it |
| Search Console / Analytics / GBP Performance data | Review provided metrics within their scope | No extrapolation beyond the supplied date range and source |

## Minimum input checklist

For a serious local SEO audit, ask for as many of these as possible:

- business name
- business type: storefront, service-area business, hybrid or unknown
- business category or service type
- address or service area
- phone number
- opening hours and special hours
- website URL or project files
- Google Business Profile URL, screenshots or exported data
- primary and secondary services
- target city, island, neighborhood, region or service area
- main conversion action
- confirmed reviews or rating evidence, if any
- current schema or JSON-LD snippet, if any
- sitemap and robots files
- Search Console, Analytics or GBP Performance screenshots, if available

Missing data should be marked with placeholders such as:

- `[TO_CONFIRM]`
- `[NAP_TO_CONFIRM]`
- `[GBP_TO_VERIFY]`
- `[REVIEW_TO_VERIFY]`
- `[RATING_TO_VERIFY]`
- `[CLAIM_REQUIRES_SOURCE]`

## Business types supported

### Storefront business

A business that receives customers at a physical location.

Examples:

- gym
- restaurant
- clinic
- academy
- shop

The audit can review visible address consistency, local content, hours, directions, contact path and LocalBusiness schema based on confirmed data.

### Service-area business

A business that visits customers or serves a defined area and may not receive customers at a public address.

Examples:

- plumber
- electrician
- mobile personal trainer
- home repair service

The audit should not assume the business must publish a street address. It should review service-area clarity and avoid doorway-page tactics.

### Hybrid business

A business that receives customers at a location and also serves customers elsewhere.

The audit should review both physical-location and service-area signals, while keeping recommendations evidence-based.

### Online-only business

If the business has no physical local or service-area relevance, this skill should not be the main workflow.

## Google Business Profile limits

Google Business Profile is important for local SEO, but the skill must not claim that a profile is verified, optimized, unrestricted or controlled unless the user provides evidence.

Without profile evidence, Claude should say that GBP alignment is pending verification.

The skill may ask for:

- GBP URL
- screenshots
- category data
- service data
- hours
- profile verification status if known
- performance screenshots if available

## Schema and structured data limits

The skill can review LocalBusiness schema readiness, but must keep these limits clear:

- schema.org vocabulary is not the same as Google rich-result eligibility
- valid structured data does not guarantee rich results
- schema must describe visible and truthful page content
- unknown values should use placeholders, not invented data
- reviews and ratings must not be invented
- `aggregateRating` and `review` require special caution

Do not imply that adding `aggregateRating` will create stars in Google Search.

## Review and rating rules

Never create or suggest:

- fake reviews
- fake ratings
- fake review count
- fake testimonials
- fake awards
- fake “best in town” claims
- fake before/after results
- fake reputation claims

Safe alternatives:

- ask for verifiable review evidence
- link to real public review sources when appropriate
- use neutral trust copy without fake numbers
- mark claims as `[CLAIM_REQUIRES_SOURCE]`

## Keyword and intent limits

Without Search Console, GBP Performance or an explicitly provided keyword source, the skill can only propose local-intent hypotheses.

Allowed wording:

```text
This is a local intent hypothesis, not confirmed keyword volume.
```

```text
Search Console, GBP Performance or a keyword tool would be needed to verify demand.
```

The skill must not invent:

- search volume
- keyword difficulty
- CTR
- impressions
- clicks
- rankings
- competitors

## Safe wording

Prefer wording such as:

- “better aligned with local SEO basics”
- “pending verification in Google Business Profile”
- “not verifiable without Search Console or profile data”
- “this is an inference, not a confirmed fact”
- “valid structured data does not guarantee rich results”
- “ready for manual indexing and performance checks”

Avoid wording such as:

- “SEO guaranteed”
- “this will rank”
- “you will be first on Google”
- “guaranteed top 3”
- “this schema will give you stars”
- “your GBP is verified” without evidence
- “your competitors are X” without evidence
- “these keywords have this volume” without a named source
- “your local reputation is strong” without evidence

## Default mode

Balanced.

## Status

Experimental v0.1.0.

Manual Claude Web testing is still pending for this skill.

Required minimum tests before marking the skill as minimum pre-packaging complete:

- expected activation
- non-activation
- missing-data behavior
- output-contract behavior

## Recommended related skills

- `web-project-architect` for project structure
- `web-premium-design` for visual trust and conversion design
- `security-web-audit` for privacy, scripts and tracking risks
- `web-testing-checklist` for pre-delivery validation
- `fact-checker-web` for current SEO facts, policies or claims
- `token-budget-controller` for large websites or long audits

These are recommended workflows, not hard dependencies.

## Important limitation

This skill does not guarantee rankings, leads, traffic, revenue, Maps visibility or rich results.

It creates a structured local SEO review workflow that requires real data, clear evidence labels and manual verification.

Do not package this skill as release-ready until the required Claude Web manual tests are completed and documented.
