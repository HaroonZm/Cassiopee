from heapq import heappush, heappop
import sys

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_input():
    N_s_t = read_ints()
    if not N_s_t:
        return 0, 0, 0, [], []
    N, s, t = N_s_t
    if N == 0:
        return N, s, t, [], []
    Q = read_ints()
    G = build_graph(N)
    return N, s, t, Q, G

def build_graph(N):
    G = []
    for _ in range(N):
        A = read_ints()
        G.append([(w, a) for w, a in enumerate(A) if a])
    return G

def dijkstra(N, G, t):
    INF = 10**9
    dist = [INF] * N
    dist[t] = 0
    que = [(0, t)]
    while que:
        cost, v = heappop(que)
        if dist[v] < cost:
            continue
        update_neighbors(G, dist, que, v, cost)
    return dist

def update_neighbors(G, dist, que, v, cost):
    for w, d in G[v]:
        if cost + d < dist[w]:
            dist[w] = cost + d
            heappush(que, (cost + d, w))

def is_impossible(dist, s):
    return dist[s] == 10**9

def write_impossible():
    sys.stdout.write("impossible\n")

def build_graph_G0(N, G, Q, dist, t):
    G0 = [[] for _ in range(N)]
    for v in range(N):
        if v == t:
            continue
        if Q[v]:
            G0[v] = get_expected_edges(v, G, dist)
        else:
            G0[v] = G[v]
    return G0

def get_expected_edges(v, G, dist):
    edges = []
    cost = dist[v]
    for w, d in G[v]:
        if cost == dist[w] + d:
            edges.append((w, d))
    return edges

def build_equations(N, G0):
    MT = [[0] * (N + 1) for _ in range(N)]
    for v in range(N):
        build_equation_row(MT[v], v, G0[v])
    return MT

def build_equation_row(Mv, v, edges):
    Mv[v] = 1
    g = len(edges)
    r = 0
    for w, d in edges:
        Mv[w] -= 1 / g
        r += d / g
    Mv[-1] = r

def gaussian_elimination(N, MT):
    for i in range(N):
        normalize_row(MT[i], i)
        eliminate_column(N, MT, i)

def normalize_row(Mi, i):
    v = Mi[i]
    for j in range(len(Mi)):
        Mi[j] /= v

def eliminate_column(N, MT, i):
    for k in range(N):
        if k == i:
            continue
        Mk = MT[k]
        e = Mk[i]
        if e == 0:
            continue
        for j in range(N + 1):
            Mk[j] -= e * MT[i][j]

def write_result(res):
    sys.stdout.write("%.16f\n" % res)

def solve():
    N, s, t, Q, G = read_input()
    if N == 0:
        return False
    s -= 1
    t -= 1
    dist = dijkstra(N, G, t)
    if is_impossible(dist, s):
        write_impossible()
        return True
    G0 = build_graph_G0(N, G, Q, dist, t)
    MT = build_equations(N, G0)
    gaussian_elimination(N, MT)
    write_result(MT[s][N])
    return True

while True:
    if not solve():
        break