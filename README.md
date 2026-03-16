# adlimen-cli

Terminal color styling utilities with chainable methods.

## Installation

### Python

```bash
pip install -e /path/to/adlimen-cli
```

### Shell

```bash
source /path/to/adlimen-cli/src/shell/colorstr.sh
```

### TypeScript/JavaScript

```bash
npm install /path/to/adlimen-cli/src/typescript
```

## Usage

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

### TypeScript/JavaScript

```typescript
import { ColorStr } from "adlimen-cli";

console.log(new ColorStr("Error").red().bold().toString());
console.log(new ColorStr("Success").green().toString());
```

## Support

If you find this useful, [buy me a coffee](https://adli.men/coffee).
