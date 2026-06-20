# Regression Prompts

Use these prompts after editing the skill to verify behavior.

## Prompt 1

```text
Tengo una web grande. Quiero revisarla sin malgastar tokens.
```

Expected behavior:

- Choose a mode.
- Prioritize files.
- Defer optional context.
- Propose a staged plan.

## Prompt 2

```text
Optimiza este prompt largo para que Claude no repita cosas.
```

Expected behavior:

- Remove duplication.
- Preserve constraints and safety rules.
- Define a clearer output format.

## Prompt 3

```text
Dame solo el siguiente paso útil, no una auditoría enorme.
```

Expected behavior:

- Keep output short.
- Identify essential context.
- Give one next action.

## Prompt 4

```text
Resume lo importante de este proyecto para seguir en otro chat.
```

Expected behavior:

- Preserve decisions, constraints, file names, risks and next actions.
- Remove repeated or obsolete context.
