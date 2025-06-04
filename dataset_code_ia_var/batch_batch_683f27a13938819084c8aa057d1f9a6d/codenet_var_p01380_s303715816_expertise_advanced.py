from sys import stdin, setrecursionlimit
from math import inf

setrecursionlimit(10_000_000)

n = int(stdin.readline())
ls = [tuple(map(int, stdin.readline().split()))[::-1] for _ in range(n)]
ls.sort()

DP = [0] + [inf] * n

for b, a in ls:
    for i in range(n, 0, -1):
        if DP[i-1] + a <= b:
            DP[i] = min(DP[i], DP[i-1] + a)

print(max(i for i, v in enumerate(DP) if v < inf))