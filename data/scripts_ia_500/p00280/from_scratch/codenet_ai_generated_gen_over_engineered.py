from typing import List, Tuple, Dict


class Score:
    def __init__(self, j: int, y: int):
        self.j = j
        self.y = y

    def __eq__(self, other):
        return self.j == other.j and self.y == other.y

    def __hash__(self):
        return hash((self.j, self.y))

    def __str__(self):
        return f"({self.j},{self.y})"

    def __lt__(self, other):
        return (self.j, self.y) < (other.j, other.y)


class MatchRules:
    MAX_SCORE = 6

    def __init__(self):
        pass

    def is_valid_score(self, score: Score) -> bool:
        j, y = score.j, score.y
        # Both zero is invalid starting state per problem statement
        if j == 0 and y == 0:
            return True

        # Score ranges
        if not (0 <= j <= self.MAX_SCORE and 0 <= y <= self.MAX_SCORE):
            return False
        # Constraint for end game score 6: only allowed if the other has 4
        if j == 6 and y != 4:
            return False
        if y == 6 and j != 4:
            return False
        # A score cannot be both 6 at once as per problem constraints
        if j == 6 and y == 6:
            return False
        return True

    def is_end(self, score: Score) -> bool:
        j, y = score.j, score.y
        # Rule1: if opponent has 3 or less and one player reaches 5 first, that player wins
        if (j >= 5 and y <= 3):
            return True
        if (y >= 5 and j <= 3):
            return True
        # Rule2: 4-4 tie, next player scoring two consecutive points wins
        if j == 6 and y == 4:
            return True
        if y == 6 and j == 4:
            return True
        # Rule3: 4-4 with each scoring one more point is draw (final)
        if j == 5 and y == 5:
            return True
        return False

    def is_tie(self, score: Score) -> bool:
        return score.j == 5 and score.y == 5


class TennisMatchGraph:
    """Directed acyclic graph to represent all states from start to the given score."""

    def __init__(self, rules: MatchRules):
        self.rules = rules
        self.adj: Dict[Score, List[Tuple[Score, str]]] = {}

    def neighbors(self, score: Score) -> List[Tuple[Score, str]]:
        if score in self.adj:
            return self.adj[score]

        neighbors = []
        if self.rules.is_end(score):
            # no next states
            self.adj[score] = neighbors
            return neighbors

        # Next scores after A (Jou scores)
        next_j = score.j + 1
        next_y = score.y
        next_score_a = Score(next_j, next_y)
        if self.rules.is_valid_score(next_score_a) and not self.rules.is_end(score):
            if not self.rules.is_end(next_score_a):
                neighbors.append((next_score_a, "A"))
            else:
                # We can reach an end state with A point too
                neighbors.append((next_score_a, "A"))

        # Next scores after B (Yae scores)
        next_j = score.j
        next_y = score.y + 1
        next_score_b = Score(next_j, next_y)
        if self.rules.is_valid_score(next_score_b) and not self.rules.is_end(score):
            if not self.rules.is_end(next_score_b):
                neighbors.append((next_score_b, "B"))
            else:
                neighbors.append((next_score_b, "B"))

        self.adj[score] = neighbors
        return neighbors


class PathFinder:
    def __init__(self, rules: MatchRules, graph: TennisMatchGraph):
        self.rules = rules
        self.graph = graph
        self.memo: Dict[Score, List[str]] = {}

    def find_paths(self, start: Score, goal: Score) -> List[str]:
        if start == goal:
            return [""]

        if self.rules.is_end(start):
            # Cannot proceed further - no path from here
            return []

        if start in self.memo:
            return self.memo[start]

        paths = []
        for next_score, action in self.graph.neighbors(start):
            if self.score_less_or_equal(next_score, goal):
                # Avoid paths that exceed the goal score
                partial_paths = self.find_paths(next_score, goal)
                for p in partial_paths:
                    paths.append(action + p)

        paths.sort()
        self.memo[start] = paths
        return paths

    @staticmethod
    def score_less_or_equal(a: Score, b: Score) -> bool:
        # a less or equal to b if j and y individually less or equal
        return a.j <= b.j and a.y <= b.y


def main():
    import sys

    class InputReader:
        def __init__(self):
            self.lines = sys.stdin.read().strip().split()
            self.pos = 0

        def next_int(self) -> int:
            val = int(self.lines[self.pos])
            self.pos += 1
            return val

    reader = InputReader()
    j = reader.next_int()
    y = reader.next_int()

    rules = MatchRules()
    graph = TennisMatchGraph(rules)
    pathfinder = PathFinder(rules, graph)

    start_score = Score(0, 0)
    target_score = Score(j, y)

    # Defensive: if target_score is end but not valid, probably no paths
    if not rules.is_valid_score(target_score):
        # No output for invalid target presumably
        return

    paths = pathfinder.find_paths(start_score, target_score)
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()