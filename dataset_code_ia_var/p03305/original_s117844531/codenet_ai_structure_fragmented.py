class Dijkstra():
    class Edge():
        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

    def __init__(self, V):
        self._init_graph(V)

    def _init_graph(self, V):
        self.G = [[] for i in range(V)]
        self._E = 0
        self._V = V

    @property
    def E(self):
        return self._get_E()

    def _get_E(self):
        return self._E

    @property
    def V(self):
        return self._get_V()

    def _get_V(self):
        return self._V

    def add(self, _from, _to, _cost):
        self._add_edge(_from, _to, _cost)

    def _add_edge(self, _from, _to, _cost):
        self.G[_from].append(self.Edge(_to, _cost))
        self._E += 1

    def shortest_path(self, s):
        return self._compute_shortest_path(s)

    def _compute_shortest_path(self, s):
        que = self._init_priority_queue()
        d = self._init_distance_list()
        self._set_start_distance(d, s)
        self._push_start_node(que, s)
        self._process_queue(que, d)
        return d

    def _init_priority_queue(self):
        return []

    def _init_distance_list(self):
        return [10**15] * self.V

    def _set_start_distance(self, d, s):
        d[s] = 0

    def _push_start_node(self, que, s):
        import heapq
        heapq.heappush(que, (0, s))

    def _process_queue(self, que, d):
        import heapq
        while self._queue_not_empty(que):
            cost, v = self._pop_queue(que)
            if self._should_skip_node(d, v, cost):
                continue
            self._update_neighbors(v, d, que)

    def _queue_not_empty(self, que):
        return len(que) != 0

    def _pop_queue(self, que):
        import heapq
        return heapq.heappop(que)

    def _should_skip_node(self, d, v, cost):
        return d[v] < cost

    def _update_neighbors(self, v, d, que):
        for i in self._get_neighbor_indices(v):
            e = self._get_neighbor_edge(v, i)
            self._try_update_distance(e, v, d, que)

    def _get_neighbor_indices(self, v):
        return range(len(self.G[v]))

    def _get_neighbor_edge(self, v, i):
        return self.G[v][i]

    def _try_update_distance(self, e, v, d, que):
        if self._should_update_distance(e, v, d):
            self._update_distance(e, v, d)
            self._push_new_candidate(e, d, que)

    def _should_update_distance(self, e, v, d):
        return d[e.to] > d[v] + e.cost

    def _update_distance(self, e, v, d):
        d[e.to] = d[v] + e.cost

    def _push_new_candidate(self, e, d, que):
        import heapq
        heapq.heappush(que, (d[e.to], e.to))

def main():
    n, m, s, t = read_main_input()
    yen, snuke = create_dijkstra_instances(n)
    process_edges(m, yen, snuke)
    s, t = adjust_node_indices(s, t)
    ye = yen.shortest_path(s)
    sn = snuke.shortest_path(t)
    answer = process_costs(n, ye, sn)
    output_result(answer)

def read_main_input():
    n, m, s, t = map(int, input().split())
    return n, m, s, t

def create_dijkstra_instances(n):
    yen = Dijkstra(n)
    snuke = Dijkstra(n)
    return yen, snuke

def process_edges(m, yen, snuke):
    for i in range(m):
        u, v, a, b = read_edge_input()
        u, v = adjust_edge_indices(u, v)
        add_both_direction_edges(u, v, a, b, yen, snuke)

def read_edge_input():
    return map(int, input().split())

def adjust_edge_indices(u, v):
    return u - 1, v - 1

def add_both_direction_edges(u, v, a, b, yen, snuke):
    add_yen_edges(u, v, a, yen)
    add_snuke_edges(u, v, b, snuke)

def add_yen_edges(u, v, a, yen):
    yen.add(u, v, a)
    yen.add(v, u, a)

def add_snuke_edges(u, v, b, snuke):
    snuke.add(u, v, b)
    snuke.add(v, u, b)

def adjust_node_indices(s, t):
    return s - 1, t - 1

def process_costs(n, ye, sn):
    answer = []
    cost = float("inf")
    for i in process_indices_reverse(n):
        cost = update_min_cost(cost, sn, ye, i)
        append_cost(answer, cost)
    return answer

def process_indices_reverse(n):
    return range(n-1, -1, -1)

def update_min_cost(cost, sn, ye, i):
    return min(cost, sn[i] + ye[i])

def append_cost(answer, cost):
    answer.append(cost)

def output_result(answer):
    for i in output_indices(answer):
        print(get_final_cost(answer, i))

def output_indices(answer):
    return range(len(answer))

def get_final_cost(answer, i):
    return 10**15 - answer[-i-1]

main()