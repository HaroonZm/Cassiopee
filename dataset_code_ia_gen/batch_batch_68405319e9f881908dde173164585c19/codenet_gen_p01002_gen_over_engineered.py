from typing import List, Tuple, Dict, Set, Optional
from copy import deepcopy
from abc import ABC, abstractmethod

class BlockType:
    def __init__(self, id_: int, score: int):
        self.id = id_
        self.score = score

class BoardChangeListener(ABC):
    @abstractmethod
    def on_blocks_erased(self, positions: Set[Tuple[int,int]]):
        pass
    @abstractmethod
    def on_blocks_fallen(self):
        pass

class Board:
    WIDTH = 5
    HEIGHT = 5

    def __init__(self, grid: List[List[int]], block_scores: Dict[int,int]):
        self.grid = deepcopy(grid)
        self.block_scores = block_scores
        self.bonus = 1
        self.total_score = 0
        self.listener: Optional[BoardChangeListener] = None

    def set_listener(self, listener: BoardChangeListener):
        self.listener = listener

    def clone(self) -> 'Board':
        return Board(self.grid, self.block_scores)

    def get_block(self, r: int, c: int) -> int:
        return self.grid[r][c]

    def set_block(self, r: int, c: int, block: int):
        self.grid[r][c] = block

    # Swap two adjacent blocks (r1,c1) and (r2,c2)
    def swap(self, r1: int, c1: int, r2: int, c2: int):
        self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]

    def find_matches(self) -> Set[Tuple[int,int]]:
        # Return positions to erase: horizontal or vertical 3 or more same blocks lined
        to_erase = set()
        # Horizontal check
        for r in range(self.HEIGHT):
            count = 1
            for c in range(1, self.WIDTH):
                if self.grid[r][c] == self.grid[r][c-1] and self.grid[r][c] != 0:
                    count += 1
                else:
                    if count >= 3:
                        for cc in range(c - count, c):
                            to_erase.add((r, cc))
                    count = 1
            if count >= 3:
                for cc in range(self.WIDTH - count, self.WIDTH):
                    to_erase.add((r, cc))

        # Vertical check
        for c in range(self.WIDTH):
            count = 1
            for r in range(1, self.HEIGHT):
                if self.grid[r][c] == self.grid[r-1][c] and self.grid[r][c] != 0:
                    count += 1
                else:
                    if count >= 3:
                        for rr in range(r - count, r):
                            to_erase.add((rr, c))
                    count = 1
            if count >= 3:
                for rr in range(self.HEIGHT - count, self.HEIGHT):
                    to_erase.add((rr, c))
        return to_erase

    def erase_blocks(self, positions: Set[Tuple[int,int]]):
        # Add score and erase blocks
        gained = 0
        for r,c in positions:
            block_type = self.grid[r][c]
            if block_type != 0:
                gained += self.block_scores[block_type] * self.bonus
                self.grid[r][c] = 0
        self.total_score += gained
        if self.listener:
            self.listener.on_blocks_erased(positions)

    def apply_gravity(self):
        # Make blocks fall down to lowest empty cell
        for c in range(self.WIDTH):
            stack = []
            for r in range(self.HEIGHT):
                if self.grid[r][c] != 0:
                    stack.append(self.grid[r][c])
            # Fill from bottom
            for r in range(self.HEIGHT-1, -1, -1):
                if stack:
                    self.grid[r][c] = stack.pop()
                else:
                    self.grid[r][c] = 0
        if self.listener:
            self.listener.on_blocks_fallen()

    def do_full_elimination_cycle(self):
        # Perform elimination, gravity, bonus increments until no more matches
        while True:
            matches = self.find_matches()
            if not matches:
                break
            self.erase_blocks(matches)
            self.apply_gravity()
            self.bonus += 1

    def try_move_path(self, path: List[Tuple[int,int]]) -> int:
        # path: list of positions that the selected block occupies step by step
        # For each adjacent swap in path perform swap then do elimination
        b = self.clone()
        score_before = b.total_score
        # The selected block moves along the path exchanging blocks step by step
        for i in range(len(path)-1):
            r1,c1 = path[i]
            r2,c2 = path[i+1]
            b.swap(r1,c1,r2,c2)
        # After final move, do all elimination cycles
        b.do_full_elimination_cycle()
        gained = b.total_score - score_before
        return gained

class GameMovePlanner:
    def __init__(self, board: Board, max_moves: int):
        self.board = board
        self.n = max_moves
        self.best_score = 0

    def find_all_positions(self) -> List[Tuple[int,int]]:
        return [(r,c) for r in range(self.board.HEIGHT) for c in range(self.board.WIDTH)]

    def is_adjacent(self, p1: Tuple[int,int], p2: Tuple[int,int]) -> bool:
        r1,c1 = p1
        r2,c2 = p2
        return (abs(r1-r2) == 1 and c1 == c2) or (abs(c1-c2) == 1 and r1 == r2)

    def generate_all_paths(self, start: Tuple[int,int], max_len: int) -> List[List[Tuple[int,int]]]:
        # BFS/DFS for paths of length up to max_len + 1 (positions count)
        # The path represents block's successive positions after swaps.
        # Positions can be revisited - cycles allowed.
        paths = []

        def dfs(current_path):
            if len(current_path)-1 > max_len:
                return
            paths.append(current_path[:])
            last_pos = current_path[-1]
            for delta_r, delta_c in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = last_pos[0]+delta_r, last_pos[1]+delta_c
                if 0 <= nr < self.board.HEIGHT and 0 <= nc < self.board.WIDTH:
                    dfs(current_path + [(nr,nc)])

        dfs([start])
        return paths

    def solve(self) -> int:
        initial_score = self.compute_score_of_no_move()
        self.best_score = initial_score
        for start_pos in self.find_all_positions():
            all_paths = self.generate_all_paths(start_pos, self.n)
            for path in all_paths:
                if len(path) < 2:
                    # no move or zero move
                    # consider doing no move if n=0 or allowed
                    if self.n == 0:
                        # zero moves, direct elimination
                        b = self.board.clone()
                        b.do_full_elimination_cycle()
                        if b.total_score > self.best_score:
                            self.best_score = b.total_score
                    continue
                # try moving along path
                gained = self.board.try_move_path(path)
                if gained > self.best_score:
                    self.best_score = gained
        return self.best_score

    def compute_score_of_no_move(self) -> int:
        b = self.board.clone()
        b.do_full_elimination_cycle()
        return b.total_score


def parse_input() -> List[Tuple[int, List[List[int]], List[int]]]:
    datasets = []
    while True:
        n_line = input().strip()
        if n_line == '':
            continue
        n = int(n_line)
        if n == -1:
            break
        grid = []
        for _ in range(5):
            row = list(map(int, input().split()))
            grid.append(row)
        scores = list(map(int, input().split()))
        datasets.append((n, grid, scores))
    return datasets

def main():
    datasets = parse_input()
    for n, grid, scores in datasets:
        block_scores = {i+1:scores[i] for i in range(5)}
        board = Board(grid, block_scores)
        planner = GameMovePlanner(board, n)
        print(planner.solve())

if __name__ == '__main__':
    main()