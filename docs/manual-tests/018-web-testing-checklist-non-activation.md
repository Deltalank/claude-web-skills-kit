# Test 018 — web-testing-checklist non-activation behavior

Skill: `web-testing-checklist`
Date: 2026-06-21
Tester: Deltalank
Claude surface: Claude Web
Result: `PASS`

## Purpose

This test verifies that `web-testing-checklist` does not activate when the user explicitly asks for a deep security audit instead of website QA/testing.

The skill definition states that `web-testing-checklist` should not be used as the main workflow for deep security review. In this case, the expected behavior is to respect the user's negative instruction, avoid QA-delivery framing, and answer as a security-audit workflow instead.

## Prompt

```text
Hola Claude, tengo añadida la habilidad “web-testing-checklist”, pero ahora NO quiero testing ni QA.

Quiero una auditoría profunda de seguridad para una web estática antes de publicarla. Revisa riesgos de CSP, HSTS, cabeceras de seguridad, exposición de secretos, JavaScript de terceros, formularios, cookies, privacidad, dependencias y configuración del servidor.

No quiero checklist de entrega al cliente, no quiero responsive testing, no quiero validar botones, no quiero revisar CTAs, no quiero QA funcional y no quiero rutas críticas de usuario.

No escribas código todavía. Dame solo una revisión profesional de seguridad y qué archivos necesitarías para auditarla bien.
```

## Expected behavior

The `web-testing-checklist` skill should not activate as the main workflow.

Expected behavior:

- Do not produce a client-delivery QA checklist.
- Do not focus on responsive testing.
- Do not focus on validating buttons, CTAs or contact paths as QA items.
- Do not focus on critical user journeys.
- Do not claim to be using `web-testing-checklist` for the security audit.
- Respond as a web security audit.
- Cover CSP, HSTS, security headers, secret exposure, third-party JavaScript, forms, cookies, privacy, dependencies and server configuration.
- Ask for or list files needed for a proper security audit.
- Avoid code.
- Avoid claiming that anything is secure or vulnerable without files or a deployed URL.

## Observed behavior

Claude did not apply `web-testing-checklist` as the main workflow.

It explicitly recognized that `web-testing-checklist` is a functional pre-delivery QA skill and should not be used as the main tool for a deep security audit. It stated that it would not apply a testing checklist and would proceed with security-audit reasoning instead.

Claude answered as a security reviewer and covered the requested security areas:

- Content Security Policy,
- HSTS,
- general security headers,
- exposed secrets in public client-side code,
- third-party JavaScript and dependencies,
- forms and endpoints,
- cookies and browser storage,
- privacy / RGPD considerations,
- server and hosting configuration.

It explained that static websites remove some backend risks but are not automatically secure. It framed the relevant risks around headers, third-party scripts, public source code, hosting configuration and privacy.

It did not produce a client handoff QA checklist. It did not focus on responsive testing, visual layout, CTA validation, navigation testing or critical user paths.

It did not write code.

It correctly stated that without files or a deployed URL it could not confirm specific vulnerabilities or security status. It listed the files and evidence needed for a real audit, including JavaScript files, HTML files, `.htaccess` or server configuration, deployment/config files, `robots.txt`, `sitemap.xml`, CSS, project file listing and a deployed URL for production headers, TLS, redirects and third-party requests.

## Issues found

- Minor context note: Claude reused some prior project context, such as Spain/Canarias, Hostinger/shared hosting, map embeds, Google fonts and strict CSP. This did not affect the result because it treated the security status as unverified and did not claim tested outcomes.

## Required change

No immediate skill change required.

Continue with the remaining minimum tests for `web-testing-checklist`:

- Test 019 — missing-data behavior
- Test 020 — output-contract behavior

`web-testing-checklist` is not minimum pre-packaging complete yet.
