# Manual Test Log

Status: active

Use this file to record Claude Web tests before packaging any ZIP files.

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
