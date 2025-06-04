import sys
readline = sys.stdin.readline
write = sys.stdout.write
from collections import deque

def solve():
    MOD = 10**9 + 7
    N = int(readline())
    dp0 = [[[0]*(N+1) for i in range(N+1)] for j in range(N+1)]
    dp0[0][0][0] = 1
    for c in range(1, N+1):
        for a in range(N+1):
            for b in range(N+1):
                r = 0
                if a:
                    r += dp0[c-1][a-1][b]
                if b:
                    r += dp0[c-1][a][b-1]
                if a and b:
                    r += dp0[c-1][a-1][b-1]
                dp0[c][a][b] = r % MOD
    G = [[] for i in range(N)]
    deg = [0]*N
    for i in range(N-1):
        a, b = map(int, readline().split())
        G[a].append(b)
        deg[b] += 1
    r = 0
    for i in range(N):
        if deg[i] == 0:
            r = i
            break
    que = deque([r])
    vs = []
    while que:
        v = que.popleft()
        vs.append(v)
        for w in G[v]:
            que.append(w)
    vs.reverse()
    hs = [0]*N
    for v in vs:
        e = 0
        for w in G[v]:
            e = max(e, hs[w] + 1)
        hs[v] = e
    def dfs(v):
        res = [1]
        hv = 0
        for w in G[v]:
            r = dfs(w)
            hw = len(r)-1
            r0 = [0]*(hv+hw+1)
            for i in range(hv+1):
                for j in range(hw+1):
                    for k in range(max(i, j), i+j+1):
                        r0[k] += res[i] * r[j] * dp0[k][i][j] % MOD
            res = r0
            hv += hw
        return [0] + res
    write("%d\n" % (sum(dfs(r)) % MOD))
solve()