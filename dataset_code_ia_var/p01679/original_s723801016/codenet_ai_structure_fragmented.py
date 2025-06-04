from heapq import heappush, heappop
import sys

def init_bit_count(L2):
    bc = [0] * L2
    for i in range(1, L2):
        bc[i] = bc[i ^ (i & -i)] + 1
    return bc

def read_integers_from_input(readline, count):
    return list(map(int, readline().split()))

def read_graph(N, M, readline):
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, readline().split())
        a -= 1
        b -= 1
        G[a].append((b, c))
        G[b].append((a, c))
    return G

def dijkstra(N, G, s, INF):
    dist = [INF] * N
    dist[s] = 0
    que = [(0, s)]
    while que:
        cost, v = heappop(que)
        if dist[v] < cost:
            continue
        for w, d in G[v]:
            if cost + d < dist[w]:
                dist[w] = cost + d
                heappush(que, (cost + d, w))
    return dist

def process_special_nodes(L, readline, dijkstra_func, N, G, T):
    G0 = [[] for _ in range(L)]
    RS = []
    BS = [0] * L
    for i in range(L):
        j, e = read_integers_from_input(readline, 2)
        j -= 1
        d0 = dijkstra_func(N, G, j)
        for k, p in enumerate(RS):
            v = d0[p]
            if v + BS[k] <= T:
                G0[i].append((k, v + BS[k], 1 << k))
            if v + e <= T:
                G0[k].append((i, v + e, 1 << i))
        RS.append(j)
        BS[i] = e
    return G0, RS, BS

def initialize_dp_structures(L):
    Q = [[{} for _ in range(L)] for _ in range(L + 1)]
    return Q

def process_initial_queue(Q, L, ds, RS, BS, T, dijkstra_s, ans):
    dw = [0] * L
    for i in range(L):
        d = ds[RS[i]]
        r = d + BS[i]
        dw[i] = T - d + 1
        if r < dw[i]:
            Q[1][i][1 << i] = r
            ans = 1
    return Q, dw, ans

def dp_relaxation(Q, G0, L, dw, ans):
    for k in range(1, L):
        qs = Q[k]
        qs1 = Q[k + 1]
        if any(qs):
            ans = k
        for v in range(L):
            qsv = qs[v]
            for w, d, b in G0[v]:
                dww = dw[w]
                qs1w = qs1[w]
                for state, cost in qsv.items():
                    if state & b:
                        continue
                    r = cost + d
                    if r < qs1w.get(state | b, dww):
                        qs1w[state | b] = r
    return ans

def check_final(Q, L, ans):
    if any(Q[L]):
        ans = L
    return ans

def solve_case(readline, write, bc, INF):
    N, M, L, s, T = read_integers_from_input(readline, 5)
    if N == M == 0:
        return False
    G = read_graph(N, M, readline)
    dijkstra_func = dijkstra
    G0, RS, BS = process_special_nodes(L, readline, dijkstra_func, N, G, T)
    ds = dijkstra(N, G, s - 1, INF)
    Q = initialize_dp_structures(L)
    ans = 0
    Q, dw, ans = process_initial_queue(Q, L, ds, RS, BS, T, dijkstra, ans)
    ans = dp_relaxation(Q, G0, L, dw, ans)
    ans = check_final(Q, L, ans)
    write("%d\n" % ans)
    return True

def main_loop(solve_func):
    while solve_func():
        ...

def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    L2 = 1 << 16
    bc = init_bit_count(L2)
    INF = 10 ** 18
    def solve_wrapper():
        return solve_case(readline, write, bc, INF)
    main_loop(solve_wrapper)

main()