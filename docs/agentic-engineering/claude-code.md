# Claude Code

Claude Code is Anthropic's AI coding agent, available as a CLI and IDE extension. It can read and edit files, run commands, manage Git operations, browse the web, and iterate on code autonomously within the boundaries you define. This page covers how to set it up and use it effectively for day-to-day development.

---

## Getting Started

Install Claude Code via npm and authenticate with your Anthropic account:

```sh
npm install -g @anthropic-ai/claude-code
claude
```

On first run, Claude Code will guide you through browser-based authentication. For full setup instructions, see the [official documentation](https://docs.anthropic.com/en/docs/claude-code/overview).

---

## Configuring Claude Code for Your Project

### CLAUDE.md

Create a `CLAUDE.md` file at the repository root. Claude Code reads this file automatically at the start of every session and uses it to align its behavior with your project's conventions and constraints.

At a minimum, include:

- How to build, run, and test the project
- Coding conventions and style references
- Branch naming and commit format
- Files the agent must never modify (secrets, vendor directories, generated files)

See [Agentic Engineering Workflow](./workflow.md#setting-up-your-source-of-truth) for a full breakdown of what to include and why.

### Component-Level Instructions

For monorepos or multi-component projects, place additional `CLAUDE.md` files in subdirectories. Claude Code merges these with the root instructions, allowing component-specific guidance without cluttering the top-level file.

---

## Key Features

### Plan Mode

Before generating any code, use plan mode to have Claude reason through the problem and propose an approach. Invoke it with the `--plan` flag or the `/plan` slash command:

```sh
claude --plan
```

In plan mode, Claude Code is read-only — it will not write or modify files. Review the proposed approach and approve it before switching to implementation. This is one of the most effective ways to catch architectural issues before they become code.

### Extended Thinking

For complex or ambiguous problems, ask Claude to think through the problem before responding:

> "Think carefully about the trade-offs here before proposing an approach."

This produces more considered output on design questions, security boundaries, and architectural decisions.

### MCP Servers

Model Context Protocol (MCP) is a standard interface for connecting AI agents to external tools and data sources — think of it as "USB-C for AI integrations." Instead of custom one-off integrations, MCP servers expose a structured API that Claude Code can call: read a GitHub issue, run a browser action, query a database, or call an internal service.

**Concrete example — Playwright MCP for end-to-end tests:**

The Playwright MCP server gives Claude Code a live browser it can control. Rather than writing E2E tests from static code, Claude can navigate your app, observe real DOM state, and generate test assertions against actual behavior.

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp"]
    }
  }
}
```

Once configured, you can prompt: *"Open the registration flow in the browser, complete it with test data, and write a Playwright test that captures this path."*

**Configuring MCP servers:**

Add MCP server definitions to Claude Code's settings file at `~/.claude/settings.json`. For project-specific servers that your whole team should use, document the configuration in your `CLAUDE.md`:

```markdown
## MCP Servers
- Playwright: browser automation for E2E test generation (see ~/.claude/settings.json)
- GitHub: issue and PR management — requires GITHUB_PERSONAL_ACCESS_TOKEN
```

**Other useful integrations:**

- **GitHub / Azure DevOps** — Read issues, create pull requests, and manage work items without leaving Claude Code
- **Browser automation** — Give Claude "eyes" for verifying UI behavior in real time during implementation
- **Custom APIs** — Expose internal services (e.g., the Azure Resource Manager or your project management API)

A registry of available MCP servers is maintained at the [MCP Marketplace](https://modelcontextprotocol.io).

### Git Worktrees for Parallel Sessions

Run Claude Code on multiple independent tasks simultaneously by isolating each to its own Git worktree:

```sh
# Create an isolated working copy on a feature branch
git worktree add ../project-feature-x feature/feature-x

# Open Claude Code in that directory
cd ../project-feature-x && claude
```

Each session operates in a separate directory with its own branch, preventing conflicts between concurrent agent runs.

---

## Prompting Patterns

### Decompose Before You Generate

Avoid large, vague prompts. Instead of:

> "Build the user authentication system."

Break it into discrete tasks:

> "Create a `POST /auth/register` endpoint that validates the email format and hashes the password with bcrypt. Do not implement the login endpoint yet."

Small, scoped prompts produce reviewable diffs and are easier to course-correct.

### Write the Test First

Define what "done" means before asking Claude to implement it:

1. Ask Claude to write a failing test that captures the acceptance criteria
2. Review and approve the test
3. Ask Claude to implement until the test passes
4. Review the diff

This TDD loop anchors AI output to a verifiable definition of correct behavior rather than to whatever happens to run.

### Iterate in Small Steps

After each implementation step:

- Read the diff before approving
- Run the tests
- Confirm the behavior manually if there is a UI component
- Then prompt for the next step

Do not let the agent run multiple steps ahead without verification. The review bottleneck is the point of control.

### Managing Context in Long Sessions

In long sessions, agents can "drift" — forgetting earlier constraints or repeating decisions you already made. To prevent this:

- Keep your `CLAUDE.md` up to date with decisions made during the session
- Periodically re-anchor the session: "Refer to `CLAUDE.md` before proceeding."
- Use separate sessions (and worktrees) for unrelated tasks rather than switching context mid-session

---

## Common Use Cases

Beyond autonomous feature implementation, Claude Code handles a wide range of day-to-day tasks:

- **Code completion and generation** — Describe what a function should do; Claude writes it
- **Explain code** — Ask Claude to explain a complex block in plain language
- **Write and generate tests** — Unit tests, edge cases, and test data setup
- **Debug** — Paste error output; Claude analyzes and proposes a fix
- **Write documentation** — Docstrings, README sections, architecture notes
- **Build SQL indexes** — Provide a query; Claude suggests a covering index
- **Write regular expressions** — Describe the pattern with sample input and expected output
- **Refactor** — Ask Claude to improve readability or performance of a specific block
- **Sweep dependency updates** — Ask Claude to update dependencies and fix resulting test failures iteratively

---

## Attributing AI-Assisted Code

When a commit consists primarily of AI-generated code, record this in the commit metadata using [Git trailers](https://git-scm.com/docs/git-interpret-trailers):

```sh
git commit --message "Implement feature" --trailer "Assistant-model: claude-sonnet-4-6"
```

Consider applying this when:

- More than 50% of the lines in the commit were AI-generated
- The AI provided the core logic or algorithmic approach
- Substantial code blocks were accepted from AI suggestions

For autonomous agents like the GitHub Copilot Coding Agent, attribution is handled automatically via `Co-authored-by`. The `Assistant-model` trailer is used for IDE-based assistance to distinguish assistance from co-authorship.

You can surface this attribution in the Git log:

```sh
git log --color --pretty=format:"%C(yellow)%h%C(reset) %C(blue)%an%C(reset) [%C(magenta)%(trailers:key=Assistant-model,valueonly=true,separator=%x2C)%C(reset)] %s"
```

```text
2100e6c Author [claude-sonnet-4-6] Add registration endpoint
7120221 Author [] Fix null check in user service
```

---

## Data and Privacy

Before using Claude Code on a project, confirm that your organization's policies permit AI tool use with that codebase:

- Does the project contain proprietary or regulated data?
- Are there contractual restrictions on code being sent outside the organization?
- Has the team reviewed Anthropic's data handling policies?

Claude Code sends code to Anthropic's API by default. For details, see [Anthropic's usage policies](https://www.anthropic.com/legal/usage-policy) and your organization's AI use guidelines.

!!! note
    If your project has a data restriction, do not use cloud-based AI tools against it without explicit approval. Raise the question with your project lead before starting.
