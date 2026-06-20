# Regression Prompts

Use these prompts after editing the skill to verify behavior.

## Prompt 1

```text
Comprueba si esta web está lista para enseñársela al cliente. Tengo index, CSS y JS, pero aún no tengo URL pública.
```

Expected behavior:

- Review provided files if available.
- Mark deployed URL checks as pending.
- Do not claim final readiness.
- Prioritize critical user paths.

## Prompt 2

```text
Dime si todos los botones, enlaces y WhatsApp funcionan.
```

Expected behavior:

- Check link format if files are available.
- Mark real device/browser behavior as needing manual review.
- Identify contact path risks.

## Prompt 3

```text
Haz un checklist responsive para móvil, tablet y desktop.
```

Expected behavior:

- Provide viewport matrix.
- Check or request screenshots/files.
- Include no horizontal overflow, readable text and CTA visibility.

## Prompt 4

```text
Está lista para publicar, ¿sí o no?
```

Expected behavior:

- Avoid unsupported certainty.
- Give a readiness decision based on reviewed scope.
- List manual checks required before publishing.
