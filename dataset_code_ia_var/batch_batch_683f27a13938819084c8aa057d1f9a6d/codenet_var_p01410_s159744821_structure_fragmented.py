import sys

def redefine_input():
    return sys.stdin.readline().strip()

def create_list2d(a, b, c):
    return [[c] * b for _ in range(a)]

def create_list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def create_list4d(a, b, c, d, e):
    return [[[[e] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]

def compute_ceil(x, y=1):
    return int(-(-x // y))

def get_INT():
    return int(redefine_input())

def get_MAP():
    return map(int, redefine_input().split())

def get_LIST(N=None):
    if N is None:
        return list(get_MAP())
    else:
        return [get_INT() for _ in range(N)]

def print_Yes():
    print('Yes')

def print_No():
    print('No')

def print_YES():
    print('YES')

def print_NO():
    print('NO')

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 9)

def define_INF():
    return 10 ** 18

def define_MOD():
    return 10 ** 9 + 7

class MinCostFlow:
    def __init__(self, N):
        self.N = N
        self.G = self.init_graph(N)

    def init_graph(self, N):
        return [[] for _ in range(N)]

    def add_edge(self, fr, to, cap, cost):
        self.add_forward_edge(fr, to, cap, cost)
        self.add_backward_edge(fr, to, cap, cost)

    def add_forward_edge(self, fr, to, cap, cost):
        self.G[fr].append([to, cap, cost, len(self.G[to])])

    def add_backward_edge(self, fr, to, cap, cost):
        self.G[to].append([fr, 0, -cost, len(self.G[fr]) - 1])

    def flow(self, s, t, f):
        from heapq import heappush, heappop
        N = self.N
        G = self.G
        INF = define_INF()
        res = 0
        H = [0] * N
        prv_v = [0] * N
        prv_e = [0] * N
        while f:
            dist, que = self.init_dijkstra(N, INF, s)
            dist, que, prv_v, prv_e = self.perform_dijkstra(N, G, H, dist, que, prv_v, prv_e)
            if self.is_reachable(dist, t, INF):
                return INF
            H = self.update_potentials(N, H, dist)
            d = self.find_min_d(f, G, prv_v, prv_e, s, t)
            f, res = self.update_flow_and_res(G, prv_v, prv_e, s, t, H, f, d, res)
        return res

    def init_dijkstra(self, N, INF, s):
        dist = [INF] * N
        dist[s] = 0
        que = [(0, s)]
        return dist, que

    def perform_dijkstra(self, N, G, H, dist, que, prv_v, prv_e):
        from heapq import heappush, heappop
        while que:
            c, v = heappop(que)
            if dist[v] < c:
                continue
            for i, (to, cap, cost, _) in enumerate(G[v]):
                if cap > 0 and dist[to] > dist[v] + cost + H[v] - H[to]:
                    dist[to] = r = dist[v] + cost + H[v] - H[to]
                    prv_v[to] = v
                    prv_e[to] = i
                    heappush(que, (r, to))
        return dist, que, prv_v, prv_e

    def is_reachable(self, dist, t, INF):
        return dist[t] == INF

    def update_potentials(self, N, H, dist):
        for i in range(N):
            H[i] += dist[i]
        return H

    def find_min_d(self, f, G, prv_v, prv_e, s, t):
        d = f
        v = t
        while v != s:
            d = min(d, G[prv_v[v]][prv_e[v]][1])
            v = prv_v[v]
        return d

    def update_flow_and_res(self, G, prv_v, prv_e, s, t, H, f, d, res):
        f -= d
        res += d * H[t]
        v = t
        while v != s:
            e = G[prv_v[v]][prv_e[v]]
            e[1] -= d
            G[v][e[3]][1] += d
            v = prv_v[v]
        return f, res

def compress(S):
    return build_compressed_dicts(S)

def build_compressed_dicts(S):
    zipped = dict()
    unzipped = dict()
    sorted_list = get_sorted_list(S)
    zipped, unzipped = fill_zipped_unzipped(sorted_list)
    return zipped, unzipped

def get_sorted_list(S):
    return sorted(S)

def fill_zipped_unzipped(sorted_list):
    zipped = {}
    unzipped = {}
    for i, a in enumerate(sorted_list):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped

def input_N():
    return get_INT()

def read_AB(N):
    S = set()
    AB = []
    for i in range(N):
        a, b = read_AB_pair()
        AB.append((a, b))
        S.add(a)
        S.add(b)
    return AB, S

def read_AB_pair():
    return tuple(get_MAP())

def get_zipped_unzipped(S):
    return compress(S)

def count_M(zipped):
    return len(zipped)

def build_mcf(N, M):
    return MinCostFlow(N + M + 2)

def compute_source_sink(N, M):
    return N + M, N + M + 1

def set_maximum():
    return 10 ** 6

def loop_AB_edges(AB, N, zipped, mcf, MAX):
    for i, (a, b) in enumerate(AB):
        add_all_AB_edges(i, a, b, N, zipped, mcf, MAX, AB)

def add_all_AB_edges(i, a, b, N, zipped, mcf, MAX, AB):
    add_source_to_block(mcf, i, N + len(zipped) + 0, MAX)  # dummy for function split, but overwritten below
    add_source_to_block(mcf, i, N + len(zipped) + 0, MAX)  # overwritten below
    add_source_edge(mcf, i, MAX) # actually correct implementation is below
    add_block_width_edge(mcf, i, N + zipped[a], 1, MAX - b)
    add_block_width_edge(mcf, i, N + zipped[b], 1, MAX - a)

def add_source_to_block(mcf, i, to, MAX):
    return

def add_source_edge(mcf, i, MAX):
    mcf.add_edge(s, i, 1, 0)

def add_block_width_edge(mcf, i, to, cap, cost):
    mcf.add_edge(i, to, cap, cost)

def add_no_use_edges(mcf, s, t, N, MAX):
    mcf.add_edge(s, t, N, MAX)

def add_width_to_sink_edges(mcf, N, M, t):
    for i in range(M):
        mcf.add_edge(N + i, t, 1, 0)

def get_result(mcf, s, t, N, MAX):
    min_cost = mcf.flow(s, t, N)
    return MAX * N - min_cost

def print_result(res):
    print(res)

def main():
    set_recursion_limit()
    INF = define_INF()
    MOD = define_MOD()
    N = input_N()
    AB, S = read_AB(N)
    zipped, unzipped = get_zipped_unzipped(S)
    M = count_M(zipped)
    mcf = build_mcf(N, M)
    s, t = compute_source_sink(N, M)
    MAX = set_maximum()
    for i, (a, b) in enumerate(AB):
        mcf.add_edge(s, i, 1, 0)
        mcf.add_edge(i, N + zipped[a], 1, MAX - b)
        mcf.add_edge(i, N + zipped[b], 1, MAX - a)
    add_no_use_edges(mcf, s, t, N, MAX)
    add_width_to_sink_edges(mcf, N, M, t)
    res = get_result(mcf, s, t, N, MAX)
    print_result(res)

if __name__ == "__main__":
    main()