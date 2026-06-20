---
name: token-budget-controller
description: Controls context size and output length for large website workflows. Use to reduce repetition, avoid context bloat, choose work modes and keep AI tasks efficient.
---

# Token Budget Controller

Version: `0.1.0`
Status: `experimental`
Default mode: `balanced`

## Purpose

Use this skill to keep large website workflows efficient, focused and maintainable.

This skill helps Claude avoid wasting context on repeated instructions, oversized responses, unnecessary file reads and uncontrolled rewrites.

It is especially useful for:

- large website projects
- multi-file audits
- repeated Claude sessions
- long prompts
- large codebases
- website redesign workflows
- security, SEO and QA audits
- client delivery workflows
- converting chaotic requests into phased work
- reducing repeated context in `CLAUDE.md`, `AGENTS.md` and skill instructions

## When to use this skill

Use this skill when the user asks to:

- reduce tokens
- make the workflow more efficient
- avoid wasting context
- split a large task into phases
- summarize a large project before continuing
- choose which files to inspect first
- avoid rewriting full files unnecessarily
- compress instructions
- remove duplicated rules
- optimize prompts
- keep Claude from going off track
- manage a long website project

Typical trigger phrases:

- "reduce tokens"
- "no malgastes tokens"
- "hazlo más eficiente"
- "ordena el trabajo por fases"
- "no leas archivos innecesarios"
- "resume el contexto útil"
- "optimiza este prompt"
- "cómo evito que Claude se vaya por las ramas"
- "controla el tamaño de la respuesta"

## When not to use this skill

Do not use this skill as the main skill for:

- visual design decisions
- security auditing
- SEO auditing
- final website QA
- factual verification
- legal review
- debugging a specific code error
- casual writing
- school exercises unrelated to prompt or context management

This skill manages efficiency and scope. It does not replace specialist workflows.

## Core principles

1. Do not read or repeat more context than needed.
2. Start with the smallest useful step.
3. Prefer phased work over one huge output.
4. Choose quick, balanced or deep mode explicitly.
5. Summarize prior decisions instead of repeating them.
6. Inspect files by priority, not by volume.
7. Avoid full rewrites unless necessary.
8. Keep reusable rules in files, not in every prompt.
9. Move long details into references.
10. Mark unknowns instead of speculating.
11. Stop and ask only when missing information changes the outcome.
12. Preserve safety rules even when compressing.

## Required labels

Use these labels when managing context:

### Essential

Information required to complete the next step.

### Useful but optional

Information that may help, but can be deferred.

### Repeated / compressible

Information already stated or safely summarized.

### Out of scope now

Information unrelated to the current phase.

### Needs later review

Information that should be checked in a later phase.

## Work modes

### Quick mode

Use when the user wants speed.

Output:

1. What matters now
2. What can be ignored for now
3. Short next-step plan
4. Recommended output size

### Balanced mode

Default mode.

Output:

1. Context summary
2. Goal for this phase
3. Essential information
4. Deferred information
5. File or task priority
6. Output size limit
7. Next action

### Deep mode

Use when the user asks for full process control.

Output:

1. Current objective
2. Context inventory
3. Essential context
4. Compressible context
5. Out-of-scope context
6. Risk of context loss
7. File inspection priority
8. Task phase plan
9. Output contract
10. Token-saving rules
11. Stop conditions
12. Handoff summary

## Context compression rules

When compressing context:

- Preserve decisions.
- Preserve constraints.
- Preserve file names and paths.
- Preserve user preferences.
- Preserve safety rules.
- Preserve unresolved questions.
- Remove repetition.
- Remove decorative wording.
- Remove obsolete attempts.
- Summarize long discussions.
- Avoid losing why a decision was made.

## File inspection priority

For website projects, inspect files by purpose:

1. Project instructions: `README.md`, `AGENTS.md`, `CLAUDE.md`
2. Main page: `index.html`
3. Main behavior: primary JavaScript files
4. Main styling: primary CSS files
5. Config: hosting and server config
6. SEO: metadata, schema, sitemap, robots
7. Legal: privacy, cookies, legal pages
8. Tests and examples
9. Large assets only when relevant

Do not inspect large or irrelevant files first unless they affect the current goal.

## Output size control

Before producing a large response, choose one:

- `short`: diagnosis and next action
- `medium`: structured plan with main details
- `long`: complete report or full specification
- `staged`: split into multiple steps

If the user did not request depth, default to `medium`.

## Prompt optimization rules

When optimizing a prompt:

- remove duplicated instructions
- clarify the role
- define the exact task
- define inputs and outputs
- define safety boundaries
- define what not to do
- define success criteria
- include placeholders for missing data
- avoid excessive examples unless needed
- keep reusable instructions in skill files or repo docs

## Avoided patterns

Avoid:

- repeating the same project context in every answer
- writing full files when only a diff is needed
- reading every file before knowing the question
- producing huge audits without a clear scope
- mixing design, SEO, security and testing in one uncontrolled answer
- asking too many questions upfront
- using vague goals like "make it professional" without criteria
- compressing away safety constraints

## Output contract

When delivering a context or token-control plan, use this format unless the user asks for something different:

```md
# Token Budget Plan

## 1. Current objective

## 2. Recommended mode

## 3. Essential context

## 4. Useful but optional

## 5. Repeated / compressible

## 6. Out of scope now

## 7. File or task priority

## 8. Output size limit

## 9. Stop conditions

## 10. Next action
```

## Stop conditions

Stop and ask for clarification when:

- the goal is unclear
- the output format is unclear
- the user asks to modify unknown files
- missing data changes the result
- continuing would require guessing real-world facts
- the task is too large for one safe pass

Do not stop for minor missing details that can be marked as placeholders.

## Quality gates

Before finalizing a response, check:

- Is the next step clear?
- Is unnecessary context removed?
- Are safety constraints preserved?
- Are assumptions labeled?
- Is the output size appropriate?
- Is the task scoped?
- Are files prioritized?
- Are specialist workflows separated?
- Are repeated instructions compressed?
- Is the user protected from false certainty?

## Token policy

This skill is the token policy controller.

- Keep answers concise by default.
- Expand only when useful.
- Prefer staged workflows.
- Use summaries for old context.
- Use tables only when they reduce complexity.
- Avoid duplicate sections.
- Do not hide important warnings just to be shorter.

## Handoff to other skills

This skill may recommend:

- `web-project-architect` for project planning
- `web-premium-design` for visual direction
- `security-web-audit` for security and privacy
- `seo-local-audit` for SEO review
- `web-testing-checklist` for final delivery validation
- `fact-checker-web` for claims and verification

Do not assume those skills are installed. Mention them as recommended workflows, not hard dependencies.

## Final rule

Efficiency is not just shorter text. A good token budget keeps the right context, removes repetition, preserves safety and makes the next action easier.
