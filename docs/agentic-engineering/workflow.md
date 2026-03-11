# Agentic Engineering Workflow

Agentic engineering is a disciplined approach to AI-assisted development where the engineer acts as an orchestrator — defining the "what" and "why," then directing AI agents to handle implementation. This contrasts with *vibe coding*, where prompts replace planning and output is accepted without deep review.

This page describes the workflow used at ESF for agentic development with Claude Code.

---

## The Project Lifecycle

Agentic engineering follows a gated sequence. Each phase produces a verifiable artifact before the next begins.

### 1. Specify

Turn the goal into a written specification before generating any code.

- Define user journeys and acceptance criteria
- Describe technical constraints and out-of-scope items
- Use Claude to expand a rough brief into a full spec, then refine it

The output is a written spec — either a dedicated `SPEC.md` or a well-formed work item description. A vague prompt produces vague code; the specification is the primary lever of quality.

### 2. Plan

Use Claude Code's plan mode to explore the codebase and draft a technical approach without writing any code.

- Review the proposed plan for architectural fit, security risks, and alignment with existing patterns
- Identify data models, integration boundaries, and dependencies upfront
- Catch logic flaws at the design stage, not after code has been written

Approve the plan before proceeding to implementation. This "waterfall in 15 minutes" approach lets you iterate on strategy without polluting the codebase with exploratory scaffolding.

### 3. Implement

Execute tasks in small, reviewable increments.

- Break the plan into bite-sized tasks (e.g., "create the user registration endpoint with email validation")
- Implement one task at a time; verify before moving to the next
- Avoid monolithic prompts that generate hundreds of lines at once

### 4. Verify

Prove the implementation is correct.

- Run automated tests and confirm the suite passes
- Review the diff — every changed line — before merging
- Perform a manual walkthrough of any user-facing changes
- Consider a second review pass (or a second agent) to check for security anti-patterns

!!! warning "The burden of proof"
    If you have not confirmed the code does the right thing, it is not done. Code you *hope* works is not ready to merge.

---

## Setting Up Your Source of Truth

Every project should maintain a `CLAUDE.md` file at the repository root. Claude Code reads this automatically at the start of each session, anchoring agent behavior to your project's conventions and constraints.

A well-structured `CLAUDE.md` includes:

| Section | Purpose | Example |
|---------|---------|---------|
| **Commands** | Key commands for build, test, and run | `npm test`, `uv run pytest -v` |
| **Project Structure** | Where source, tests, and docs live | `/src`, `/tests`, `/docs` |
| **Tech Stack** | Languages, frameworks, and versions in use | React 18, TypeScript 5, Python 3.12 |
| **Code Style** | A representative snippet or link to linting config | `.eslintrc`, `pyproject.toml` |
| **Git Workflow** | Branch naming, commit format, PR requirements | `feature/<alias>/<title>` |
| **Boundaries** | Files and directories agents must not modify | `vendor/`, `.env`, `migrations/` |

See [Claude Code](./claude-code.md) for more on configuring `CLAUDE.md` and sub-agent instructions.

---

## Three-Tier Boundaries

Define explicit rules for agent behavior in your `CLAUDE.md`. Three tiers:

- **Always** — Actions the agent performs without asking: run tests before committing, follow the style guide, log errors to the monitoring system.
- **Ask** — High-impact changes requiring your sign-off before proceeding: modifying database schemas, adding third-party dependencies, changing CI/CD pipelines.
- **Never** — Hard stops: commit secrets, modify vendor directories, remove failing tests without approval.

Clear boundaries prevent the agent from making well-intentioned but harmful changes autonomously.

---

## The PR Contract

Every pull request must satisfy the following contract before review:

- [ ] **Intent** — 1–2 sentences describing what changed and why
- [ ] **Proof it works** — Passing test output, screenshots, or logs
- [ ] **AI role and risk tier** — Which parts were AI-generated and the associated risk level (e.g., *Auth logic — High Risk*)
- [ ] **Review focus** — 1–2 specific areas where the reviewer should apply critical judgment

This contract makes AI authorship explicit and keeps the review conversation anchored to risk rather than implementation detail.

---

## Managing Parallel Work

For running multiple Claude Code sessions simultaneously (e.g., separate tasks for frontend and backend), use Git worktrees to give each agent its own working directory and branch:

```sh
# Create an isolated working copy on a feature branch
git worktree add ../my-project-feature feature/my-feature

# Open Claude Code in that directory
cd ../my-project-feature && claude
```

This prevents file-system conflicts and keeps context boundaries clean between sessions.

---

## What AI Handles Well vs. Where You Own the Problem

AI accelerates the first ~70% of any task — scaffolding, boilerplate, routine functions, and initial implementations. The remaining 30% requires engineering judgment:

| AI handles well | You own this |
|----------------|-------------|
| Boilerplate and project setup | Business logic and edge cases |
| Routine CRUD and standard patterns | Authentication and authorization |
| CSS and UI layout iteration | Security-sensitive code paths |
| Documentation drafts | Architectural consistency |
| Test scaffolding | Threat modeling and risk assessment |

Understanding this boundary prevents over-trusting AI output in the areas that matter most.
