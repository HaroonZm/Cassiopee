from abc import ABC, abstractmethod
from collections import defaultdict
from typing import List, Dict, Tuple, Iterator


class Team:
    def __init__(self, team_id: int, university_id: int, solved: int, penalty: int):
        self.team_id = team_id
        self.university_id = university_id
        self.solved = solved
        self.penalty = penalty

    def __repr__(self):
        return (f"Team(ID={self.team_id}, Univ={self.university_id}, "
                f"Solved={self.solved}, Penalty={self.penalty})")


class Comparator(ABC):
    @abstractmethod
    def key(self, team: Team):
        pass


class TeamRankingComparator(Comparator):
    def key(self, team: Team):
        # Sort by descending solved, ascending penalty, ascending ID
        return (-team.solved, team.penalty, team.team_id)


class SelectionRule(ABC):
    @abstractmethod
    def can_select(self,
                   selected_teams: List[Team],
                   candidate: Team) -> bool:
        pass


class RuleOne(SelectionRule):
    def can_select(self,
                   selected_teams: List[Team],
                   candidate: Team) -> bool:
        if len(selected_teams) >= 10:
            return False
        university_team_count = sum(1 for t in selected_teams if t.university_id == candidate.university_id)
        return university_team_count < 3


class RuleTwo(SelectionRule):
    def can_select(self,
                   selected_teams: List[Team],
                   candidate: Team) -> bool:
        if len(selected_teams) >= 20:
            return False
        university_team_count = sum(1 for t in selected_teams if t.university_id == candidate.university_id)
        return university_team_count < 2


class RuleThree(SelectionRule):
    def can_select(self,
                   selected_teams: List[Team],
                   candidate: Team) -> bool:
        if len(selected_teams) >= 26:
            return False
        university_team_count = sum(1 for t in selected_teams if t.university_id == candidate.university_id)
        return university_team_count == 0


class Selector:
    def __init__(self, rules: List[SelectionRule]):
        self.rules = rules

    def select(self, teams: List[Team]) -> List[Team]:
        selected = []
        for team in teams:
            for rule in self.rules:
                if rule.can_select(selected, team):
                    selected.append(team)
                    break
            if len(selected) >= 26:
                break
        return selected


class InputParser:
    def __init__(self):
        pass

    def parse_input(self) -> Iterator[List[Team]]:
        while True:
            raw = input().strip()
            if not raw:
                continue
            n = int(raw)
            if n == 0:
                break
            teams = []
            for _ in range(n):
                line = input().strip()
                while not line:
                    line = input().strip()
                i, u, a, p = map(int, line.split())
                teams.append(Team(i, u, a, p))
            yield teams


class TeamSelectorApplication:
    def __init__(self):
        self.comparator = TeamRankingComparator()
        self.rules = [RuleOne(), RuleTwo(), RuleThree()]
        self.selector = Selector(self.rules)
        self.parser = InputParser()

    def run(self):
        for teams in self.parser.parse_input():
            sorted_teams = sorted(teams, key=self.comparator.key)
            selected_teams = self.selector.select(sorted_teams)
            for team in selected_teams:
                print(team.team_id)


if __name__ == "__main__":
    app = TeamSelectorApplication()
    app.run()