"""
Colored terminal log formatting for stdlib logging.

Loguru-identical design: dim timestamp, bold level badge, message colored by level.
Format mirrors loguru exactly: "YYYY-MM-DD HH:MM:SS.mmm | LEVEL    | name - message"

  DEBUG    → dark gray entire line (background noise, near-invisible)
  INFO     → bold white badge, plain message
  WARNING  → bold yellow badge + yellow message
  ERROR    → bold red badge + red message
  CRITICAL → bold red badge + bold red message

Color is ON by default when writing to a TTY.
Set NO_COLOR=1 or TERM=dumb to disable.
Set FORCE_COLOR=1 or LIMEN_LOG_COLOR=1 to force-enable (e.g. when piped to limen logs -f).

ColorLogFormatter: drop-in logging.Formatter subclass with ANSI color output.
colorize_log_line: post-hoc colorizer for existing log file lines.
wrap_ansi: flat ANSI wrapper, reusable for CLI output.

Usage:
    handler = logging.StreamHandler()
    handler.setFormatter(ColorLogFormatter())
    logging.basicConfig(handlers=[handler], level=logging.DEBUG)
"""

import logging
import os
import re
import sys

# ---------------------------------------------------------------------------
# ANSI codes
# ---------------------------------------------------------------------------


class ANSI:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    DARK_GRAY = "\033[90m"  # "bright black" — visually distinct from white
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


def _color_enabled(stream=None) -> bool:
    """Return True if ANSI colors should be emitted.

    Rules (in order):
      1. NO_COLOR env var set → always False
      2. TERM=dumb → always False
      3. FORCE_COLOR or LIMEN_LOG_COLOR env var set → always True
      4. stream.isatty() → follow TTY
      5. Default: False (safe for files/pipes)
    """
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("TERM") == "dumb":
        return False
    if os.environ.get("FORCE_COLOR") or os.environ.get("LIMEN_LOG_COLOR"):
        return True
    if stream is None:
        stream = sys.stderr
    return hasattr(stream, "isatty") and stream.isatty()


# ---------------------------------------------------------------------------
# Level styling: (badge_codes, message_codes)
# Both use component-level ANSI — never wrap the whole line.
# ---------------------------------------------------------------------------

_LevelStyle = tuple[tuple[str, ...], tuple[str, ...]]

LEVEL_STYLES: dict[str, _LevelStyle] = {
    "DEBUG": ((ANSI.DIM,), (ANSI.DIM,)),
    "INFO": ((ANSI.BOLD, ANSI.WHITE), ()),
    "WARNING": ((ANSI.BOLD, ANSI.YELLOW), (ANSI.YELLOW,)),
    "ERROR": ((ANSI.BOLD, ANSI.RED), (ANSI.RED,)),
    "CRITICAL": ((ANSI.BOLD, ANSI.RED), (ANSI.BOLD, ANSI.RED)),
}

# Legacy alias — tests/external code that imports LEVEL_COLORS still works
LEVEL_COLORS: dict[str, tuple[str, ...]] = {k: v[0] for k, v in LEVEL_STYLES.items()}

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

_DEFAULT_FMT = "%(asctime)s | %(levelname)-8s | %(name)s - %(message)s"
_DEFAULT_DATEFMT = "%Y-%m-%d %H:%M:%S"

# Matches: "2026-03-18 12:42:34 | INFO     | limen.x - msg"
# Also tolerates optional .NNN milliseconds for lines already on disk.
_LOG_LINE_RE = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?:\.\d+)?) \| (\w+)\s*\| ([^-]+) - (.*)$"
)
# Legacy bracket format: "2026-03-18 12:42:34[,NNN] [LEVEL   ] name: msg"
_LOG_LINE_RE_LEGACY = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})(?:,\d+)? \[(\w+)\s*\] ([^:]+): (.*)$"
)

# ---------------------------------------------------------------------------
# Public utilities
# ---------------------------------------------------------------------------


def wrap_ansi(text: str, *codes: str) -> str:
    """Wrap text with one or more ANSI codes, ending with RESET.

    Flat — never nests sequences. Each call produces exactly one RESET.
    Returns text unchanged if no codes given.
    """
    if not codes:
        return text
    return f"{''.join(codes)}{text}{ANSI.RESET}"


def _shorten_name(name: str, parts: int = 2) -> str:
    """Shorten dotted logger name to last N components.

    "limen.adapters.telegram.adapter" → "telegram.adapter"
    """
    segments = name.split(".")
    return ".".join(segments[-parts:]) if len(segments) > parts else name


def colorize_log_line(line: str) -> str:
    """Apply ANSI colors to a pre-formatted log file line.

    Matches pipe format: "YYYY-MM-DD HH:MM:SS.NNN | LEVEL    | name - message"
    Also matches legacy bracket format for backward compatibility.
    Non-matching lines (stack traces, blank lines) returned unchanged.
    Trailing newline preserved.
    """
    trail = "\n" if line.endswith("\n") else ""
    stripped = line.rstrip("\n")

    m = _LOG_LINE_RE.match(stripped)
    if not m:
        m = _LOG_LINE_RE_LEGACY.match(stripped)
    if not m:
        return line

    timestamp, level, name, message = m.groups()
    level = level.strip()
    name = name.strip()
    badge_codes, msg_codes = LEVEL_STYLES.get(level, ((ANSI.WHITE,), ()))

    return (
        f"{wrap_ansi(timestamp, ANSI.DIM)} "
        f"{wrap_ansi('|', ANSI.DIM)} "
        f"{wrap_ansi(f'{level:<8}', *badge_codes)} "
        f"{wrap_ansi('|', ANSI.DIM)} "
        f"{wrap_ansi(_shorten_name(name), ANSI.CYAN)} "
        f"{wrap_ansi('-', ANSI.DIM)} "
        f"{wrap_ansi(message, *msg_codes) if msg_codes else message}"
        f"{trail}"
    )


# ---------------------------------------------------------------------------
# ColorLogFormatter
# ---------------------------------------------------------------------------


class ColorLogFormatter(logging.Formatter):
    """logging.Formatter subclass with loguru-inspired terminal colors.

    Visual hierarchy:
      DEBUG    → dark gray (fades into background)
      INFO     → bold green badge, plain message
      WARNING  → bold yellow badge + yellow message
      ERROR    → bold red badge + red message
      CRITICAL → bold red everywhere

    Timestamp uses no milliseconds (%Y-%m-%d %H:%M:%S) by default.
    Logger name shortened to last 2 dotted components.

    Color detection order: NO_COLOR → TERM=dumb → FORCE_COLOR/LIMEN_LOG_COLOR → isatty.

    Args:
        force_color: None=auto-detect (default), True=always, False=never.
    """

    def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = None,
        style: str = "%",
        *,
        force_color: bool | None = None,
    ) -> None:
        super().__init__(
            fmt=fmt or _DEFAULT_FMT,
            datefmt=datefmt or _DEFAULT_DATEFMT,
            style=style,
        )
        self._force_color = force_color

    def _use_color(self) -> bool:
        if self._force_color is not None:
            return self._force_color
        return _color_enabled(sys.stderr)

    def format(self, record: logging.LogRecord) -> str:
        if not self._use_color():
            return super().format(record)

        # Call super() to resolve asctime, exc_info, stack_info
        plain = super().format(record)

        level_str = record.levelname
        badge_codes, msg_codes = LEVEL_STYLES.get(level_str, ((ANSI.WHITE,), ()))
        asctime = self.formatTime(record, self.datefmt)
        message = record.getMessage()
        short_name = _shorten_name(record.name)

        # Preserve exc_info / stack_info suffix appended by super()
        suffix = plain[plain.find(message) + len(message) :]

        return (
            f"{wrap_ansi(asctime, ANSI.DIM)} "
            f"{wrap_ansi('|', ANSI.DIM)} "
            f"{wrap_ansi(f'{level_str:<8}', *badge_codes)} "
            f"{wrap_ansi('|', ANSI.DIM)} "
            f"{wrap_ansi(short_name, ANSI.CYAN)} "
            f"{wrap_ansi('-', ANSI.DIM)} "
            f"{wrap_ansi(message, *msg_codes) if msg_codes else message}" + suffix
        )
