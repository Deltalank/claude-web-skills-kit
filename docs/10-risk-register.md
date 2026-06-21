# Risk Register

Status: active
Packaging: not started

This register tracks risks that must be controlled before packaging and uploading skills to Claude Web.

## Risk levels

- `High`: must be fixed before packaging.
- `Medium`: should be fixed before broad use.
- `Low`: track and improve over time.

## Current risks

| Risk | Level | Status | Control |
|---|---:|---|---|
| Skill activates too broadly | Medium | Open | Manual Claude Web activation tests. |
| Skill does not activate when expected | Medium | Open | Trigger prompt tests and description tuning. |
| Output ignores contract | Medium | Open | Manual output checks. |
| Missing data is treated as fact | High | Controlled | Fact-checker rules, placeholders and quality gates. |
| Demo content used as production content | High | Controlled | Demo-only labels and replacement warnings. |
| Context grows too large | Medium | Controlled | Token budget controller and staged workflow. |
| Packaging changes folder structure | Medium | Open | ZIP inspection before upload. |
| Automation passes but manual behavior fails | Medium | Open | Claude Web manual test plan. |
| README and CHANGELOG drift | Low | Controlled | Release consistency check. |
| Sensitive data appears in examples | High | Controlled | Repository hygiene check. |

## SEO-local specific risks

These risks apply especially to `seo-local-audit` and must be controlled before packaging.

| Risk | Level | Status | Control |
|---|---:|---|---|
| Hallucination of local business facts | High | Controlled | `seo-local-audit` must label confirmed, inferred, missing and not-verifiable data; never invent NAP, services, hours, locations or prices. |
| False Google Business Profile verification claims | High | Controlled | Do not claim GBP verification, ownership, restrictions, optimization or performance without supplied profile evidence or account-derived data. |
| Review or rating fabrication | High | Controlled | Refuse fake reviews, fake ratings, fake testimonials, fake awards and fake reputation claims; use verification placeholders. |
| Self-serving review or `aggregateRating` misuse | High | Controlled | Do not imply that review/rating markup on the business's own website guarantees stars or rich results; require verified and compliant evidence. |
| Ranking or rich-result overclaims | High | Controlled | Never guarantee top rankings, Maps visibility, traffic, leads, revenue or rich-result display. |
| Doorway-page recommendation risk | High | Controlled | Reject duplicate city-page strategies that only swap location names; recommend distinct, useful local pages only when justified. |
| Service-area business address exposure | High | Controlled | Classify storefront, service-area and hybrid businesses before location advice; do not assume a private address should be public. |
| Keyword volume or competitor hallucination | High | Controlled | Treat keywords and competitors as hypotheses unless supported by Search Console, GBP Performance, keyword tools, user evidence or explicit research. |
| schema.org and Google support confusion | Medium | Controlled | Treat schema.org as vocabulary and Google documentation as the source for rich-result eligibility and limits. |
| Confidence inflation under incomplete input | High | Controlled | When URL, files, GBP, Search Console, Analytics or screenshots are missing, output a readiness pre-audit and mark blocked checks clearly. |
| Unsafe Google Business Profile policy advice | High | Controlled | Do not recommend keyword stuffing in business names, fake engagement, misleading categories, fake addresses or deceptive profile changes. |
| Local SEO workflow used for non-SEO tasks | Medium | Open | Regression prompts must verify non-activation for security, visual design, testing, fact-checking and token-optimization workflows. |

## Release rule

A risk can be accepted only if it is documented with a reason and a follow-up action.

No skill should be packaged while a high-risk behavior remains uncontrolled or untested in Claude Web.
