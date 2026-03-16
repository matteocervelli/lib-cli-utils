# Getting Started

adlimen-cli provides terminal color styling utilities for Python, Shell (Bash), and TypeScript.
All three implementations expose the same API surface via the `ColorStr` class / functions.

## Installation

### Python

```bash
pip install -e /path/to/adlimen-cli
```

Requires Python ≥ 3.11 (`typing.Self` dependency).

### Shell

```bash
source /path/to/adlimen-cli/src/shell/colorstr.sh
```

Add to your `.bashrc` / `.zshrc` for persistent availability.

### TypeScript / JavaScript

```bash
npm install /path/to/adlimen-cli/src/typescript
```

## Basic Usage

### Python

```python
from cli_utils import ColorStr

print(ColorStr("Error").red().bold())
print(ColorStr("Success").green())
print(ColorStr("Warning").yellow().underline())
```

### Shell

```bash
echo -e "$(color_red "Error")"
echo -e "$(color_green "Success")"
echo -e "$(color_bold "$(color_yellow "Warning")")"
```

### TypeScript

```typescript
import { ColorStr } from "adlimen-cli";

console.log(new ColorStr("Error").red().bold().toString());
console.log(new ColorStr("Success").green().toString());
console.log(new ColorStr("Warning").yellow().underline().toString());
```

## Known Limitation

Chaining wraps ANSI reset codes — `.red().bold()` produces nested escape sequences.
See [Chaining Limitation](guides/chaining-limitation.md) for details and workarounds.
