from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, M = map(int, readline().split())
    G = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, readline().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    col = [-1]*N
    C = {}
    L0 = 0
    L = 0
    for i in range(N):
        if col[i] != -1:
            continue
        que = deque([i])
        col[i] = 0
        cs = [1, 0]
        while que:
            v = que.popleft()
            c = col[v]^1
            for w in G[v]:
                if col[w] != -1:
                    if col[w] != c:
                        write("-1\n")
                        return
                else:
                    col[w] = c
                    cs[c] += 1
                    que.append(w)
        e = abs(cs[1] - cs[0])
        L += e
        if e > 0:
            C[e] = C.get(e, 0) + 1
    W = L//2
    dp = [0]*(W+1)
    dp[0] = 1
    for v, c in C.items():
        for b in range(v):
            s = 0
            k0 = (W - b) // v * v + b
            for i in range(c):
                if k0-v*i >= 0:
                    s += dp[k0-v*i]
            for k in range(k0, -1, -v):
                s -= dp[k]
                if k-c*v >= 0:
                    s += dp[k-c*v]
                if s:
                    dp[k] = 1
    k = 0
    for i in range(W, -1, -1):
        if dp[i]:
            k = i
            break
    A = (N - L) // 2 + k
    B = (N - L) // 2 + L - k
    write("%d\n" % (A*B - M))
solve()