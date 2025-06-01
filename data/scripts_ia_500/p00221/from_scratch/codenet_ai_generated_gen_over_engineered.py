from abc import ABC, abstractmethod
from typing import List, Union, Iterator, Set


class FizzBuzzRule(ABC):
    @abstractmethod
    def is_applicable(self, number: int) -> bool:
        pass

    @abstractmethod
    def representation(self) -> str:
        pass


class DivisibleByRule(FizzBuzzRule):
    def __init__(self, divisor: int, output: str):
        self._divisor = divisor
        self._output = output

    def is_applicable(self, number: int) -> bool:
        return number % self._divisor == 0

    def representation(self) -> str:
        return self._output


class CompositeFizzBuzzRule(FizzBuzzRule):
    def __init__(self, rules: List[FizzBuzzRule], output: str):
        self._rules = rules
        self._output = output

    def is_applicable(self, number: int) -> bool:
        return all(rule.is_applicable(number) for rule in self._rules)

    def representation(self) -> str:
        return self._output


class FizzBuzzEvaluator:
    def __init__(self):
        # Compose rules anticipating extension
        self._rules = [
            CompositeFizzBuzzRule(
                rules=[DivisibleByRule(3, "Fizz"), DivisibleByRule(5, "Buzz")],
                output="FizzBuzz",
            ),
            DivisibleByRule(3, "Fizz"),
            DivisibleByRule(5, "Buzz"),
        ]

    def evaluate(self, number: int) -> str:
        for rule in self._rules:
            if rule.is_applicable(number):
                return rule.representation()
        return str(number)

    def is_valid_call(self, number: int, call: str) -> bool:
        return self.evaluate(number) == call


class Player:
    def __init__(self, player_id: int):
        self._player_id = player_id
        self._active = True

    @property
    def id(self) -> int:
        return self._player_id

    @property
    def active(self) -> bool:
        return self._active

    def deactivate(self):
        self._active = False


class PlayerManager:
    def __init__(self, count: int):
        self._players = [Player(i+1) for i in range(count)]

    def active_players(self) -> List[Player]:
        return [p for p in self._players if p.active]

    def next_active_player(self, start_pos: int) -> Player:
        n = len(self._players)
        pos = start_pos % n
        for i in range(n):
            candidate = self._players[(pos + i) % n]
            if candidate.active:
                return candidate
        raise RuntimeError("No active players remain")

    def deactivate_player(self, player_id: int):
        for p in self._players:
            if p.id == player_id:
                p.deactivate()

    def count_active(self) -> int:
        return len(self.active_players())

    def active_player_ids(self) -> List[int]:
        return sorted([p.id for p in self.active_players()])


class TurnIterator:
    def __init__(self, player_manager: PlayerManager):
        self._player_manager = player_manager
        self._last_index = 0
        self._total_players = len(player_manager.active_players())

    def __iter__(self) -> Iterator[Player]:
        return self

    def __next__(self) -> Player:
        if self._player_manager.count_active() == 0:
            raise StopIteration
        # Start search from last index mod length
        next_player = self._player_manager.next_active_player(self._last_index)
        # Update last index to one after found player's index
        self._last_index = next_player.id % len(self._player_manager._players)
        return next_player


class FizzBuzzGame:
    def __init__(self, player_count: int, calls: List[str]):
        self._player_manager = PlayerManager(player_count)
        self._calls = calls
        self._fb_evaluator = FizzBuzzEvaluator()
        self._turn_iterator = TurnIterator(self._player_manager)
        self._current_call_number = 1

    def play(self):
        # If any time only one active player remains,
        # stop processing further calls
        turn_iter = iter(self._turn_iterator)

        for call in self._calls:
            if self._player_manager.count_active() == 1:
                break
            try:
                player = next(turn_iter)
            except StopIteration:
                # No players remain active
                break
            expected_call = self._fb_evaluator.evaluate(self._current_call_number)
            # Validate call
            if call != expected_call:
                # Player eliminates themselves by mistake
                self._player_manager.deactivate_player(player.id)
                # Next call number proceeds, adjusted by skipping mistaken number
                self._current_call_number += 1
                # Next player turn should start exactly after this player,
                # handled by TurnIterator logic automatically
                continue
            self._current_call_number += 1

    def surviving_player_ids(self) -> List[int]:
        return self._player_manager.active_player_ids()


class InputDataParser:
    def __init__(self):
        self._datasets = []

    def parse(self, lines: List[str]) -> List[tuple]:
        # Parse the entire input to get datasets as tuples of (m, n, calls)
        idx = 0
        length = len(lines)
        parsed_datasets = []
        while idx < length:
            if lines[idx].strip() == "":
                idx += 1
                continue
            first_line = lines[idx].strip()
            idx += 1
            if first_line == "0 0":
                break
            m, n = map(int, first_line.split())
            calls = []
            for _ in range(n):
                calls.append(lines[idx].strip())
                idx += 1
            parsed_datasets.append((m, n, calls))
        return parsed_datasets


def main():
    import sys

    lines = [line.rstrip('\n') for line in sys.stdin]
    parser = InputDataParser()
    datasets = parser.parse(lines)

    for m, n, calls in datasets:
        game = FizzBuzzGame(m, calls)
        game.play()
        survivors = game.surviving_player_ids()
        print(" ".join(str(s) for s in survivors))


if __name__ == "__main__":
    main()