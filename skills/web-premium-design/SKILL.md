---
name: web-premium-design
description: Creates distinctive premium visual direction for websites and landing pages. Use for web UI design, redesign, UX structure, conversion-focused sections and design audits.
---

# Web Premium Design

Version: `0.1.0`
Status: `experimental`
Default mode: `balanced`

## Purpose

Use this skill to create or improve the visual direction, UX structure and conversion-focused layout of professional websites and landing pages.

This skill helps Claude avoid generic AI-looking web design and behave more like a senior web designer, UX strategist and conversion-focused creative director.

It is especially useful for:

- local business websites
- gym and fitness websites
- landing pages
- homepages
- portfolio websites
- client demos
- website redesigns
- visual audits
- premium website proposals
- mobile-first web experiences

## When to use this skill

Use this skill when the user asks to:

- create a premium web design
- improve the look of a website
- make a landing page look less generic
- redesign a homepage
- define a visual direction
- choose layout, sections, typography, color, spacing or imagery
- improve conversion through design
- review if a website looks professional enough for a client
- prepare a demo website for selling to a business
- make a website feel more trustworthy, modern or premium

Typical trigger phrases:

- "quiero que la web se vea premium"
- "no quiero que parezca hecha por IA"
- "mejora el diseño de esta landing"
- "haz una dirección visual profesional"
- "cómo haría esto un diseñador experto"
- "quiero vender esta web a un gimnasio"
- "dime qué le falta visualmente"
- "rediseña esta home"

## When not to use this skill

Do not use this skill as the main skill for:

- pure security review
- legal compliance review
- deep SEO audit
- backend architecture
- isolated JavaScript bug fixing
- school exercises unrelated to web design
- writing casual messages
- translating text
- generating fake reviews or fake business claims

If the task is mainly project planning, use a project-architecture workflow first. If it is mainly security, SEO, factual verification or testing, this skill can contribute visual guidance but should not pretend to replace the specialist workflow.

## Core principles

1. Design from the business goal, not from decoration.
2. Define a clear visual thesis before proposing sections or code.
3. Avoid generic AI design patterns unless intentionally justified.
4. Prioritize mobile-first structure.
5. Make the main CTA obvious.
6. Use trust, clarity and conversion as design requirements.
7. Do not invent testimonials, ratings, photos, prices, awards or claims.
8. Mark missing assets and unknown business facts with placeholders.
9. Prefer one strong visual direction over many weak options.
10. Explain important design trade-offs.
11. If a design choice is risky, say why it is worth it or avoid it.
12. Keep the output practical enough to implement.

## Required certainty labels

Always separate:

### Confirmed

Information explicitly provided by the user or visible in supplied materials.

### Inferred

Reasonable assumptions based on context. Must be marked as inferred.

### Missing / To confirm

Important design or business inputs that are unavailable and must not be invented.

### Not verifiable here

Information that cannot be checked in the current environment.

## Minimum design intake

Before proposing a premium direction, identify:

- business type
- website goal
- target audience
- main CTA
- offer or service focus
- brand tone
- existing assets
- current visual problems
- desired style
- technical stack or platform
- mobile priority
- conversion constraints
- legal or claim-sensitive content

If data is missing, continue only with clearly marked assumptions and placeholders.

## Work modes

### Quick mode

Use when the user wants fast visual direction.

Output:

1. Current design risk
2. Recommended visual direction
3. Hero improvement
4. Top 5 design changes
5. Next action

### Balanced mode

Default mode.

Output:

1. Design summary
2. Confirmed / Inferred / Missing
3. Visual thesis
4. Audience and conversion goal
5. Recommended visual direction
6. Section-by-section UX structure
7. Typography, color and spacing guidance
8. Imagery and asset guidance
9. CTA and trust strategy
10. Anti-generic improvements
11. Risks and placeholders
12. Next action

### Deep mode

Use when the user asks for a complete professional design strategy.

Output:

1. Creative brief
2. Confirmed / Inferred / Missing / Not verifiable
3. Audience psychology
4. Conversion path
5. Visual positioning
6. Design system direction
7. Hero strategy
8. Page architecture
9. Section-by-section design plan
10. Mobile-first layout strategy
11. Typography system
12. Color system
13. Imagery system
14. CTA system
15. Trust and proof strategy
16. Accessibility considerations
17. Performance-aware visual choices
18. Anti-template audit
19. Risks and mitigations
20. Handoff checklist

## Visual thesis

Every meaningful design proposal must define a visual thesis:

- What should the visitor feel in the first 3 seconds?
- What should the visitor understand immediately?
- What should the visitor do next?
- Why does this design fit the business?
- What makes it different from a generic template?

## Anti-generic design rules

Avoid these unless intentionally justified:

- meaningless gradients
- repeated generic cards
- random icon sets
- fake counters
- fake testimonials
- fake ratings
- stock photos that contradict the business
- vague headlines such as "Transform your life"
- overused SaaS-style sections for local businesses
- decorative animations that weaken clarity
- desktop-only hero compositions
- too many CTAs competing at once

## Premium design requirements

A premium website should usually have:

- clear hierarchy
- strong first screen
- mobile-first readability
- intentional typography
- consistent spacing
- controlled color palette
- real or clearly marked placeholder imagery
- obvious CTA
- trust signals
- local relevance when applicable
- accessible contrast
- fast-loading visual choices
- section rhythm
- no invented proof

## Local business and gym defaults

For local businesses, prioritize:

- location clarity
- simple contact path
- phone or WhatsApp CTA
- trust signals
- service clarity
- real photos
- local SEO-friendly structure
- mobile navigation

For gyms and fitness businesses, consider:

- beginner confidence
- training atmosphere
- facilities
- trainers
- schedule clarity
- trial class or WhatsApp contact
- visual energy without false transformation claims
- community and trust
- no exaggerated health or body-result promises

## Output contract

When delivering a design proposal, use this format unless the user asks for something different:

```md
# Premium Web Design Plan

## 1. Design summary

## 2. Confirmed

## 3. Inferred

## 4. Missing / To confirm

## 5. Visual thesis

## 6. Audience and conversion goal

## 7. Recommended visual direction

## 8. Section-by-section UX structure

## 9. Typography, color and spacing guidance

## 10. Imagery and asset guidance

## 11. CTA and trust strategy

## 12. Anti-generic improvements

## 13. Risks and placeholders

## 14. Next action
```

## Quality gates

Before saying a design is premium or client-ready, check:

- Does the hero communicate the offer quickly?
- Is the main CTA obvious on mobile?
- Are design choices intentional and justified?
- Does the structure match the business goal?
- Are photos, reviews and claims real or clearly placeholders?
- Is the layout mobile-first?
- Is the page visually coherent from section to section?
- Are typography and spacing consistent?
- Is the design accessible enough to continue?
- Are heavy assets or animations controlled?
- Does the design avoid generic AI patterns?

Never say a design is ready for a real client if business facts, assets, legal claims, reviews or final copy are still missing.

## Token policy

Use context carefully.

- Do not generate many full design variants unless requested.
- Prefer one strong direction plus one short alternative when useful.
- Do not repeat the entire brief in every section.
- Do not rewrite full code when the user asks only for design critique.
- Keep feedback prioritized.
- If the user provides many files, ask to inspect only the relevant visual files first.
- If the request is large, propose quick, balanced or deep mode.

## Handoff to other skills

This skill may recommend:

- `web-project-architect` for project structure
- `security-web-audit` for security and privacy
- `seo-local-audit` for SEO details
- `web-testing-checklist` for validation before delivery
- `fact-checker-web` for claims, reviews and external data
- `token-budget-controller` for large projects

Do not assume those skills are installed. Mention them as recommended workflows, not hard dependencies.

## Final rule

A premium website is not just a prettier website. It is clearer, more trustworthy, more conversion-focused, more intentional and less generic while remaining honest about missing data and limitations.
