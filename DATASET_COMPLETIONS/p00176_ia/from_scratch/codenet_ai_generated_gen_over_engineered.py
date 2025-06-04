from abc import ABC, abstractmethod
from typing import List, Tuple


class Color(ABC):
    """Abstract base class representing a color with RGB components."""

    def __init__(self, name: str, r_hex: str, g_hex: str, b_hex: str) -> None:
        self.name = name
        self.r = self._hex_to_int(r_hex)
        self.g = self._hex_to_int(g_hex)
        self.b = self._hex_to_int(b_hex)

    @staticmethod
    def _hex_to_int(value: str) -> int:
        try:
            return int(value, 16)
        except ValueError:
            # If invalid hex, treat as 0 for robustness
            return 0

    def distance_to(self, r: int, g: int, b: int) -> int:
        """Calculate the squared Euclidean distance between this color and another RGB tuple."""
        return (self.r - r) ** 2 + (self.g - g) ** 2 + (self.b - b) ** 2

    @abstractmethod
    def description(self) -> str:
        ...

    def __str__(self) -> str:
        return self.name


class BasicColor(Color):
    """Concrete implementation for a basic color from the color table."""

    def description(self) -> str:
        # In case of extensions, provide description
        return f"BasicColor(name={self.name}, r={self.r}, g={self.g}, b={self.b})"


class ColorPalette:
    """Palette maintaining a list of reference colors."""

    def __init__(self) -> None:
        self._colors: List[Color] = []

    def add_color(self, color: Color) -> None:
        self._colors.append(color)

    def find_closest_color(self, r: int, g: int, b: int) -> Color:
        """Find the closest color from the palette to the given RGB."""
        # Minimal distance initialized with very large number
        min_dist = float('inf')
        closest_color = None
        for color in self._colors:
            dist = color.distance_to(r, g, b)
            if dist < min_dist:
                min_dist = dist
                closest_color = color
        return closest_color


class InputProcessor:
    """Process input lines and parse color codes."""

    def __init__(self, raw_input: List[str]) -> None:
        self.lines = raw_input

    @staticmethod
    def is_valid_color_code(code: str) -> bool:
        if len(code) != 7 or code[0] != '#':
            return False
        # Check if subsequent 6 characters are valid hex digits
        hex_part = code[1:]
        try:
            int(hex_part, 16)
            return True
        except ValueError:
            return False

    def parse_color_code(self, code: str) -> Tuple[int, int, int]:
        if self.is_valid_color_code(code):
            r = int(code[1:3], 16)
            g = int(code[3:5], 16)
            b = int(code[5:7], 16)
            return r, g, b
        # If invalid, fallback to white (255,255,255) per problem example
        return 255, 255, 255

    def extract_color_codes(self) -> List[str]:
        """Extract all input color codes until a line with single 0 is encountered."""
        result = []
        for line in self.lines:
            stripped = line.strip()
            if stripped == '0':
                break
            result.append(stripped)
        return result


class ColorMatcher:
    """Encapsulates the logic to match input colors to the closest palette colors."""

    def __init__(self, palette: ColorPalette) -> None:
        self.palette = palette

    def match(self, r: int, g: int, b: int) -> str:
        closest = self.palette.find_closest_color(r, g, b)
        return closest.name if closest else "unknown"


def main() -> None:
    import sys

    # Initialize color palette with given colors in specified order
    palette = ColorPalette()
    predefined_colors = [
        ("black", "00", "00", "00"),
        ("blue", "00", "00", "ff"),
        ("lime", "00", "ff", "00"),
        ("aqua", "00", "ff", "ff"),
        ("red", "ff", "00", "00"),
        ("fuchsia", "ff", "00", "ff"),
        ("yellow", "ff", "ff", "00"),
        ("white", "ff", "ff", "ff"),
    ]
    for name, r, g, b in predefined_colors:
        palette.add_color(BasicColor(name, r, g, b))

    input_lines = [line.rstrip('\n') for line in sys.stdin]
    processor = InputProcessor(input_lines)
    color_codes = processor.extract_color_codes()

    matcher = ColorMatcher(palette)

    for code in color_codes:
        r, g, b = processor.parse_color_code(code)
        print(matcher.match(r, g, b))


if __name__ == "__main__":
    main()