from typing import List, Tuple, Set, Optional

class Stone:
    def __init__(self, digit: int):
        self.digit = digit
        self.disappeared = False

    def __repr__(self):
        return f"{self.digit if not self.disappeared else '.'}"

class Board:
    WIDTH = 5

    def __init__(self, rows: List[List[int]]):
        # board as H rows x WIDTH cols, top row is rows[0]
        self.height = len(rows)
        self.grid: List[List[Optional[Stone]]] = [
            [Stone(d) for d in row] for row in rows
        ]
        self.score = 0

    def _find_chains_to_disappear(self) -> Set[Tuple[int,int]]:
        to_disappear = set()
        for r in range(self.height):
            c = 0
            while c < Board.WIDTH:
                cur_stone = self.grid[r][c]
                if cur_stone is None or cur_stone.disappeared:
                    c += 1
                    continue
                digit = cur_stone.digit
                start = c
                while c < Board.WIDTH and self.grid[r][c] is not None and not self.grid[r][c].disappeared and self.grid[r][c].digit == digit:
                    c += 1
                length = c - start
                if length >= 3:
                    for cc in range(start, c):
                        to_disappear.add((r, cc))
                # If length < 3, we already moved c forward, so continue without incrementing c again.
        return to_disappear

    def _disappear_stones(self, positions: Set[Tuple[int,int]]) -> int:
        disappeared_score = 0
        for r,c in positions:
            stone = self.grid[r][c]
            if stone is not None and not stone.disappeared:
                stone.disappeared = True
                disappeared_score += stone.digit
        return disappeared_score

    def _drop_stones(self):
        # For each column, simulate gravity: stones fall down to fill disappeared stones
        for c in range(Board.WIDTH):
            stack = []
            # Collect stones that have not disappeared
            for r in range(self.height-1, -1, -1):
                stone = self.grid[r][c]
                if stone is not None and not stone.disappeared:
                    stack.append(stone)
            # Fill from bottom up with stones in stack, fill remainder with None
            for r in range(self.height-1, -1, -1):
                if stack:
                    self.grid[r][c] = stack.pop(0)
                else:
                    self.grid[r][c] = None

    def step(self) -> bool:
        """
        Perform one full step:
        - find all horizontal chains of 3+ same digit stones
        - disappear them simultaneously
        - drop stones above disappeared stones
        Return True if any stones disappeared, False otherwise.
        """
        chains = self._find_chains_to_disappear()
        if not chains:
            return False
        gained = self._disappear_stones(chains)
        self.score += gained
        self._drop_stones()
        return True

    def solve(self) -> int:
        """
        Solve the puzzle by repeating steps until no more disappearances occur.
        Return the total score of disappeared stones.
        """
        while self.step():
            pass
        return self.score

class PuzzleParser:
    def __init__(self):
        self.datasets = []

    def parse_input(self, lines: List[str]):
        idx = 0
        while idx < len(lines):
            h_line = lines[idx].strip()
            idx += 1
            if h_line == "0":
                break
            h = int(h_line)
            rows = []
            for _ in range(h):
                row_str = lines[idx].strip()
                idx += 1
                nums = list(map(int, row_str.split()))
                rows.append(nums)
            self.datasets.append(rows)

class PuzzleSolver:
    def __init__(self, datasets: List[List[List[int]]]):
        self.datasets = datasets

    def run(self) -> List[int]:
        results = []
        for data in self.datasets:
            board = Board(data)
            score = board.solve()
            results.append(score)
        return results

def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    parser = PuzzleParser()
    parser.parse_input(input_lines)
    solver = PuzzleSolver(parser.datasets)
    results = solver.run()
    for res in results:
        print(res)

if __name__ == "__main__":
    main()