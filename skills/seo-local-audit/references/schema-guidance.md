# Schema Guidance

Structured data should represent the real business accurately.

## Rules

- Use only confirmed business data.
- Do not invent address, phone, hours, reviews or ratings.
- Do not add `aggregateRating` unless ratings are verified and appropriate.
- Choose schema types that match the actual business.
- Validate structured data after implementation.
- Mark unknown fields as placeholders.

## Useful placeholders

- `[BUSINESS_NAME_TO_CONFIRM]`
- `[ADDRESS_TO_CONFIRM]`
- `[PHONE_TO_CONFIRM]`
- `[OPENING_HOURS_TO_CONFIRM]`
- `[GEO_COORDINATES_TO_CONFIRM]`
- `[REVIEW_TO_VERIFY]`
- `[RATING_TO_VERIFY]`

## Warning

Schema does not guarantee ranking. It helps search engines understand eligible structured information when implemented correctly.
