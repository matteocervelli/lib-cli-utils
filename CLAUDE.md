# adlimen-cli

Multi-language terminal color styling library — Python, Shell, and TypeScript.
Part of the `adlimen-*` library ecosystem (Apache-2.0, public).

## Structure

| Path                              | Purpose                                           |
| --------------------------------- | ------------------------------------------------- |
| `src/cli_utils/`                  | Python package (`from cli_utils import ColorStr`) |
| `src/shell/`                      | Bash functions (`source colorstr.sh`)             |
| `src/typescript/`                 | TypeScript/JS module (`import { ColorStr }`)      |
| `tests/`                          | Python pytest suite                               |
| `src/typescript/colorstr.test.ts` | TypeScript Jest suite                             |

## Development

### Python

```bash
pip install -e ".[dev]"
pytest                          # run tests
ruff check src/ tests/          # lint
ruff format src/ tests/         # format
mypy src/                       # type check
```

### TypeScript

```bash
cd src/typescript
npm install
npm test
```

## Conventions

- Python: ruff format + lint, mypy strict, pytest ≥80% coverage
- All three implementations must expose equivalent API surface
- Version must be kept in sync: `pyproject.toml` ↔ `src/typescript/package.json`
- `typing.Self` requires Python ≥3.11 — do not raise minimum

## API Surface (all languages)

Colors: `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`
Styles: `bold`, `dim`, `underline`
Backgrounds: `bg_red`/`bgRed`, `bg_green`/`bgGreen`, `bg_yellow`/`bgYellow`, `bg_blue`/`bgBlue`

## Known Limitation

Chaining wraps ANSI reset codes: `.red().bold()` → `\033[1m\033[91mtext\033[0m\033[0m`.
Reset code inside the inner wrap terminates early when displayed inline with other styled output.
Documented behavior — fix planned via `strip_ansi()` + single-pass ANSI builder.
