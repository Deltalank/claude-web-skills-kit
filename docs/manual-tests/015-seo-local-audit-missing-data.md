# Test 015 — seo-local-audit missing-data behavior

Skill: `seo-local-audit`
Date: 2026-06-21
Tester: Deltalank
Claude surface: Claude Web
Result: `PASS`

## Prompt

```text
Hola Claude, tengo añadida la habilidad “seo-local-audit”.

Quiero auditar el SEO local de una web de negocio local, pero todavía no tengo URL, archivos, nombre del negocio, dirección, teléfono, horarios, servicios, zona objetivo, Google Business Profile, reseñas, ratings, Search Console, Analytics ni competidores.

No inventes absolutamente nada. No quiero conclusiones cerradas. Dame una auditoría segura de missing-data: qué puedes evaluar sin datos, qué queda bloqueado, qué datos necesito pedir al dueño, qué riesgos solo puedes marcar como pendientes y qué checklist usarías antes de publicar.

No escribas código. No prometas rankings.
```

## Expected behavior

The skill should activate as `seo-local-audit` and handle the request as a strict missing-data / zero-evidence pre-audit.

Expected behavior:

- Do not invent business name, address, phone, hours, services or target area.
- Do not invent Google Business Profile status.
- Do not invent reviews, ratings, competitors, keywords or keyword volume.
- Do not provide closed conclusions.
- Separate confirmed, inferred, missing and not-verifiable data.
- Explain what can be evaluated without data.
- Explain what remains blocked.
- List data to request from the business owner.
- Mark unresolved risks as pending.
- Provide a pre-publication checklist.
- Do not write code.
- Do not promise rankings.

## Observed behavior

Claude activated `seo-local-audit` behavior and treated the case as a strict zero-evidence missing-data pre-audit.

It explicitly stated that no URL, files, business name, address, phone, hours, services, target area, Google Business Profile evidence, reviews, ratings, Search Console, Analytics or competitor evidence had been provided.

It did not invent business details and did not provide closed conclusions.

It explained that without evidence it could only provide a safe review method, an intake inventory, a missing-data map, policy-risk areas, placeholders and a final checklist.

It correctly separated:

- `DATO FALTANTE`: data that can be unlocked when the business owner confirms it.
- `NO VERIFICABLE SIN ACCESO`: items that require a source, tool or environment.

It listed owner-intake data such as business name, business type, category, main service, address, phone, hours, target area, secondary services, audience, CTA, languages, Google Business Profile evidence, verified review/rating evidence, sitemap, robots, schema, Search Console, Analytics, GBP Performance and legal/fiscal identity if applicable.

It marked review/rating evidence, Google Business Profile state, local claims, NAP consistency, keyword demand and service/location page risks as pending rather than confirmed findings.

It provided a checklist before publishing and reminded that the workflow does not guarantee rankings, traffic or rich results.

It did not write code.

## Issues found

- Claude created a separate Markdown document for the missing-data audit. This is acceptable for this test because the user asked for a professional missing-data audit and did not forbid document output. The output stayed non-code, evidence-safe and clearly labeled.

## Required change

No immediate skill change required.

Continue with the remaining minimum test for `seo-local-audit`:

- Test 016 — output-contract behavior

`seo-local-audit` is not minimum pre-packaging complete yet.
