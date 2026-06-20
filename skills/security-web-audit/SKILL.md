---
name: security-web-audit
description: Reviews static websites and simple web projects for security, privacy and configuration risks before publishing or client delivery.
---

# Security Web Audit

Version: `0.1.0`
Status: `experimental`
Default mode: `balanced`

## Purpose

Use this skill to review websites and simple web projects for security, privacy and configuration risks before publishing, delivering to a client or asking another AI to modify the project.

This skill is especially useful for:

- static websites
- HTML/CSS/JavaScript projects
- local business websites
- gym and fitness websites
- client demos
- Hostinger or shared-hosting deployments
- GitHub Pages deployments
- `.htaccess` review
- CSP and security header review
- privacy and cookies review
- external scripts and CDN review
- forms and contact flows
- pre-delivery safety checks

## When to use this skill

Use this skill when the user asks to:

- review website security
- audit a web project before publishing
- check privacy risks
- check `.htaccess`
- check CSP or security headers
- review scripts, CDNs or external resources
- check forms that collect personal data
- review cookies, localStorage or analytics
- find exposed keys, tokens or secrets
- verify whether a static website is safe enough to deliver
- identify risks before selling or uploading a website

Typical trigger phrases:

- "revisa la seguridad de esta web"
- "audita este .htaccess"
- "comprueba si hay riesgos"
- "antes de publicarla dime si es segura"
- "revisa cookies y privacidad"
- "mira si hay API keys expuestas"
- "comprueba CSP"
- "qué riesgos tiene esta landing"
- "quiero entregar esta web a un cliente"

## When not to use this skill

Do not use this skill as the main skill for:

- penetration testing
- exploitation
- bypassing security systems
- malware analysis or creation
- attacking third-party websites
- deep backend security review without code and permission
- legal compliance certification
- pure visual design
- pure SEO strategy
- isolated styling issues
- school exercises unrelated to web security

This skill is a review and risk-identification workflow. It is not a guarantee that the website is secure, legally compliant or ready for production.

## Core principles

1. Do not claim a website is secure with certainty.
2. Separate verified findings from assumptions.
3. Do not invent vulnerabilities.
4. Do not ignore serious risks because the website is static.
5. Do not expose secrets in the response.
6. Redact sensitive data when discussing it.
7. Prefer practical, low-risk fixes.
8. Explain impact and recommended correction for each finding.
9. Distinguish real risk, hardening improvement, false-positive possibility and pending verification.
10. Do not recommend headers or CSP rules that are likely to break the site without warning.
11. Mark legal/privacy questions as requiring human/legal review when appropriate.
12. Keep outputs useful for a web developer or client handoff.

## Required certainty labels

Always separate:

### Confirmed

Information visible in provided files, screenshots, logs or user context.

### Inferred

Reasonable assumptions based on the project type. Must be marked as inferred.

### Missing / To confirm

Important files, settings or facts that are unavailable.

### Not verifiable here

Security, hosting, legal or runtime behavior that cannot be checked in the current environment.

## Severity labels

Use these labels for findings:

### Critical

A high-impact issue that may expose secrets, personal data, admin access or dangerous functionality.

### High

A serious issue that should be fixed before publishing or delivery.

### Medium

A meaningful weakness or misconfiguration that should be fixed soon.

### Low

A minor hardening or hygiene improvement.

### Informational

Useful context or best-practice note.

## Finding types

Classify each issue as one of:

- `real risk`
- `hardening improvement`
- `privacy risk`
- `configuration risk`
- `claim requires verification`
- `pending verification`
- `possible false positive`

## Minimum audit intake

Before producing a full audit, identify available context:

- website type
- hosting target
- whether there is backend code
- whether forms collect personal data
- whether cookies or analytics are used
- whether external scripts/CDNs are used
- whether `.htaccess` or server config exists
- whether legal pages exist
- whether secrets or environment files exist
- whether deployment is public or local only

If files are missing, provide a scoped audit and clearly list what cannot be verified.

## Work modes

### Quick mode

Use when the user wants a fast risk check.

Output:

1. Security summary
2. Top risks
3. Fast fixes
4. Missing files to review
5. Next action

### Balanced mode

Default mode.

Output:

1. Audit summary
2. Confirmed / Inferred / Missing / Not verifiable
3. Findings by severity
4. Privacy and cookies review
5. Headers and hosting review
6. External scripts and dependencies review
7. Forms and data collection review
8. SEO/legal-adjacent risks when relevant
9. Recommended fixes
10. What must be checked manually
11. Next action

### Deep mode

Use when the user asks for a full professional audit.

Output:

1. Executive summary
2. Scope and limitations
3. Confirmed / Inferred / Missing / Not verifiable
4. Asset and file inventory
5. Secrets and sensitive data review
6. HTML security review
7. JavaScript security review
8. External scripts and CDN review
9. Form and data collection review
10. Cookies, analytics and consent review
11. Server and `.htaccess` review
12. Security headers review
13. CSP review
14. Privacy and legal placeholders
15. Hosting and deployment risks
16. Findings table
17. Fix plan by priority
18. Verification checklist
19. Residual risks
20. Handoff notes

## Security areas to review

When relevant, check:

- exposed API keys, tokens or credentials
- `.env` or secret files
- public backup files
- source maps or debug files
- forms collecting personal data
- insecure form targets
- third-party scripts
- analytics and tracking pixels
- cookies and localStorage/sessionStorage
- `target="_blank"` without `rel="noopener noreferrer"`
- inline scripts that affect CSP
- mixed content
- insecure external links
- dependency or CDN risk
- missing security headers
- CSP that is too loose or too strict
- HSTS deployment readiness
- robots and sitemap exposure issues
- legal pages and privacy notices
- public personal data

## Static website baseline

For static websites, recommend checking:

- no secrets in repository
- no private client data in files
- no fake legal claims
- no unnecessary third-party scripts
- no forms collecting data without privacy flow
- external links use safe attributes when opening new tabs
- security headers are configured where hosting allows
- CSP is appropriate for actual scripts and assets
- legal pages are linked if required
- cookies and analytics are handled transparently
- images do not leak private metadata when relevant

## `.htaccess` and headers guidance

When reviewing `.htaccess`, consider:

- `Content-Security-Policy`
- `Referrer-Policy`
- `X-Content-Type-Options`
- `X-Frame-Options` or `frame-ancestors` through CSP
- `Permissions-Policy`
- `Strict-Transport-Security` only when HTTPS is correctly configured
- caching rules
- compression rules
- blocking access to sensitive file types
- custom error pages

Warn that server header behavior must be verified on the deployed host.

## CSP guidance

When suggesting CSP:

- start from actual resources used by the site
- avoid blindly using `unsafe-inline` unless required and clearly marked
- do not block required fonts, images, maps or scripts without warning
- explain what may break
- recommend testing in report-only mode when appropriate
- mark CSP as pending verification until tested in the browser

## Privacy and cookies guidance

Flag privacy risks when:

- forms collect names, emails, phone numbers or health-related information
- analytics, maps, videos or pixels are embedded
- cookies or localStorage are used
- WhatsApp links include personal or sensitive prefilled data
- legal pages are missing or generic
- real personal data is present without clear purpose

This skill does not provide legal advice. Mark legal compliance as requiring review.

## Output contract

When delivering an audit, use this format unless the user asks for something different:

```md
# Security Web Audit

## 1. Audit summary

## 2. Scope and limitations

## 3. Confirmed

## 4. Inferred

## 5. Missing / To confirm

## 6. Not verifiable here

## 7. Findings by severity

| Severity | Type | Finding | Impact | Recommended fix | Verification |
|---|---|---|---|---|---|

## 8. Privacy and cookies review

## 9. Headers and hosting review

## 10. External scripts and dependencies review

## 11. Forms and data collection review

## 12. Recommended fix order

## 13. Manual checks before delivery

## 14. Next action
```

## Quality gates

Before saying the audit is complete, check:

- Are secrets and private data considered?
- Are external scripts listed or marked as missing?
- Are forms and data flows reviewed?
- Are cookies and tracking handled?
- Are headers and hosting limits discussed?
- Are findings prioritized by severity?
- Are limitations clear?
- Are legal claims avoided?
- Are fixes practical?
- Are verification steps included?

Never say "secure" or "compliant" as a guarantee. Use wording like "no obvious issue found in the reviewed files" or "pending deployment verification".

## Token policy

Use context carefully.

- Do not request every project file if the user asks for a targeted review.
- Inspect the most security-relevant files first.
- Avoid rewriting full files unless necessary.
- Redact secrets instead of repeating them.
- Summarize repeated patterns.
- If the project is large, recommend staged review.
- Keep the audit actionable and prioritized.

## Recommended file priority

For static web projects, inspect in this order when available:

1. `README.md`
2. `index.html`
3. main CSS and JS files
4. `.htaccess`
5. legal pages
6. `robots.txt`
7. `sitemap.xml`
8. forms or contact scripts
9. package/dependency files if present
10. deployment config files

## Handoff to other skills

This skill may recommend:

- `web-project-architect` for scope and delivery planning
- `web-premium-design` for visual improvements
- `seo-local-audit` for SEO-specific review
- `web-testing-checklist` for browser validation
- `fact-checker-web` for claims, laws, tools and current data
- `token-budget-controller` for large projects

Do not assume those skills are installed. Mention them as recommended workflows, not hard dependencies.

## Final rule

A security audit is useful only when it is scoped, honest about limitations, prioritized by risk and followed by verification. Do not overclaim.
