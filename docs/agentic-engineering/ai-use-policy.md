# AI Use Policy

This policy establishes principles and requirements for AI-assisted development at ESF. It applies to all use of AI coding tools — including Claude Code, GitHub Copilot, and similar agents — on ESF projects.

---

## Guiding Principles

### The Human Remains Accountable

Every commit is the responsibility of the human who authored it. AI tools accelerate implementation; they do not transfer accountability. You must be able to explain every line of code as if you wrote it by hand. No pull request should be approved if the author cannot articulate the logic and its long-term impact on the system.

### Proof Over Hope

Committing code you *hope* works is not acceptable. Every AI-assisted contribution must be accompanied by evidence that it works: passing tests, logs, screenshots, or manual verification steps documented in the pull request.

### Use AI to Amplify, Not Bypass

AI tools are most valuable when they amplify engineering judgment — accelerating routine implementation, surfacing alternatives, and reducing friction on well-understood tasks. They are least appropriate as a shortcut around understanding, review, or testing. Accepting code you cannot explain is a risk, not a productivity gain.

---

## When AI Tools Are Appropriate

| Use Case | Appropriate | Notes |
|----------|-------------|-------|
| Boilerplate and scaffolding | Yes | Standard patterns; review the output |
| Unit test generation | Yes | Verify tests exercise the right behavior |
| Documentation drafts | Yes | Edit for accuracy before committing |
| Routine refactors | Yes | Small, focused tasks with clear scope |
| Business logic implementation | With review | Verify edge cases and domain correctness |
| Authentication and authorization | With mandatory sign-off | See [High-Stakes Areas](#high-stakes-areas) |
| Security-sensitive code | With mandatory sign-off | See [High-Stakes Areas](#high-stakes-areas) |
| Secrets and key management | No | Never generate or handle secrets with AI |

---

## Verification Requirements

All AI-assisted contributions must meet the following standards before merging.

### Test Coverage

- Maintain automated test coverage at or above 70% for all changed modules
- Tests must be written *before* or *alongside* implementation — post-hoc tests confirm what code does, not what it should do
- Failing tests must not be removed or suppressed without explicit documented approval

### Pull Request Contract

Every AI-assisted pull request must include:

- [ ] **Intent** — 1–2 sentences describing what changed and why
- [ ] **Proof it works** — Passing test output, screenshots, or logs
- [ ] **AI role and risk tier** — Which parts were AI-generated and the associated risk (e.g., *Auth logic — High Risk*)
- [ ] **Review focus** — Specific areas where the reviewer's judgment is required

See [Agentic Engineering Workflow — The PR Contract](./workflow.md#the-pr-contract) for details.

### Diff Review

Authors must read every changed line before requesting review. Reviewers may reject a pull request if the author cannot explain the AI-generated logic.

---

## High-Stakes Areas

The following areas require explicit human sign-off and may not be merged based on AI generation alone:

- [ ] Authentication and authorization logic
- [ ] Payment processing and financial calculations
- [ ] Secrets management and API key handling
- [ ] Processing of untrusted user input
- [ ] Changes to CI/CD pipelines and deployment configuration

For these areas:

1. A second engineer must review the implementation independently
2. The pull request must include a brief note describing the attack surface and threat model considered
3. Static analysis or a security-focused review pass is strongly recommended before merge

---

## Responsible Use

### Data and Confidentiality

- Do not send confidential client data, personally identifiable information (PII), or proprietary intellectual property to external AI services unless explicitly permitted by project policy
- When in doubt, raise the question with your project lead before starting work

### Transparency

- Attribute AI-generated code in commits using the `Assistant-model` Git trailer (see [Claude Code — Attributing AI-Assisted Code](./claude-code.md#attributing-ai-assisted-code))
- Disclose AI tool use in pull request descriptions when the majority of the change was AI-generated

### Skill Development

Using AI as a crutch for code you cannot explain creates a compounding risk: when the model fails or produces something incorrect, you will lack the judgment to catch it. Use AI tools to accelerate work you understand — not to avoid understanding it.

---

## Scope

This policy applies to all engineers working on ESF projects. It covers:

- Autonomous coding agents (e.g., Claude Code, GitHub Copilot Coding Agent)
- IDE assistants (e.g., GitHub Copilot extension, Cursor)
- Chat-based AI tools used to generate production code (e.g., ChatGPT, Claude.ai)

Exemptions for prototypes, hackathons, or throwaway scripts must be agreed with the project lead and documented in the relevant work item.
