import sys
from collections import deque
from typing import Deque, Tuple

input = sys.stdin.readline

class ConvexHullTrick:
    def __init__(self):
        self.lines: Deque[Tuple[int, int]] = deque()

    @staticmethod
    def is_redundant(l1, l2, l3):
        # Cross-multiplication to avoid floating-point division
        return (l2[0] - l1[0]) * (l3[1] - l2[1]) >= (l2[1] - l1[1]) * (l3[0] - l2[0])

    @staticmethod
    def evaluate(line, x):
        return line[0] * x + line[1]

    def add(self, a: int, b: int):
        line = (a, b)
        while len(self.lines) >= 2 and self.is_redundant(self.lines[-2], self.lines[-1], line):
            self.lines.pop()
        self.lines.append(line)

    def query(self, x: int) -> int:
        while len(self.lines) >= 2 and self.evaluate(self.lines[0], x) >= self.evaluate(self.lines[1], x):
            self.lines.popleft()
        return self.evaluate(self.lines[0], x)

def main():
    n, c = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [0] * n

    cht = ConvexHullTrick()
    cht.add(-2 * h[0], h[0] ** 2)

    for i in range(1, n):
        dp[i] = cht.query(h[i]) + h[i] ** 2 + c
        cht.add(-2 * h[i], h[i] ** 2 + dp[i])

    print(dp[-1])

if __name__ == "__main__":
    main()