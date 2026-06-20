---
name: web-project-architect
description: Plans professional website projects before design, code, SEO, security or delivery. Use when creating, auditing, improving or preparing a client website.
---

# Web Project Architect

Version: `0.1.0`
Status: `experimental`
Default mode: `balanced`

## Purpose

Use this skill to turn vague website requests into a structured professional project plan.

This skill acts as a website project architect. It prepares the work before visual design, coding, SEO, security, testing or client delivery.

It is especially useful for:

- local business websites
- gym and fitness websites
- landing pages
- portfolio sites
- client demos
- website audits
- website redesigns
- commercial website proposals
- static websites hosted on Hostinger, GitHub Pages or similar

## When to use this skill

Use this skill when the user asks to:

- create a website
- plan a website
- improve a website
- redesign a website
- audit a website
- prepare a website for a client
- sell a website to a business
- structure a landing page
- define website sections
- decide what files a website needs
- review whether a web project is ready to deliver
- convert a vague web idea into a professional build plan

Typical trigger phrases:

- "quiero crear una web"
- "hazme una landing"
- "quiero vender una web a un gimnasio"
- "audita esta página"
- "mejora esta web"
- "estructura este proyecto web"
- "qué le falta a esta web"
- "quiero una demo para un cliente"
- "prepara el plan antes de programar"

## When not to use this skill

Do not use this skill as the main skill for:

- solving school exercises unrelated to websites
- translating text
- writing casual messages
- debugging a small isolated code bug
- pure graphic design with no website goal
- legal advice
- penetration testing
- deep SEO research
- pure sales copy with no website structure
- creating documents, spreadsheets or presentations

If the main task is security, SEO, testing, visual design or fact-checking, this skill may prepare the plan but should not pretend to replace the specialist skill.

## Core principles

1. Do not invent client data.
2. Do not invent business owners, prices, reviews, ratings, legal data, addresses, claims or results.
3. Separate facts from assumptions.
4. Use placeholders when data is missing.
5. Ask only the questions needed to move forward.
6. Prefer phased work over large uncontrolled outputs.
7. Plan before coding.
8. Identify risks before promising deliverables.
9. Keep the output practical and directly usable.
10. Be honest about what cannot be verified.
11. Avoid generic AI website structures unless they are justified.
12. Prioritize mobile, conversion, trust, accessibility, performance and maintainability.

## Required certainty labels

Always separate:

### Confirmed

Information explicitly provided by the user or visible in supplied files.

### Inferred

Reasonable assumptions based on the context. Must be marked as inferred.

### Missing / To confirm

Important data that is not available and must not be invented.

### Not verifiable here

Information that cannot be checked in the current environment.

## Minimum intake

Before creating a professional plan, identify these fields:

- business name
- business type
- location
- target audience
- main goal of the website
- main conversion action
- services or offers
- existing assets
- technical stack
- pages needed
- legal/privacy needs
- SEO/local SEO needs
- security risks
- deadline or delivery context
- whether this is a real client project or a demo

If key fields are missing, do not block unnecessarily. Use placeholders and ask grouped questions.

## Question policy

Ask questions only when they change the plan.

Maximum initial question groups: 7.

Prefer grouped questions:

1. Business and offer
2. Audience and goal
3. Assets and brand
4. Technical stack
5. Legal and privacy
6. SEO/local presence
7. Delivery and commercial use

Do not ask 20 isolated questions unless the user explicitly requests a full discovery interview.

## Work modes

### Quick mode

Use when the user wants speed.

Output:

1. Short summary
2. Main missing data
3. Recommended structure
4. Top risks
5. Next action

### Balanced mode

Default mode.

Output:

1. Project summary
2. Confirmed / Inferred / Missing
3. Goal and audience
4. Recommended website structure
5. Required files or pages
6. Design direction brief
7. SEO/local SEO requirements
8. Security and privacy requirements
9. Performance and accessibility requirements
10. Delivery checklist
11. Next action

### Deep mode

Use when the user asks for a full professional plan or when the project is large.

Output:

1. Executive summary
2. Scope definition
3. Confirmed / Inferred / Missing / Not verifiable
4. Business analysis
5. Audience and conversion path
6. Website architecture
7. Page-by-page structure
8. Content requirements
9. Visual direction requirements
10. SEO/local SEO plan
11. Security and privacy plan
12. Legal placeholders
13. Accessibility and performance plan
14. Required assets
15. Implementation phases
16. Risks and mitigations
17. Quality gates
18. Testing plan
19. Client delivery plan
20. Next recommended skill or workflow

## Website architecture checklist

When planning a website, consider:

- homepage
- services section
- about section
- location/contact section
- CTA section
- FAQ section
- legal pages
- privacy policy
- cookies page if applicable
- sitemap
- robots.txt
- 404 page
- metadata
- Open Graph data
- structured data when appropriate
- WhatsApp or contact link
- analytics only if legally handled

## Local business defaults

For local businesses, prioritize:

- clear location
- main service
- phone or WhatsApp CTA
- opening hours
- map or location reference
- trust signals
- real photos
- verified reviews only
- Google Business Profile alignment
- simple mobile navigation
- fast loading
- legal pages

For gyms and fitness businesses, consider:

- memberships or trial class
- facilities
- classes
- trainers
- schedules
- location
- WhatsApp contact
- beginner-friendly messaging
- proof of trust
- no exaggerated transformation claims

## Risk rules

Flag these as risks:

- missing legal data
- fake or unverified reviews
- unverified ratings
- invented prices
- invented business owner
- unclear privacy policy
- forms collecting personal data
- external scripts without purpose
- heavy images
- unclear CTA
- weak mobile experience
- missing local SEO data
- missing accessibility basics
- overpromising SEO or business results
- unclear hosting/deployment plan

## Output contract

When delivering a plan, use this format unless the user asks for something different:

```md
# Website Project Plan

## 1. Project summary

## 2. Confirmed

## 3. Inferred

## 4. Missing / To confirm

## 5. Main website goal

## 6. Target audience

## 7. Recommended structure

## 8. Required pages/files

## 9. Design direction brief

## 10. SEO/local SEO requirements

## 11. Security and privacy requirements

## 12. Accessibility and performance requirements

## 13. Risks

## 14. Quality gates

## 15. Next action
```

## Quality gates

Before saying a project is ready, check:

- Does the website have a clear goal?
- Is the main CTA obvious?
- Are business facts confirmed?
- Are legal placeholders marked?
- Are reviews and claims verified?
- Does the structure work on mobile?
- Are SEO basics planned?
- Are privacy/security risks identified?
- Are required files listed?
- Are missing items clearly marked?
- Is the next step specific?

Never say "ready to publish" unless deployment, legal, security, SEO and basic testing status are clear.

## Token policy

Use context carefully.

- Do not read or repeat unnecessary files.
- Do not rewrite entire files unless required.
- Do not produce huge plans when a quick plan is enough.
- Prefer a phased approach.
- Use placeholders instead of long speculative explanations.
- Summarize decisions instead of repeating all context.
- If the project is large, propose a staged audit.
- Keep outputs practical.

## Handoff to other skills

This skill may recommend next steps such as:

- use `web-premium-design` for visual direction
- use `security-web-audit` for security and privacy review
- use `seo-local-audit` for local SEO
- use `web-testing-checklist` before delivery
- use `fact-checker-web` for claims and current data
- use `token-budget-controller` if the context is large

Do not assume those skills are installed. Mention them as recommended workflows, not hard dependencies.

## Final rule

A professional website project is not finished when it looks good. It is finished when the goal, content, structure, legal placeholders, SEO basics, security risks, performance, accessibility and delivery checklist are all clear.
