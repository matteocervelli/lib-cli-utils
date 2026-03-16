import { ColorStr } from "./colorstr";

describe("ColorStr", () => {
  describe("foreground colors", () => {
    test("red wraps with ANSI 91", () => {
      const result = new ColorStr("hello").red().toString();
      expect(result).toContain("\x1b[91m");
      expect(result).toContain("hello");
      expect(result).toContain("\x1b[0m");
    });

    test("green wraps with ANSI 92", () => {
      const result = new ColorStr("hello").green().toString();
      expect(result).toContain("\x1b[92m");
    });

    test("yellow wraps with ANSI 93", () => {
      expect(new ColorStr("x").yellow().toString()).toContain("\x1b[93m");
    });

    test("blue wraps with ANSI 94", () => {
      expect(new ColorStr("x").blue().toString()).toContain("\x1b[94m");
    });

    test("magenta wraps with ANSI 95", () => {
      expect(new ColorStr("x").magenta().toString()).toContain("\x1b[95m");
    });

    test("cyan wraps with ANSI 96", () => {
      expect(new ColorStr("x").cyan().toString()).toContain("\x1b[96m");
    });

    test("white wraps with ANSI 97", () => {
      expect(new ColorStr("x").white().toString()).toContain("\x1b[97m");
    });
  });

  describe("styles", () => {
    test("bold wraps with ANSI 1", () => {
      const result = new ColorStr("hello").bold().toString();
      expect(result).toContain("\x1b[1m");
      expect(result).toContain("hello");
    });

    test("dim wraps with ANSI 2", () => {
      expect(new ColorStr("x").dim().toString()).toContain("\x1b[2m");
    });

    test("underline wraps with ANSI 4", () => {
      expect(new ColorStr("x").underline().toString()).toContain("\x1b[4m");
    });
  });

  describe("background colors", () => {
    test("bgRed wraps with ANSI 41", () => {
      expect(new ColorStr("x").bgRed().toString()).toContain("\x1b[41m");
    });

    test("bgGreen wraps with ANSI 42", () => {
      expect(new ColorStr("x").bgGreen().toString()).toContain("\x1b[42m");
    });

    test("bgYellow wraps with ANSI 43", () => {
      expect(new ColorStr("x").bgYellow().toString()).toContain("\x1b[43m");
    });

    test("bgBlue wraps with ANSI 44", () => {
      expect(new ColorStr("x").bgBlue().toString()).toContain("\x1b[44m");
    });
  });

  describe("chaining", () => {
    test("chaining preserves original text", () => {
      const result = new ColorStr("hello").red().bold().toString();
      expect(result).toContain("hello");
    });

    test("chaining applies outer wrapper last", () => {
      const result = new ColorStr("hello").red().bold().toString();
      // bold is outermost — starts with bold code
      expect(result.startsWith("\x1b[1m")).toBe(true);
    });

    test("returns ColorStr instance for chaining", () => {
      const cs = new ColorStr("x");
      expect(cs.red()).toBeInstanceOf(ColorStr);
    });
  });

  describe("toString", () => {
    test("plain text unchanged", () => {
      expect(new ColorStr("hello").toString()).toBe("hello");
    });
  });
});
