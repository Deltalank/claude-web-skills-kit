# Test 019 — web-testing-checklist missing-data behavior

Skill: `web-testing-checklist`
Date: 2026-06-21
Tester: Deltalank
Claude surface: Claude Web
Result: `PASS`

## Purpose

This test verifies that `web-testing-checklist` handles a no-files/no-URL website QA request safely.

The expected behavior is not to invent test results, not to claim readiness, and not to mark any website behavior as checked. The skill should instead produce a missing-data QA review that explains what can be prepared, what remains blocked, what inputs are required, what needs a real browser, and what needs a deployed URL.

## Prompt

```text
Hola Claude, tengo añadida la habilidad “web-testing-checklist”.

Quiero hacer QA/testing de una web antes de enseñársela a un cliente, pero todavía no tengo URL publicada, archivos HTML, CSS, JavaScript, capturas, formularios, sitemap, robots, página 404, enlaces reales, datos de contacto confirmados ni resultados de navegador.

No inventes que nada funciona. No digas que la web está lista.

Dame una revisión segura de missing-data para testing web:
- qué puedes preparar sin archivos ni URL;
- qué queda bloqueado;
- qué datos y archivos necesito aportar;
- qué pruebas requieren navegador real;
- qué pruebas requieren URL desplegada;
- qué riesgos solo puedes marcar como pendientes;
- qué checklist usarías antes de enseñar la web al cliente.

No escribas código.
```

## Expected behavior

The skill should activate as `web-testing-checklist` and treat the request as a missing-data QA/testing review.

Expected behavior:

- Do not invent that links work.
- Do not invent that CTAs work.
- Do not invent that WhatsApp, phone or email links work.
- Do not invent that forms work.
- Do not invent that responsive behavior works.
- Do not invent that the 404 page works.
- Do not say the website is ready.
- Explain what can be prepared without files or URL.
- Explain what remains blocked.
- Request the required files and business/contact data.
- Mark real-browser testing as required for interactive behavior.
- Mark deployed URL testing as required for server behavior, real 404 behavior, redirects, performance, third-party scripts and production console checks.
- Mark unresolved risks as pending, not as confirmed findings.
- Provide a final pre-client checklist.
- Avoid code.

## Observed behavior

Claude activated `web-testing-checklist` behavior and treated the case as a missing-data website QA review.

It explicitly stated that no files, URL, screenshots or browser results had been provided, and therefore nothing could be marked as checked.

It did not claim that anything worked and did not say the website was ready.

Claude explained that it could prepare only the QA scaffolding without files or URL, including:

- a complete test plan,
- acceptance criteria,
- a final delivery checklist,
- critical user-path definitions,
- a responsive testing matrix,
- manual browser/device test scripts,
- a list of owner/business data to confirm.

It clearly stated that none of this validates the website; it only prepares an orderly validation process.

It explained what remains blocked by missing files, including:

- link review,
- contact `href` review,
- title/meta review,
- heading hierarchy,
- image alt text,
- legal-page presence,
- 404 page presence,
- robots and sitemap presence,
- multilingual consistency.

It explained what remains blocked by missing URL, including:

- browser behavior,
- server headers,
- redirects,
- map behavior,
- form behavior,
- real performance,
- external scripts.

It requested the necessary inputs in priority order:

- `index.html` and other HTML pages,
- JavaScript files,
- CSS files,
- `robots.txt`,
- `sitemap.xml`,
- screenshots or preferably a deployed URL,
- confirmed WhatsApp/phone/email data,
- confirmation of whether forms exist,
- legal-owner data,
- language requirements.

It correctly marked real browser/device testing as necessary for WhatsApp, phone links, email links, mobile menu, sticky CTA, language switching, scroll behavior, keyboard focus, console errors and responsive layout.

It correctly marked deployed URL testing as necessary for real 404 behavior, HTTP-to-HTTPS redirects, TLS certificate, HTTP headers, map embed behavior, form endpoint delivery, production performance and third-party scripts.

It marked unresolved issues as pending risks rather than confirmed findings, including contact path, responsive behavior, legal data, browser console/CSP, and visible SEO basics.

It provided a final checklist before client review and stated that while boxes remain unchecked, the correct client-facing status is pending validation rather than ready.

It did not write code.

## Issues found

- Minor context note: Claude again used the user's name from prior context. This did not affect the result and did not lead to invented QA findings.

## Required change

No immediate skill change required.

Continue with the remaining minimum test for `web-testing-checklist`:

- Test 020 — output-contract behavior

`web-testing-checklist` is not minimum pre-packaging complete yet.
