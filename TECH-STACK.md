# Tech Stack

## Languages

| Layer              | Technology | Version |
| ------------------ | ---------- | ------- |
| Python library     | Python     | ≥3.11   |
| Shell library      | Bash       | 3+      |
| TypeScript library | TypeScript | ^5.0    |

## Build

| Tool      | Purpose                    |
| --------- | -------------------------- |
| hatchling | Python wheel build backend |
| tsc       | TypeScript compilation     |

## Tooling (Python)

| Tool                | Purpose              |
| ------------------- | -------------------- |
| ruff                | Linting + formatting |
| mypy (strict)       | Type checking        |
| pytest + pytest-cov | Testing + coverage   |

## Tooling (TypeScript)

| Tool           | Purpose          |
| -------------- | ---------------- |
| jest + ts-jest | Testing          |
| @types/jest    | Type definitions |

## Dependencies

- **Python runtime**: zero — pure stdlib (`typing` only)
- **TypeScript runtime**: zero
- **Shell runtime**: zero — POSIX `echo` only
