import sys
from heapq import heapify, heappop, heappush
from collections import defaultdict

readline = sys.stdin.readline
write = sys.stdout.write

def solve(q):
    N, M = map(int, readline().split())
    if not (N or M):
        return False
    if q: write('\n')

    INF = float('inf')
    G = [[] for _ in range(N)]
    E = [ [INF]*N for _ in range(N) ]
    for _ in range(M):
        a, b, c = map(int, readline().split())
        a -= 1; b -= 1
        G[a].append((b, c))
        G[b].append((a, c))
        E[a][b] = E[b][a] = c

    L = int(readline())
    P, R, B, I = [], [], [], [0]*L
    Q = []
    res = [0]*L

    # Compute all pairwise shortest paths on the fly using a more compact Dijkstra
    for i in range(L):
        a, b, c, s = readline().strip().split()
        a, b, c = int(a)-1, int(b)-1, int(c)
        P.append(s)
        B.append(b)

        dist = [INF]*N
        prv = [None]*N
        dist[b] = 0
        pq = [(0, b)]
        while pq:
            cost, v = heappop(pq)
            if dist[v] < cost: continue
            for w, d in G[v]:
                new_c = cost + d
                if new_c < dist[w]:
                    dist[w], prv[w] = new_c, v
                    heappush(pq, (new_c, w))
                elif new_c == dist[w] and (prv[w] is None or v < prv[w]):
                    prv[w] = v
        # Recover reverse path efficiently
        path, x = [], a
        while x != b:
            path.append(x)
            x = prv[x]
        path.append(b)
        R.append(path)
        Q.append((c, 1, i))

    heapify(Q)
    queue_states = [ [] for _ in range(N) ]
    waits = [defaultdict(list) for _ in range(N)]
    finished = [dict() for _ in range(N)]
    available = [1]*N
    remain = L

    while remain:
        t = Q[0][0]
        # Collect all tasks scheduled at the current time
        buf = []
        while Q and Q[0][0] == t:
            buf.append(heappop(Q))
        for _, p, idx in buf:
            # Main driver
            if p:
                v = R[idx][I[idx]]
                I[idx] += 1
                if B[idx]==v:
                    remain -= 1
                    res[idx] = t
                else:
                    w = R[idx][I[idx]]
                    heappush(queue_states[v], (t, w, idx))
                    waits[v][w].append(idx)
                    finished[v][idx]=0
            else:
                available[idx] = 1

        # Try to start as many tasks as possible from each node
        for v, qv in enumerate(queue_states):
            while qv and finished[v].get(qv[0][2], 0):
                heappop(qv)
            if not (available[v] and qv): continue
            t0, w, idx = heappop(qv)
            d = E[v][w]
            for idx2 in waits[v][w]:
                finished[v][idx2] = 1
                heappush(Q, (t+d, 1, idx2))
            waits[v][w].clear()
            heappush(Q, (t+2*d, 0, v))
            available[v] = 0

    for t, s in sorted(zip(res, P)):
        write(f"{s} {t}\n")
    return True

for q in iter(int, 1):
    if not solve(q): break