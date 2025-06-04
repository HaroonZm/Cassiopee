from functools import reduce
from bisect import bisect_left

class ConvexHullTrick:
    __slots__ = 'lines',   # Optimise memory usage

    def __init__(self):
        self.lines = []

    def _is_bad(self, l1, l2, l3):
        # Uses cross-multiplication to avoid division and floating errors
        (a1, b1), (a2, b2), (a3, b3) = l1, l2, l3
        return (b3 - b2) * (a2 - a1) <= (b2 - b1) * (a3 - a2)

    def add_line(self, a, b):
        line = (a, b)
        while len(self.lines) >= 2 and self._is_bad(self.lines[-2], self.lines[-1], line):
            self.lines.pop()
        self.lines.append(line)

    def query(self, x):
        # Because x's are increasing, we can use pointer-like binary search
        l, r = 0, len(self.lines) - 1
        while l < r:
            m = (l + r) // 2
            y1 = self.lines[m][0] * x + self.lines[m][1]
            y2 = self.lines[m + 1][0] * x + self.lines[m + 1][1]
            if y1 <= y2:
                r = m
            else:
                l = m + 1
        a, b = self.lines[l]
        return a * x + b

def solve():
    import sys

    N, C = map(int, sys.stdin.readline().split())
    hs = list(map(int, sys.stdin.readline().split()))
    dp = [0] * N
    cht = ConvexHullTrick()
    for i in range(1, N):
        cht.add_line(-2 * hs[i-1], dp[i-1] + hs[i-1] ** 2)
        dp[i] = cht.query(hs[i]) + hs[i] ** 2 + C
    print(dp[-1])

solve()