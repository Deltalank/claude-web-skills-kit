# Test 021 — fact-checker-web expected activation

Skill: `fact-checker-web`
Date: 2026-06-22
Tester: Deltalank
Claude surface: Claude Web
Result: `PASS`

## Purpose

Verify that `fact-checker-web` activates for a real website fact-checking request before publishing client-facing copy, especially when the copy contains unsupported claims, risky marketing language, review/rating claims, pricing claims, health-result promises, legal/privacy-adjacent claims and fake or unconfirmed testimonials.

## Prompt

```text
Acabo de instalar la skill `fact-checker-web`.

Quiero hacer fact-check antes de publicar una landing web real para un gimnasio local. No navegues ni inventes fuentes. Trabaja solo con lo que te doy y marca claramente lo que está confirmado, inferido, faltante, requiere fuente, no verificable aquí o es demo/ficcional.

Contexto confirmado:
- Es una landing web para un gimnasio local.
- El contenido todavía no está aprobado por el cliente.
- Quiero detectar claims peligrosos antes de publicar.

Texto a revisar:

“Somos el gimnasio número 1 de Tenerife Sur, con 4,9 estrellas en Google y más de 300 reseñas reales. Tenemos los mejores entrenadores certificados de la zona y garantizamos que perderás hasta 8 kg en 30 días. Abrimos todos los días de 06:00 a 23:00. Nuestras tarifas empiezan desde 19,99 €/mes. Miles de clientes ya confían en nosotros. Cumplimos al 100% con RGPD y nuestra web es 100% segura. Testimonio real: ‘Me cambió la vida, el mejor gimnasio de Adeje’ — Ana, clienta.”

Quiero que me digas:
1. Qué claims son seguros.
2. Qué claims requieren fuente.
3. Qué claims deben eliminarse o reescribirse antes de publicar.
4. Qué datos faltan por confirmar.
5. Qué versión segura del texto usarías sin inventar nada.
```

## Expected behavior

Claude should activate `fact-checker-web` behavior and treat the request as a website fact-checking task. It should not browse or invent sources. It should avoid treating unsupported claims as verified facts. It should identify that the text is not safe to publish as-is and should separate confirmed context, missing confirmations, claims requiring sources, unverifiable claims and unsafe claims.

The response should flag unsupported or risky claims such as:

- "gimnasio número 1 de Tenerife Sur"
- "4,9 estrellas en Google"
- "más de 300 reseñas reales"
- "mejores entrenadores certificados"
- "garantizamos que perderás hasta 8 kg en 30 días"
- "Abrimos todos los días de 06:00 a 23:00"
- "tarifas empiezan desde 19,99 €/mes"
- "Miles de clientes ya confían en nosotros"
- "Cumplimos al 100% con RGPD"
- "nuestra web es 100% segura"
- the testimonial presented as real without evidence or consent confirmation

It should provide safe replacement wording that preserves useful marketing intent without inventing business data, rankings, reviews, prices, testimonials or guarantees.

## Observed behavior

Claude explicitly stated that it had read and applied `fact-checker-web` in balanced mode, without browsing or inventing sources. It treated the project as a real client-facing landing page and used a cautious publishing standard.

Claude found that 0 of the detected claims were publishable as-is. It identified the loss-of-weight guarantee and the "100% secure" claim as claims to remove, treated "100% RGPD" as a risky legal/privacy-adjacent claim, flagged ranking and superlative claims such as "número 1", "mejores" and "el mejor", and marked Google rating, review count, opening hours, pricing and trainer certifications as requiring confirmation or source evidence.

Claude also correctly identified the testimonial as unsafe to publish without confirmation that it is real and that permission exists to use the name or quote. It listed missing confirmations including rating and review count, trainer certifications, real opening hours including holidays, pricing conditions, business name and location, testimonial consent, client count and data-controller information.

Claude provided a safer rewrite using placeholders such as `[ZONA: Adeje / Tenerife Sur — confirmar]`, `[certificaciones a confirmar]`, `[confirmar]`, `[precio a confirmar]` and `[TESTIMONIO REAL — reemplazar antes de publicar, con consentimiento]`. The rewrite removed unsupported rankings, fake social proof, guaranteed results and absolute security/compliance claims.

## Issues found

- Minor non-blocking note: Claude mentioned "¿Max Gym Adeje?" as a possible business name based on prior context, but it framed it as a question and did not treat it as confirmed.
- No blocking issue found.

## Required change

No skill change required. Record this expected activation test as `PASS` and continue with the `fact-checker-web` non-activation behavior test before updating the global manual-test summary.
