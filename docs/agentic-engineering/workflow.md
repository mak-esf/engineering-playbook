# Agentic Engineering Workflow

Agentic engineering is a disciplined approach to AI-assisted development where the engineer acts as an orchestrator — defining the "what" and "why," then directing AI agents to handle implementation. This contrasts with *vibe coding*, where prompts replace planning and output is accepted without deep review.

This page describes the workflow used at ESF for agentic development with Claude Code.

---

## The Project Lifecycle

Agentic engineering follows a gated sequence. Each phase produces a verifiable artifact before the next begins.

### 1. Specify

Turn the goal into a written specification before generating any code. A vague prompt produces vague code — if requirements are ambiguous, the agent fills the vacuum with assumptions that lead to expensive downstream refactors.

The output is a written spec — either a dedicated `SPEC.md` or a well-formed work item description. Use this minimal template:

```markdown
## Commands
<!-- Key build/test/run commands the agent will need -->

## User Journeys
<!-- Numbered list: Actor → Action → Outcome -->

## Success Criteria
<!-- Testable acceptance criteria, one per line -->

## Technical Constraints
<!-- Languages, frameworks, APIs, versions in use -->

## Out of Scope
<!-- Explicit list of what this spec does NOT cover -->

## Boundaries
<!-- Files or systems the agent must not touch -->
```

**Example user journey + acceptance criterion pair:**

> **Journey:** A new user submits the registration form with a valid email and password.
>
> **Criterion:** `POST /auth/register` returns HTTP 201, stores a bcrypt-hashed password, and sends a confirmation email. It returns HTTP 422 if the email is already registered.

Write at least one acceptance criterion per journey. If you can't write a testable criterion, the journey isn't specific enough yet.

### 2. Plan

Use Claude Code's plan mode to explore the codebase and draft a technical approach without writing any code. Invoke it with:

```sh
# Start a session in plan mode (read-only, no code changes)
claude --plan
# Or, inside an existing session:
/plan
```

Before approving the plan, review it against this checklist:

- [ ] Does it reuse existing patterns and utilities, or invent new ones unnecessarily?
- [ ] Are integration boundaries (external APIs, database schemas) clearly identified?
- [ ] Does it touch any **Never** boundaries defined in `CLAUDE.md`?
- [ ] Are there security-sensitive paths (auth, input handling, permission checks)? If so, flag them explicitly before implementation begins.
- [ ] Is the task sequence ordered smallest-to-largest to maximize early feedback?

Approve the plan before proceeding. This "waterfall in 15 minutes" approach lets you iterate on strategy without polluting the codebase with exploratory scaffolding.

### 3. Implement

Execute tasks in small, reviewable increments. The quality of your task prompt directly determines the quality of the output.

**Prompt quality matters — bad vs. good:**

| | Example |
|--|--|
| **Bad** | `"Build the user authentication system."` |
| **Good** | `"Create a POST /auth/register endpoint. Validate email format (RFC 5322) and hash passwords with bcrypt (cost factor 12). Do not implement login yet. Run existing tests before and after."` |

The bad prompt leaves scope, security decisions, and sequencing entirely to the agent. The good prompt constrains all three.

**TDD loop — four steps per task:**

1. Ask Claude to write a failing test that expresses the acceptance criterion
2. Review and approve the test before any implementation runs
3. Ask Claude to implement until the test passes
4. Review every line of the diff before moving to the next task

**Kill criteria — when to abort and restart:**

- Agent fails to fix the same bug in **3 consecutive attempts** → stop, start a new session with a more constrained prompt
- Diff exceeds **~200 lines** on a single task → the task was too large; undo and decompose further
- Agent **removes or skips a test** to make the suite pass → hard stop; reject and re-prompt with an explicit constraint against it

### 4. Managing Context Drift

In long sessions, agents "forget" earlier constraints. This is called context drift (or the "curse of instructions") — the agent re-implements something you already approved, ignores a boundary rule, or starts inventing new conventions.

**Signs of drift:**

- Agent repeats a decision you already made differently
- A `CLAUDE.md` boundary rule is quietly violated
- The code style shifts mid-session

**How to recover:**

- Re-anchor mid-session: `"Refer to CLAUDE.md and the spec before continuing."`
- If drift is severe, start a new session — paste the spec, summarize decisions made so far, then continue
- Update `CLAUDE.md` with decisions made mid-session so they survive a session restart

### 5. Verify

Prove the implementation is correct. The burden of proof rests entirely with you: if you haven't confirmed the code does the right thing, it is not done.

**Diff review checklist — what to look for in AI-generated code:**

- [ ] Hardcoded values that should be config (credentials, magic numbers, environment-specific URLs)
- [ ] Missing input validation at system boundaries
- [ ] Error cases silently swallowed (bare `except:`, empty `catch {}`)
- [ ] Tests deleted or skipped to make the suite pass
- [ ] New dependencies added without your explicit approval
- [ ] Auth and permission checks on every data-mutating path

**Two-agent review pattern:**

After implementation, open a separate Claude session with no prior context. Paste in the diff and the acceptance criteria. Ask:

> "Review this diff against the spec. Identify logic errors, missing edge cases, and security anti-patterns."

This second session has no stake in the original implementation and catches what the first session rationalizes away.

Research shows logic errors are 75% more common and XSS vulnerabilities occur at 2.74x higher frequency in AI-generated code versus human-written code — treat every diff as requiring active proof of correctness, not a passive scan.

---

## Setting Up Your Source of Truth

Every project should maintain a `CLAUDE.md` file at the repository root. Claude Code reads this automatically at the start of each session, anchoring agent behavior to your project's conventions and constraints.

Here is a complete template to adapt:

```markdown
## Commands
- Build: `npm run build`
- Test: `npm test -- --coverage`
- Lint: `npm run lint`

## Project Structure
- `/src` — application source
- `/tests` — unit and integration tests
- `/docs` — documentation

## Conventions
- Branch: `feature/<alias>/<title>`
- Commit format: conventional commits (`feat:`, `fix:`, `docs:`)
- Functions: camelCase; files: kebab-case

## Boundaries
### Always
- Run `npm test` before every commit
- Add a test for every new function

### Ask
- Adding a third-party dependency
- Modifying database schema files

### Never
- Modify files in `/vendor` or `/.env`
- Remove a failing test without approval
- Commit secrets or credentials
```

See [Claude Code](./claude-code.md) for more on configuring `CLAUDE.md` and sub-agent instructions.

---

## Three-Tier Boundaries

Define explicit rules for agent behavior in your `CLAUDE.md` using the template above. Three tiers:

- **Always** — Actions the agent performs without asking: run tests before committing, follow the style guide, log errors to the monitoring system.
- **Ask** — High-impact changes requiring your sign-off before proceeding: modifying database schemas, adding third-party dependencies, changing CI/CD pipelines.
- **Never** — Hard stops: commit secrets, modify vendor directories, remove failing tests without approval.

As an `Always` rule, define kill criteria: maximum retry count (e.g., 3 attempts on the same bug) and maximum diff size (e.g., ~200 lines per task). When either threshold is hit, the agent stops and you re-scope before continuing.

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

AI accelerates the first ~70% of any task — scaffolding, boilerplate, routine functions, and initial implementations. The remaining 30% requires engineering judgment that AI measurably struggles with (logic errors are 75% more common; XSS vulnerabilities occur at 2.74x higher frequency in AI-generated code):

| AI handles well | You own this |
|----------------|-------------|
| Boilerplate and project setup | Business logic and edge cases |
| Routine CRUD and standard patterns | Authentication flows, permission checks, role escalation paths |
| CSS and UI layout iteration | Security-sensitive code paths |
| Documentation drafts | Architectural consistency |
| Test scaffolding | Threat modeling and risk assessment |

Understanding this boundary prevents over-trusting AI output in the areas that matter most.
