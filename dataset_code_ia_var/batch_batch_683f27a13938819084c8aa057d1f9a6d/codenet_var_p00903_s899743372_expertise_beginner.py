import sys
import heapq

def solve():
    N_and_M = sys.stdin.readline().split()
    N = int(N_and_M[0])
    M = int(N_and_M[1])
    if N == 0 and M == 0:
        return False

    D = [0]*N
    E = [0]*N
    B = [0]*N
    H = {}
    H[0] = 1
    H[1000] = H.get(1000, 0) + 1
    E[N-1] = 1000

    for i in range(1, N-1):
        line = sys.stdin.readline().split()
        D[i] = int(line[0])
        E[i] = int(line[1])
        B[i] = H.get(E[i], 0)
        H[E[i]] = H.get(E[i], 0) + 1

    G = []
    RG = []
    for _ in range(N):
        G.append([])
        RG.append([])

    for _ in range(M):
        line = sys.stdin.readline().split()
        a = int(line[0])-1
        b = int(line[1])-1
        c = int(line[2])
        if E[a] <= E[b]:
            G[a].append((b, c))
        if E[b] <= E[a]:
            RG[b].append((a, c))

    dist = {}
    dist[(0, 0, 1)] = 0
    que = []
    heapq.heappush(que, (0, 0, 0, 1))
    INF = 10**18

    while que:
        node = heapq.heappop(que)
        cost = node[0]
        v0 = node[1]
        v1 = node[2]
        state = node[3]
        if dist.get((v0, v1, state), INF) < cost:
            continue
        d0 = E[v0]
        d1 = E[v1]

        if d0 < d1:
            for elem in G[v0]:
                w0 = elem[0]
                d = elem[1]
                if E[w0] == d1:
                    if w0 == v1:
                        de = cost + d
                        n_state = (1 << B[w0])
                    else:
                        de = cost + d + D[w0]
                        n_state = (1 << B[w0]) | (1 << B[v1])
                    n_key = (w0, v1, n_state)
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heapq.heappush(que, (de, w0, v1, n_state))
                else:
                    n_key = (w0, v1, 0)
                    de = cost + d + D[w0]
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heapq.heappush(que, (de, w0, v1, 0))
        elif d0 > d1:
            for elem in RG[v1]:
                w1 = elem[0]
                d = elem[1]
                if E[w1] == d0:
                    if w1 == v0:
                        de = cost + d
                        n_state = (1 << B[w1])
                    else:
                        de = cost + d + D[w1]
                        n_state = (1 << B[w1]) | (1 << B[v0])
                    n_key = (v0, w1, n_state)
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heapq.heappush(que, (de, v0, w1, n_state))
                else:
                    n_key = (v0, w1, 0)
                    de = cost + d + D[w1]
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heapq.heappush(que, (de, v0, w1, 0))
        else:
            ds = d0
            for elem in G[v0]:
                w0 = elem[0]
                d = elem[1]
                if ds == E[w0]:
                    b = (1 << B[w0])
                    if (state & b):
                        de = cost + d
                        n_state = state
                    else:
                        de = cost + d + D[w0]
                        n_state = state | b
                    n_key = (w0, v1, n_state)
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heapq.heappush(que, (de, w0, v1, n_state))
                else:
                    n_key = (w0, v1, 0)
                    de = cost + d + D[w0]
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heapq.heappush(que, (de, w0, v1, 0))
            for elem in RG[v1]:
                w1 = elem[0]
                d = elem[1]
                if ds == E[w1]:
                    b = (1 << B[w1])
                    if (state & b):
                        de = cost + d
                        n_state = state
                    else:
                        de = cost + d + D[w1]
                        n_state = state | b
                    n_key = (v0, w1, n_state)
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heapq.heappush(que, (de, v0, w1, n_state))
                else:
                    n_key = (v0, w1, 0)
                    de = cost + d + D[w1]
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heapq.heappush(que, (de, v0, w1, 0))

    g_key = (N-1, N-1, 1)
    if g_key in dist:
        print(dist[g_key])
    else:
        print(-1)
    return True

while True:
    if not solve():
        break