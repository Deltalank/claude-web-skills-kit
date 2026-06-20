# Manual Test Log

Status: active

Use this file to record Claude Web tests before packaging any ZIP files.

## Manual test coverage summary

Last updated: 2026-06-20

| Skill | Test IDs | Expected activation | Non-activation | Missing-data behavior | Output-contract behavior | Overall status | Notes |
|---|---:|---|---|---|---|---|---|
| `web-project-architect` | 001-004 | `PASS` | `PASS` | `PASS` | `PASS` | Minimum pre-packaging set complete | Watch clean-room location assumptions in future tests. |
| `web-premium-design` | 005-008 | `PASS` | `PASS` | `PASS` | `PASS` | Minimum pre-packaging set complete | Activation and non-activation tests reused some existing Max Gym context; clean-room retest remains useful later, but no blocking issue was found. |
| `security-web-audit` | 009 | `PASS` | Not tested | Not tested | Not tested | In progress | Expected activation passed; remaining non-activation, missing-data and output-contract tests pending. |
| `seo-local-audit` | Not started | Not tested | Not tested | Not tested | Not tested | Pending | No Claude Web manual tests recorded yet. |
| `web-testing-checklist` | Not started | Not tested | Not tested | Not tested | Not tested | Pending | No Claude Web manual tests recorded yet. |
| `fact-checker-web` | Not started | Not tested | Not tested | Not tested | Not tested | Pending | No Claude Web manual tests recorded yet. |
| `token-budget-controller` | Not started | Not tested | Not tested | Not tested | Not tested | Pending | No Claude Web manual tests recorded yet. |

Do not mark a skill as ready for ZIP packaging until its four minimum Claude Web manual tests are recorded as passing or any issues are fixed and retested.

## Test result labels

- `PASS`
- `FAIL`
- `PARTIAL`
- `NEEDS DESCRIPTION TUNING`
- `NEEDS OUTPUT CONTRACT TUNING`
- `NEEDS SAFETY TUNING`

## Test template

```md
## Test ID

Skill:
Date:
Tester:
Claude surface:
Prompt:
Expected behavior:
Observed behavior:
Result:
Issues found:
Required change:
```

## Required minimum before packaging

Each skill needs at least:

- one expected activation test
- one non-activation test
- one output contract test
- one missing-data behavior test

## Test records

## Test 001

Skill: `web-project-architect`
Date: 2026-06-20
Tester: Deltalank
Claude surface: Claude Web
Prompt:

```text
Quiero crear una web para un gimnasio local y venderla al dueño. Quiero que me digas cómo estructurar el proyecto antes de diseñar o programar nada.
```

Expected behavior:

The skill should activate and produce a website project plan before design or coding. It should separate confirmed facts, inferred assumptions and missing data. It should avoid inventing business details.

Observed behavior:

Claude activated the skill-oriented behavior and produced a balanced project plan. The response separated confirmed data, inferred assumptions and missing data, identified demo/speculative-sale risk, warned against inventing business data, proposed a one-page local gym structure, listed required files, identified SEO, privacy, accessibility and performance considerations, and ended with a focused intake block.

Result:

`PASS`

Issues found:

- Minor wording note: the response said "He añadido el enfoque de la habilidad", which is acceptable but may sound implementation-facing rather than user-facing.
- The response inferred "Tú estás en Canarias" from user context. This is acceptable for this user test, but the skill should continue marking location assumptions as inferred when not explicitly provided in a new chat.

Required change:

No immediate skill change required. Continue testing with a non-activation prompt and a missing-data prompt before packaging.

## Test 002

Skill: `web-project-architect`
Date: 2026-06-20
Tester: Deltalank
Claude surface: Claude Web
Prompt:

```text
Tradúceme este texto al inglés: quiero entrenar hoy.
```

Expected behavior:

The skill should not activate. Claude should translate the sentence normally and should not produce a website project plan, intake questions, project phases or confirmed/inferred/missing sections.

Observed behavior:

Claude answered only with the translation:

```text
"I want to train today."
```

No website planning behavior appeared.

Result:

`PASS`

Issues found:

None.

Required change:

No change required for this non-activation test.

## Test 003

Skill: `web-project-architect`
Date: 2026-06-20
Tester: Deltalank
Claude surface: Claude Web
Prompt:

```text
Quiero crear una web para un negocio local, pero todavía no tengo nombre, ubicación, fotos, horarios ni precios. Haz el plan sin inventar nada.
```

Expected behavior:

The skill should activate and produce a plan that does not invent missing business information. It should mark missing fields clearly, use placeholders, identify what can still be planned, and explain what is blocked until the user confirms details.

Observed behavior:

Claude activated the project-architect behavior and produced a skeleton plan. It explicitly stated that there were no confirmed details and that it would not invent name, business type, location, photos, opening hours or prices. It separated confirmed data, inferred assumptions and missing content, used placeholders such as `[NOMBRE]`, `[TIPO DE NEGOCIO]`, `[UBICACIÓN]`, `[HORARIOS]`, `[PRECIOS]`, `[FOTOS]`, `[CONTACTO/WHATSAPP]`, `[RESEÑAS verificables]` and `[DATOS LEGALES]`, explained that the business type is the most important missing field, and provided safe next-step intake questions.

Result:

`PASS`

Issues found:

- Minor note: the response inferred Spain/Canarias and RGPD applicability. This is acceptable for this user's context, but in a clean external test this should remain clearly marked as inferred unless the location is confirmed.

Required change:

No immediate change required. Continue with output-contract behavior test before packaging.

## Test 004

Skill: `web-project-architect`
Date: 2026-06-20
Tester: Deltalank
Claude surface: Claude Web
Prompt:

```text
Actúa como arquitecto de proyecto web. Hazme un plan en formato profesional para una web de negocio local, separando Confirmado, Inferido, Falta por confirmar, Riesgos, Fases, Archivos necesarios, Quality gates y Siguiente acción. No escribas código todavía.
```

Expected behavior:

The skill should activate and follow the requested output structure. It should include confirmed facts, inferred assumptions, missing data, risks, phases, required files, quality gates and next action. It should not write HTML, CSS or JavaScript.

Observed behavior:

Claude produced a professional project plan with the requested sections: Confirmado, Inferido, Falta por confirmar, Riesgos, Fases, Archivos necesarios, Quality gates and Siguiente acción. It did not write code. It used placeholders for missing business data, warned against invented content, identified the business type as the main blocking field, and provided a phase table with gates.

Result:

`PASS`

Issues found:

- Minor note: the response again inferred Spain/Canarias and RGPD/LOPDGDD. This remains acceptable for this user context, but future clean-room tests should confirm whether the skill behaves equally well without user-location context.

Required change:

No immediate change required. `web-project-architect` has passed the minimum pre-packaging Claude Web manual tests.

## Test 005

Skill: `web-premium-design`
Date: 2026-06-20
Tester: Deltalank
Claude surface: Claude Web
Prompt:

```text
Hola Claude, acabo de añadir la habilidad “web-premium-design”. Quiero que esta landing parezca premium, menos genérica y más convincente visualmente para un gimnasio local. No quiero código todavía, quiero dirección visual, UX, secciones, estilo y criterios para que no parezca una web hecha rápido con IA.
```

Expected behavior:

The skill should activate and provide premium visual direction, UX guidance, section strategy, anti-generic design criteria and conversion-oriented recommendations. It should not write code and should not turn into a deep security or SEO audit.

Observed behavior:

Claude activated premium-design behavior and produced a visual direction plan for a local gym landing. It focused on making the design feel less generic, identified overuse of dark/cyan visual language as a risk, proposed an editorial dark direction, emphasized real photos and coaches as differentiators, recommended section ordering, CTA hierarchy, typography, spacing, image strategy, trust signals and anti-generic priorities. It did not write HTML, CSS or JavaScript.

Result:

`PASS`

Issues found:

- The response used existing Max Gym context and specific details such as current palette, languages, coaches, schedule and WhatsApp. This is useful in the user's current Claude context, but future clean-room tests should verify the skill does not invent project-specific facts when that context is absent.
- The response briefly mentioned privacy/CSP, but it remained secondary and did not become a security audit.

Required change:

No immediate change required. Continue with a non-activation test for `web-premium-design` before merging this manual test pass.

## Test 006

Skill: `web-premium-design`
Date: 2026-06-20
Tester: Deltalank
Claude surface: Claude Web
Prompt:

```text
Revisa si las cabeceras de seguridad de una web estática están bien configuradas: CSP, HSTS, X-Content-Type-Options, Permissions-Policy y Referrer-Policy.
```

Expected behavior:

The `web-premium-design` skill should not activate. Claude should treat the request as a security-header review, not as a premium design, UX, branding, typography, hero-section or visual-direction task.

Observed behavior:

Claude did not respond as a premium designer. It identified that the current `.htaccess` was not available in the conversation and avoided claiming a line-by-line audit without the file. It then handled the request as a security-header review, covering CSP, HSTS, X-Content-Type-Options, Permissions-Policy and Referrer-Policy. The response also mentioned relevant security nuances such as avoiding `unsafe-inline` where possible, using `object-src 'none'`, `base-uri 'self'`, `frame-ancestors 'none'`, HSTS preload caution, `nosniff`, modern Permissions-Policy syntax, `strict-origin-when-cross-origin`, optional `no-referrer`, and external validation with securityheaders.com or Mozilla Observatory.

Result:

`PASS`

Issues found:

- The test response still reused existing Max Gym/project context, including references to Apache/Hostinger, vanilla stack, strict CSP, self-hosted fonts and map click-to-load. This does not indicate premium-design activation, but it means this was not a fully clean-room context test.
- No visual-design behavior appeared. Claude did not discuss premium aesthetic direction, hero layout, branding, typography hierarchy, color palette decisions, imagery style or landing-page section design.

Required change:

No immediate skill change required for non-activation. Continue with `web-premium-design` missing-data behavior and output-contract behavior tests before considering this skill ready for pre-packaging.

## Test 007

Skill: `web-premium-design`
Date: 2026-06-20
Tester: Deltalank
Claude surface: Claude Web
Prompt:

```text
Quiero mejorar visualmente una landing para que parezca premium, pero todavía no tengo marca, sector, fotos, colores, público objetivo ni contenido real. No inventes datos. Dame una dirección visual segura usando placeholders y dime qué queda bloqueado hasta confirmar información.
```

Expected behavior:

The skill should activate as premium-design guidance while avoiding invented business, brand or audience details. It should use placeholders, explain what can be decided safely without data, list what remains blocked until confirmation, and avoid producing a full implementation or switching into SEO, security or project-architecture mode.

Observed behavior:

Claude activated premium-design behavior and explicitly stated that no brand, sector, photos, colors, audience or copy were confirmed. It avoided inventing concrete project details, used placeholders such as `[PROPUESTA DE VALOR]`, `[BENEFICIO PRINCIPAL]`, `[ACCIÓN]`, `[DESTINO CTA]`, `[SERVICIO 1/2/3]`, `[RAZÓN 1/2/3]`, `[ZONA DE CONFIANZA]`, `[DATOS NEGOCIO]`, `[LEGAL]` and `[CONTACTO]`, and clearly listed what remained blocked until confirmation. It proposed a safe neutral premium direction based on white space, typographic hierarchy, a restrained palette, real grid alignment, a single CTA, placeholder image ratios and honest proof/social-trust handling. It did not invent testimonials, ratings, sector-specific claims, brand colors or final fonts.

Result:

`PASS`

Issues found:

- Claude included a small CSS token snippet for placeholder variables. This does not count as a full implementation and did not violate the test objective, but future output-contract tests should verify that the skill respects a strict "no code" instruction when requested.
- Claude inferred that the project may be a local business based on user context, but explicitly marked it as a supposition and did not treat it as confirmed.

Required change:

No immediate skill change required. Continue with the `web-premium-design` output-contract behavior test before considering this skill ready for its minimum pre-packaging manual-test set.

## Test 008

Skill: `web-premium-design`
Date: 2026-06-20
Tester: Deltalank
Claude surface: Claude Web
Prompt:

```text
Actúa como diseñador premium para landing web. Responde exactamente con estas secciones: Confirmado, Falta por confirmar, Dirección visual, Jerarquía UX, Sistema visual, Anti-genérico, Riesgos visuales, Quality gates y Siguiente acción. No escribas código. No inventes datos.
```

Expected behavior:

The skill should activate and follow the requested output contract. It should respond using the requested sections, avoid code, avoid invented project details, provide premium visual direction, include UX hierarchy, visual-system guidance, anti-generic criteria, visual risks, quality gates and a clear next action. It should not switch into SEO, security or general project-architecture mode.

Observed behavior:

Claude followed the requested output structure with the sections Confirmado, Falta por confirmar, Dirección visual, Jerarquía UX, Sistema visual, Anti-genérico, Riesgos visuales, Quality gates and Siguiente acción. It stated that no brand, sector, photos, colors, audience, objective or copy were confirmed, and it listed missing inputs without inventing them. It provided a premium visual direction based on editorial restraint, white space, typographic hierarchy, high contrast, one restrained accent and non-decorative decisions. It included UX hierarchy, anti-generic criteria, visual risks, quality gates and a focused next action. It did not write code and did not switch into security, SEO or architecture.

Result:

`PASS`

Issues found:

None.

Required change:

No immediate skill change required. `web-premium-design` has now passed the minimum pre-packaging Claude Web manual tests: expected activation, non-activation, missing-data behavior and output-contract behavior.

## Test 009

Skill: `security-web-audit`
Date: 2026-06-20
Tester: Deltalank
Claude surface: Claude Web
Prompt:

```text
Hola Claude, acabo de añadir la habilidad “security-web-audit”. Hola Claude, acabo de añadir la habilidad “security-web-audit”. Quiero auditar la seguridad de una web estática antes de publicarla. No tengo todavía todos los archivos, así que no inventes datos. Dame una revisión profesional de riesgos y un plan de auditoría cubriendo cabeceras de seguridad, CSP, HTTPS/HSTS, formularios, JavaScript de terceros, exposición de secretos, dependencias, cookies, privacidad, configuración del servidor y checklist final. No escribas código todavía salvo ejemplos mínimos si son imprescindibles. ¿Puedes crear algo increíble con ella?
```

Expected behavior:

The skill should activate as a web security audit. It should avoid invented findings because no project files were provided, ask for or list missing files/context, produce a professional risk-review and audit plan, and cover security headers, CSP, HTTPS/HSTS, forms, third-party JavaScript, secret exposure, dependencies, cookies, privacy, server configuration and a final checklist. It should not switch into premium design, SEO local, general project architecture or full implementation mode.

Observed behavior:

Claude activated security-audit behavior and framed the response as a deep pre-file/pre-intake audit. It explicitly stated that no concrete findings were confirmed because no files, deployed URL or hosting configuration had been provided. It separated confirmed facts, inferred assumptions and pending inputs, listed required files and context, identified what could not be verified without deployment, and provided a risk catalogue covering secret exposure, HTML, first-party JavaScript, third-party scripts/CDN, forms, cookies/storage/analytics, privacy/contact links, dependencies, `.htaccess`/server configuration, security headers, CSP and HTTPS/HSTS. It included severity-oriented guidance, correction order, manual post-deployment checks, a final pre-delivery checklist and a reminder not to claim that the site is guaranteed secure or legally compliant. It did not invent specific vulnerabilities or confirmed findings.

Result:

`PASS`

Issues found:

- Claude created a downloadable Markdown audit/playbook document. This is acceptable for this activation test because the content remained a plan/audit framework rather than a coded implementation, but future output-contract tests should verify that the skill respects stricter output format instructions when requested.
- Claude included a few inferred assumptions based on the user's typical stack, such as static vanilla, Hostinger/Apache `.htaccess`, WhatsApp contact, maps, fonts and local SEO data. These were explicitly marked as assumptions to confirm or correct, so they do not count as invented findings.

Required change:

No immediate skill change required. Continue with the `security-web-audit` non-activation, missing-data behavior and output-contract behavior tests before considering this skill ready for its minimum pre-packaging manual-test set.