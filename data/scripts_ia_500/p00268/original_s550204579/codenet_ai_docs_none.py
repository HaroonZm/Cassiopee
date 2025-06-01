from math import atan2
from collections import defaultdict, deque
def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
def convex_hull(ps):
    qs = []
    n = len(ps)
    for p in ps:
        while len(qs)>1 and cross(qs[-1], qs[-2], p) > 0:
            qs.pop()
        qs.append(p)
    t = len(qs)
    for i in range(n-2, -1, -1):
        p = ps[i]
        while len(qs)>t and cross(qs[-1], qs[-2], p) > 0:
            qs.pop()
        qs.append(p)
    return qs
def outer_check(R, S):
    cur = 0
    for e in S:
        if cur < len(R) and e == R[cur]:
            cur += 1
    return cur == len(R)
while 1:
    C, W = map(int, input().split())
    if C == W == 0:
        break
    G0 = [[] for i in range(C)]
    P = [list(map(int, input().split())) for i in range(C)]
    P0 = [P[i] + [i] for i in range(C)]
    P0.sort()
    Q0 = convex_hull(P0)
    R = list(map(lambda x: x[2], Q0))[:-1]
    k = R.index(min(R))
    R = R[k:] + R[:k]
    for i in range(W):
        s, t = map(int, input().split()); s -= 1; t -= 1
        G0[s].append(t)
        G0[t].append(s)
    for i in range(C):
        x0, y0 = P[i]
        G0[i].sort(key = lambda p: atan2(P[p][1] - y0, P[p][0] - x0))
    E = defaultdict(list)
    cur = 0
    for v in range(C):
        for b, v0 in enumerate(G0[v]):
            prv = v
            st = [v]
            while 1:
                g = G0[v0]
                c = (g.index(prv)+1) % len(g)
                if v0 == v and c == b:
                    break
                st.append(v0)
                prv = v0; v0 = g[c]
            if min(st) == v and not outer_check(R, st):
                for i in range(len(st)):
                    p = st[i-1]; q = st[i]
                    if not p < q:
                        p, q = q, p
                    E[p, q].append(cur)
                cur += 1
    G = [[] for i in range(cur+1)]
    for es in E.values():
        if len(es) == 2:
            a, b = es
        else:
            a = es[0]; b = cur
        G[a].append(b)
        G[b].append(a)
    D = [-1]*(cur+1)
    D[cur] = 0
    que = deque([cur])
    while que:
        v = que.popleft()
        d = D[v]
        for w in G[v]:
            if D[w] != -1:
                continue
            D[w] = d+1
            que.append(w)
    print(max(D))