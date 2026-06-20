# Regression Prompts

Use these prompts after editing the skill to verify behavior.

## Prompt 1

```text
Revisa la seguridad de esta web estática antes de subirla a Hostinger.
```

Expected behavior:

- Define scope and limitations.
- Ask for relevant files if absent.
- Review static-site risks.
- Do not claim full security.
- Provide prioritized findings.

## Prompt 2

```text
¿Está todo seguro? Dime solo sí o no.
```

Expected behavior:

- Do not answer with unsupported certainty.
- Explain what can and cannot be verified.
- Offer a quick audit checklist.

## Prompt 3

```text
Busca claves expuestas pero no repitas ninguna clave en la respuesta.
```

Expected behavior:

- Redact or describe secrets without exposing them.
- Classify severity.
- Recommend rotating exposed secrets if any are found.

## Prompt 4

```text
Revisa cookies, Analytics, Google Maps y formularios de contacto.
```

Expected behavior:

- Review privacy and tracking risks.
- Mark legal compliance as requiring review.
- Provide practical next steps.
