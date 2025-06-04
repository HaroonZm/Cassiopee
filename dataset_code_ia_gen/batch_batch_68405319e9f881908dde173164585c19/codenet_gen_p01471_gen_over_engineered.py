import sys
from typing import List, Tuple, Protocol

class InputReader(Protocol):
    def read(self) -> Tuple[int, int, List[Tuple[int,int]]]:
        ...

class StdInputReader:
    def read(self) -> Tuple[int, int, List[Tuple[int,int]]]:
        input=sys.stdin.readline
        N, W = map(int, input().split())
        items = [tuple(map(int, input().split())) for _ in range(N)]
        return N, W, items

class Item:
    def __init__(self, w: int, v: int) -> None:
        self.w = w
        self.v = v
        self.ratio = self._compute_ratio()
    
    def _compute_ratio(self) -> float:
        # handle zero weight case safely, but problem states |w_i|<=10^4 and all integers
        if self.w == 0:
            # If w=0 and v>0, ratio is +inf, else -inf or 0. Always handle to put items with w=0 appropriately.
            if self.v > 0:
                return float('inf')
            elif self.v < 0:
                return float('-inf')
            else:
                return 0.0
        return self.v / self.w

    def __lt__(self, other: 'Item') -> bool:
        # sort descending by ratio
        return self.ratio > other.ratio

class FractionalKnapsackSolver:
    def __init__(self, N: int, W: int, items_data: List[Tuple[int,int]]) -> None:
        self.N = N
        self.W = W
        self.items = [Item(w, v) for w, v in items_data]
    
    def solve(self) -> float:
        # Because w_i and v_i can be negative, we must be careful and consider the greedy approach properly.
        # Sort by ratio descending
        self.items.sort()

        total_value = 0.0
        remaining_capacity = self.W

        for item in self.items:
            if remaining_capacity == 0:
                break
            # Because w_i can be negative or zero, we must consider carefully
            # Approach:
            # - For positive weight: take min(1, remaining_capacity / w_i)
            # - For zero weight items with positive value: take all (x_i in [0,1], max is 1)
            # - For negative weights, this is tricky: since 0<=x_i<=1 and we want to maximize value
            #   For negative w and positive v, taking full x_i=1 reduces total weight (since w_i negative),
            #   increasing capacity effectively. So we want to take x_i=1 if it improves total.
            # So we will implement a linear programming style greedy:
            # At each item try to take full 1 if possible, else fractional to fit constraints.

            w = item.w
            v = item.v

            if w > 0:
                # maximum fraction we can take for this item without exceeding capacity
                frac = min(1, remaining_capacity / w)
                total_value += v * frac
                remaining_capacity -= w * frac
            elif w == 0:
                # weight zero: if value >0 take fully, else skip
                if v > 0:
                    total_value += v * 1
                    # no capacity change
                # else value <=0 take 0 to maximize
            else:
                # w < 0
                # Taking fraction x_i in [0,1] will reduce total weight by abs(w)*x_i, increasing capacity by that much.
                # We want to max value, so if v>0 take fully x_i=1, else 0
                if v > 0:
                    total_value += v * 1
                    remaining_capacity -= w * 1 # since w<0, remaining_capacity increases
                # else v <=0 skip taking

            # no lower bound violation check because x_i in [0,1]

        return total_value

class OutputWriter:
    def write(self, val: float) -> None:
        # print with 6 decimal places, making sure error <1e-3
        print(f"{val:.6f}")

class Solution:
    def __init__(self, reader: InputReader, writer: OutputWriter) -> None:
        self.reader = reader
        self.writer = writer

    def run(self) -> None:
        N, W, items = self.reader.read()
        solver = FractionalKnapsackSolver(N, W, items)
        ans = solver.solve()
        self.writer.write(ans)

if __name__ == "__main__":
    sol = Solution(StdInputReader(), OutputWriter())
    sol.run()