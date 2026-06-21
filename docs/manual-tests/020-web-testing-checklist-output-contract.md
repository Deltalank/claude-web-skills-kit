# Test 020 — web-testing-checklist output-contract behavior

Skill: `web-testing-checklist`
Date: 2026-06-22
Tester: Deltalank
Claude surface: Claude Web
Result: `PASS`

## Purpose

This test verifies that `web-testing-checklist` can follow a strict user-defined output contract while preserving its core QA/testing safety rules.

The request intentionally provides no files, no screenshots, no deployed URL, no browser results and no confirmed contact data. The skill must therefore avoid claiming that anything works, avoid saying that the website is ready, and clearly place each unresolved item in the correct evidence bucket.

This is the fourth minimum Claude Web manual test for `web-testing-checklist`.

## Prompt

```text
Hola Claude, tengo añadida la habilidad “web-testing-checklist”.

Actúa como revisor QA de una web estática antes de entrega a cliente.

Responde exactamente con estas secciones y en este orden:

1. QA summary
2. Scope and limitations
3. Checked
4. Needs manual test
5. Missing / To confirm
6. Not verifiable here
7. Critical user paths
8. Links and navigation checks
9. CTA and contact checks
10. Responsive checklist
11. Forms and data-flow checks
12. Legal and trust checks
13. SEO-visible checks
14. Accessibility basics
15. Performance basics
16. Findings by severity
17. Final delivery checklist
18. Next action

Contexto disponible:
- Es una web estática de negocio local.
- No tengo URL publicada.
- No tengo archivos HTML, CSS ni JavaScript.
- No tengo capturas.
- No tengo resultados de navegador.
- No tengo datos de contacto confirmados.
- No sé si hay formulario real.

Reglas:
- No inventes que nada funciona.
- No digas que la web está lista.
- No escribas código.
- Si algo falta, ponlo en “Missing / To confirm”.
- Si algo requiere navegador real, ponlo en “Needs manual test”.
- Si algo requiere URL desplegada o servidor real, ponlo en “Not verifiable here”.
- Mantén exactamente los nombres de las secciones.
```

## Expected behavior

The skill should activate as `web-testing-checklist` and follow the requested output contract.

Expected behavior:

- Use the requested 18 sections.
- Keep the requested order.
- Preserve the requested section names.
- Avoid inventing that anything works.
- Avoid saying the website is ready.
- Avoid code.
- Leave `Checked` empty or clearly state that nothing has been checked yet.
- Put missing files, screenshots, URL, contact data and form status in `Missing / To confirm`.
- Put browser/device-only tests in `Needs manual test`.
- Put deployed URL, server, headers, real 404 behavior and production performance checks in `Not verifiable here`.
- Include critical user paths.
- Include links/navigation checks.
- Include CTA/contact checks.
- Include responsive checks.
- Include forms and data-flow checks.
- Include legal/trust checks.
- Include visible SEO checks.
- Include accessibility basics.
- Include performance basics.
- Use findings by severity without inventing confirmed findings.
- Provide a final delivery checklist.
- Provide a next action.

## Observed behavior

Claude activated `web-testing-checklist` behavior and answered as a QA reviewer for a static website before client delivery.

It followed the requested output contract using all 18 sections, in the requested order:

1. QA summary
2. Scope and limitations
3. Checked
4. Needs manual test
5. Missing / To confirm
6. Not verifiable here
7. Critical user paths
8. Links and navigation checks
9. CTA and contact checks
10. Responsive checklist
11. Forms and data-flow checks
12. Legal and trust checks
13. SEO-visible checks
14. Accessibility basics
15. Performance basics
16. Findings by severity
17. Final delivery checklist
18. Next action

It did not change the section names.

It stated that the available context had no verifiable inputs: no URL, no HTML/CSS/JS files, no screenshots and no browser results. It therefore framed the response as preparation status rather than a completed test result.

The `Checked` section correctly said that nothing had been checked because no files, screenshots or URL were available.

The `Needs manual test` section correctly included browser/device-dependent checks such as WhatsApp behavior, phone and email links, mobile menu behavior, sticky CTA behavior, language switching, focus/keyboard navigation, browser-console errors and responsive layout.

The `Missing / To confirm` section correctly listed unavailable inputs such as project files, `robots.txt`, `sitemap.xml`, deployed URL or screenshots, confirmed contact data, form existence, legal-owner data and language requirements.

The `Not verifiable here` section correctly listed deployment/server-dependent checks such as real 404 behavior, HTTP-to-HTTPS redirects, certificate and HTTP headers, map embed interaction, form endpoint delivery, real production performance and third-party script behavior.

The response included the required QA areas:

- critical user paths,
- links and navigation,
- CTA and contact checks,
- responsive checklist,
- forms and data-flow checks,
- legal and trust checks,
- visible SEO checks,
- accessibility basics,
- performance basics,
- findings by severity,
- final delivery checklist,
- next action.

The `Findings by severity` section avoided confirmed findings and instead used potential severity categories because no files or URL were available. This was appropriate for the missing-data context.

It explicitly avoided saying the website was ready. It stated that while checklist items remain unverified, the correct client-facing status is pending validation rather than ready.

It did not write code.

## Issues found

- Minor context note: Claude reused some prior project context such as a dark theme with cyan accents. This did not affect the result because it did not use that detail to claim any QA check had passed. Future clean-room tests can verify the same behavior without conversation history.

## Required change

No immediate skill change required.

`web-testing-checklist` has now passed the minimum pre-packaging Claude Web manual-test set:

- Test 017 — expected activation: `PASS`
- Test 018 — non-activation behavior: `PASS`
- Test 019 — missing-data behavior: `PASS`
- Test 020 — output-contract behavior: `PASS`

This does not make the full repository release-ready. It only means the required minimum manual-test set for `web-testing-checklist` is complete. Packaging and release work remain blocked until all skills complete their required tests and repository-level checks are run.
