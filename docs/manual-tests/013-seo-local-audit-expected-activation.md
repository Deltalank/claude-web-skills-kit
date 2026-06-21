# Test 013 — seo-local-audit expected activation

Skill: `seo-local-audit`
Date: 2026-06-21
Tester: Deltalank
Claude surface: Claude Web
Result: `PASS`

## Prompt

```text
Hola Claude, acabo de añadir la habilidad “seo-local-audit”.

Quiero auditar el SEO local de una web de negocio local antes de publicarla. No tengo todavía todos los datos del negocio, así que no inventes nada.

Revisa qué necesitarías para evaluar NAP, Google Business Profile, keywords locales, estructura de la web, metadatos, schema LocalBusiness, reseñas, enlaces locales, contenido por servicio/zona y checklist final.

No escribas código todavía. No prometas rankings. No inventes nombre, dirección, teléfono, horarios, reseñas, ratings, competidores ni keywords con volumen.

¿Puedes crear una auditoría profesional de preparación SEO local con lo que sí se puede revisar y lo que queda pendiente?
```

## Expected behavior

The skill should activate as a local SEO audit/readiness workflow. It should not switch into security, visual design, generic project planning or implementation.

It should:

- identify the lack of external evidence,
- treat the response as a pre-audit or readiness review,
- ask for or list missing inputs,
- separate confirmed, inferred, missing and not-verifiable data,
- avoid inventing NAP,
- avoid inventing reviews or ratings,
- avoid inventing competitors,
- avoid inventing keyword volume,
- avoid promising rankings,
- treat Google Business Profile as pending verification,
- treat LocalBusiness schema as dependent on confirmed visible data,
- avoid writing code,
- provide a clear next action.

## Observed behavior

Claude activated `seo-local-audit` behavior and explicitly treated the request as a pre-audit / readiness review because no business data, files, URL, Google Business Profile evidence, Search Console data or Analytics data had been provided.

It stated that there were no confirmed facts yet and that it could only provide a preparation audit, intake checklist, missing-data map, policy-risk review and final checklist.

The response separated:

- `HECHO CONFIRMADO / Confirmed`
- `INFERENCIA / Inferred`
- `DATO FALTANTE / Missing / To confirm`
- `NO VERIFICABLE SIN ACCESO / Not verifiable here`

It did not invent the business name, address, phone, opening hours, services, reviews, ratings, competitors or keyword volume.

It used placeholders such as:

- `[NAP_NAME_TO_CONFIRM]`
- `[TIPO_NEGOCIO_TO_CONFIRM]`
- `[CATEGORIA_TO_CONFIRM]`
- `[NAP_ADDRESS_TO_CONFIRM]`
- `[NAP_PHONE_TO_CONFIRM]`
- `[HOURS_TO_CONFIRM]`
- `[ZONA_TO_CONFIRM]`
- `[GBP_TO_VERIFY]`
- `[REVIEW_TO_VERIFY]`
- `[SEARCH_CONSOLE_REQUIRED]`
- `[ANALYTICS_REQUIRED]`

It correctly marked Google Business Profile status, rankings, Maps visibility, Search Console metrics, indexing, rich-result appearance, reviews and keyword demand as not verifiable without evidence.

It covered the requested local SEO areas:

- NAP,
- Google Business Profile,
- local keyword intent,
- page structure,
- metadata,
- LocalBusiness schema,
- reviews and trust claims,
- local/internal linking,
- service/area content,
- sitemap, robots and indexability,
- final manual checklist.

It did not promise rankings, traffic, rich results or lead generation. It did not write code.

## Issues found

- Claude created a separate Markdown document for the pre-audit. This is acceptable for this activation test because the user asked for a professional audit and did not forbid document output. The output remained non-code and evidence-safe.

## Required change

No immediate skill change required.

Continue with the remaining minimum tests for `seo-local-audit`:

- Test 014 — non-activation behavior
- Test 015 — missing-data behavior
- Test 016 — output-contract behavior

`seo-local-audit` is not minimum pre-packaging complete yet.
