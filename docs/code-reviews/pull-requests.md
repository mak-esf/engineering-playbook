# Pull Requests & Code Reviews

## Why Code Reviews

Peer code reviews on every pull request are a core engineering practice. Code review is a way to have a conversation about the code where participants will:

- **Improve code quality** by identifying and removing defects before they can be introduced into shared code branches.
- **Learn and grow** by getting exposed to unfamiliar design patterns or languages, and breaking bad habits.
- **Build shared understanding** between developers over the project's code.

---

## Pull Requests

Changes to any main codebase must be done using pull requests (PR).

Pull requests enable:

- Code inspection and review
- Running automated qualification of the code (linters, compilation, unit tests, integration tests)

The requirements of pull requests can and should be enforced by policies in your version control system.

## General Process

1. Implement changes based on the well-defined description and acceptance criteria of the task at hand
1. Before creating a new pull request:
    - Make sure the code conforms with the agreed coding conventions (partially automated using linters)
    - Ensure the code compiles and runs without errors or warnings
    - Write and/or update tests to cover the changes and make sure all new and existing tests pass
    - Write and/or update the documentation to match the changes
1. Create and submit a new pull request
1. Follow the code review process to merge the changes to the main codebase

## Size Guidance

Always aim to keep pull requests small. Small PRs:

- Are easier to review
- Are easier to deploy (aligned with release fast and release often)
- Minimize possible conflicts and stale PRs

Keep PRs focused around a functional feature, optimization, or code readability concern. Start small — it is easier to create a small PR from the start than to break up a bigger one.

## Pull Request Description

Well written PR descriptions help maintain a clean, well-structured change history. A widely used specification is [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/):

```txt
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

Common `<type>` values: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`.

---

## Author Checklist

When creating a PR:

- [ ] Give the PR a descriptive title (one short sentence describing what the PR is about)
- [ ] Write a proper description that shows the reviewer what has been changed and why
- [ ] Link the corresponding work item/task to the PR
- [ ] Add one or more reviewers — ideally someone with expertise in the project or language, plus someone less familiar to verify readability
- [ ] In code-with projects, include reviewers from both organizations for knowledge transfer
- [ ] If the PR is large, add inline code comments explaining the goal of key code blocks
- [ ] Resolve all review comments: either make the requested change, or mark as "won't fix" with clear reasoning; if the change is out of scope, create a new work item
- [ ] If you don't understand a comment, ask questions in the review itself (not in a private chat)

---

## Reviewer Checklist

Human reviewers should focus on architectural and functional correctness (linters handle style). Key areas:

### Design Pass

- [ ] Does the PR description make sense?
- [ ] Do all the changes logically fit in this PR, or are there unrelated changes?
- [ ] Are there updates to README or docs if the change affects how users build/use the code?
- [ ] For user-facing changes: is there a screenshot/GIF explaining the functionality?
- [ ] Do the interactions of the various pieces of code make sense?
- [ ] Does the code recognize and incorporate existing architectural patterns?

### Code Quality Pass

- [ ] Are functions too complex? Is the single responsibility principle followed?
- [ ] Did the developer pick good names for functions and variables?
- [ ] Are errors handled gracefully and explicitly where necessary?
- [ ] Is there any parallel programming that could cause race conditions?
- [ ] Are there security flaws? Does any variable name reveal customer-specific or PII data?
- [ ] Is PII and EUII treated correctly? Are we logging any PII information?

### Tests

- [ ] Tests are committed in the same PR as the code ("I'll add tests next" is not acceptable)
- [ ] Test assumptions are sensible and edge cases are handled
- [ ] Tests can be used to understand the changes (consider reading tests first)

### Reviewer Etiquette

- Be positive — encourage good practices, acknowledge good work
- Prefix minor polish comments with "Nit:"
- Use "we" or "this line" rather than "you" — code reviews are not personal
- Prefer asking questions over making statements; there may be a good reason for an author's approach
- If a few back-and-forth comments don't resolve a disagreement, have a quick call

---

## Resources

- [Google's Engineering Practices: How to do a code review](https://google.github.io/eng-practices/review/reviewer/)
- [Writing a great pull request description](https://www.pullrequest.com/blog/writing-a-great-pull-request-description/)
- [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)
- [Google approach to PR size](https://google.github.io/eng-practices/review/developer/small-cls.html)
