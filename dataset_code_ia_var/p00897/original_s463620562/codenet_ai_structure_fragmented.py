from heapq import heappush, heappop

def read_input_line():
    return raw_input()

def parse_ints_from_line(line):
    return map(int, line.split())

def get_n_m_cap():
    line = read_input_line()
    return parse_ints_from_line(line)

def parse_src_dest():
    line = read_input_line()
    return line.split()

def build_graph(n):
    G = {}
    for i in xrange(n):
        c1, c2, d = parse_graph_edge()
        update_graph(G, c1, c2, d)
    return G

def parse_graph_edge():
    line = read_input_line()
    c1, c2, d = line.split()
    return c1, c2, int(d)

def update_graph(G, c1, c2, d):
    if c1 not in G:
        G[c1] = {}
    if c2 not in G:
        G[c2] = {}
    G[c1][c2] = d
    G[c2][c1] = d

def read_interesting_nodes(m):
    S = set()
    for i in xrange(m):
        S.add(read_input_line())
    return S

def get_INF():
    return 10**18

def multiply_capacity(cap):
    return cap * 10

def dijkstra(s, G, INF):
    dist = initialize_dist(s)
    que = initialize_queue(s)
    while not is_queue_empty(que):
        co, v = pop_from_queue(que)
        if dist_value_is_less(dist, v, co, INF):
            continue
        process_neighbors(G, v, co, dist, que, INF)
    return dist

def initialize_dist(s):
    return {s: 0}

def initialize_queue(s):
    return [(0, s)]

def is_queue_empty(que):
    return not que

def pop_from_queue(que):
    return heappop(que)

def dist_value_is_less(dist, v, co, INF):
    return dist.get(v, INF) < co

def process_neighbors(G, v, co, dist, que, INF):
    for t, cost in get_neighbors(G, v):
        try_relax_edge(dist, t, co, cost, que, INF)

def get_neighbors(G, v):
    return G[v].items()

def try_relax_edge(dist, t, co, cost, que, INF):
    if co + cost < dist.get(t, INF):
        dist[t] = co + cost
        heappush(que, (co + cost, t))

def build_reduced_graph(S, G, cap, INF):
    H = {}
    for s in S:
        dist = dijkstra(s, G, INF)
        for k, v in dist.items():
            if k in S and v <= cap:
                add_edge_to_H(H, s, k, v)
    return H

def add_edge_to_H(H, s, k, v):
    if s not in H:
        H[s] = {}
    H[s][k] = v

def print_result(dist, dest):
    print dist.get(dest, -1)

def main_loop():
    while True:
        n, m, cap = get_n_m_cap()
        if check_termination(n):
            break
        src, dest = parse_src_dest()
        G = build_graph(n)
        S = build_S_set(m, src, dest)
        INF = get_INF()
        cap_value = multiply_capacity(cap)
        H = build_reduced_graph(S, G, cap_value, INF)
        dist = dijkstra(src, H, INF)
        print_result(dist, dest)

def build_S_set(m, src, dest):
    return read_interesting_nodes(m) | {src, dest}

def check_termination(n):
    return n == 0

main_loop()