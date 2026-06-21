# Test 014 — seo-local-audit non-activation

Skill: `seo-local-audit`
Date: 2026-06-21
Tester: Deltalank
Claude surface: Claude Web
Result: `PASS`

## Prompt

```text
Hola Claude, tengo añadida la habilidad “seo-local-audit”, pero ahora NO quiero SEO local.

Quiero que revises la seguridad de una web estática antes de publicarla. Revisa CSP, HSTS, cabeceras de seguridad, secretos expuestos, formularios, cookies, scripts de terceros, dependencias y configuración del servidor.

No quiero auditoría SEO, no quiero NAP, no quiero Google Business Profile, no quiero keywords, no quiero schema LocalBusiness y no quiero recomendaciones de posicionamiento.

No escribas código todavía. Dame solo una revisión profesional de seguridad y qué archivos necesitarías para auditarla bien.
```

## Expected behavior

The `seo-local-audit` skill should not activate.

Claude should treat the request as a static-web security audit, not as a local SEO audit.

It should:

- avoid local SEO recommendations,
- avoid NAP review,
- avoid Google Business Profile review,
- avoid local keyword review,
- avoid LocalBusiness schema review,
- avoid ranking or positioning recommendations,
- cover CSP,
- cover HSTS,
- cover security headers,
- cover exposed secrets,
- cover forms,
- cover cookies,
- cover third-party scripts,
- cover dependencies,
- cover server configuration,
- ask for the security-relevant files and live response headers.

## Observed behavior

Claude explicitly stated that this was not an SEO task and that `seo-local-audit` did not apply.

It responded as a pure static-web security pre-audit because no files, URL or headers had been provided.

The response covered:

- CSP,
- HSTS,
- security headers,
- exposed secrets,
- forms,
- cookies,
- third-party scripts,
- dependencies,
- server configuration,
- live HTTP response headers,
- `curl -sI` / DevTools response headers,
- project files needed for a real audit.

It did not perform a local SEO audit and did not review:

- NAP,
- Google Business Profile,
- local keywords,
- LocalBusiness schema,
- rankings,
- positioning recommendations.

It did not write configuration snippets or code. It kept the result as a professional security pre-audit and listed the evidence needed to turn it into concrete findings.

## Issues found

- Claude mentioned `robots.txt` as a file that could be relevant in the security context. This is acceptable because the mention was about public configuration/file exposure and not SEO.
- Claude mentioned `curl -sI` as a way to provide live headers. This is acceptable because it was a verification input, not implementation code.

## Required change

No immediate skill change required.

Continue with the remaining minimum tests for `seo-local-audit`:

- Test 015 — missing-data behavior
- Test 016 — output-contract behavior

`seo-local-audit` is not minimum pre-packaging complete yet.
