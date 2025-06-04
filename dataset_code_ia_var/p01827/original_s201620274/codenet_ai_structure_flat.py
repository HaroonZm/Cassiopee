from collections import deque
import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
C = list(map(int, readline().split()))
M = int(readline())
p = list(range(N))
G = [[] for _ in range(N)]
G0 = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    ca = C[a]
    cb = C[b]
    if ca < cb:
        G0[a].append(b)
    elif cb < ca:
        G0[b].append(a)

for v in range(N):
    ws = G[v]
    if not ws:
        continue
    ws.sort(key=C.__getitem__)
    c = C[v]
    prv = ws[0]
    pw = C[prv]
    # root
    x = v
    while p[x] != x:
        x = p[x]
    rv = x
    x = prv
    while p[x] != x:
        x = p[x]
    rprv = x
    if C[prv] == c:
        if rv < rprv:
            p[rprv] = rv
        else:
            p[rv] = rprv
    for w in ws[1:]:
        cw = C[w]
        # root for prv and w
        x = prv
        while p[x] != x:
            x = p[x]
        rprv = x
        x = w
        while p[x] != x:
            x = p[x]
        rw = x
        if pw == cw:
            if rprv < rw:
                p[rw] = rprv
            else:
                p[rprv] = rw
        else:
            G0[prv].append(w)
        if cw == c:
            # unite v and w
            x = v
            while p[x] != x:
                x = p[x]
            rv = x
            x = w
            while p[x] != x:
                x = p[x]
            rw = x
            if rv < rw:
                p[rw] = rv
            else:
                p[rv] = rw
        prv = w
        pw = cw

G1 = [[] for _ in range(N)]
deg = [0] * N
for v in range(N):
    x = v
    while p[x] != x:
        x = p[x]
    pv = x
    for w in G0[v]:
        x = w
        while p[x] != x:
            x = p[x]
        pw = x
        if pv != pw:
            G1[pv].append(pw)
            deg[pw] += 1

que = deque()
D = [0] * N
for i in range(N):
    x = i
    while p[x] != x:
        x = p[x]
    if x != i:
        continue
    if deg[i] == 0:
        que.append(i)
        D[i] = 1

while que:
    v = que.popleft()
    d = D[v]
    for w in G1[v]:
        deg[w] -= 1
        if deg[w] == 0:
            que.append(w)
        if D[w] < d + 1:
            D[w] = d + 1

for i in range(N):
    x = i
    while p[x] != x:
        x = p[x]
    if x == i:
        continue
    D[i] = D[x]
write("%d\n" % sum(D))