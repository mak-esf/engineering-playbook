# Multi-Agent Orchestration

A single Claude Code session handles most tasks well. For larger, parallelizable work — separate frontend and backend tracks, specialist reviewers, or independent refactors — multiple coordinated agents deliver faster results with better separation of concerns.

This page covers when and how to use multi-agent patterns at ESF.

---

## When to Use Multiple Agents

Use multiple agents when tasks are genuinely independent — they can proceed concurrently without waiting on shared state, and their outputs can be merged cleanly.

**Good candidates:**

- Parallel workstreams: frontend and backend implementation of the same feature
- Specialist review: a dedicated agent focused solely on security or performance
- Independent refactors across modules that don't call each other
- Generating tests and generating implementation separately for the same spec

**Not a good fit:**

- Tasks with tight dependencies (agent B needs agent A's output to proceed)
- When a single session is fast enough — orchestration adds overhead
- When the merge will be complex — parallel branches that heavily overlap increase conflict risk

---

## Role-Based Orchestration

For complex features, assign distinct roles to each agent rather than giving every agent the same broad mandate. A common pattern:

```
Planner → Coder → Tester → Reviewer
```

| Role | Responsibility | What to give it |
|------|---------------|-----------------|
| **Planner** | Produces a technical approach and task list | The spec, relevant files, architecture notes |
| **Coder** | Implements one task at a time | The plan, relevant source files, acceptance criteria |
| **Tester** | Writes or expands tests against the implementation | The implementation diff, acceptance criteria |
| **Reviewer** | Critiques correctness, security, and edge cases | The diff, the spec, no prior implementation context |

Each agent starts a fresh session with only what it needs. Keeping contexts narrow reduces drift and produces more focused output.

---

## Critique-Driven Development

The Reviewer role is most effective when it has *no stake* in the original implementation — a fresh session with no prior context. This is the two-agent review pattern from [Agentic Engineering Workflow](./workflow.md#5-verify), extended into a feedback loop.

**Pattern:**

1. Coder agent produces an implementation
2. Reviewer agent receives only the diff and the spec — no conversation history
3. Reviewer returns a list of issues: logic errors, missing edge cases, security gaps
4. Convert each issue into a targeted refinement prompt for the Coder agent

**Converting review comments into refinement prompts:**

Instead of pasting the raw review back and asking the agent to "fix it," translate each comment into a scoped prompt:

| Review comment | Refinement prompt |
|----------------|-------------------|
| *"No input validation on the email field"* | `"Add RFC 5322 email validation to POST /auth/register before the bcrypt call. Do not change anything else."` |
| *"Error from the DB is swallowed in the catch block"* | `"In registerUser(), log the caught database error and re-throw it as a typed ApplicationError. Keep the rest of the function unchanged."` |
| *"Missing permission check on DELETE /items/:id"* | `"Add an ownership check to DELETE /items/:id: the requesting user must own the item or have admin role. Return 403 otherwise."` |

Targeted prompts produce targeted diffs, which are faster to review and less likely to introduce regressions.

---

## Git Worktree Setup for Agent Isolation

Each parallel agent session should operate in its own Git worktree. This prevents file-system conflicts between concurrent sessions and keeps each agent's branch history clean.

```sh
# Create an isolated working copy for a parallel workstream
git worktree add ../project-feature-auth feature/auth
git worktree add ../project-feature-ui feature/ui

# Start Claude Code in each worktree
cd ../project-feature-auth && claude
cd ../project-feature-ui && claude   # in a separate terminal
```

When both workstreams are complete, merge or rebase the branches as you normally would. See [Managing Parallel Work](./workflow.md#managing-parallel-work) for the full context.

---

## Tool Ecosystem Overview

Claude Code is one of several capable coding agents available. Understanding the landscape helps you pick the right tool for specific tasks.

**CLI agents:**

| Tool | Best for |
|------|---------|
| **Claude Code** | General-purpose agentic coding; strong at multi-file edits, planning, and code review |
| **Gemini CLI** | Google Workspace integrations; large context window useful for whole-repo analysis |
| **Aider** | Lightweight terminal agent; good for targeted single-file edits in any model |
| **Amp** | Fast interactive coding sessions; model-agnostic |

**Orchestrators (agent-over-agents):**

| Tool | What it does |
|------|-------------|
| **Claude Squad** | Runs multiple Claude Code instances in parallel worktrees from a single terminal |
| **Conductor** | Workflow orchestrator that routes tasks to specialist agents and aggregates results |
| **Jules** (Google) | Async background agent that works in a separate branch while you continue other work |

At ESF, Claude Code is the default. Introduce other tools only when there is a specific, documented reason — each additional tool in the stack is another surface to configure, secure, and maintain.
