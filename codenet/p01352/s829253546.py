from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, K = map(int, readline().split())
    ES = [list(map(int, readline().split())) for i in range(K)]
    emp = {}
    sq = int(K**.5) + 1
    def root(x):
        if x == p[x]:
            return x
        p[x] = y = root(p[x])
        return y
    def unite(x, y):
        px = root(x); py = root(y)
        if px < py:
            p[py] = px
        else:
            p[px] = py
    que = deque()
    used = [0]*N
    lb = 0

    p = [0]*N
    for i in range(sq):
        s = set()
        for j in range(i*sq, min(i*sq+sq, K)):
            t, a, b = ES[j]
            if t == 3:
                continue
            e = (a, b)
            if emp.get(e, 0):
                s.add(e)
            emp[e] = 0

        p[:] = range(N)
        for (v, w), d in emp.items():
            if d == 1:
                unite(v, w)

        G0 = [[] for i in range(N)]
        emp0 = {}
        for a, b in s:
            pa = root(a); pb = root(b)
            if pa == pb:
                continue
            e = (pa, pb) if pa < pb else (pb, pa)
            if e in emp0:
                e1, e2 = emp0[e]
                e1[1] = e2[1] = e1[1] + 1
            else:
                e1 = [pb, 1]; e2 = [pa, 1]
                G0[pa].append(e1)
                G0[pb].append(e2)
                emp0[e] = e1, e2

        for j in range(i*sq, min(i*sq+sq, K)):
            t, a, b = ES[j]
            pa = root(a); pb = root(b)
            e = (pa, pb) if pa < pb else (pb, pa)
            if t == 1:
                emp[a, b] = 1
                if pa == pb:
                    continue
                if e not in emp0:
                    e1 = [pb, 1]; e2 = [pa, 1]
                    G0[pa].append(e1)
                    G0[pb].append(e2)
                    emp0[e] = e1, e2
                else:
                    e1, e2 = emp0[e]
                    e1[1] = e2[1] = e1[1] + 1
            elif t == 2:
                emp[a, b] = 0
                if pa == pb:
                    continue
                e1, e2 = emp0[e]
                e1[1] = e2[1] = e1[1] - 1
            elif t == 3:
                if pa == pb:
                    write("YES\n")
                else:
                    lb += 1
                    que.append(pa)
                    used[pa] = lb
                    while que:
                        v = que.popleft()
                        for w, d in G0[v]:
                            if d and used[w] != lb:
                                used[w] = lb
                                que.append(w)
                    if used[pb] == lb:
                        write("YES\n")
                    else:
                        write("NO\n")
solve()