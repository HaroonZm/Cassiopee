import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v, p = -1):
    deg[v] = len(U[v])
    dp[v] = [0] * deg[v]
    ans = 1
    for i in range(deg[v]):
        u = U[v][i]
        if u == p:
            par[v] = i
            continue
        dp[v][i] = dfs(u, v)
        ans *= dp[v][i] + 1
        ans %= M
    return(ans)

def bfs(v, ans_p = 0, p = -1):
    if p != -1:
        dp[v][par[v]] = ans_p
    lmul = [1] * (deg[v] + 1)
    rmul = [1] * (deg[v] + 1)
    for i in range(1, deg[v] + 1):
        lmul[i] = lmul[i - 1] * (dp[v][i - 1] + 1) % M
        rmul[-i - 1] = rmul[-i] * (dp[v][-i] + 1) % M
    ans[v] = rmul[0]
    for i in range(deg[v]):
        u = U[v][i]
        if u == p:
            continue
        bfs(u, lmul[i] * rmul[i + 1] % M, v)

N, M = map(int, input().split()) # 1 <= N <= 10^5, 2 <= M <= 10^9
U = [list() for _ in range(N)]
for x, y in [map(int, input().split()) for _ in range(N - 1)]:
    U[x - 1].append(y - 1)
    U[y - 1].append(x - 1)
deg = [0] * N
par = [0] * N
dp = [None] * N
ans = [0] * N
dfs(0)
bfs(0)
print("\n".join([str(x) for x in ans]))