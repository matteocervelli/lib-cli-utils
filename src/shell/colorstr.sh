#!/bin/bash
# colorstr.sh - Terminal color styling functions
# Usage: echo -e "$(color_red "text")"

# Foreground colors
color_red()     { echo -e "\033[91m$1\033[0m"; }
color_green()   { echo -e "\033[92m$1\033[0m"; }
color_yellow()  { echo -e "\033[93m$1\033[0m"; }
color_blue()    { echo -e "\033[94m$1\033[0m"; }
color_magenta() { echo -e "\033[95m$1\033[0m"; }
color_cyan()    { echo -e "\033[96m$1\033[0m"; }
color_white()   { echo -e "\033[97m$1\033[0m"; }

# Styles
color_bold()      { echo -e "\033[1m$1\033[0m"; }
color_dim()       { echo -e "\033[2m$1\033[0m"; }
color_underline() { echo -e "\033[4m$1\033[0m"; }

# Background colors
color_bg_red()    { echo -e "\033[41m$1\033[0m"; }
color_bg_green()  { echo -e "\033[42m$1\033[0m"; }
color_bg_yellow() { echo -e "\033[43m$1\033[0m"; }
color_bg_blue()   { echo -e "\033[44m$1\033[0m"; }
