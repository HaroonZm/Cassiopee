from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Optional


class Color:
    RED = 1
    BLUE = 2
    YELLOW = 3

    _names = {
        RED: "RED",
        BLUE: "BLUE",
        YELLOW: "YELLOW",
    }

    @classmethod
    def all(cls) -> List[int]:
        return [cls.RED, cls.BLUE, cls.YELLOW]

    @classmethod
    def name(cls, c: int) -> str:
        return cls._names.get(c, "UNKNOWN")


class CharacterSequence(ABC):
    """
    Abstract base class representing a sequence of characters with colors.
    """

    @abstractmethod
    def length(self) -> int:
        pass

    @abstractmethod
    def get_color(self, idx: int) -> int:
        pass

    @abstractmethod
    def set_color(self, idx: int, color: int) -> None:
        pass

    @abstractmethod
    def clone(self) -> 'CharacterSequence':
        pass


class LinearCharacterSequence(CharacterSequence):
    """
    Concrete character sequence modeled as a linear list.
    """

    def __init__(self, colors: List[int]):
        self._colors: List[int] = colors[:]

    def length(self) -> int:
        return len(self._colors)

    def get_color(self, idx: int) -> int:
        return self._colors[idx]

    def set_color(self, idx: int, color: int) -> None:
        self._colors[idx] = color

    def clone(self) -> 'LinearCharacterSequence':
        return LinearCharacterSequence(self._colors)

    def __repr__(self):
        return "LinearCharacterSequence(" + ",".join(Color.name(c) for c in self._colors) + ")"


class EliminationStrategy(ABC):
    """
    Abstract base class for elimination logic.
    """

    @abstractmethod
    def eliminate(self, sequence: CharacterSequence) -> CharacterSequence:
        """
        Returns a new sequence with all eliminations applied until no more eliminations are possible.
        """
        pass


class ChainEliminationStrategy(EliminationStrategy):
    """
    Implements the chain elimination rule:
    - Remove sequences of 4 or more consecutive characters of the same color.
    - Repeat until no more eliminations are possible.
    """

    def eliminate(self, sequence: CharacterSequence) -> CharacterSequence:
        current_sequence = sequence.clone()
        while True:
            groups = self._find_groups(current_sequence)
            removable_indices = set()
            for start, end, color, length in groups:
                if length >= 4:
                    removable_indices.update(range(start, end))
            if not removable_indices:
                break
            current_sequence = self._remove_indices(current_sequence, sorted(removable_indices))
        return current_sequence

    def _find_groups(self, sequence: CharacterSequence) -> List[Tuple[int, int, int, int]]:
        groups = []
        n = sequence.length()
        if n == 0:
            return groups
        start = 0
        current_color = sequence.get_color(0)
        for i in range(1, n):
            if sequence.get_color(i) != current_color:
                groups.append((start, i, current_color, i - start))
                start = i
                current_color = sequence.get_color(i)
        groups.append((start, n, current_color, n - start))
        return groups

    def _remove_indices(self, sequence: CharacterSequence, indices: List[int]) -> CharacterSequence:
        # Remove characters at specified indices and return new sequence
        new_colors = []
        remove_set = set(indices)
        for i in range(sequence.length()):
            if i not in remove_set:
                new_colors.append(sequence.get_color(i))
        return LinearCharacterSequence(new_colors)


class Move:
    """
    Represents a single move of changing one character's color.
    """

    def __init__(self, position: int, new_color: int):
        self.position = position
        self.new_color = new_color

    def __repr__(self):
        return f"Move(pos={self.position}, new_color={Color.name(self.new_color)})"


class GameSolver:
    """
    Encapsulates the problem-solving logic with possible extensibility.
    """

    def __init__(self, sequence: CharacterSequence, elimination_strategy: EliminationStrategy):
        self.sequence = sequence
        self.elimination_strategy = elimination_strategy
        self.n = sequence.length()

    def minimal_remaining(self) -> int:
        """
        Try all possible single-character color changes (not to the same color),
        apply eliminations and return the minimal size remaining.
        """
        original_colors = [self.sequence.get_color(i) for i in range(self.n)]
        min_remaining = self.n  # worst case: no elimination
        for pos in range(self.n):
            original_color = original_colors[pos]
            for color in Color.all():
                if color == original_color:
                    continue  # no change
                modified_sequence = self.sequence.clone()
                modified_sequence.set_color(pos, color)
                eliminated_sequence = self.elimination_strategy.eliminate(modified_sequence)
                remaining = eliminated_sequence.length()
                if remaining < min_remaining:
                    min_remaining = remaining
        return min_remaining


class InputReader:
    """
    Handles input reading, supports multiple data sets.
    """

    def __init__(self):
        pass

    def read_dataset(self) -> Optional[Tuple[int, List[int]]]:
        try:
            line = input()
            if line == "":
                return None
            n = int(line)
            if n == 0:
                return None
            colors = []
            for _ in range(n):
                col = int(input())
                colors.append(col)
            return n, colors
        except EOFError:
            return None


class OutputWriter:
    """
    Handles output formatting and writing.
    """

    @staticmethod
    def write_result(min_remaining: int) -> None:
        print(min_remaining)


def main():
    reader = InputReader()
    writer = OutputWriter()
    elimination_strategy = ChainEliminationStrategy()

    while True:
        data = reader.read_dataset()
        if data is None:
            break
        n, colors = data
        sequence = LinearCharacterSequence(colors)
        solver = GameSolver(sequence, elimination_strategy)
        result = solver.minimal_remaining()
        writer.write_result(result)


if __name__ == "__main__":
    main()