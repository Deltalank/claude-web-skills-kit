# Security Baseline

Use this baseline for static websites and simple client websites.

## Check first

- No secrets in repository files.
- No private client data in public files.
- No `.env`, backup, zip or database dump files exposed.
- No fake legal, SEO or security guarantees.
- No unnecessary third-party scripts.
- Forms are understood and documented.
- Cookies and analytics are disclosed.
- External links opening new tabs use safe attributes.
- Security headers are planned and verified after deployment.
- CSP matches actual resources.

## Static website risks

Static websites can still leak data or create risk through:

- exposed keys in JavaScript
- tracking scripts
- third-party embeds
- unsafe external links
- form endpoints
- missing privacy notices
- overly broad CSP
- public backup files
- unverified claims
