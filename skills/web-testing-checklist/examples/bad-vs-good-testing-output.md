# Bad vs Good Testing Output

## Bad output

```text
La web está perfecta y lista para publicar.
```

Why this is bad:

- no scope
- no manual checks
- no responsive matrix
- no critical path review
- no limitations
- overclaims readiness

## Good output

```text
Within the reviewed files, no obvious blocker was found in the main navigation.

Checked:
- homepage structure
- visible navigation links
- WhatsApp link format

Needs manual review:
- WhatsApp behavior on a real phone
- deployed URL
- browser console
- mobile menu interaction
- form submission

Decision:
Not ready to call final until manual checks are completed.
```

Why this is good:

- avoids false certainty
- separates checked from pending
- focuses on delivery risk
- gives a clear next step
