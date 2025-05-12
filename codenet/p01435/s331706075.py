from heapq import heappush, heappop
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, E, T = map(int, readline().split())
    *W, = map(int, readline().split())
    G = [[] for i in range(N)]
    R = [[] for i in range(N)]
    C = [0]*E
    Q = [None]*E
    for i in range(E):
        g, c, *s = map(int, readline().split())
        for e in s:
            R[e-1].append(i)
        C[i] = c
        Q[i] = (g, s)
    que = []
    INF = 10**9
    def calc(s):
        s.sort(key = lambda x: dp[x-1], reverse=1)
        r = 0
        for i, j in enumerate(s):
            r = max(r, i + dp[j-1])
        return r

    dp = [INF]*N
    for i in range(N):
        if W[i]:
            dp[i] = 1
            for j in R[i]:
                C[j] -= 1
                if C[j] == 0:
                    g0, s0 = Q[j]
                    heappush(que, (calc(s0), j))
    while que:
        cost, e = heappop(que)
        g, s = Q[e]
        if dp[g-1] < cost:
            continue
        if cost < dp[g-1]:
            dp[g-1] = cost
            for j in R[g-1]:
                C[j] -= 1
                if C[j] <= 0:
                    g0, s0 = Q[j]
                    heappush(que, (calc(s0), j))
    if dp[T-1] != INF:
        write("%d\n" % dp[T-1])
    else:
        write("-1\n")
solve()