from fractions import Fraction
from typing import Union, List

class Angle:
    """
    Represents an angle in degrees as a fraction.
    Provides utilities for addition, subtraction, and fraction simplification.
    """
    def __init__(self, value: Union[int, Fraction]):
        if isinstance(value, int):
            self.value = Fraction(value, 1)
        elif isinstance(value, Fraction):
            self.value = value
        else:
            raise TypeError("Angle value must be int or Fraction")

    def __add__(self, other: "Angle") -> "Angle":
        return Angle(self.value + other.value)

    def __sub__(self, other: "Angle") -> "Angle":
        return Angle(self.value - other.value)

    def __truediv__(self, other: Union[int, Fraction]) -> "Angle":
        if isinstance(other, int):
            return Angle(self.value / other)
        elif isinstance(other, Fraction):
            return Angle(self.value / other)
        else:
            raise TypeError("Division must be by int or Fraction")

    def __str__(self) -> str:
        num = self.value.numerator
        den = self.value.denominator
        if den == 1:
            return str(num)
        else:
            return f"{num}/{den}"

    def is_integer(self) -> bool:
        return self.value.denominator == 1

class DirectionNode:
    """
    Abstract base class for direction nodes.
    """
    def angle(self) -> Angle:
        raise NotImplementedError()

    def level(self) -> int:
        """
        The sum of occurrences of 'north' and 'west' down to this node.
        Used to calculate the division factor in angle adjustment.
        """
        raise NotImplementedError()

class BaseDirection(DirectionNode):
    """
    Represents the base directions: 'north' or 'west'.
    """
    def __init__(self, base: str):
        if base not in {"north", "west"}:
            raise ValueError(f"Invalid base direction: {base}")
        self.base = base

    def angle(self) -> Angle:
        if self.base == "north":
            return Angle(0)
        else:
            return Angle(90)

    def level(self) -> int:
        # Base direction count is 1
        return 1

class CompositeDirection(DirectionNode):
    """
    Represents a direction formed by prefixing 'north' or 'west' to another direction.
    """
    def __init__(self, prefix: str, sub_direction: DirectionNode):
        if prefix not in {"north", "west"}:
            raise ValueError(f"Invalid prefix direction: {prefix}")
        self.prefix = prefix
        self.sub_direction = sub_direction

    def angle(self) -> Angle:
        base_angle = self.sub_direction.angle()
        n = self.sub_direction.level() + 1
        adjustment = Angle(Fraction(90, 2 ** n))
        if self.prefix == "north":
            return base_angle - adjustment
        else:  # prefix == "west"
            return base_angle + adjustment

    def level(self) -> int:
        return self.sub_direction.level() + 1

class DirectionParser:
    """
    Parses a direction string composed of concatenated 'north' and 'west' words into a DirectionNode tree.
    """

    # Words considered in the input:
    DIRECTIONS = ("north", "west")

    def __init__(self, s: str):
        self.s = s
        self.index = 0
        self.length = len(s)

    def parse(self) -> DirectionNode:
        # The direction string is the concatenation of 'north' and 'west' words.
        # We parse from left to right greedily.
        tokens = self.tokenize()
        # Build a tree from right to left, because angle calculation depends on nested prefixes.
        # For example: "northnorthwest" => tokens = ['north', 'north', 'west']
        # We represent as CompositeDirection('north', CompositeDirection('north', BaseDirection('west')))
        node: DirectionNode = BaseDirection(tokens[-1])
        for prefix in reversed(tokens[:-1]):
            node = CompositeDirection(prefix, node)
        return node

    def tokenize(self) -> List[str]:
        """
        Tokenize input string into a list of 'north' and 'west'.
        Assumes the string is valid and can only be formed by these concatenations.
        """
        tokens = []
        i = 0
        while i < self.length:
            # Try to match "north" or "west"
            if self.s.startswith("north", i):
                tokens.append("north")
                i += 5
            elif self.s.startswith("west", i):
                tokens.append("west")
                i += 4
            else:
                raise ValueError(f"Invalid direction token at position {i} in {self.s}")
        return tokens

def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if line == "#":
            break
        parser = DirectionParser(line)
        direction_tree = parser.parse()
        angle = direction_tree.angle()
        print(str(angle))

if __name__ == "__main__":
    main()