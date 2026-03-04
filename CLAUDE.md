# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **documentation-only repository** — the ESF Engineering Playbook, a static site built with MkDocs and published to GitHub Pages. All content lives in `/docs/` as Markdown files.

## Development Commands

A `uv`-managed virtual environment is used. The `.venv` is at the project root.

```bash
# Create virtual environment and install dependencies
uv venv && uv pip install -r requirements-docs.txt

# Serve locally with live reload (http://localhost:8000)
uv run mkdocs serve

# Build static site to /site/
uv run mkdocs build
```

## Linting

Linting runs automatically via GitHub Actions (MegaLinter) on push/PR to `main`. Active linters:
- `MARKDOWN_MARKDOWNLINT` — rules in `.markdownlint.json`
- `SPELL_CSPELL` — custom word list in `.cspell.json`
- `SPELL_LYCHEE` — link validation (config in `lychee.toml`)
- `YAML_PRETTIER` and `YAML_YAMLLINT`
- `ACTION_ACTIONLINT`

To run MegaLinter locally: `npx mega-linter-runner`

## Architecture

- **`/docs/`** — All Markdown content, organized by topic (agile, testing, CI-CD, code-reviews, security, etc.)
- **`/docs/.pages`** files control navigation order via `mkdocs-awesome-pages-plugin`
- **`/mkdocs-overrides/`** — Custom Material theme overrides (partials, assets)
- **`/site/`** — Generated output, not committed
- **`mkdocs.yml`** — Site config: theme, plugins, nav, markdown extensions
- **`.github/workflows/`** — Two workflows: `mega-linter.yml` (quality checks) and `mkdocs.yml` (build + deploy to GitHub Pages)

## Contributing

- Branch naming: `<github-alias>/<title>`
- PRs require 2 reviewers
- Spell checker uses `.cspell.json` — add new technical terms there rather than marking them as errors
- Markdown admonitions (`!!! note`, `!!! warning`, etc.) are supported via `pymdownx` extensions
