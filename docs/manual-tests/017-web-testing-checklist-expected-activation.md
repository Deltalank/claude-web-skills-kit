# Test 017 — web-testing-checklist expected activation

Skill: `web-testing-checklist`
Date: 2026-06-21
Tester: Deltalank
Claude surface: Claude Web
Result: `PASS`

## Purpose

This test verifies that `web-testing-checklist` activates for a pre-delivery website QA request and stays focused on practical web testing rather than switching into visual design, deep security review or advanced local SEO.

The request intentionally provides no files and no deployed URL. The expected behavior is therefore not to claim that anything works, but to produce a professional QA preparation checklist with clear evidence boundaries.

## Prompt

```text
Hola Claude, tengo añadida la habilidad “web-testing-checklist”.

Quiero validar una web estática antes de enseñársela a un cliente. Todavía no quiero diseño nuevo, ni auditoría profunda de seguridad, ni SEO local avanzado. Quiero un checklist profesional de testing y QA previo a entrega.

Contexto:
- Es una web estática de negocio local.
- Puede tener página principal, páginas legales, botones CTA, enlaces internos, WhatsApp, teléfono, email, mapa, sitemap, robots y página 404.
- Todavía no tengo una URL publicada ni resultados reales de navegador.
- No quiero que inventes que algo funciona si no lo has probado.

Dame una revisión profesional de preparación QA cubriendo:
- alcance de pruebas;
- qué se puede revisar con archivos;
- qué requiere prueba manual en navegador;
- qué requiere URL desplegada;
- rutas críticas de usuario;
- navegación y enlaces;
- CTAs y contacto;
- responsive móvil/tablet/escritorio;
- formularios si existen;
- páginas legales;
- SEO visible básico;
- accesibilidad básica;
- rendimiento básico;
- errores de consola;
- checklist final antes de enseñar al cliente.

No escribas código. No digas que la web está lista si faltan pruebas manuales.
```

## Expected behavior

The skill should activate as `web-testing-checklist`.

Expected behavior:

- Respond as a website QA/testing checklist workflow.
- Avoid switching into new visual design work.
- Avoid switching into deep security audit mode.
- Avoid switching into advanced local SEO strategy.
- Avoid inventing that links, buttons, contact methods, responsive behavior, forms, map embeds or WhatsApp links work.
- Separate checked items from items requiring manual testing, missing inputs and items not verifiable in the current environment.
- State that without files there is no real static review.
- State that without a deployed URL there is no real browser/server validation.
- Include critical user paths.
- Include navigation, links, CTAs and contact checks.
- Include responsive checks for mobile, tablet and desktop.
- Include forms if they exist.
- Include legal/trust checks.
- Include visible SEO basics.
- Include accessibility basics.
- Include performance basics.
- Include browser-console checks.
- Provide a final delivery checklist and a next action.
- Avoid code.
- Avoid saying the site is ready while manual checks remain pending.

## Observed behavior

Claude activated `web-testing-checklist` behavior and answered as a website QA reviewer.

It framed the response as a pre-delivery QA preparation report for a static local-business website. It explicitly stated that no files or deployed URL had been provided and therefore the response was a testing plan, not a result of completed tests.

It did not claim that anything worked. The `Comprobado` section was deliberately empty because no files, screenshots or deployed URL were available.

It separated the review into evidence categories:

- `Comprobado`
- `Requiere prueba manual`
- `Falta / Por confirmar`
- `No verificable aquí`

It correctly marked browser/device-only behavior as requiring manual testing, including WhatsApp behavior on a real phone, `tel:` links, `mailto:` links, map interaction, mobile-menu behavior, sticky CTA behavior, scroll behavior, language selector behavior if present, responsive behavior, keyboard navigation and browser-console errors.

It correctly marked deployment-dependent behavior as not verifiable without a live URL, including redirects, headers, real server 404 behavior, form endpoints, third-party scripts and real performance metrics.

It covered the required QA areas:

- test scope and limitations,
- critical user path,
- navigation and links,
- CTA and contact flows,
- responsive testing,
- forms and data flow,
- legal and trust checks,
- visible SEO basics,
- accessibility basics,
- performance basics,
- browser-console checks,
- findings by severity,
- final pre-client checklist,
- next action.

It prioritized the main conversion route for a local business: user lands on the homepage, understands service/location and can contact through WhatsApp, phone, email or map. It correctly stated that a broken contact path should block delivery or be treated as a high-severity issue.

It did not write code and did not say the website was ready for client delivery. Instead, it stated that while checklist items remain unverified, the honest status is pending validation rather than ready.

## Issues found

- Minor context note: Claude reused some prior conversation/project context, such as a personal name, possible languages and visual-theme details. This did not affect the result because it did not use those details to claim that any tests had passed. Future clean-room tests should confirm the same behavior without prior project context.

## Required change

No immediate skill change required.

Continue with the remaining minimum tests for `web-testing-checklist`:

- Test 018 — non-activation behavior
- Test 019 — missing-data behavior
- Test 020 — output-contract behavior

`web-testing-checklist` is not minimum pre-packaging complete yet.
