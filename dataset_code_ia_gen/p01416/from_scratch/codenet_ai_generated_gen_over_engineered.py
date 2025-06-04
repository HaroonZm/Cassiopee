from collections import defaultdict
from typing import List, Optional, Tuple, Dict, Set

class Tile:
    __slots__ = ['color', 'row', 'col']
    def __init__(self, color: str, row: int, col: int):
        self.color = color
        self.row = row
        self.col = col

class Board:
    def __init__(self, grid: List[str]):
        self.M = len(grid)
        self.N = len(grid[0]) if self.M > 0 else 0
        self.grid = [list(row) for row in grid]
        self.tiles_by_color: Dict[str, List[Tile]] = defaultdict(list)
        self.empty_cells: List[Tuple[int,int]] = []
        self._index_tiles()

    def _index_tiles(self):
        for r in range(self.M):
            for c in range(self.N):
                cell = self.grid[r][c]
                if cell == '.':
                    self.empty_cells.append((r,c))
                else:
                    self.tiles_by_color[cell].append(Tile(cell,r,c))

    def all_colors(self) -> List[str]:
        return list(self.tiles_by_color.keys())

    def positions_of_color(self, color: str) -> List[Tile]:
        return self.tiles_by_color[color]

    def remove_color(self, color: str):
        for tile in self.tiles_by_color[color]:
            self.grid[tile.row][tile.col] = '.'
        del self.tiles_by_color[color]

    def clone(self):
        clone_board = Board(["".join(row) for row in self.grid])
        return clone_board

    def find_focused_tiles(self, r: int, c: int) -> List[Optional[Tile]]:
        # Given an empty cell (r,c), find tiles as per problem statement
        focused = []
        # Up
        fr = r-1
        while fr >= 0 and self.grid[fr][c] == '.':
            fr -= 1
        focused.append(Tile(self.grid[fr][c],fr,c) if fr >= 0 and self.grid[fr][c] != '.' else None)
        # Down
        fr = r+1
        while fr < self.M and self.grid[fr][c] == '.':
            fr += 1
        focused.append(Tile(self.grid[fr][c],fr,c) if fr < self.M and self.grid[fr][c] != '.' else None)
        # Left
        fc = c-1
        while fc >= 0 and self.grid[r][fc] == '.':
            fc -= 1
        focused.append(Tile(self.grid[r][fc],r,fc) if fc >= 0 and self.grid[r][fc] != '.' else None)
        # Right
        fc = c+1
        while fc < self.N and self.grid[r][fc] == '.':
            fc += 1
        focused.append(Tile(self.grid[r][fc],r,fc) if fc < self.N and self.grid[r][fc] != '.' else None)
        return focused

class Move:
    def __init__(self, pos: Tuple[int,int], tiles_to_remove: Set[str], points: int):
        self.pos = pos
        self.tiles_to_remove = tiles_to_remove
        self.points = points

class Solver:
    def __init__(self, board: Board):
        self.board = board
        self.memo: Dict[Tuple[int,...], int] = dict()
        self.color_id: Dict[str,int] = {c:i for i,c in enumerate(sorted(board.all_colors()))}
        # Each color occurs 2 times or 0 times
        # We encode state by bitmask presence of each color: 1 means color tiles remain, 0 means removed.
        self.full_state = (1<<len(self.color_id)) - 1

    def state_bitmask(self, board: Board) -> int:
        present = 0
        for color in self.color_id:
            if color in board.tiles_by_color:
                present |= (1<<self.color_id[color])
        return present

    def tiles_by_color_in_state(self, state: int) -> Set[str]:
        # return colors present in state
        return {c for c,i in self.color_id.items() if (state & (1<<i)) != 0}

    def can_remove(self, focused: List[Optional[Tile]]) -> Tuple[Set[str], int]:
        # Determine which colors have >= 2 tiles in focused tiles
        color_counts: Dict[str,int] = defaultdict(int)
        for t in focused:
            if t is not None:
                color_counts[t.color] += 1
        to_remove = set(c for c,count in color_counts.items() if count >= 2)
        points = 2 * len(to_remove)
        return (to_remove, points) if points > 0 else (set(),0)

    def solve(self) -> int:
        # DFS + Memo over bitmask state of colors remaining
        return self._dfs(self.full_state)

    def _dfs(self, state: int) -> int:
        if state == 0:
            return 0
        if state in self.memo:
            return self.memo[state]
        max_score = 0
        colors_remaining = self.tiles_by_color_in_state(state)
        # Rebuild board for this state
        cur_grid = [['.' for _ in range(self.board.N)] for _ in range(self.board.M)]
        for c in colors_remaining:
            for tile in self.board.positions_of_color(c):
                cur_grid[tile.row][tile.col] = c
        cur_board = Board([''.join(row) for row in cur_grid])
        # Consider all empty cells as move candidates
        for (r,c) in cur_board.empty_cells:
            focused = cur_board.find_focused_tiles(r,c)
            to_remove, points = self.can_remove(focused)
            if points == 0:
                continue
            # Remove those colors from state
            new_state = state
            for rem_color in to_remove:
                new_state &= ~(1 << self.color_id[rem_color])
            score = points + self._dfs(new_state)
            if score > max_score:
                max_score = score
        self.memo[state] = max_score
        return max_score

def main():
    import sys
    input = sys.stdin.readline
    M,N = map(int, input().split())
    grid = [input().rstrip('\n') for _ in range(M)]
    board = Board(grid)
    solver = Solver(board)
    print(solver.solve())

if __name__ == "__main__":
    main()