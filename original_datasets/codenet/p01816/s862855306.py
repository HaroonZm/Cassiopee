from collections import deque
from itertools import permutations
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M = map(int, readline().split())
    OP = [0]*N
    ops = ["T=T&X\n", "T=T&Y\n", "T=T|X\n", "T=T|Y\n", "T=T^X\n", "T=T^Y\n"]
    for i in range(N-1):
        s = readline()
        OP[i+1] = ops.index(s)
    G = [[] for i in range(N)]
    for i in range(N-1):
        u, v = map(int, readline().split())
        G[u].append(v)
        G[v].append(u)
    used = [0]*N
    used[0] = 1
    P = [-1]*N
    V = []
    D = [0]*N
    que = deque([0])
    for i in range(N):
        v = que.popleft()
        d = D[v]+1
        for w in G[v]:
            if used[w]:
                continue
            used[w] = 1
            que.append(w)
            P[w] = v
            D[w] = d
            V.append(w)
    def check(x, y):
        S = [0]*N
        for v in V:
            op = OP[v]
            s = S[P[v]]
            if op & 1:
                if op & 2:
                    s |= y
                elif op & 4:
                    s ^= y
                else:
                    s &= y
            else:
                if op & 2:
                    s |= x
                elif op & 4:
                    s ^= x
                else:
                    s &= x
            S[v] = s
        T = [-1]*N
        for v in reversed(V):
            if T[v] == -1:
                T[v] = S[v]
            p = P[v]
            if D[v] & 1:
                T[p] = max(T[p], T[v]) if T[p] != -1 else T[v]
            else:
                T[p] = min(T[p], T[v]) if T[p] != -1 else T[v]
        return T[0]

    Q = [(1, 1), (1, 0), (0, 1)]
    R = {}
    for (x0, y0), (x1, y1), (x2, y2) in permutations(Q):
        x = x0 + x1*2 + x2*4
        y = y0 + y1*2 + y2*4
        d = check(x, y)
        d0 = d & 1; d1 = +((d & 2) > 0); d2 = +((d & 4) > 0)
        R[(x0, x1, x2), (y0, y1, y2)] = (d0, d1, d2)
        R[(x1, x2), (y1, y2)] = (d1, d2)
        R[(x2,), (y2,)] = (d2,)
    for i in range(M):
        x, y = map(int, readline().split())
        c = 0
        E = {}
        Q = []
        x0 = x; y0 = y
        while x0 or y0:
            x1 = x0 & 1; y1 = y0 & 1
            if x1 or y1:
                E[x1, y1] = c
            Q.append((x1, y1))
            x0 >>= 1; y0 >>= 1
            c += 1
        if not E:
            write("0\n")
            continue
        *S, = E.keys()
        S.sort(key = E.__getitem__)
        x1 = tuple(p for p, q in S)
        y1 = tuple(q for p, q in S)
        d1 = R[x1, y1]
        for p, q, d in zip(x1, y1, d1):
            E[p, q] = d
        Q.reverse()
        ans = 0
        for p, q in Q:
            if p or q:
                ans = (ans << 1) | E[p, q]
            else:
                ans <<= 1
        write("%d\n" % ans)
solve()