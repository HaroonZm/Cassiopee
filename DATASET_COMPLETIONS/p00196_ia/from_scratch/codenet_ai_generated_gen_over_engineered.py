from abc import ABC, abstractmethod
from typing import List, Optional, Iterator


class ResultCode:
    WIN = 0
    LOSE = 1
    DRAW = 2


class Team:
    def __init__(self, name: str, results: List[int], index: int):
        self.name = name
        self.results = results
        self.index = index  # preserve input order for tiebreakers
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self._compute_record()

    def _compute_record(self):
        for r in self.results:
            if r == ResultCode.WIN:
                self.wins += 1
            elif r == ResultCode.LOSE:
                self.losses += 1
            elif r == ResultCode.DRAW:
                self.draws += 1

    def __repr__(self):
        return f"Team({self.name}, W:{self.wins}, L:{self.losses}, D:{self.draws}, idx:{self.index})"


class AbstractRankingStrategy(ABC):
    @abstractmethod
    def rank(self, teams: List[Team]) -> List[Team]:
        pass


class SophisticatedRankingStrategy(AbstractRankingStrategy):
    """
    Implements the ranking with:
    - Priority 1: Higher wins
    - Priority 2: Lower losses (if wins tie)
    - Priority 3: Preserve input order in tie (stable sort)
    """

    def rank(self, teams: List[Team]) -> List[Team]:
        # Note: sort is stable in python so we apply criteria in reverse order for tie-break
        # But here since only 3 levels, a single sorted with a custom key is simpler.
        return sorted(
            teams,
            key=lambda t: (-t.wins, t.losses, t.index)
        )


class TeamDataParser:
    """
    Parses a single team's input line into a Team instance.
    Isolated from main logic for easy extension.
    """

    @staticmethod
    def parse(line: str, n: int, index: int) -> Team:
        parts = line.strip().split()
        if len(parts) != n:
            raise ValueError(f"Invalid number of results on line: {line}")
        name = parts[0]
        results = list(map(int, parts[1:]))
        if len(results) != n - 1:
            raise ValueError(f"Results count mismatch for team {name}")
        return Team(name, results, index)


class InputDataIterator:
    """
    Iterator over data sets.
    Each iteration yields (n, List[str]) where n is team count and list of team lines.
    Ends iteration on 0.
    """

    def __init__(self, lines: Iterator[str]):
        self.lines = lines

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                line = next(self.lines).strip()
            except StopIteration:
                raise StopIteration
            if line == '':
                continue  # skip empty lines
            if line == '0':
                raise StopIteration
            n = int(line)
            if not (2 <= n <= 10):
                raise ValueError("n must be between 2 and 10")
            team_lines = []
            for _ in range(n):
                team_lines.append(next(self.lines).rstrip('\n'))
            return n, team_lines


class Tournament:
    """
    Encapsulates full tournament processing:
    - Parse teams
    - Rank teams
    - Output result
    """

    def __init__(self, ranking_strategy: AbstractRankingStrategy):
        self.ranking_strategy = ranking_strategy

    def process_dataset(self, n: int, team_lines: List[str]) -> List[str]:
        teams: List[Team] = []
        for idx, line in enumerate(team_lines):
            team = TeamDataParser.parse(line, n, idx)
            teams.append(team)
        ranked = self.ranking_strategy.rank(teams)
        return [team.name for team in ranked]


def main():
    import sys
    lines_iter = iter(sys.stdin)
    data_iter = InputDataIterator(lines_iter)
    tournament = Tournament(SophisticatedRankingStrategy())

    for n, team_lines in data_iter:
        result = tournament.process_dataset(n, team_lines)
        for name in result:
            print(name)


if __name__ == '__main__':
    main()