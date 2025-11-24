/**
 * ColorStr - Terminal color styling with chainable methods.
 * Usage: new ColorStr("text").red().bold().toString()
 */

export class ColorStr {
  private value: string;

  constructor(text: string) {
    this.value = text;
  }

  // Foreground colors
  red(): ColorStr { return new ColorStr(`\x1b[91m${this.value}\x1b[0m`); }
  green(): ColorStr { return new ColorStr(`\x1b[92m${this.value}\x1b[0m`); }
  yellow(): ColorStr { return new ColorStr(`\x1b[93m${this.value}\x1b[0m`); }
  blue(): ColorStr { return new ColorStr(`\x1b[94m${this.value}\x1b[0m`); }
  magenta(): ColorStr { return new ColorStr(`\x1b[95m${this.value}\x1b[0m`); }
  cyan(): ColorStr { return new ColorStr(`\x1b[96m${this.value}\x1b[0m`); }
  white(): ColorStr { return new ColorStr(`\x1b[97m${this.value}\x1b[0m`); }

  // Styles
  bold(): ColorStr { return new ColorStr(`\x1b[1m${this.value}\x1b[0m`); }
  dim(): ColorStr { return new ColorStr(`\x1b[2m${this.value}\x1b[0m`); }
  underline(): ColorStr { return new ColorStr(`\x1b[4m${this.value}\x1b[0m`); }

  // Background colors
  bgRed(): ColorStr { return new ColorStr(`\x1b[41m${this.value}\x1b[0m`); }
  bgGreen(): ColorStr { return new ColorStr(`\x1b[42m${this.value}\x1b[0m`); }
  bgYellow(): ColorStr { return new ColorStr(`\x1b[43m${this.value}\x1b[0m`); }
  bgBlue(): ColorStr { return new ColorStr(`\x1b[44m${this.value}\x1b[0m`); }

  toString(): string { return this.value; }
}

export default ColorStr;
