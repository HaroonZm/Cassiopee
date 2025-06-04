import sys
from functools import reduce
from operator import mul
from itertools import accumulate

input = sys.stdin.readline
sys.setrecursionlimit(1 << 20)

def dfs(node, parent=-1):
    neighbors = U[node]
    deg[node] = d = len(neighbors)
    dp[node] = arr = [0] * d
    res = 1
    for i, child in enumerate(neighbors):
        if child == parent:
            par[node] = i
            continue
        arr[i] = dfs(child, node)
        res = (res * (arr[i] + 1)) % M
    return res

def bfs(node, incoming=0, parent=-1):
    if parent != -1:
        dp[node][par[node]] = incoming
    vals = [x + 1 for x in dp[node]]
    lprod = [1] + list(accumulate(vals, lambda x, y: x * y % M))
    rprod = list(accumulate(reversed(vals), lambda x, y: x * y % M, initial=1))[::-1]
    ans[node] = rprod[0]
    for i, child in enumerate(U[node]):
        if child == parent:
            continue
        bfs(child, lprod[i] * rprod[i + 1] % M, node)

N, M = map(int, input().split())
U = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    U[x - 1].append(y - 1)
    U[y - 1].append(x - 1)

deg = [0] * N
par = [0] * N
dp = [None] * N
ans = [0] * N

dfs(0)
bfs(0)
print(*ans, sep='\n')