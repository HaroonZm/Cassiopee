class Vertex:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.stone = 0  # 0 means empty

    def __repr__(self):
        return f"V({self.row},{self.col}):{self.stone}"

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[Vertex(r, c) for c in range(r+1)] for r in range(size)]
        self.adjacency_map = {}  # key: (r,c) value: list of adjacent (r,c)

    def set_stone(self, r, c, stone):
        self.grid[r][c].stone = stone

    def get_stone(self, r, c):
        return self.grid[r][c].stone

    def in_bounds(self, r, c):
        return 0 <= r < self.size and 0 <= c <= r

    def build_adjacency(self):
        # In a triangular lattice, each vertex connects to up to 6 others.
        # Adjacency rules:
        # Up-left: (r-1, c-1)
        # Up-right: (r-1, c)
        # Left: (r, c-1)
        # Right: (r, c+1)
        # Down-left: (r+1, c)
        # Down-right: (r+1, c+1)
        for r in range(self.size):
            for c in range(r+1):
                neighbors = []
                for (nr,nc) in [(r-1,c-1),(r-1,c),(r,c-1),(r,c+1),(r+1,c),(r+1,c+1)]:
                    if self.in_bounds(nr,nc):
                        neighbors.append((nr,nc))
                self.adjacency_map[(r,c)] = neighbors

    def neighbors(self, r, c):
        return self.adjacency_map.get((r,c),[])

    def empty_vertices(self):
        for r in range(self.size):
            for c in range(r+1):
                if self.grid[r][c].stone == 0:
                    yield (r,c)

    def copy(self):
        new_board = Board(self.size)
        for r in range(self.size):
            for c in range(r+1):
                new_board.set_stone(r,c,self.get_stone(r,c))
        new_board.build_adjacency()
        return new_board

class GroupFinder:
    def __init__(self, board):
        self.board = board
        self.visited = set()
        self.groups = []

    def find_groups(self):
        self.visited.clear()
        self.groups.clear()
        for r in range(self.board.size):
            for c in range(r+1):
                if self.board.get_stone(r,c) > 0 and (r,c) not in self.visited:
                    group = self._dfs(r,c)
                    self.groups.append(group)
        return self.groups

    def _dfs(self, r, c):
        start_stone = self.board.get_stone(r,c)
        stack = [(r,c)]
        group = []
        self.visited.add((r,c))
        while stack:
            vr, vc = stack.pop()
            group.append((vr,vc))
            for nr,nc in self.board.neighbors(vr,vc):
                if (nr,nc) not in self.visited and self.board.get_stone(nr,nc) == start_stone:
                    self.visited.add((nr,nc))
                    stack.append((nr,nc))
        return group

class RemovalJudge:
    def __init__(self, board):
        self.board = board

    def groups_to_remove(self):
        gf = GroupFinder(self.board)
        groups = gf.find_groups()
        removable = []
        for group in groups:
            # A group is removed if no vertex in the group touches an empty vertex
            if not self._group_has_empty_adjacent(group):
                removable.append(group)
        return removable

    def _group_has_empty_adjacent(self, group):
        for (r,c) in group:
            for (nr,nc) in self.board.neighbors(r,c):
                if self.board.get_stone(nr,nc) == 0:
                    return True
        return False

class GameState:
    def __init__(self, board, current_player):
        self.board = board
        self.current_player = current_player

    def put_stone_and_score(self, r, c):
        # Put current player's stone at (r,c)
        new_board = self.board.copy()
        new_board.set_stone(r,c, self.current_player)
        # Check removable groups
        judge = RemovalJudge(new_board)
        removable = judge.groups_to_remove()
        if not removable:
            return 0
        gain = 0
        loss = 0
        for group in removable:
            for (gr,gc) in group:
                stone = new_board.get_stone(gr,gc)
                if stone == self.current_player:
                    loss += 1
                else:
                    gain += 1
        return gain - loss

class LifeLineSolver:
    def __init__(self):
        self.results = []

    def solve(self):
        import sys
        lines = sys.stdin.read().strip('\n ').split('\n')
        idx = 0
        while True:
            if idx >= len(lines):
                break
            line = lines[idx].strip()
            if line == "":
                idx += 1
                continue
            if line == "0 0":
                break
            N_C = line.split()
            if len(N_C) !=2:
                idx+=1
                continue
            N, C = map(int, N_C)
            idx +=1
            size = N
            current_player = C
            board = Board(size)
            # Read board state
            for r in range(size):
                row_values = []
                while True:
                    if idx >= len(lines):
                        break
                    row_line = lines[idx].strip()
                    if row_line == "":
                        idx+=1
                        continue
                    parts = row_line.split()
                    if len(parts) != r+1:
                        idx+=1
                        continue
                    try:
                        row_values = list(map(int, parts))
                        idx+=1
                        break
                    except:
                        idx+=1
                        continue
                for c in range(r+1):
                    board.set_stone(r,c,row_values[c])
            board.build_adjacency()
            result = self._max_points_turn(board, current_player)
            print(result)

    def _max_points_turn(self, board, current_player):
        gs = GameState(board, current_player)
        max_points = None
        for (r,c) in board.empty_vertices():
            pts = gs.put_stone_and_score(r,c)
            if max_points is None or pts > max_points:
                max_points = pts
        if max_points is None:
            # No empty vertices
            return 0
        return max_points

if __name__ == "__main__":
    solver = LifeLineSolver()
    solver.solve()