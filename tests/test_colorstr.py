"""Tests for cli_utils.ColorStr."""

import pytest

from cli_utils import ColorStr

# --- Foreground colors ---


@pytest.mark.parametrize(
    "method,code",
    [
        ("red", "91"),
        ("green", "92"),
        ("yellow", "93"),
        ("blue", "94"),
        ("magenta", "95"),
        ("cyan", "96"),
        ("white", "97"),
    ],
)
def test_foreground_color(method: str, code: str) -> None:
    result = str(getattr(ColorStr("hello"), method)())
    assert f"\033[{code}m" in result
    assert "hello" in result
    assert "\033[0m" in result


# --- Styles ---


@pytest.mark.parametrize(
    "method,code",
    [
        ("bold", "1"),
        ("dim", "2"),
        ("underline", "4"),
    ],
)
def test_style(method: str, code: str) -> None:
    result = str(getattr(ColorStr("hello"), method)())
    assert f"\033[{code}m" in result
    assert "hello" in result


# --- Background colors ---


@pytest.mark.parametrize(
    "method,code",
    [
        ("bg_red", "41"),
        ("bg_green", "42"),
        ("bg_yellow", "43"),
        ("bg_blue", "44"),
    ],
)
def test_background_color(method: str, code: str) -> None:
    result = str(getattr(ColorStr("hello"), method)())
    assert f"\033[{code}m" in result
    assert "hello" in result


# --- Type behavior ---


def test_colorstr_is_str_subclass() -> None:
    cs = ColorStr("test")
    assert isinstance(cs, str)


def test_methods_return_colorstr() -> None:
    cs = ColorStr("test")
    assert isinstance(cs.red(), ColorStr)
    assert isinstance(cs.bold(), ColorStr)
    assert isinstance(cs.bg_red(), ColorStr)


def test_plain_text_unchanged() -> None:
    cs = ColorStr("hello")
    assert str(cs) == "hello"


# --- Chaining ---


def test_chaining_preserves_text() -> None:
    result = str(ColorStr("hello").red().bold())
    assert "hello" in result


def test_chaining_outermost_wraps_inner() -> None:
    # bold() is called last → its escape code is outermost
    result = str(ColorStr("hello").red().bold())
    assert result.startswith("\033[1m")
    assert "\033[91m" in result


def test_chaining_returns_colorstr() -> None:
    cs = ColorStr("x").red().bold().underline()
    assert isinstance(cs, ColorStr)
