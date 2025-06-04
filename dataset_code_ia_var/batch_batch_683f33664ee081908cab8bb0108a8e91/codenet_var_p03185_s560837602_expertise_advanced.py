from sys import stdin
from itertools import accumulate
from collections import deque

n, C, *H = map(int, stdin.read().split())

p = [0]
P = deque([0])

for i, h in enumerate(H[1:], 1):
    def slope(x, y):
        dx = H[P[x]] - H[P[y]]
        dp = p[P[y]] - p[P[x]]
        return dp / dx - H[P[y]] - H[P[x]] + 2 * h

    while len(P) > 1 and slope(1, 0) > 0:
        P.popleft()

    p.append(p[P[0]] + (H[P[0]] - h) ** 2 + C)
    P.append(i)

    while len(P) > 2 and slope(-1, -2) > slope(-2, -3):
        P.remove(P[-2])

print(p[-1])