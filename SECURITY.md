# Security Policy

## Supported versions

This project is experimental. Security-related reports are welcome for the current `main` branch and active pull requests.

## Scope

This repository contains Claude Skills, documentation and helper scripts. It does not provide pentesting, legal compliance certification, SEO guarantees or proof that a website is safe.

## Do not include sensitive data

Never open an issue, pull request or example containing:

- API keys
- tokens
- credentials
- passwords
- private client data
- private phone numbers
- private screenshots
- unredacted emails
- private legal documents

Use placeholders instead:

- `[API_KEY_REDACTED]`
- `[CLIENT_NAME]`
- `[BUSINESS_ADDRESS_TO_CONFIRM]`
- `[LEGAL_EMAIL_TO_CONFIRM]`
- `[PRIVATE_DATA_REDACTED]`

## Reporting a vulnerability

Open a GitHub issue if the report does not contain sensitive data. If sensitive data is involved, remove it before reporting.

## Security philosophy

- Local-first validation is preferred.
- Claims must be honest and limited.
- A clean checklist does not prove security.
- Human review is required before using these workflows for real client projects.
