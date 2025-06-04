from itertools import pairwise
from sys import stdin

N, A, B = map(int, stdin.readline().split())
X = list(map(int, stdin.readline().split()))

ans = sum(
    min(A * (x2 - x1), B)
    for x1, x2 in pairwise(X)
)

print(ans)