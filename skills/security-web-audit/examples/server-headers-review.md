# Server Headers Review Example

## User request

```text
Review the server header configuration for a static client website before delivery.
```

## Expected behavior

The skill should:

- identify which headers are present
- flag risky or missing directives
- warn that strict transport settings require confirmed HTTPS
- warn that content security rules must be tested against actual scripts, fonts, images and embeds
- avoid one-size-fits-all recommendations without caveats

## Expected notes

- Header policy should be based on actual resources.
- Strict transport settings should only be enabled when HTTPS is correctly configured.
- Header behavior must be verified after deployment.
