# Manual Structural Audit

Date: 2026-06-20
Status: professional draft audit
Packaging: not started

## Purpose

This audit reviews whether the current skill suite is structurally ready for deeper manual testing in Claude Web.

It does not prove that the skills are perfect. It checks whether the repository has the right shape to continue toward a higher-quality release.

## Summary

| Area | Status | Notes |
|---|---|---|
| Skill count | Pass | Seven skills are implemented. |
| Skill folders | Pass | Each skill follows the expected folder pattern. |
| Core files | Pass | Each skill has `SKILL.md` and `README.md`. |
| References | Pass | Each skill has reference material. |
| Examples | Pass | Each skill has practical examples. |
| Trigger tests | Pass | Each skill has activation prompts. |
| Non-trigger tests | Pass | Missing `fact-checker-web` test was added in the previous cleanup pass. |
| Regression tests | Pass | Each skill has regression prompts. |
| Validation script | Improved | Script now checks frontmatter name, description length, reference/example markdown files and required test files. |
| GitHub Actions | Present | Workflow exists. Needs live confirmation on a PR run. |
| ZIP packaging | Not started | Intentionally deferred. |
| Claude Web upload | Not started | Requires packaging later. |

## Skill-by-skill review

### web-project-architect

Status: Pass for structure.

Strengths:

- Clear planning purpose.
- Strong separation between confirmed, inferred and missing data.
- Useful for local business and gym projects.
- Good handoff to other skills.

Next improvements:

- Test activation in Claude Web with vague website creation prompts.
- Check whether the description triggers too broadly.

### web-premium-design

Status: Pass for structure.

Strengths:

- Strong anti-generic design framing.
- Visual thesis requirement is useful.
- Good focus on conversion and mobile-first design.

Next improvements:

- Test whether it activates for design-only prompts and not for SEO/security prompts.
- Add real Claude Web output examples after manual testing.

### security-web-audit

Status: Pass for structure.

Strengths:

- Honest scope and limitations.
- Strong severity labels.
- Good coverage of static website risks, privacy and headers.

Next improvements:

- Test with a real static website file set.
- Confirm the skill does not overclaim security readiness.

### seo-local-audit

Status: Pass for structure.

Strengths:

- Clear NAP and source policy.
- Avoids ranking guarantees.
- Covers metadata, schema and Google Business Profile alignment.

Next improvements:

- Test with a local business landing page.
- Check schema guidance for over-triggering or over-detail.

### web-testing-checklist

Status: Pass for structure.

Strengths:

- Strong final delivery framing.
- Separates checked, manual and not-verifiable items.
- Good critical path focus.

Next improvements:

- Test with a deployed URL and with files-only context.
- Confirm it does not claim device testing without evidence.

### fact-checker-web

Status: Pass for structure.

Strengths:

- Strong source and claim classification.
- Handles demo content safely when explicitly requested.
- Protects against unsupported real-world claims.

Next improvements:

- Test with mock content and real-client content.
- Confirm the demo-content mode does not weaken safety for production copy.

### token-budget-controller

Status: Pass for structure.

Strengths:

- Good context-control model.
- Clear file priority and work modes.
- Useful for long Claude sessions and large projects.

Next improvements:

- Test with long prompts and multi-file audit requests.
- Confirm it preserves safety rules while compressing.

## Current release maturity

| Maturity area | Rating | Reason |
|---|---:|---|
| Structure | 9/10 | Strong folder and file consistency. |
| Documentation | 8/10 | Good docs, but needs real test results. |
| Safety framing | 9/10 | Strong no-overclaim and placeholder rules. |
| Automation | 7/10 | Validation workflow exists, but must be confirmed in action. |
| Claude Web readiness | 6/10 | Needs packaging and upload tests. |
| Overall current maturity | 8/10 | Good professional draft, not yet stable. |

## Not 10/10 yet because

- The skills have not been uploaded and tested in Claude Web.
- The GitHub Actions workflow has not yet been observed passing on a fresh PR.
- There are no recorded real outputs from Claude Web.
- No ZIP packages have been generated or inspected.
- No agent-rules-kit reports have been committed to `audits/`.

## Next steps toward 10/10

1. Let the validation workflow run on this PR.
2. Fix any validation failures.
3. Add Claude Web manual test plan.
4. After merge, clone locally and run `python scripts/validate-skills.py`.
5. Run `agent-rules-kit` and save reports in `audits/`.
6. Only after that, package ZIP files.
7. Upload one skill at a time to Claude Web.
8. Record activation results and adjust descriptions.
