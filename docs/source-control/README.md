# Source Control

There are many options when working with Source Control. In [ESF Engineering](../ESF-engineering.md) we use [AzureDevOps](https://azure.microsoft.com/en-us/services/devops/) for private repositories and [GitHub](https://github.com/) for public repositories.

## Goal

- Follow industry best practice to work in geo-distributed teams which encourage contributions from all across ESF Engineering as well as the broader OSS community
- Improve code quality by enforcing reviews before merging into main branches
- Improve traceability of features and fixes through a clean commit history

## General Guidance

Consistency is important, so agree to the approach as a team before starting to code. Treat this as a design decision and document it in the team's [Working Agreement](../agile-development/team-agreements/working-agreement.md).

## Creating a New Repository

When creating a new repository, the team should at least:

- Agree on the **branch**, **release** and **merge strategy**
- Lock the default branch and merge using [pull requests (PRs)](../code-reviews/pull-requests.md)
- Agree on branch naming (see [Branch Naming](#branch-naming) below)
- Establish branch/PR policies
- For public repositories the default branch should contain: LICENSE, README.md, contributing.md

## Contributing to an Existing Repository

When working on an existing project, `git clone` the repository and ensure you understand the team's branch, merge and release strategy (e.g. through the project's CONTRIBUTING.md file).

---

## Branch Naming

When contributing to existing projects, look for and stick with the agreed branch naming convention. For new projects, agree on the convention at project start.

Recommended convention:

```sh
<user alias>/[feature|bug|hotfix]/<work item ID>_<title>
```

Example:

```sh
dickinson/feature/271_add_more_cowbell
```

Focus on simplicity and reducing ambiguity. A good branch naming strategy allows the team to understand the purpose and ownership of each branch at a glance.

---

## Commit Best Practices

A commit combines changes into a logical unit. Consider the following:

- **Make small commits.** This makes changes easier to review, and if we need to revert, we lose less work. Consider splitting with `git add -p` if a commit includes more than one logical change.
- **Don't mix whitespace changes with functional code changes.**
- **Commit complete and well-tested code.** Never commit incomplete code.
- **Write good commit messages.** Explain *why* the change is necessary, not just what changed.

### Commit Message Structure

```
<subject line: max 50 characters>

<optional body: wrapped at 72 characters, explaining why>

<optional trailers: Co-authored-by, Reviewed-by, etc.>
```

A widely used convention is [Conventional Commits](https://www.conventionalcommits.org/), which also complements [SemVer](https://semver.org/):

```
feat(auth): add OAuth2 login support

Implements GitHub and Google OAuth2 providers to replace
the legacy username/password flow.
```

Common types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `ci`.

---

## Resources

- [Git](https://git-scm.com/)
- [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/)
- [GitHub - Removing sensitive data from a repository](https://help.github.com/articles/removing-sensitive-data-from-a-repository/)
- [Conventional Commits](https://www.conventionalcommits.org)
- [How to Write a Git Commit Message](https://cbea.ms/git-commit)
