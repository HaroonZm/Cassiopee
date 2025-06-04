import sys
from collections import defaultdict

sys.setrecursionlimit(pow(2, 31) - 1)

N, M = map(int, input().split())
values = []
for _ in range(M):
    values.append(tuple(map(int, input().split())))

succ = defaultdict(list)
for s, d in values:
    succ[s].append(d)

dp = defaultdict(lambda: -1)

for vertex in frozenset(succ.keys()):
    # Instead of the dfs function, perform all logic inline
    stack = [(vertex, False)]
    local_stack = []
    while stack:
        v, visited = stack.pop()
        if visited:
            length = 0
            for s in succ[v]:
                length = max(length, 1 + dp[s])
            dp[v] = length
        elif dp[v] == -1:
            stack.append((v, True))
            for s in succ[v]:
                if dp[s] == -1:
                    stack.append((s, False))

result = 0
for v in dp:
    result = max(result, dp[v])

print(result)