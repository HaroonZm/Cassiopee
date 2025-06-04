import sys
from collections import defaultdict
from functools import lru_cache

sys.setrecursionlimit(10_000_000)

MOD = 10**30 + 7
TREE_MOD = 10**9 + 7

N = int(input())
E = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

m = defaultdict(int)

def func(num, pre):
    S = 1
    for to in E[num]:
        if to != pre:
            S = (S + func(to, num) * TREE_MOD) % MOD
    m[S] += 1
    return S

func(0, -1)

ans = sum(v * (v - 1) // 2 for v in m.values())
print(ans)