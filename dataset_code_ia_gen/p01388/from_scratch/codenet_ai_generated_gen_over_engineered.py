from collections import Counter
from abc import ABC, abstractmethod
from typing import Dict, List


class CharacterCounter:
    def __init__(self, source: str):
        # Normalize to uppercase for case insensitivity
        self.char_counts = Counter(source.upper())

    def count(self, char: str) -> int:
        return self.char_counts.get(char.upper(), 0)


class SignPanel(ABC):
    @abstractmethod
    def required_characters(self) -> Dict[str, int]:
        pass

    def max_constructible(self, counter: CharacterCounter) -> int:
        required = self.required_characters()
        # Calculate how many full panels can be made given the char counts
        potential_counts = []
        for char, needed in required.items():
            available = counter.count(char)
            potential_counts.append(available // needed)
        return min(potential_counts) if potential_counts else 0


class KUPCPanel(SignPanel):
    def required_characters(self) -> Dict[str, int]:
        return {'K': 1, 'U': 1, 'P': 1, 'C': 1}


class PanelFactory:
    def __init__(self):
        self.panel_types: List[SignPanel] = []

    def register_panel(self, panel: SignPanel):
        self.panel_types.append(panel)

    def create_max_panels(self, board_string: str) -> Dict[str, int]:
        counter = CharacterCounter(board_string)
        results = {}
        for panel in self.panel_types:
            panel_name = type(panel).__name__
            results[panel_name] = panel.max_constructible(counter)
        return results


class KUPCContest:
    def __init__(self, boards: str):
        self.boards = boards
        self.factory = PanelFactory()
        self.factory.register_panel(KUPCPanel())

    def solve(self) -> int:
        results = self.factory.create_max_panels(self.boards)
        # Return the count for KUPCPanel only
        return results.get('KUPCPanel', 0)


def main():
    boards = input()
    contest = KUPCContest(boards)
    print(contest.solve())


if __name__ == "__main__":
    main()