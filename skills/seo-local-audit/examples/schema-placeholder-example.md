# Schema Placeholder Example

## User request

```text
Crea schema para una web de gimnasio local, pero todavía no tengo todos los datos.
```

## Expected behavior

The skill should:

- not invent business data
- use placeholders
- avoid fake ratings
- recommend validation after implementation

## Example placeholders

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[BUSINESS_NAME_TO_CONFIRM]",
  "address": "[ADDRESS_TO_CONFIRM]",
  "telephone": "[PHONE_TO_CONFIRM]",
  "openingHours": "[OPENING_HOURS_TO_CONFIRM]"
}
```

## Warning

The exact schema type and fields must match the real business and verified data.
