from abc import ABC, abstractmethod
from typing import List, Tuple, Union, Optional, Iterator


class GenomeComponent(ABC):
    """
    Abstract base class representing any component in the genome sequence.
    """

    @abstractmethod
    def length(self) -> int:
        """
        Returns the length of the expanded genome sequence represented by this component.
        """
        pass

    @abstractmethod
    def get_char_at(self, index: int) -> Optional[str]:
        """
        Returns the character at the given index in the expanded genome sequence.
        If index is out of bounds, returns None.
        """
        pass


class Literal(GenomeComponent):
    """
    Represents a literal sequence of characters (A-Z) without compression.
    """

    def __init__(self, sequence: str):
        self._sequence = sequence
        self._len = len(sequence)

    def length(self) -> int:
        return self._len

    def get_char_at(self, index: int) -> Optional[str]:
        if 0 <= index < self._len:
            return self._sequence[index]
        return None


class Repetition(GenomeComponent):
    """
    Represents a repetition of a component multiple times.
    Example: 4(AB) or 10C
    """

    def __init__(self, count: int, component: GenomeComponent):
        assert count >= 2, "Repetition count must be at least 2"
        self._count = count
        self._component = component
        self._len = self._count * self._component.length()

    def length(self) -> int:
        return self._len

    def get_char_at(self, index: int) -> Optional[str]:
        if 0 <= index < self._len:
            comp_len = self._component.length()
            inner_index = index % comp_len
            return self._component.get_char_at(inner_index)
        return None


class GenomeParser:
    """
    A sophisticated recursive descent parser for the compressed genome representation,
    anticipating extensibility for more features and complexity.
    """

    def __init__(self, data: str):
        self._data = data
        self._pos = 0
        self._length = len(data)

    def parse(self) -> GenomeComponent:
        """
        Parse the entire genome string into a GenomeComponent hierarchy.
        """
        components: List[GenomeComponent] = []
        while self._pos < self._length:
            comp = self._parse_element()
            if comp is not None:
                components.append(comp)
            else:
                break
        if len(components) == 1:
            return components[0]
        else:
            # If multiple components, unify them as a single literal sequence
            # or a compound Literal if parsing found multiple discrete literals
            # Combine Literal components into one where possible
            combined_literals = []
            combined_components = []
            for component in components:
                if isinstance(component, Literal):
                    combined_literals.append(component._sequence)
                else:
                    if combined_literals:
                        combined_components.append(Literal(''.join(combined_literals)))
                        combined_literals = []
                    combined_components.append(component)
            if combined_literals:
                combined_components.append(Literal(''.join(combined_literals)))
            if len(combined_components) == 1:
                return combined_components[0]
            else:
                # Create a CompoundSequence to keep abstractions uniform
                return CompoundSequence(combined_components)

    def _peek(self) -> Optional[str]:
        """
        Peek the current character without consuming it.
        """
        if self._pos < self._length:
            return self._data[self._pos]
        return None

    def _consume(self, expected: Optional[str] = None) -> str:
        """
        Consume and return the current character. If expected is provided,
        asserts the current character is the expected one.
        """
        if self._pos >= self._length:
            raise ValueError("Unexpected end of input while parsing")
        current_char = self._data[self._pos]
        if expected is not None and current_char != expected:
            raise ValueError(f"Expected '{expected}' but found '{current_char}' at position {self._pos}")
        self._pos += 1
        return current_char

    def _parse_digits(self) -> int:
        """
        Parses a sequence of digits from current position, returns as integer.
        Raises ValueError if no digits found.
        """
        start_pos = self._pos
        while self._pos < self._length and self._data[self._pos].isdigit():
            self._pos += 1
        if start_pos == self._pos:
            raise ValueError(f"Expected digits at position {start_pos}")
        num = int(self._data[start_pos:self._pos])
        return num

    def _parse_element(self) -> Optional[GenomeComponent]:
        """
        Parses one element which can be:
         - a repetition with parentheses e.g., N(...)
         - a repetition of a single letter e.g., N c
         - a literal sequence of letters (A-Z)
        Returns GenomeComponent or None if no more elements.
        """
        if self._pos >= self._length:
            return None
        curr = self._peek()
        if curr is None:
            return None

        if curr.isdigit():
            # Parse repetition count
            count = self._parse_digits()
            if self._pos < self._length and self._peek() == '(':
                # repetition on a parenthesized sequence
                self._consume('(')
                # parse sequence inside parentheses recursively until matching )
                inner_component = self._parse_until_closing_paren()
                self._consume(')')
                return Repetition(count, inner_component)
            else:
                # repetition on a single character literal (no parentheses)
                if self._pos >= self._length:
                    raise ValueError("Unexpected end of input after repetition count")
                char = self._consume()
                if not ('A' <= char <= 'Z'):
                    raise ValueError(f"Expected uppercase letter after repetition count at position {self._pos-1}")
                inner_component = Literal(char)
                return Repetition(count, inner_component)
        else:
            # Parse a literal sequence until digit or '(' or ')' or end
            literal_chars = []
            while self._pos < self._length:
                curr = self._peek()
                if curr is None or curr.isdigit() or curr in '()':
                    break
                if 'A' <= curr <= 'Z':
                    literal_chars.append(curr)
                    self._pos += 1
                else:
                    raise ValueError(f"Unexpected character '{curr}' in literal at position {self._pos}")
            if literal_chars:
                return Literal(''.join(literal_chars))
            return None

    def _parse_until_closing_paren(self) -> GenomeComponent:
        """
        Parses until matching closing parenthesis.
        Components inside may be nested repetitions or literals.
        """
        components: List[GenomeComponent] = []
        while self._pos < self._length:
            if self._peek() == ')':
                break
            comp = self._parse_element()
            if comp is None:
                break
            components.append(comp)
        if not components:
            # Empty parentheses could theoretically occur but problem states seq length >=1, we'll treat empty as error
            raise ValueError("Empty parentheses are invalid")
        if len(components) == 1:
            return components[0]
        else:
            return CompoundSequence(components)


class CompoundSequence(GenomeComponent):
    """
    A complex sequence composed of multiple genome components in order.
    Abstracting concatenation to handle pieces of parsed sequences uniformly.
    """

    def __init__(self, components: List[GenomeComponent]):
        self._components = components
        self._length = sum(c.length() for c in self._components)

    def length(self) -> int:
        return self._length

    def get_char_at(self, index: int) -> Optional[str]:
        if not (0 <= index < self._length):
            return None
        current_index = 0
        for component in self._components:
            comp_len = component.length()
            if current_index + comp_len > index:
                return component.get_char_at(index - current_index)
            current_index += comp_len
        return None


class GenomeQuery:
    """
    External interface representing a query to fetch the i-th character from genome.
    This abstraction is made anticipating support for bulk queries or caching.
    """

    def __init__(self, genome_str: str):
        parser = GenomeParser(genome_str)
        self._genome = parser.parse()

    def query(self, index: int) -> str:
        if index < 0 or index >= self._genome.length():
            return '0'
        result = self._genome.get_char_at(index)
        if result is None:
            return '0'
        return result


def main():
    import sys
    lines = (line.rstrip('\n') for line in sys.stdin)
    for line in lines:
        if line == "0 0":
            break
        if not line:
            continue
        genome_str, idx_str = line.split(' ', 1)
        idx = int(idx_str)
        gql = GenomeQuery(genome_str)
        print(gql.query(idx))


if __name__ == "__main__":
    main()