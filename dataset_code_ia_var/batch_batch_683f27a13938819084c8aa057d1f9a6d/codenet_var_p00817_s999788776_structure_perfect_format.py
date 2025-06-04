from collections import deque
import sys

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, p1, p2 = map(int, readline().split())
    if N == p1 == p2 == 0:
        return False
    P = p1 + p2
    G = [[] for _ in range(P)]
    for _ in range(N):
        x, y, a = readline().strip().split()
        x = int(x)
        y = int(y)
        d = (a == "no")
        if x == y:
            continue
        G[x - 1].append((y - 1, d))
        G[y - 1].append((x - 1, d))
    L = [-1] * P
    ok = 1
    U = []
    for i in range(P):
        if L[i] != -1:
            continue
        que = deque([i])
        L[i] = 0
        cs = [[], []]
        while que:
            v = que.popleft()
            e = L[v]
            cs[e].append(v + 1)
            for w, d in G[v]:
                if L[w] != -1:
                    if L[w] != (e ^ d):
                        ok = 0
                    continue
                L[w] = e ^ d
                que.append(w)
        a, b = map(len, cs)
        if a == b:
            ok = 0
        U.append((cs[0], cs[1]))
    if not ok:
        write("no\n")
        return True
    S = [0] * (p1 + 1)
    S[0] = 1
    SS = [S]
    M = len(U)
    for c0, c1 in U:
        p = len(c0)
        q = len(c1)
        T = [0] * (p1 + 1)
        for i in range(p1 + 1):
            if S[i]:
                if i + p <= p1:
                    T[i + p] += S[i]
                if i + q <= p1:
                    T[i + q] += S[i]
        SS.append(T)
        S = T
    if S[p1] > 1:
        write("no\n")
        return True
    ans = []
    rest = p1
    for i in range(M - 1, -1, -1):
        T0 = SS[i]
        c0, c1 = U[i]
        p = len(c0)
        q = len(c1)
        if rest - p >= 0 and T0[rest - p]:
            ans.extend(c0)
            rest -= p
        else:
            ans.extend(c1)
            rest -= q
    if ans:
        ans.sort()
        write("\n".join(map(str, ans)))
        write("\n")
    write("end\n")
    return True

while solve():
    ...