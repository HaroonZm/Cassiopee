from abc import ABC, abstractmethod
from typing import List, Tuple


class GameMode(ABC):
    def __init__(self, name: str):
        self.name = name
        self.games_played = 0

    @abstractmethod
    def play_games(self, count: int) -> int:
        """Play given count of games under this mode.
        Returns net medal change after these games."""
        pass


class NormalGame(GameMode):
    COST_PER_GAME = 3

    def __init__(self, b: int, r: int, g: int, c: int, s: int):
        super().__init__("Normal")
        self.b = b  # big bonus times
        self.r = r  # regular bonus times
        self.g = g  # grape (ブドウ) times during normal game
        self.c = c  # cherry times during normal game
        self.s = s  # normal games count
        # Pre-calculated winnings for normal games based on input counts
        # From problem statement and inferred payout logic:
        # - Big bonus counts and regular bonus counts cause free games
        # - Grape in normal games grant 1 medal each
        # - Cherry payout (not clearly specified in prompt) is 2 medals each (from standard pachislot)
        # They have not specified cherry payout explicitly, but we infer 2 per cherry for consistent logic
        self.cherry_payout = 2
        self.grape_payout = 1

    def play_games(self, count: int) -> int:
        # Confirm that count matches self.s, or else takes s as count for normal games
        assert count == self.s
        # Cost for all normal games played
        total_cost = self.COST_PER_GAME * count
        # Medals gained from grape during normal games
        grape_gain = self.g * self.grape_payout
        # Medals gained from cherry during normal games
        cherry_gain = self.c * self.cherry_payout
        # Medals from normal games (grape + cherry)
        normal_gain = grape_gain + cherry_gain
        # Cost is paid always for normal games
        net_gain = normal_gain - total_cost
        self.games_played += count
        return net_gain


class BonusGame(GameMode):
    COST_PER_GAME = 2
    GRAPE_TRIPLE_GAIN = 15

    def __init__(self, name: str, count: int):
        super().__init__(name)
        self.count = count

    def play_games(self, count: int = None) -> int:
        if count is None:
            count = self.count
        assert count == self.count
        # Each bonus game consumes 2 medals and returns 15 from triple grapes
        net_gain = (self.GRAPE_TRIPLE_GAIN - self.COST_PER_GAME) * count
        self.games_played += count
        return net_gain


class FreeGame(GameMode):
    COST_PER_GAME = 0

    def __init__(self, count: int):
        super().__init__("Free")
        self.count = count

    def play_games(self, count: int = None) -> int:
        if count is None:
            count = self.count
        assert count == self.count
        # No medal gain or cost
        self.games_played += count
        return 0


class SlotMachine:
    INITIAL_MEDALS = 100

    def __init__(self,
                 b: int,
                 r: int,
                 g: int,
                 c: int,
                 s: int,
                 t: int):
        self.b = b  # big bonus count
        self.r = r  # regular bonus count
        self.g = g  # grape count in normal games
        self.c = c  # cherry count in normal games
        self.s = s  # normal games count
        self.t = t  # total games, includes bonus games

        # Calculate bonus game totals:
        self.big_bonus_games = b * 5
        self.regular_bonus_games = r * 3
        # free games count is s - (normal_games + bonus_games)
        self.free_games = max(0, t - (self.s + self.big_bonus_games + self.regular_bonus_games))

    def simulate(self) -> int:
        # Start with initial medals
        medals = self.INITIAL_MEDALS
        # Play normal games
        normal_mode = NormalGame(self.b, self.r, self.g, self.c, self.s)
        medals += normal_mode.play_games(self.s)

        # Play big bonus games
        big_bonus_mode = BonusGame("BigBonus", self.big_bonus_games)
        medals += big_bonus_mode.play_games()

        # Play regular bonus games
        regular_bonus_mode = BonusGame("RegularBonus", self.regular_bonus_games)
        medals += regular_bonus_mode.play_games()

        # Play free games
        free_game_mode = FreeGame(self.free_games)
        medals += free_game_mode.play_games()

        return medals


class InputParser:
    def __init__(self):
        self.datasets: List[Tuple[int, int, int, int, int, int]] = []

    def parse(self, lines: List[str]) -> None:
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 6:
                continue
            b, r, g, c, s, t = map(int, parts)
            if b == 0 and r == 0 and g == 0 and c == 0 and s == 0 and t == 0:
                break
            self.datasets.append((b, r, g, c, s, t))


class SlotSimulator:
    def __init__(self, datasets: List[Tuple[int, int, int, int, int, int]]):
        self.datasets = datasets

    def run(self) -> List[int]:
        results = []
        for data in self.datasets:
            b, r, g, c, s, t = data
            machine = SlotMachine(b, r, g, c, s, t)
            result = machine.simulate()
            results.append(result)
        return results


def main():
    import sys
    lines = sys.stdin.readlines()
    parser = InputParser()
    parser.parse(lines)
    simulator = SlotSimulator(parser.datasets)
    results = simulator.run()
    for r in results:
        print(r)


if __name__ == "__main__":
    main()