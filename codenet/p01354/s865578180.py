import sys
def solve():
    readline = sys.stdin.buffer.readline
    write = sys.stdout.buffer.write
    M, N = map(int, readline().split())
    P = [list(map(float, readline().split())) + [0] for i in range(M)]
    M2 = (1 << M)
    dp = [[0]*(N+1) for i in range(M2)]
    dp[0][N] = 1
    for state in range(1, M2):
        dps = dp[state]
        for k in range(M):
            if state & (1 << k) == 0:
                continue
            pk = P[k]
            dpk = dp[state ^ (1 << k)]
            s = 0
            for i in range(N, -1, -1):
                s += dpk[i] * (1 - pk[i])
                dps[i] = max(dps[i], s)
                s *= pk[i-1]
    write(b"%.16f\n" % dp[M2-1][0])
solve()