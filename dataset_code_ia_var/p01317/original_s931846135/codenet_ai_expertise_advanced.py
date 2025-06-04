from heapq import heappush, heappop
import sys
import functools
import operator

INF = float('inf')

def dijkstra(n, src, graph):
    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        cost, v = heappop(heap)
        if cost > dist[v]:
            continue
        for w, d in graph[v]:
            new_cost = cost + d
            if new_cost < dist[w]:
                dist[w] = new_cost
                heappush(heap, (new_cost, w))
    return dist

def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write
    N, M = map(int, readline().split())
    if N == M == 0:
        return False

    GL = [[] for _ in range(N)]
    GS = [[] for _ in range(N)]

    for _ in range(M):
        x, y, t, sl = readline().split()
        x, y, t = int(x) - 1, int(y) - 1, int(t)
        if sl == 'L':
            GL[x].append((y, t))
            GL[y].append((x, t))
        else:
            GS[x].append((y, t))
            GS[y].append((x, t))

    # Dijkstra for all pairs
    EL = [dijkstra(N, i, GL) for i in range(N)]
    ES = [dijkstra(N, i, GS) for i in range(N)]

    R = int(readline())
    Z = [int(x) - 1 for x in readline().split()]

    S = [INF] * N
    S[Z[0]] = 0
    T = [0] * N
    buf_D = [0] * N

    for prev, cur in zip(Z, Z[1:]):
        AL = EL[prev]
        BL = EL[cur]
        v = AL[cur]
        # Calculate D = S + AL
        for j in range(N):
            buf_D[j] = S[j] + AL[j]
        for j in range(N):
            add_path = min(T[j] if T[j] != 0 else INF for T[j] in (map(operator.add, buf_D, ES[j])))
            T[j] = min(S[j] + v, add_path + BL[j])
        S, T = T, S

    result = min(S)
    write(f"{result}\n")
    return True

while solve():
    pass