# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- pytest test suite for Python `ColorStr`
- Jest test suite for TypeScript `ColorStr`
- `[tool.ruff]`, `[tool.mypy]`, `[tool.pytest]` config in `pyproject.toml`
- `CLAUDE.md`, `CHANGELOG.md`, `ROADMAP.md`, `TECH-STACK.md`

## [0.1.0] - 2025-11-24

### Added

- `ColorStr` Python class — chainable ANSI color and style methods (`str` subclass)
- Shell `color_*` functions for Bash terminal styling
- TypeScript `ColorStr` class with equivalent API surface
- `py.typed` marker for mypy consumers
