# Chaining Limitation

## The Problem

Chaining color and style methods wraps ANSI reset codes inside each other.

For example, `.red().bold()` produces:

```
\033[1m\033[91mtext\033[0m\033[0m
```

The inner `\033[0m` (reset) terminates the red coloring before the bold's outer wrapper ends.
When this styled string is printed **inline with other styled output**, the reset can bleed into
adjacent text unexpectedly.

## When It Matters

This is only visible when the styled string is concatenated with other ANSI-styled strings:

```python
# Potentially incorrect: red resets before bold's context ends
label = ColorStr("ERROR").red().bold()
line = f"{label}: something happened"
print(line)
```

For standalone `print()` calls, the visual result is typically correct because the terminal
resets at end-of-line anyway.

## Workaround (Python)

Apply the outermost style last, and avoid mixing styles that conflict visually:

```python
# Workaround: apply color then style separately works for most terminals
print(ColorStr("Done").green())        # single style — always safe
print(ColorStr("Title").bold())        # single style — always safe
print(ColorStr("Warning").yellow())    # single style — always safe
```

If you receive an already-styled string from another source and need to apply different styles,
strip ANSI codes first to avoid compounding escape sequences:

```python
import re

def strip_ansi(text: str) -> str:
    return re.sub(r'\033\[[0-9;]*m', '', text)

# Use this when re-styling an already-colored string from an external source
already_styled = str(ColorStr("text").red())  # has ANSI codes
clean = strip_ansi(already_styled)            # remove existing ANSI
restyled = ColorStr(clean).bold()             # apply single style — safe
```

Note: `strip_ansi` does not fix chaining itself. `ColorStr(clean).red().bold()` still
produces the double-reset sequence. Use a single style method when possible.

## Planned Fix

A single-pass ANSI builder will replace the current wrap-on-each-method approach.
This is tracked in the roadmap under `v0.2.0`.

The fix will produce:

```
\033[1;91mtext\033[0m   # single open, single reset
```
