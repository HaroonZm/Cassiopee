from functools import reduce, partial
import itertools
import sys

def main():
    rd, wr = sys.stdin.readline, sys.stdout.write

    def trampoline(f):
        def tramp(*args, **kwargs):
            res = f(*args, **kwargs)
            while callable(res):
                res = res()
            return res
        return tramp

    N = int(filter(str.isdigit, rd()).__next__())
    def to_int(x): return int(x)
    C = list(map(to_int, rd().split()))
    M = int(filter(str.isdigit, rd()).__next__())
    p = list(range(N))
    G = [list() for _ in map(lambda _:None, range(N))]
    G0 = [list() for _ in map(lambda _:None, range(N))]

    @trampoline
    def r(x):
        if p[x] == x:
            return x
        def callback():
            nonlocal x
            p[x] = r(p[x])
            return p[x]
        return callback

    def runite(x, y):
        rx, ry = r(x), r(y)
        (lambda a, b: p.__setitem__(b, a) if a < b else p.__setitem__(a, b)) (rx, ry)

    # Build graph
    _ = [(
        lambda a, b:
           (G[a].append(b),
            G[b].append(a)) and
           (G0[a].append(b) if C[a] < C[b] else (G0[b].append(a) if C[a] > C[b] else None))
        )(*(map(lambda z: z-1, map(int, rd().split()))))
        for _ in range(M)
    ]

    # Complicated grouping
    for v, ws in filter(lambda x: x[1], zip(range(N), G)):
        ws_sorted = sorted(ws, key=C.__getitem__)
        c = C[v]
        pairwise = zip([ws_sorted[0]]+ws_sorted, ws_sorted)
        prv, pw = ws_sorted[0], C[ws_sorted[0]]
        if pw == c: runite(v, prv)
        for prew, w in itertools.islice(pairwise, 1, None):
            cw = C[w]
            if pw == cw:
                runite(prv, w)
            else:
                G0[prv].append(w)
            if cw == c:
                runite(v, w)
            prv, pw = w, cw

    # Build new graph with representatives
    G1 = [[] for _ in range(N)]
    deg = [0]*N
    for v, out in enumerate(G0):
        rep_v = r(v)
        for w in out:
            rep_w = r(w)
            if rep_w != rep_v:
                G1[rep_v].append(rep_w)
                deg[rep_w] += 1

    # Topo sort & dp
    D = [0]*N
    que = list(filter(lambda z: deg[z]==0 and r(z)==z, range(N)))
    for i in que: D[i]=1
    from collections import deque
    dq = deque(que)
    while dq:
        v = dq.popleft()
        d = D[v]
        for w in G1[v]:
            deg[w] -= 1
            if deg[w]==0:
                dq.append(w)
            D[w] = max(D[w], d+1)
    list(map(lambda i: D.__setitem__(i, D[r(i)]) if r(i)!=i else None, range(N)))
    wr("%d\n"%reduce(int.__add__, D, 0))

main()