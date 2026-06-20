# Bad vs Good Security Output

## Bad output

```text
Todo está seguro. Puedes publicarlo.
```

Why this is bad:

- no scope
- no limitations
- no severity
- no verification steps
- no privacy review
- overclaims security

## Good output

```text
No obvious critical issue was found in the reviewed files, but this is not a full security guarantee.

Scope reviewed:
- index.html
- styles.css
- main.js
- .htaccess

Missing / To confirm:
- deployed headers
- real cookie behavior
- form endpoint
- hosting HTTPS configuration

Finding:
Medium — configuration risk — CSP not verified on deployed host.
Impact: scripts or resources may be blocked or policy may be too loose.
Fix: test deployed CSP in browser and adjust allowed sources.
```

Why this is good:

- avoids overclaiming
- states scope
- lists missing checks
- classifies severity
- gives a practical fix
