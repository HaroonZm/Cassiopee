from heapq import heappush, heappop

class MinCostFlow:
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = self._create_graph(N)

    def _create_graph(self, N):
        return [[] for _ in range(N)]

    def add_edge(self, fr, to, cap, cost):
        self._append_forward_edge(fr, to, cap, cost)
        self._append_backward_edge(fr, to, cap, cost)

    def _append_forward_edge(self, fr, to, cap, cost):
        G = self.G
        G[fr].append([to, cap, cost, len(G[to])])

    def _append_backward_edge(self, fr, to, cap, cost):
        G = self.G
        G[to].append([fr, 0, -cost, len(G[fr]) - 1])

    def flow(self, s, t, f):
        return self._min_cost_flow(s, t, f)

    def _min_cost_flow(self, s, t, f):
        N = self.N
        G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = self._init_potentials(N)
        prv_v = self._init_prev_nodes(N)
        prv_e = self._init_prev_edges(N)

        while self._flow_remaining(f):
            dist = self._init_distances(N, s, INF)
            que = self._init_priority_queue(s)

            self._perform_dijkstra(que, dist, H, prv_v, prv_e, G)

            if self._no_path_found(dist, t, INF):
                return -1

            self._update_potentials(H, dist, N)

            d = self._find_flow_to_add(f, s, t, prv_v, prv_e, G)

            f = self._decrement_flow_left(f, d)

            res = self._update_total_cost(res, d, H, t)

            self._update_graph_flows(d, t, s, prv_v, prv_e, G)

        return res

    def _init_potentials(self, N):
        return [0] * N

    def _init_prev_nodes(self, N):
        return [0] * N

    def _init_prev_edges(self, N):
        return [0] * N

    def _flow_remaining(self, f):
        return f > 0

    def _init_distances(self, N, s, INF):
        dist = [INF] * N
        dist[s] = 0
        return dist

    def _init_priority_queue(self, s):
        return [(0, s)]

    def _perform_dijkstra(self, que, dist, H, prv_v, prv_e, G):
        while que:
            c, v = heappop(que)
            if dist[v] < c:
                continue
            self._relax_edges(v, dist, H, prv_v, prv_e, G, que)

    def _relax_edges(self, v, dist, H, prv_v, prv_e, G, que):
        for i, (w, cap, cost, rev) in enumerate(G[v]):
            if self._can_relax_edge(cap, dist, w, v, cost, H):
                new_dist = self._calculate_new_distance(dist, v, cost, H, w)
                self._update_distance_and_prev_nodes(dist, w, new_dist, prv_v, prv_e, v, i)
                heappush(que, (new_dist, w))

    def _can_relax_edge(self, cap, dist, w, v, cost, H):
        return (cap > 0) and (dist[w] > dist[v] + cost + H[v] - H[w])

    def _calculate_new_distance(self, dist, v, cost, H, w):
        return dist[v] + cost + H[v] - H[w]

    def _update_distance_and_prev_nodes(self, dist, w, new_dist, prv_v, prv_e, v, i):
        dist[w] = new_dist
        prv_v[w] = v
        prv_e[w] = i

    def _no_path_found(self, dist, t, INF):
        return dist[t] == INF

    def _update_potentials(self, H, dist, N):
        for i in range(N):
            H[i] += dist[i]

    def _find_flow_to_add(self, f, s, t, prv_v, prv_e, G):
        d = f
        v = t
        while v != s:
            d = min(d, G[prv_v[v]][prv_e[v]][1])
            v = prv_v[v]
        return d

    def _decrement_flow_left(self, f, d):
        return f - d

    def _update_total_cost(self, res, d, H, t):
        return res + d * H[t]

    def _update_graph_flows(self, d, t, s, prv_v, prv_e, G):
        v = t
        while v != s:
            e = G[prv_v[v]][prv_e[v]]
            self._decrease_edge_capacity(e, d)
            self._increase_reverse_edge_capacity(G, e, d, v)
            v = prv_v[v]

    def _decrease_edge_capacity(self, e, d):
        e[1] -= d

    def _increase_reverse_edge_capacity(self, G, e, d, v):
        G[v][e[3]][1] += d


def read_ints():
    return list(map(int, input().split()))

def read_ints_line():
    return map(int, input().split())

def process_input_loop():
    while True:
        M, W = read_ints_line()
        if input_ends(M, W):
            break
        A = read_A(M)
        B = read_B(W)
        mcf = create_min_cost_flow(M, W)
        add_edges_source_to_M(mcf, M)
        add_edges_M_to_W(mcf, M, W, A, B)
        add_edges_W_to_sink(mcf, M, W)
        result = calculate_min_cost_flow(mcf, M, W)
        print_result(result)

def input_ends(M, W):
    return M == 0 and W == 0

def read_A(M):
    return list(map(int, input().split()))

def read_B(W):
    return list(map(int, input().split()))

def create_min_cost_flow(M, W):
    return MinCostFlow(M + W + 2)

def add_edges_source_to_M(mcf, M):
    for i in range(M):
        mcf.add_edge(0, i + 1, 1, 0)

def add_edges_M_to_W(mcf, M, W, A, B):
    for i in range(M):
        for j in range(W):
            cost = calculate_edge_cost(A[i], B[j])
            mcf.add_edge(i + 1, M + 1 + j, 1, cost)

def calculate_edge_cost(a_i, b_j):
    d = abs(a_i - b_j)
    return -d * (d - 30) * (d - 30)

def add_edges_W_to_sink(mcf, M, W):
    for i in range(W):
        mcf.add_edge(M + 1 + i, M + W + 1, 1, 0)

def calculate_min_cost_flow(mcf, M, W):
    flow_amount = min(M, W)
    return -mcf.flow(0, M + W + 1, flow_amount)

def print_result(result):
    print(result)

process_input_loop()