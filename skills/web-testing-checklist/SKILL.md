---
name: web-testing-checklist
description: Validates websites before publishing or client delivery. Use for final QA, responsive checks, links, forms, CTAs, SEO basics, accessibility and browser testing.
---

# Web Testing Checklist

Version: `0.1.0`
Status: `experimental`
Default mode: `balanced`

## Purpose

Use this skill to validate a website before publishing, client review or final delivery.

This skill helps Claude behave like a practical QA reviewer for websites. It focuses on what must be checked before a real user or client sees the site.

It is especially useful for:

- static websites
- local business websites
- gym and fitness websites
- landing pages
- client demos
- GitHub Pages deployments
- Hostinger or shared-hosting deployments
- final pre-delivery reviews
- manual QA checklists
- responsive checks
- contact and CTA validation

## When to use this skill

Use this skill when the user asks to:

- test a website before delivery
- check if a website is ready to publish
- create a final QA checklist
- validate links, buttons or CTAs
- check mobile, tablet and desktop layout
- review forms and contact flows
- check WhatsApp links
- check navigation
- check legal links
- check browser console issues
- check images and loading behavior
- prepare a client handoff checklist

Typical trigger phrases:

- "comprueba si la web está lista"
- "haz un checklist antes de entregar"
- "valida esta landing"
- "revisa botones y enlaces"
- "comprueba responsive"
- "qué pruebas hago antes de publicarla"
- "testea la web antes de subirla"
- "dime si puedo enseñársela al cliente"
- "haz QA de esta web"

## When not to use this skill

Do not use this skill as the main skill for:

- deep security review
- penetration testing
- legal compliance certification
- deep SEO strategy
- pure visual design
- project architecture from zero
- backend test automation unless specifically scoped
- creating fake reviews or fake proof
- school exercises unrelated to website QA

If the main problem is security, SEO, design or project planning, this skill can provide final validation but should not replace the specialist workflow.

## Core principles

1. Do not say a site is ready unless scope and missing checks are clear.
2. Separate checked items from unchecked items.
3. Mark what requires manual browser testing.
4. Mark what requires deployed URL testing.
5. Do not invent test results.
6. Do not claim that a website passed tests that were not performed.
7. Prioritize user-facing failures before minor polish.
8. Validate the main conversion path first.
9. Keep findings actionable and ordered by delivery risk.
10. Include mobile checks by default.
11. Include accessibility and performance basics.
12. Make final client handoff criteria explicit.

## Required certainty labels

Always separate:

### Checked

Items actually reviewed from provided files, screenshots, user context or explicit test results.

### Needs manual test

Items that require a browser, device, deployment URL or user interaction.

### Missing / To confirm

Required project files, links, business data or access that are unavailable.

### Not verifiable here

Behavior that cannot be checked in the current environment.

## Severity labels

Use these labels for findings:

### Blocker

Issue that should prevent client delivery or publishing.

### High

Serious issue that should be fixed before handoff.

### Medium

Meaningful issue that should be fixed soon.

### Low

Minor polish or quality improvement.

### Pass

Checked item appears acceptable within the reviewed scope.

## Minimum QA intake

Before producing a final delivery checklist, identify:

- website type
- deployment target
- pages to test
- main CTA
- contact method
- forms or external links
- legal pages
- responsive requirements
- browser/device targets
- whether a live URL exists
- whether files or screenshots were provided
- whether analytics, maps, videos or third-party scripts exist

If key context is missing, create a scoped checklist and mark what requires manual testing.

## Work modes

### Quick mode

Use when the user wants fast pre-delivery QA.

Output:

1. Readiness summary
2. Top blockers
3. Main CTA test
4. Responsive checks
5. Next action

### Balanced mode

Default mode.

Output:

1. QA summary
2. Checked / Needs manual test / Missing / Not verifiable
3. Critical user paths
4. Links and navigation checks
5. CTA and contact checks
6. Responsive checklist
7. Forms and data-flow checks
8. Legal and trust checks
9. SEO-visible checks
10. Accessibility basics
11. Performance basics
12. Findings by severity
13. Final delivery checklist
14. Next action

### Deep mode

Use when the user asks for a complete professional QA plan.

Output:

1. Executive QA summary
2. Scope and limitations
3. Checked / Needs manual test / Missing / Not verifiable
4. Page inventory
5. Critical user journeys
6. Navigation and link audit
7. CTA and conversion flow audit
8. Form and contact flow audit
9. Responsive testing matrix
10. Cross-browser testing matrix
11. Visual regression notes
12. Accessibility basics
13. Performance basics
14. SEO-visible basics
15. Legal and trust links
16. External scripts and embeds
17. Error and fallback states
18. Findings table
19. Fix order
20. Client handoff checklist
21. Regression checklist
22. Next workflow handoff

## Core test areas

When relevant, check:

- navigation links
- anchor links
- CTA buttons
- WhatsApp links
- phone links
- email links
- forms and success/error states
- maps and external embeds
- social links
- legal page links
- cookie banner behavior if present
- 404 page
- sitemap and robots presence
- title and meta visible basics
- H1 and heading hierarchy basics
- image loading and alt text basics
- lazy loading
- responsive layout
- mobile menu
- sticky CTA behavior
- keyboard navigation basics
- focus states
- contrast basics
- browser console errors
- broken assets
- performance basics
- deployment path issues

## Critical user path rule

Always test or define the main user path first.

For a local business website, this is often:

1. User lands on homepage.
2. User understands the service and location.
3. User taps WhatsApp, phone, form or map.
4. User receives a working contact path.

If this path is broken, mark it as `Blocker` or `High` depending on severity.

## Responsive baseline

Check at least:

- mobile small width
- mobile large width
- tablet width
- desktop width

For each, verify:

- hero readability
- CTA visibility
- navigation usability
- no horizontal overflow
- images scale correctly
- text is readable
- sections do not overlap
- legal/footer links remain usable

## Browser and deployment notes

A file-level review is not enough to confirm final readiness.

Mark these as requiring manual or deployed testing when not available:

- real deployed URL
- server redirects
- headers
- form endpoints
- WhatsApp behavior on phone
- map behavior
- third-party scripts
- browser console errors
- mobile device behavior
- performance metrics

## Output contract

When delivering a QA report, use this format unless the user asks for something different:

```md
# Web Testing Checklist

## 1. QA summary

## 2. Scope and limitations

## 3. Checked

## 4. Needs manual test

## 5. Missing / To confirm

## 6. Not verifiable here

## 7. Critical user paths

## 8. Links and navigation checks

## 9. CTA and contact checks

## 10. Responsive checklist

## 11. Forms and data-flow checks

## 12. Legal and trust checks

## 13. SEO-visible checks

## 14. Accessibility basics

## 15. Performance basics

## 16. Findings by severity

| Severity | Area | Finding | Impact | Recommended fix | Verification |
|---|---|---|---|---|---|

## 17. Final delivery checklist

## 18. Next action
```

## Quality gates

Before saying a website is ready for client review, check:

- Main CTA works or is marked as needing manual test.
- Navigation works or is marked as needing manual test.
- Mobile layout is checked or marked as pending.
- Legal links are present or marked as missing.
- Contact paths are checked or marked as pending.
- Forms are checked or marked as pending.
- Broken links and assets are considered.
- Console errors are checked or marked as pending.
- SEO-visible basics are reviewed.
- Accessibility basics are reviewed.
- Performance basics are reviewed.
- Remaining risks are listed.

Never say "ready" without listing the review scope and remaining manual checks.

## Token policy

Use context carefully.

- Do not audit every file when the user asks for a final checklist only.
- Prioritize pages and files affecting user flow.
- Do not paste entire files unless necessary.
- Summarize repeated issues.
- Use tables for findings when useful.
- Ask for live URL only when deployed behavior matters.
- If the project is large, recommend staged QA.

## Recommended file priority

For static sites, inspect in this order when available:

1. `README.md`
2. `index.html`
3. main HTML pages
4. main JavaScript files
5. main CSS files
6. legal pages
7. `404.html`
8. `robots.txt`
9. `sitemap.xml`
10. deployment config files

## Handoff to other skills

This skill may recommend:

- `web-project-architect` for scope and delivery planning
- `web-premium-design` for visual or UX improvements
- `security-web-audit` for security and privacy risks
- `seo-local-audit` for SEO-specific review
- `fact-checker-web` for claims and external facts
- `token-budget-controller` for large projects

Do not assume those skills are installed. Mention them as recommended workflows, not hard dependencies.

## Final rule

Testing is not a feeling. A website is ready only when the critical user paths, responsive behavior, contact flows, legal links, visible SEO basics, accessibility basics, performance basics and remaining risks are clearly checked or marked as pending.
