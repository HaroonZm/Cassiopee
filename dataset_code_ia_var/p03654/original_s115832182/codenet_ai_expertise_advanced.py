import sys
from collections import defaultdict
from itertools import starmap
from operator import itemgetter

input = sys.stdin.readline

n = int(input())
abd = [tuple(map(int, input().split())) for _ in range(n - 1)]

if n == 2:
    print(abd[0][2])
    sys.exit()

graph = defaultdict(list)
deg = [0] * (n + 1)
for a, b, d in abd:
    graph[a].append((b, d))
    graph[b].append((a, d))
    deg[a] += 1
    deg[b] += 1

leaves = [i for i in range(1, n + 1) if deg[i] == 1]
root = next((i for i in range(1, n + 1) if deg[i] != 1), 1)
deg[root] += 1  # ensure root is never declared as leaf

dp = [[] for _ in range(n + 1)]
sm = [1] * (n + 1)
mx = [0] * (n + 1)
stack = leaves.copy()
ans, flg = 0, False

while stack:
    x = stack.pop()
    if dp[x]:
        sm[x] += sum(dp[x])
    if sm[x] * 2 == n:
        flg = True
    for y, d in graph[x]:
        if deg[y] > 1:
            dp[y].append(sm[x])
            c = min(sm[x], n - sm[x])
            if sm[x] == n - sm[x]:
                ans += (sm[x] * 2 - 1) * d
            else:
                ans += c * 2 * d
            deg[y] -= 1
            if deg[y] == 1:
                stack.append(y)

if flg:
    print(ans)
    sys.exit()

# Advanced selection using generator and inline max-computation
for a, b, d in abd:
    for v in (a, b):
        if not mx[v]:
            mx[v] = max((max(dp[v]) if dp[v] else 0), n - 1 - sm[v] if dp[v] else n - 2)
mn_edge = min(
    (d for (a, b, d) in abd if min(mx[a], mx[b]) * 2 < n),
    default=float('inf')
)

print(ans - mn_edge if mn_edge != float('inf') else ans)