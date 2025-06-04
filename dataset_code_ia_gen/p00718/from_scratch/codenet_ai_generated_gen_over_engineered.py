from abc import ABC, abstractmethod
from typing import Optional, List, Tuple


class MCXILetter(ABC):
    """Abstract base class representing one of the numeral letters with their multipliers."""

    _letter_order = ['m', 'c', 'x', 'i']
    _letter_values = {'m': 1000, 'c': 100, 'x': 10, 'i': 1}

    def __init__(self, count: int = 1):
        if not (1 <= count <= 9):
            raise ValueError(f"Invalid count {count}. Must be 1..9.")
        self.count = count

    @property
    @abstractmethod
    def letter(self) -> str:
        pass

    @property
    def value(self) -> int:
        return self.count * self._letter_values[self.letter]

    @classmethod
    def letter_index(cls, letter: str) -> int:
        return cls._letter_order.index(letter)

    def __str__(self):
        if self.count == 1:
            return self.letter
        else:
            return f"{self.count}{self.letter}"

    def __repr__(self):
        return f"{self.__class__.__name__}(count={self.count})"


class M(MCXILetter):
    @property
    def letter(self) -> str:
        return 'm'


class C(MCXILetter):
    @property
    def letter(self) -> str:
        return 'c'


class X(MCXILetter):
    @property
    def letter(self) -> str:
        return 'x'


class I(MCXILetter):
    @property
    def letter(self) -> str:
        return 'i'


_LETTER_CLASSES = {
    'm': M,
    'c': C,
    'x': X,
    'i': I,
}

class MCXIString:
    """Represents an MCXI-string as a sequence of letters, with parsing and arithmetic."""

    def __init__(self, letters: Optional[List[MCXILetter]] = None):
        # Letters are stored in order m,c,x,i; each at most once
        self.letters = letters if letters is not None else []

    @classmethod
    def parse(cls, s: str) -> "MCXIString":
        # Parsing must validate:
        # - letters appear in order m,c,x,i
        # - letters appear at most once
        # - digits 2..9 only as prefix to letter
        # - no '0', no '1' anywhere
        # - must not be empty
        if not s:
            raise ValueError("Empty string is not a valid MCXI-string")

        letters_found = set()
        last_letter_index = -1

        letters_instances: List[MCXILetter] = []

        pos = 0
        length = len(s)

        while pos < length:
            ch = s[pos]

            if ch in '23456789':
                # Digit prefix found, must be followed by letter
                count = int(ch)
                pos += 1
                if pos >= length:
                    raise ValueError("Digit prefix without following letter")
                letter_char = s[pos]
                pos += 1
                if letter_char not in _LETTER_CLASSES:
                    raise ValueError(f"Invalid letter '{letter_char}' after digit {ch}")

                letter_idx = MCXILetter.letter_index(letter_char)

                if letter_char in letters_found:
                    raise ValueError(f"Duplicate letter '{letter_char}'")
                if letter_idx <= last_letter_index:
                    raise ValueError(f"Letters out of order: {letter_char} after index {last_letter_index}")
                if count == 1:
                    # Explicitly forbid '1' digit prefix
                    raise ValueError("Prefix digit cannot be 1")

                letters_found.add(letter_char)
                last_letter_index = letter_idx

                letter_obj = _LETTER_CLASSES[letter_char](count)
                letters_instances.append(letter_obj)
            elif ch in _LETTER_CLASSES:
                # Single letter without digit prefix
                letter_char = ch
                pos += 1

                letter_idx = MCXILetter.letter_index(letter_char)
                if letter_char in letters_found:
                    raise ValueError(f"Duplicate letter '{letter_char}'")
                if letter_idx <= last_letter_index:
                    raise ValueError(f"Letters out of order: {letter_char} after index {last_letter_index}")

                letters_found.add(letter_char)
                last_letter_index = letter_idx

                letter_obj = _LETTER_CLASSES[letter_char](1)
                letters_instances.append(letter_obj)
            else:
                # Invalid character
                raise ValueError(f"Invalid character '{ch}' in MCXI-string")

        if len(letters_instances) == 0:
            raise ValueError("Empty MCXI-string")

        return cls(letters_instances)

    def to_value(self) -> int:
        return sum(letter.value for letter in self.letters)

    @classmethod
    def from_value(cls, val: int) -> "MCXIString":
        # val must be 1..9999
        if not (1 <= val <= 9999):
            raise ValueError(f"Value {val} out of range 1..9999")

        parts: List[MCXILetter] = []

        for letter_char in MCXILetter._letter_order:
            base = MCXILetter._letter_values[letter_char]
            count = val // base
            val = val % base
            if count > 0:
                letter_obj = _LETTER_CLASSES[letter_char](count)
                parts.append(letter_obj)

        return cls(parts)

    def __str__(self):
        # Stringify by concatenating letter objects string representations in order
        return ''.join(str(letter) for letter in self.letters)

    def __repr__(self):
        return f"MCXIString({repr(self.letters)})"

    def __add__(self, other: "MCXIString") -> "MCXIString":
        # Add by summing the values and reconverting
        sum_val = self.to_value() + other.to_value()
        return MCXIString.from_value(sum_val)


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    for _ in range(n):
        line = input().strip()
        if not line:
            # Defensive: skip empty lines if any
            continue
        s1, s2 = line.split()
        first_mcxi = MCXIString.parse(s1)
        second_mcxi = MCXIString.parse(s2)
        result = first_mcxi + second_mcxi
        print(result)


if __name__ == '__main__':
    main()