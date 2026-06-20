# Release Process

## Versioning

Use semantic versioning for public skill behavior.

- `0.x.x` experimental
- `1.0.0` stable
- patch version: wording fixes and small corrections
- minor version: new examples, modes or references
- major version: output contract or core behavior changes

## Release checklist

- [ ] Skill files are complete.
- [ ] Examples are reviewed.
- [ ] Trigger tests are reviewed.
- [ ] Non-trigger tests are reviewed.
- [ ] Safety boundaries are clear.
- [ ] Changelog is updated.
- [ ] ZIP file is generated in `dist/`.
- [ ] No secrets or real client private data are included.

## Packaging

Run:

```bash
./scripts/package-skills.sh
```

Expected output:

```text
dist/<skill-name>.zip
```

Upload the ZIP in Claude Web through:

```text
Personalizar → Skills → + → Cargar una habilidad
```
