# seishin.py
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    MOD = 10**9 + 7
    N = int(readline())
    M = 20
    L = 26
    ca = ord('a')
    cq = ord('?')
    S = [[ca-1]*M for i in range(N)]
    for i in range(N):
        s = readline().strip()
        S[i][:len(s)] = map(ord, s)

    memo = [[[[-1]*(L+2) for i in range(M+1)] for j in range(N+1)] for k in range(N+1)]
    for i in range(N+1):
        for p in range(M+1):
            for c in range(L+2):
                memo[i][i][p][c] = 1
    for i in range(N+1):
        for j in range(i+1, N+1):
            for p in range(M+1):
                memo[i][j][p][L+1] = 0
            for c in range(L+2):
                memo[i][j][M][c] = (i+1 == j)

    def dfs(l, r, p, c):
        if memo[l][r][p][c] != -1:
            return memo[l][r][p][c]
        res = dfs(l, r, p, c+1)
        for i in range(l+1, r+1):
            if (S[i-1][p] != ca + c - 1) if S[i-1][p] != cq else (c == 0):
                break
            res += dfs(l, i, p+1, 0) * dfs(i, r, p, c+1) % MOD
        memo[l][r][p][c] = res = res % MOD
        return res
    write("%d\n" % dfs(0, N, 0, 0))
solve()