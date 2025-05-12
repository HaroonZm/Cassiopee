import sys
sys.setrecursionlimit(10**5)

def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write

    N, M, L = map(int, readline().split())
    *K, = map(int, readline().split())
    *S, = map(int, readline().split())
    su = [0]*(M+1)
    r = 0
    for i in range(M):
        su[i+1] = r = r + S[i]
    K.sort()
    memo = [[-1]*N for i in range(N)]
    def calc(a, b):
        sa = K[a]; sb = K[b]
        if not sa < sb:
            sa, sb = sb, sa
        return (su[sb] - su[sa-1]) // L
    def dfs(i, a, b):
        if i == N:
            return calc(a, b)
        if memo[a][b] != -1:
            return memo[a][b]
        r = min(dfs(i+1, a, i) + calc(b, i), dfs(i+1, b, i) + calc(a, i))
        memo[a][b] = r
        return r
    write("%d\n" % dfs(1, 0, 0))
solve()