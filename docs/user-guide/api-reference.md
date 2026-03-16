# API Reference

Full method reference for `ColorStr` across all three language implementations.

## Python — `cli_utils.ColorStr`

`ColorStr` is a `str` subclass. All methods return a new `ColorStr` instance (chainable).

```python
from cli_utils import ColorStr
```

### Foreground Colors

| Method       | ANSI Code  | Example                   |
| ------------ | ---------- | ------------------------- |
| `.red()`     | `\033[91m` | `ColorStr("x").red()`     |
| `.green()`   | `\033[92m` | `ColorStr("x").green()`   |
| `.yellow()`  | `\033[93m` | `ColorStr("x").yellow()`  |
| `.blue()`    | `\033[94m` | `ColorStr("x").blue()`    |
| `.magenta()` | `\033[95m` | `ColorStr("x").magenta()` |
| `.cyan()`    | `\033[96m` | `ColorStr("x").cyan()`    |
| `.white()`   | `\033[97m` | `ColorStr("x").white()`   |

### Styles

| Method         | ANSI Code | Example                     |
| -------------- | --------- | --------------------------- |
| `.bold()`      | `\033[1m` | `ColorStr("x").bold()`      |
| `.dim()`       | `\033[2m` | `ColorStr("x").dim()`       |
| `.underline()` | `\033[4m` | `ColorStr("x").underline()` |

### Background Colors

| Method         | ANSI Code  | Example                     |
| -------------- | ---------- | --------------------------- |
| `.bg_red()`    | `\033[41m` | `ColorStr("x").bg_red()`    |
| `.bg_green()`  | `\033[42m` | `ColorStr("x").bg_green()`  |
| `.bg_yellow()` | `\033[43m` | `ColorStr("x").bg_yellow()` |
| `.bg_blue()`   | `\033[44m` | `ColorStr("x").bg_blue()`   |

---

## Shell — `src/shell/colorstr.sh`

Functions write directly to stdout via `echo -e`. No chaining — call directly or embed via `$(...)` when composing with other output.

```bash
source /path/to/colorstr.sh
```

### Foreground Colors

| Function               | Usage                 |
| ---------------------- | --------------------- |
| `color_red "text"`     | `color_red "Error"`   |
| `color_green "text"`   | `color_green "OK"`    |
| `color_yellow "text"`  | `color_yellow "Warn"` |
| `color_blue "text"`    | `color_blue "Info"`   |
| `color_magenta "text"` | `color_magenta "x"`   |
| `color_cyan "text"`    | `color_cyan "x"`      |
| `color_white "text"`   | `color_white "x"`     |

### Styles

| Function                 | Usage                    |
| ------------------------ | ------------------------ |
| `color_bold "text"`      | `color_bold "Title"`     |
| `color_dim "text"`       | `color_dim "hint"`       |
| `color_underline "text"` | `color_underline "link"` |

### Background Colors

| Function                 | Usage                    |
| ------------------------ | ------------------------ |
| `color_bg_red "text"`    | `color_bg_red "ERROR"`   |
| `color_bg_green "text"`  | `color_bg_green "OK"`    |
| `color_bg_yellow "text"` | `color_bg_yellow "WARN"` |
| `color_bg_blue "text"`   | `color_bg_blue "INFO"`   |

---

## TypeScript — `ColorStr`

Not a string subclass — call `.toString()` to get the styled string.

```typescript
import { ColorStr } from "cli-utils";
// or: import ColorStr from 'cli-utils';
```

### Foreground Colors

| Method       | ANSI Code  |
| ------------ | ---------- |
| `.red()`     | `\x1b[91m` |
| `.green()`   | `\x1b[92m` |
| `.yellow()`  | `\x1b[93m` |
| `.blue()`    | `\x1b[94m` |
| `.magenta()` | `\x1b[95m` |
| `.cyan()`    | `\x1b[96m` |
| `.white()`   | `\x1b[97m` |

### Styles

| Method         | ANSI Code |
| -------------- | --------- |
| `.bold()`      | `\x1b[1m` |
| `.dim()`       | `\x1b[2m` |
| `.underline()` | `\x1b[4m` |

### Background Colors

| Method        | ANSI Code  |
| ------------- | ---------- |
| `.bgRed()`    | `\x1b[41m` |
| `.bgGreen()`  | `\x1b[42m` |
| `.bgYellow()` | `\x1b[43m` |
| `.bgBlue()`   | `\x1b[44m` |

### `.toString()`

Required to extract the styled string from a `ColorStr` instance:

```typescript
const msg = new ColorStr("Done").green().bold().toString();
console.log(msg);
```
