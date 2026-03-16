# Roadmap

## Planned

### v0.1.1

- [ ] CI: GitHub Actions workflow (lint + test + type-check on push/PR) — [#4](https://github.com/matteocervelli/lib-cli-utils/issues/4)

### v0.2.0

- [ ] `strip_ansi()` — remove ANSI codes from a string (Python + TS + Shell) — [#2](https://github.com/matteocervelli/lib-cli-utils/issues/2)
- [ ] `ColorStr.from_hex(color)` — 24-bit true-color support — [#3](https://github.com/matteocervelli/lib-cli-utils/issues/3)
- [ ] Single-pass ANSI builder to fix chaining reset-code collision — [#7](https://github.com/matteocervelli/lib-cli-utils/issues/7)
- [ ] Shell: `color_strip()` function — [#8](https://github.com/matteocervelli/lib-cli-utils/issues/8)

## Released

### v0.1.1 — upcoming

- pytest test suite for Python `ColorStr` (20 tests, 100% coverage)
- Jest test suite for TypeScript `ColorStr` (18 tests)
- Tooling config: ruff, mypy strict, pytest-cov in `pyproject.toml`; tsconfig.json
- Docs: `CLAUDE.md`, `CHANGELOG.md`, `ROADMAP.md`, `TECH-STACK.md`
- Fixes: package name, requires-python >=3.11, LICENSE year

### v0.1.0 — 2025-11-24

- Python `ColorStr` class with chainable ANSI methods
- Shell `color_*` functions
- TypeScript `ColorStr` class
