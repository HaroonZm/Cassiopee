from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
P = list(map(int, readline().split()))
G = []
prt = [0]*N
for i in range(N):
    items = list(map(int, readline().split()))
    k, t = items[0], items[1:]
    G.append([e-1 for e in t])
    for e in t:
        prt[e-1] = i
D = [len(x) for x in G]
A = [0]*N
deg = D[:]
que = deque()
for v in range(N):
    if deg[v] == 0:
        A[v] = P[v]
        que.append(v)
while que:
    v = que.popleft()
    p = prt[v]
    deg[p] -= 1
    if deg[p] == 0:
        A[p] = max(-A[w] for w in G[p])
        que.append(p)
for v in range(N):
    if D[v] == 0:
        A[v] = P[v]
    else:
        A[v] = max(-A[w] for w in G[v])
memo = {}
INF = 10**9
r0 = r1 = None
stack = []
stack.append((0, 0, 0, -INF, INF, 0))
results = {}
while stack:
    v, state, c, a, b, step = stack.pop()
    key = (v, state, a, b)
    if (key, c) in results:
        continue
    if step == 0:
        if (v, state, a, b) in memo:
            results[(key, c)] = memo[(v, state, a, b)]
            continue
        if c == D[v]:
            if c == 0:
                results[(key, c)] = (1, 1)
            else:
                results[(key, c)] = (0, 0)
            continue
        c0 = N+1
        c1 = 0
        Gv = G[v]
        k = 0
        stack.append((v, state, c, a, b, 1))
        for k in range(D[v]):
            if state & (1 << k): continue
            w = Gv[k]
            stack.append((w, 0, 0, -b, -a, 2))
            stack.append((v, state, c, a, b, 3 + 2*k))
    elif step == 1:
        c0 = N+1
        c1 = 0
    elif step >= 3:
        k = (step - 3)//2
        Gv = G[v]
        w = Gv[k]
        s0, s1 = results[((w, 0, -b, -a), 0)]
        val = -A[w]
        if val >= b:
            c0 = min(c0, s0)
            c1 = max(c1, s1)
            continue
        t0, t1 = results[((v, state | (1 << k), c+1, max(a, val), b), 0)]
        c0 = min(c0, s0+t0)
        c1 = max(c1, s1+t1)
        if k == D[v]-1:
            memo[(v, state, a, b)] = (c0, c1)
            results[(key, c)] = (c0, c1)
if ((0,0,-INF,INF), 0) in results:
    r0, r1 = results[((0,0,-INF,INF), 0)]
else:
    r0 = r1 = 1
write("%d %d\n" % (r0, r1))