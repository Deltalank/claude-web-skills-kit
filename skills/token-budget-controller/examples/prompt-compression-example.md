# Prompt Compression Example

## User request

```text
Reduce this long prompt and keep only what matters.
```

## Expected behavior

The skill should:

- preserve the task goal
- preserve constraints
- preserve safety rules
- remove duplicated instructions
- define output format
- mark missing inputs
- keep the next action clear

## Example result shape

```text
Role: web project reviewer
Task: audit the homepage before delivery
Inputs: index.html, styles.css, main.js
Output: prioritized findings table
Rules: do not invent client data, mark unknowns, avoid full rewrites unless needed
```
