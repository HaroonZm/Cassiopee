import heapq

def read_ints():
    return map(int, raw_input().split())

def parse_input():
    n, m, s, t = read_ints()
    src = [tuple(map(int, raw_input().split())) for _ in range(m)]
    return n, m, s, t, src

def create_adjacency_list(n, m, src):
    def empty_list():
        return [[] for _ in range(n + 1)]
    def add_edges(nl, src):
        for u, v, a, b in src:
            add_single_edge(nl, u, v, a, b)
            add_single_edge(nl, v, u, a, b)
    def add_single_edge(nl, u, v, a, b):
        nl[u].append((v, a, b))
    nl = empty_list()
    add_edges(nl, src)
    return nl

def initialize_distances(n, index):
    d = [float("inf")] * (n + 1)
    d[index] = 0
    return d

def dijkstra(nl, start, use_weight):
    d = initialize_distances(len(nl) - 1, start)
    Q = []
    heapq.heappush(Q, (0, start))
    def should_update(u, v, cost, weight):
        return d[v] > cost + weight
    while Q:
        cost, u = heapq.heappop(Q)
        process_neighbors(nl, d, u, cost, use_weight, should_update, Q)
    return d

def process_neighbors(nl, d, u, cost, use_weight, should_update, Q):
    for v, yen, snuuk in nl[u]:
        weight = yen if use_weight == "yen" else snuuk
        if should_update(u, v, cost, weight):
            d[v] = cost + weight
            heapq.heappush(Q, (d[v], v))

def accumulate_min_costs(n, d_y, d_s):
    val = float("inf")
    A = []
    for i in xrange(n, 0, -1):
        tmp = d_y[i] + d_s[i]
        val = min(val, tmp)
        A.append(val)
    return A

def print_results(A):
    for i in reversed(A):
        print 10 ** 15 - i

def main():
    n, m, s, t, src = parse_input()
    nl = create_adjacency_list(n, m, src)
    d_y = dijkstra(nl, s, use_weight="yen")
    d_s = dijkstra(nl, t, use_weight="snuuk")
    A = accumulate_min_costs(n, d_y, d_s)
    print_results(A)

main()