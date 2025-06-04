class MatchResult:
    def __init__(self, winner: int, loser: int):
        self.winner = winner
        self.loser = loser

class TeamRankingSolver:
    def __init__(self, n_teams: int):
        self.n = n_teams
        self.graph = [[] for _ in range(n_teams)]
        self.inverse_graph = [[] for _ in range(n_teams)]
        self.indegree = [0] * n_teams
    
    def add_match_result(self, winner: int, loser: int):
        # Adjust indices to zero-based internally
        w, l = winner - 1, loser - 1
        self.graph[w].append(l)
        self.inverse_graph[l].append(w)
        self.indegree[l] += 1
    
    def topological_sort_and_check_unique(self):
        from collections import deque
        q = deque()
        for i in range(self.n):
            if self.indegree[i] == 0:
                q.append(i)
        order = []
        multiple_options = False
        while q:
            if len(q) >= 2:
                # More than one node with no incoming edges means multiple topological orders
                multiple_options = True
            current = q.popleft()
            order.append(current)
            for nxt in self.graph[current]:
                self.indegree[nxt] -= 1
                if self.indegree[nxt] == 0:
                    q.append(nxt)
        if len(order) != self.n:
            # Cycle detected or inconsistent data
            raise ValueError("No valid ranking possible (cycle detected)")
        return order, multiple_options

class AbstractRankingModel:
    def __init__(self, n: int, matches: list):
        self.n = n
        self.matches = matches
        self.solver = TeamRankingSolver(n)
        self._build_graph()
    
    def _build_graph(self):
        for match in self.matches:
            self.solver.add_match_result(match.winner, match.loser)
    
    def solve(self):
        try:
            order, multiple = self.solver.topological_sort_and_check_unique()
            # order is zero-based indexes of teams from highest rank (1st) to lowest rank (nth)
            return order, multiple
        except ValueError:
            # No valid order
            return None, None

class RankingIOHandler:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.matches = []
    
    def read_input(self):
        import sys
        input = sys.stdin.readline
        self.n = int(input())
        self.m = int(input())
        self.matches = []
        for _ in range(self.m):
            winner, loser = map(int, input().split())
            self.matches.append(MatchResult(winner, loser))
    
    def output_result(self, order, multiple_possible):
        # order: zero-based team indices from 1st to nth
        # multiple_possible: boolean, True if multiple valid rankings exist
        for team_idx in order:
            print(team_idx+1)
        print(1 if multiple_possible else 0)

class ApplicationController:
    def __init__(self):
        self.io_handler = RankingIOHandler()
    
    def run(self):
        self.io_handler.read_input()
        model = AbstractRankingModel(self.io_handler.n, self.io_handler.matches)
        order, multiple = model.solve()
        if order is None:
            # According to problem statement, no invalid inputs will be given,
            # but if cycle or contradiction appears, fallback output:
            # Just output any permutation and 0 for uniqueness
            for i in range(1, self.io_handler.n + 1):
                print(i)
            print(0)
        else:
            self.io_handler.output_result(order, multiple)

if __name__ == "__main__":
    app = ApplicationController()
    app.run()