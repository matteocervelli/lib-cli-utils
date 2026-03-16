# Roadmap

## Planned

- [ ] `strip_ansi()` — remove ANSI codes from a string (Python + TS + Shell)
- [ ] Single-pass ANSI builder to fix chaining reset-code collision
- [ ] `ColorStr.from_hex(color)` — 24-bit true-color support
- [ ] CI: GitHub Actions workflow (lint + test + type-check on push/PR)
- [ ] Shell: `color_strip()` function

## In Progress

- [ ] Test suite (Python pytest + TypeScript Jest)
- [ ] Tooling config (ruff, mypy, pytest)

## Released

### v0.1.0 — 2025-11-24

- Python `ColorStr` class with chainable ANSI methods
- Shell `color_*` functions
- TypeScript `ColorStr` class
