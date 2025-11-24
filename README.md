# lib-cli-utils

Terminal color styling utilities with chainable methods.

## Installation

### Python

```bash
pip install -e /path/to/lib-cli-utils
```

### Shell

```bash
source /path/to/lib-cli-utils/src/shell/colorstr.sh
```

### TypeScript/JavaScript

```bash
npm install /path/to/lib-cli-utils/src/typescript
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
import { ColorStr } from 'cli-utils';

console.log(new ColorStr("Error").red().bold().toString());
console.log(new ColorStr("Success").green().toString());
```

## Support

If you find this useful, [buy me a coffee](https://adli.men/coffee).
