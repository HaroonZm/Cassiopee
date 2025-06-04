import sys
sys.setrecursionlimit(10**7)

N, E, T = map(int, input().split())
W = list(map(int, input().split()))

rules = [[] for _ in range(N+1)]
for _ in range(E):
    line = list(map(int, input().split()))
    G = line[0]
    C = line[1]
    S = line[2:]
    rules[G].append(S)

INF = 10**9
memo = {}

def dfs(m):
    if m in memo:
        return memo[m]
    if W[m-1] == 1:
        memo[m] = 1
        return 1
    if not rules[m]:
        memo[m] = INF
        return INF
    res = INF
    for comb in rules[m]:
        ssum = 0
        used = set()
        ok = True
        for x in comb:
            if x in used:
                ok = False
                break
            used.add(x)
            val = dfs(x)
            if val == INF:
                ok = False
                break
            ssum += val
        if ok:
            if ssum < res:
                res = ssum
    memo[m] = res
    return res

ans = dfs(T)
if ans == INF:
    print(-1)
else:
    print(ans)