"""Tests for ColorLogFormatter and colorize_log_line."""

import logging
import sys
from unittest.mock import patch

import pytest

from cli_utils.log_formatter import (
    ANSI,
    LEVEL_COLORS,
    ColorLogFormatter,
    colorize_log_line,
    wrap_ansi,
)


# ---------------------------------------------------------------------------
# wrap_ansi
# ---------------------------------------------------------------------------


def test_wrap_ansi_single_code() -> None:
    result = wrap_ansi("hello", ANSI.GREEN)
    assert result == f"\033[92mhello\033[0m"


def test_wrap_ansi_multiple_codes() -> None:
    result = wrap_ansi("hello", ANSI.RED, ANSI.BOLD)
    assert result == f"\033[91m\033[1mhello\033[0m"


def test_wrap_ansi_no_nesting() -> None:
    """wrap_ansi must not re-wrap already-colored text with extra RESET sequences."""
    result = wrap_ansi("text", ANSI.DIM)
    # Exactly one RESET at end, not multiple
    assert result.count("\033[0m") == 1


def test_wrap_ansi_no_codes() -> None:
    result = wrap_ansi("plain")
    assert result == "plain"


# ---------------------------------------------------------------------------
# ColorLogFormatter — TTY auto-detection
# ---------------------------------------------------------------------------


def _make_record(level: int = logging.INFO, msg: str = "hello") -> logging.LogRecord:
    record = logging.LogRecord(
        name="limen.test",
        level=level,
        pathname="",
        lineno=0,
        msg=msg,
        args=(),
        exc_info=None,
    )
    return record


def test_format_plain_when_not_tty() -> None:
    formatter = ColorLogFormatter()
    with patch.object(sys.stderr, "isatty", return_value=False):
        result = formatter.format(_make_record())
    assert "\033[" not in result


def test_format_contains_ansi_when_tty() -> None:
    formatter = ColorLogFormatter()
    with patch.object(sys.stderr, "isatty", return_value=True):
        result = formatter.format(_make_record())
    assert "\033[" in result


def test_force_color_true_overrides_non_tty() -> None:
    formatter = ColorLogFormatter(force_color=True)
    with patch.object(sys.stderr, "isatty", return_value=False):
        result = formatter.format(_make_record())
    assert "\033[" in result


def test_force_color_false_overrides_tty() -> None:
    formatter = ColorLogFormatter(force_color=False)
    with patch.object(sys.stderr, "isatty", return_value=True):
        result = formatter.format(_make_record())
    assert "\033[" not in result


# ---------------------------------------------------------------------------
# ColorLogFormatter — level colors
# ---------------------------------------------------------------------------


LEVEL_CASES = [
    (logging.DEBUG, ANSI.DIM),  # DEBUG: all components dim, no CYAN
    (logging.INFO, ANSI.WHITE),  # loguru-identical: plain white badge
    (logging.WARNING, ANSI.YELLOW),
    (logging.ERROR, ANSI.RED),
    (logging.CRITICAL, ANSI.RED),
]


@pytest.mark.parametrize("level, expected_color", LEVEL_CASES)
def test_level_color_present_in_output(level: int, expected_color: str) -> None:
    formatter = ColorLogFormatter(force_color=True)
    result = formatter.format(_make_record(level=level))
    assert expected_color in result


def test_critical_has_bold() -> None:
    formatter = ColorLogFormatter(force_color=True)
    result = formatter.format(_make_record(level=logging.CRITICAL))
    assert ANSI.BOLD in result


def test_debug_has_dim() -> None:
    formatter = ColorLogFormatter(force_color=True)
    result = formatter.format(_make_record(level=logging.DEBUG))
    assert ANSI.DIM in result


# ---------------------------------------------------------------------------
# ColorLogFormatter — structure
# ---------------------------------------------------------------------------


def test_output_contains_logger_name() -> None:
    formatter = ColorLogFormatter(force_color=True)
    result = formatter.format(_make_record())
    assert "limen.test" in result


def test_output_contains_message() -> None:
    formatter = ColorLogFormatter(force_color=True)
    result = formatter.format(_make_record(msg="my message"))
    assert "my message" in result


def test_timestamp_is_dimmed() -> None:
    formatter = ColorLogFormatter(force_color=True)
    result = formatter.format(_make_record())
    # DIM code appears before the timestamp (which starts the line)
    assert result.startswith(ANSI.DIM)


def test_plain_format_matches_stdlib_default() -> None:
    """Non-TTY output must be identical when using the same format string."""
    from cli_utils.log_formatter import _DEFAULT_DATEFMT, _DEFAULT_FMT

    formatter = ColorLogFormatter(force_color=False)
    plain = logging.Formatter(_DEFAULT_FMT, datefmt=_DEFAULT_DATEFMT)
    record = _make_record()
    record.asctime = "2026-03-18 12:00:00"
    assert formatter.format(record) == plain.format(record)


# ---------------------------------------------------------------------------
# colorize_log_line
# ---------------------------------------------------------------------------


SAMPLE_LINE = "2026-03-18 12:42:34,783 [INFO] limen.agent.session: Starting"


def test_colorize_matching_line_adds_ansi() -> None:
    result = colorize_log_line(SAMPLE_LINE)
    assert "\033[" in result


def test_colorize_preserves_message_content() -> None:
    result = colorize_log_line(SAMPLE_LINE)
    assert "Starting" in result
    # Name is shortened to last 2 components
    assert "agent.session" in result
    # Milliseconds stripped from display (,783 removed)
    assert "2026-03-18 12:42:34" in result
    assert ",783" not in result


def test_colorize_preserves_trailing_newline() -> None:
    line = SAMPLE_LINE + "\n"
    result = colorize_log_line(line)
    assert result.endswith("\n")


def test_colorize_no_newline_stays_without() -> None:
    result = colorize_log_line(SAMPLE_LINE)  # no trailing \n
    assert not result.endswith("\n")


def test_colorize_non_matching_line_passthrough() -> None:
    line = "    at some traceback line"
    assert colorize_log_line(line) == line


def test_colorize_empty_line_passthrough() -> None:
    assert colorize_log_line("") == ""


@pytest.mark.parametrize(
    "level",
    ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
)
def test_colorize_all_levels(level: str) -> None:
    line = f"2026-03-18 12:00:00,000 [{level}] limen.x: msg"
    result = colorize_log_line(line)
    assert "\033[" in result
    assert "msg" in result


def test_colorize_info_has_white() -> None:
    line = "2026-03-18 12:00:00,000 [INFO] limen.x: msg"
    assert ANSI.WHITE in colorize_log_line(line)


def test_colorize_warning_has_yellow() -> None:
    line = "2026-03-18 12:00:00,000 [WARNING] limen.x: msg"
    assert ANSI.YELLOW in colorize_log_line(line)


def test_colorize_error_has_red() -> None:
    line = "2026-03-18 12:00:00,000 [ERROR] limen.x: msg"
    assert ANSI.RED in colorize_log_line(line)


# ---------------------------------------------------------------------------
# LEVEL_COLORS completeness
# ---------------------------------------------------------------------------


def test_level_colors_covers_all_stdlib_levels() -> None:
    for name in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
        assert name in LEVEL_COLORS, f"LEVEL_COLORS missing {name}"
