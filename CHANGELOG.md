# Changelog

## 0.2.5

### Fixes
- `plumb sync` now correctly expands directory `spec_paths` (e.g. `specs/`) the same way `parse_spec_files` does, preventing silent decision/spec drift.
- DuckDB failures in `read_all_decisions` now log a warning instead of silently returning an empty list. Dependency pinned to `duckdb>=1.0`.

### Features
- Secret redaction: obvious API keys, tokens, and private keys are stripped from transcript and diff text before it is sent to the LLM.
- Pre-commit hook bypass: set `PLUMB_SKIP_HOOK=1` to skip analysis and allow the commit.
- Claude Code CLI fallback: when using an Anthropic model without an API key, Plumb automatically routes inference through the `claude` CLI if it is available.

### Docs
- Fixed "Triangle" typo in README.
- Added venv install recommendation (especially for macOS / PEP 668).
- Documented privacy surface and hook bypass.
