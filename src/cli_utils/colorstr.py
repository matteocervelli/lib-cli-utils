"""
ColorStr - Terminal color styling with chainable methods.

Provides ANSI escape code wrapping for terminal text coloring and styling.
Methods can be chained: ColorStr("text").red().bold()
"""

from typing import Self


class ColorStr(str):
    """
    String subclass with chainable terminal color and style methods.

    Each method wraps the string with ANSI escape codes and returns
    a new ColorStr instance for method chaining.
    """

    # Foreground colors (90-97 = bright variants)
    def red(self) -> Self:
        return self.__class__(f"\033[91m{self}\033[0m")

    def green(self) -> Self:
        return self.__class__(f"\033[92m{self}\033[0m")

    def yellow(self) -> Self:
        return self.__class__(f"\033[93m{self}\033[0m")

    def blue(self) -> Self:
        return self.__class__(f"\033[94m{self}\033[0m")

    def magenta(self) -> Self:
        return self.__class__(f"\033[95m{self}\033[0m")

    def cyan(self) -> Self:
        return self.__class__(f"\033[96m{self}\033[0m")

    def white(self) -> Self:
        return self.__class__(f"\033[97m{self}\033[0m")

    # Text styles
    def bold(self) -> Self:
        return self.__class__(f"\033[1m{self}\033[0m")

    def dim(self) -> Self:
        return self.__class__(f"\033[2m{self}\033[0m")

    def underline(self) -> Self:
        return self.__class__(f"\033[4m{self}\033[0m")

    # Background colors (40-47 = standard variants)
    def bg_red(self) -> Self:
        return self.__class__(f"\033[41m{self}\033[0m")

    def bg_green(self) -> Self:
        return self.__class__(f"\033[42m{self}\033[0m")

    def bg_yellow(self) -> Self:
        return self.__class__(f"\033[43m{self}\033[0m")

    def bg_blue(self) -> Self:
        return self.__class__(f"\033[44m{self}\033[0m")
