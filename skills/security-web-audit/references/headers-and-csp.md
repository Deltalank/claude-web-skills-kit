# Headers and CSP

## Headers to consider

- `Content-Security-Policy`
- `Referrer-Policy`
- `X-Content-Type-Options`
- `X-Frame-Options` or CSP `frame-ancestors`
- `Permissions-Policy`
- `Strict-Transport-Security`

## HSTS warning

Only recommend HSTS when HTTPS is correctly configured and the site owner understands the persistence risk.

## CSP workflow

1. Inventory actual scripts, styles, images, fonts and embeds.
2. Start with a restrictive but realistic policy.
3. Avoid `unsafe-inline` unless required and clearly marked.
4. Test in browser.
5. Use report-only mode when appropriate.
6. Mark CSP as pending verification until deployed and tested.

## Shared hosting note

Some shared hosts may not apply all headers the same way. Verify deployed headers after publishing.
