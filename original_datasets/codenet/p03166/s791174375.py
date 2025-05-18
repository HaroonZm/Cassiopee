import sys

sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

inf = float('inf')

def rec(v):
    if used[v]:
        return dp[v]
    used[v] = True
    res = 0
    for u in es[v]:
        res = max(res, rec(u) + 1)
    dp[v] = res
    return res

n, m = map(int, input().split())

es = tuple(set() for _ in range(n))
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    es[x].add(y)

used = [False] * n
dp = [inf] * n

ans = 0
for i in range(n):
    ans = max(ans, rec(i))
print(ans)