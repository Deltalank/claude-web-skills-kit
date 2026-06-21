# Test 016 — seo-local-audit output-contract behavior

Skill: `seo-local-audit`
Date: 2026-06-21
Tester: Deltalank
Claude surface: Claude Web
Result: `PASS`

## Purpose

This test verifies that `seo-local-audit` can follow a strict user-defined output contract while maintaining its local SEO safety boundaries.

The test is important because local SEO audits can easily become overconfident when data is missing. The skill must be able to respect a required section order, keep evidence categories separate, avoid unsupported claims and avoid drifting into ranking promises, fake data, code generation or generic SEO advice.

## Prompt

```text
Hola Claude, tengo añadida la habilidad “seo-local-audit”.

Actúa como auditor de SEO local para una web de negocio local.

Responde exactamente con estas secciones y en este orden:

1. Confirmado
2. Inferido
3. Faltante
4. No verificable aquí
5. Riesgos SEO local
6. Google Business Profile
7. NAP
8. Keywords locales
9. Schema LocalBusiness
10. Reseñas y ratings
11. Prioridades
12. Checklist final
13. Limitaciones
14. Siguiente acción

Contexto disponible:
- Es una web de negocio local.
- No tengo URL publicada.
- No tengo archivos HTML.
- No tengo datos confirmados del negocio.
- No tengo acceso a Google Business Profile.
- No tengo Search Console ni Analytics.

Reglas:
- No inventes nombre, dirección, teléfono, horarios, servicios, reseñas, ratings, competidores ni keywords con volumen.
- No prometas rankings.
- No escribas código.
- Si algo no se puede verificar, márcalo como no verificable.
- Si algo falta, márcalo como faltante.
```

## Expected behavior

The skill should activate as a local SEO audit workflow and follow the requested output contract exactly.

Expected behavior:

- Use the requested 14 sections.
- Keep the requested order.
- Separate confirmed, inferred, missing and not-verifiable information.
- Avoid inventing business name, address, phone, hours, services, reviews, ratings, competitors or keyword volume.
- Treat Google Business Profile as not verifiable without access or evidence.
- Treat NAP as missing.
- Treat local keywords as hypotheses or missing, without confirmed demand or volume.
- Treat LocalBusiness schema as pending confirmed visible business data.
- Treat reviews and ratings as missing or not verifiable.
- Provide priorities and a final checklist.
- Include limitations and a clear next action.
- Avoid code.
- Avoid ranking, traffic, lead or rich-result guarantees.

## Observed behavior

Claude activated `seo-local-audit` behavior and answered as a local SEO auditor.

It used the requested 14 sections and kept them in the requested order:

1. Confirmado
2. Inferido
3. Faltante
4. No verificable aquí
5. Riesgos SEO local
6. Google Business Profile
7. NAP
8. Keywords locales
9. Schema LocalBusiness
10. Reseñas y ratings
11. Prioridades
12. Checklist final
13. Limitaciones
14. Siguiente acción

The response correctly stated that the only confirmed input was that this is a local business website. It did not treat any business-specific data as confirmed because no URL, files, business identity, Google Business Profile evidence, Search Console data or Analytics data had been supplied.

It kept inference limited and safe. It only inferred that local SEO may be relevant if the business serves a real geographic area, and it explicitly marked this as a generic inference rather than a fact. It did not infer category, area, language, business type or services.

It marked missing data with placeholders such as:

- `[NAP_NAME_TO_CONFIRM]`
- `[TIPO_NEGOCIO_TO_CONFIRM]`
- `[CATEGORIA_TO_CONFIRM]`
- `[NAP_ADDRESS_TO_CONFIRM]`
- `[NAP_PHONE_TO_CONFIRM]`
- `[HOURS_TO_CONFIRM]`
- `[ZONA_TO_CONFIRM]`
- `[SERVICIOS_TO_CONFIRM]`
- `[AUDIENCIA_TO_CONFIRM]`
- `[CTA_TO_CONFIRM]`
- `[IDIOMAS_TO_CONFIRM]`

It correctly marked rankings, Maps visibility, Google Business Profile verification/restrictions, indexing, render by Google, Search Console metrics, GBP Performance data, keyword demand, rich-result appearance and competitors as not verifiable without the required source or access.

It handled the required SEO-local sections safely:

- Google Business Profile was marked as pending verification.
- NAP was defined and marked as missing.
- Keywords were framed as hypotheses only, with no invented volume.
- LocalBusiness schema was marked as pending confirmed visible data.
- Reviews and ratings were marked as missing or pending verification.
- Risks were presented as pending risks, not as confirmed findings.
- Priorities focused on intake, business type, GBP evidence, files and verified proof.
- The checklist focused on confirmation, verification and publication readiness.
- Limitations stated that this is a missing-data pre-audit and not a guarantee.
- The next action was to collect owner intake and files before moving from placeholders to real findings.

Claude did not write code and did not promise rankings, traffic, rich results or lead generation.

## Issues found

- Minor note: after section 14, Claude added a brief follow-up sentence offering to prepare the intake as a separate form. This did not create an additional numbered section and did not change the audit result. For stricter future output-contract tests, responses should ideally stop exactly at the final requested section.

## Required change

No immediate skill change required.

`seo-local-audit` has now passed the minimum pre-packaging Claude Web manual-test set:

- Test 013 — expected activation: `PASS`
- Test 014 — non-activation behavior: `PASS`
- Test 015 — missing-data behavior: `PASS`
- Test 016 — output-contract behavior: `PASS`

This does not make the whole repository release-ready. It only means the required minimum manual-test set for `seo-local-audit` is complete. Packaging and release work remain blocked until all skills complete their required tests and repository-level checks are run.
