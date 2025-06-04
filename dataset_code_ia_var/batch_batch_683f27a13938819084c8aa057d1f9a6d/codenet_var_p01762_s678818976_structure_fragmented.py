from collections import deque

INF = float("inf")

def read_input():
    N = int(input())
    C = list(map(int, input().split()))
    uvp = [list(map(int, input().split())) for _ in range(N-1)]
    return N, C, uvp

def init_edge_utov(N):
    edge = [[0]*(N+1) for _ in range(N+1)]
    utov = [[] for _ in range(N+1)]
    return edge, utov

def build_graph(uvp, edge, utov):
    for u, v, p in uvp:
        add_undirected_edge(u, v, p, edge, utov)

def add_undirected_edge(u, v, p, edge, utov):
    update_edge(u, v, p, edge)
    update_edge(v, u, p, edge)
    utov[u].append(v)
    utov[v].append(u)

def update_edge(x, y, p, edge):
    edge[x][y] = p

def connect_to_sink(C, edge, utov, N):
    for i in range(1, N):
        if node_capacity_positive(C, i):
            connect_edge_to_sink(edge, utov, i, N)

def node_capacity_positive(C, idx):
    return C[idx-1] > 0

def connect_edge_to_sink(edge, utov, i, N):
    edge[i][N] = INF
    utov[i].append(N)
    utov[N].append(i)

def bfs_setup(n):
    return [-1] * n

def bfs(s, g, n, utov, edge):
    bfs_map = bfs_setup(n)
    set_start_distance(bfs_map, s)
    q = initialize_queue(s)
    perform_bfs(q, bfs_map, utov, edge)
    return bfs_map

def set_start_distance(bfs_map, s):
    bfs_map[s] = 0

def initialize_queue(s):
    q = deque()
    q.append(s)
    return q

def perform_bfs(q, bfs_map, utov, edge):
    while queue_not_empty(q):
        u = pop_from_queue(q)
        scan_neighbors(u, q, bfs_map, utov, edge)

def queue_not_empty(q):
    return bool(q)

def pop_from_queue(q):
    return q.popleft()

def scan_neighbors(u, q, bfs_map, utov, edge):
    for v in utov[u]:
        try_update_bfs(u, v, q, bfs_map, edge)

def try_update_bfs(u, v, q, bfs_map, edge):
    if edge_has_capacity(u, v, edge) and not_visited(v, bfs_map):
        update_distance(v, u, bfs_map)
        add_to_queue(v, q)

def edge_has_capacity(u, v, edge):
    return edge[u][v] > 0

def not_visited(v, bfs_map):
    return bfs_map[v] < 0

def update_distance(v, u, bfs_map):
    bfs_map[v] = bfs_map[u] + 1

def add_to_queue(v, q):
    q.append(v)

def update(s, g, bfs_map, utov, edge):
    f, distance, p, y = prepare_update(g, bfs_map)
    for i in reversed(range(distance)):
        found = find_previous_node(i, y, bfs_map, utov, edge)
        if found is None:
            return 0
        x, minf = found
        if minf < f:
            f = minf
        y = x
        p[i][0] = x
        p[i][1] = y
    update_edges_in_path(p, f, edge)
    return f

def prepare_update(g, bfs_map):
    f = INF
    distance = bfs_map[g]
    p = [[None, None] for _ in range(distance)]
    y = g
    return f, distance, p, y

def find_previous_node(i, y, bfs_map, utov, edge):
    for x in utov[y]:
        if edge_has_capacity(x, y, edge) and correct_layer(x, i, bfs_map):
            return x, edge[x][y]
    return None

def correct_layer(x, i, bfs_map):
    return bfs_map[x] == i

def update_edges_in_path(p, f, edge):
    for x, y in p:
        edge[x][y] -= f
        edge[y][x] += f

def dinic(s, g, n, utov, edge):
    max_flow = 0
    while True:
        bfs_map = bfs(s, g, n, utov, edge)
        if flow_not_possible(bfs_map, g):
            return max_flow
        cap = update(s, g, bfs_map, utov, edge)
        while more_flow(cap):
            max_flow += cap
            cap = update(s, g, bfs_map, utov, edge)

def flow_not_possible(bfs_map, g):
    return bfs_map[g] < 0

def more_flow(cap):
    return cap > 0

def main():
    N, C, uvp = read_input()
    edge, utov = init_edge_utov(N)
    build_graph(uvp, edge, utov)
    connect_to_sink(C, edge, utov, N)
    result = dinic(0, N, N+1, utov, edge)
    print(result)

main()