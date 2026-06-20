# Static Gym Site Audit Example

## User request

```text
Revisa la seguridad de esta web estática de gimnasio antes de subirla a Hostinger.
```

## Expected behavior

The skill should:

- ask for or inspect relevant files
- identify scope and limitations
- check for exposed secrets
- review `.htaccess` if present
- check external scripts and embeds
- check forms and data collection
- flag privacy and cookies issues
- avoid claiming that the website is fully secure
- produce findings by severity

## Expected output outline

- Audit summary
- Scope and limitations
- Confirmed / Inferred / Missing / Not verifiable
- Findings by severity
- Privacy and cookies review
- Headers and hosting review
- External scripts review
- Forms review
- Recommended fix order
- Manual checks before delivery
- Next action
