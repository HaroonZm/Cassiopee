def read_vertices_edges(f):
    line = f.readline()
    return map(int, line.split())

def init_edge_lists(E):
    s = [None for _ in range(E)]
    t = [None for _ in range(E)]
    return s, t

def read_edge(f):
    return map(int, f.readline().split())

def process_edges(f, E, s, t):
    for i in range(E):
        s[i], t[i] = read_edge(f)

def read_queries_count(f):
    return int(f.readline())

def init_query_lists(Q):
    u = [None for _ in range(Q)]
    v = [None for _ in range(Q)]
    return u, v

def read_query(f):
    return map(int, f.readline().split())

def process_queries(f, Q, u, v):
    for i in range(Q):
        u[i], v[i] = read_query(f)

def input(f):
    global V, E, s, t, Q, u, v
    V, E = read_vertices_edges(f)
    s, t = init_edge_lists(E)
    process_edges(f, E, s, t)
    Q = read_queries_count(f)
    u, v = init_query_lists(Q)
    process_queries(f, Q, u, v)

import sys
sys.setrecursionlimit(1000000)

def build_empty_graph(V):
    return [[] for _ in range(V)]

def add_edges_to_graph(E, s, t, G, G_inv):
    for i in range(E):
        G[s[i]].append(t[i])
        G_inv[t[i]].append(s[i])

def find_order_single_vertex(cur, G, used, order):
    if used[cur]:
        return
    used[cur] = True
    for nxt in G[cur]:
        find_order_single_vertex(nxt, G, used, order)
    order.append(cur)

def build_find_order_range(V, G):
    order = []
    used = [False for _ in range(V)]
    for i in range(V):
        find_order_single_vertex(i, G, used, order)
    return list(reversed(order))

def rec_decomp(cur, group_id, G_inv, used, groups):
    if used[cur]:
        return
    used[cur] = True
    groups[cur] = group_id
    for nxt in G_inv[cur]:
        rec_decomp(nxt, group_id, G_inv, used, groups)

def run_decomp(order, V, G_inv):
    groups = [None for _ in range(V)]
    used = [False for _ in range(V)]
    group_id = 0
    for start in order:
        if used[start]:
            continue
        rec_decomp(start, group_id, G_inv, used, groups)
        group_id += 1
    return groups

def print_query_answer(q_idx, groups, u, v):
    if groups[u[q_idx]] == groups[v[q_idx]]:
        print('1')
    else:
        print('0')

def process_all_queries(Q, groups, u, v):
    for i in range(Q):
        print_query_answer(i, groups, u, v)

def solve():
    G = build_empty_graph(V)
    G_inv = build_empty_graph(V)
    add_edges_to_graph(E, s, t, G, G_inv)
    order = build_find_order_range(V, G)
    groups = run_decomp(order, V, G_inv)
    process_all_queries(Q, groups, u, v)

with open('/dev/stdin') as f:
    input(f)
    solve()