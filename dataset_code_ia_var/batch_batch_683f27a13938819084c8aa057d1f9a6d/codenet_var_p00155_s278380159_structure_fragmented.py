import sys
from sys import stdin
from math import sqrt

def read_int():
    return int(stdin.readline())

def read_ints():
    return list(map(int, stdin.readline().split()))

def make_graph(n, data):
    size = 101
    graph = [[float('inf')] * size for _ in range(size)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            add_edge_if_close(graph, data[i], data[j])
    return graph

def add_edge_if_close(graph, node1, node2):
    b1, x1, y1 = node1
    b2, x2, y2 = node2
    if b1 == b2:
        return
    dist = calc_distance(x1, y1, x2, y2)
    if dist <= 50.0:
        set_edge(graph, b1, b2, dist)

def calc_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def set_edge(graph, u, v, w):
    graph[u][v] = w
    graph[v][u] = w

def input_data(n):
    result = []
    for _ in range(n):
        result.append(read_ints())
    return result

def handle_queries(m, graph):
    for _ in range(m):
        s, g = read_ints()
        handle_query_single(s, g, graph)

def handle_query_single(s, g, graph):
    if s == g:
        print_single_station(s)
        return
    if not is_valid_station(s) or not is_valid_station(g):
        print_na()
        return
    d, p = run_dijkstra(s, graph)
    if not is_reachable(d, g):
        print_na()
    else:
        print_path(p, s, g)

def print_single_station(s):
    print(s)

def print_na():
    print('NA')

def is_valid_station(x):
    return 1 <= x <= 100

def run_dijkstra(s, graph):
    return dijkstra_fragmented(s, graph)

def dijkstra_fragmented(s, G):
    size = 101
    BLACK, GRAY, WHITE = 0, 1, 2
    d = [float('inf')] * size
    color = [WHITE] * size
    p = [-1] * size
    d[s] = 0
    while True:
        u, mincost = get_min_cost_node(d, color)
        if mincost == float('inf'):
            break
        color[u] = BLACK
        update_neighbors(u, d, p, color, G)
    return d, p

def get_min_cost_node(d, color):
    mincost = float('inf')
    u = -1
    for i in range(101):
        if color[i] != 0 and d[i] < mincost:
            mincost = d[i]
            u = i
    for i in range(101):
        if color[i] == 2 and d[i] < mincost:
            mincost = d[i]
            u = i
    return choose_min_node(d, color, mincost, u)

def choose_min_node(d, color, mincost, u):
    for i in range(101):
        if color[i] != 0 and d[i] < mincost:
            mincost = d[i]
            u = i
    return (u, mincost)

def update_neighbors(u, d, p, color, G):
    for v in range(101):
        if color[v] == 0:
            continue
        if G[u][v] == float('inf'):
            continue
        relax(u, v, d, p, color, G)

def relax(u, v, d, p, color, G):
    if d[u] + G[u][v] < d[v]:
        d[v] = d[u] + G[u][v]
        p[v] = u
        color[v] = 1

def is_reachable(d, g):
    return d[g] != float('inf')

def print_path(p, s, g):
    path = build_path(p, s, g)
    print_path_list(path)

def build_path(p, s, g):
    path = [g]
    cur = g
    while p[cur] != s:
        path.append(p[cur])
        cur = p[cur]
    path.append(s)
    return list(reversed(path))

def print_path_list(path):
    print(' '.join(map(str, path)))

def fragment_main(args):
    while True:
        n = read_int()
        if is_end_input(n):
            break
        data = input_data(n)
        graph = make_graph(n, data)
        m = read_int()
        handle_queries(m, graph)

def is_end_input(n):
    return n == 0

if __name__ == '__main__':
    fragment_main(sys.argv[1:])