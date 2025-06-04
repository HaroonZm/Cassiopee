from bisect import bisect
from heapq import heappush, heappop
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    cA = ord('A')
    ds = "LURD"
    hi, hm = map(int, readline().split())
    if hi == hm == 0:
        return False
    R, C = map(int, readline().split())
    A = [list(map(lambda x: (ord(x) - cA), readline().strip())) for i in range(R)]
    T = int(readline())
    D = [0]*26
    for i in range(T):
        c, d = readline().split()
        D[ord(c) - cA] = int(d)
    RS = [D[A[0][0]]]
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    x = 0; y = 0
    S = int(readline())
    for i in range(S):
        c, n = readline().split()
        dx, dy = dd[ds.index(c)]
        for j in range(int(n)):
            x += dx; y += dy
            v = D[A[y][x]]
            if v:
                RS.append(v)
    L = len(RS)
    SS = [0]*(L+1)
    for i in range(L):
        SS[i+1] = SS[i] + RS[i]
    def check(h, i):
        idx = bisect(SS, SS[i] + h - 1)
        return h - (SS[idx-1] - SS[i]), idx-1
    P = int(readline())
    PS = [int(readline()) for i in range(P)]
    INF = 10**18
    D = [INF]*(1 << P)
    D[0] = 0
    C = [0]*(L+1)
    U = [0]*(1 << P)
    hi, k = check(hi, 0)
    que = [(0, 0, k, hi)]
    while que:
        df, state, k, h0 = heappop(que)
        if D[state] < df or U[state]:
            continue
        C[k] += 1
        U[state] = 1
        for i in range(P):
            n_state = state | (1 << i)
            if state == n_state:
                continue
            h, k0 = check(min(h0 + PS[i], hm), k)
            n_df = df + max(h0 + PS[i] - hm, 0)
            if n_df < D[n_state]:
                heappush(que, (n_df, n_state, k0, h))
    if C[L]:
        write("YES\n")
    else:
        write("NO\n")
    return True
while solve():
    ...