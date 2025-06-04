import sys
from collections import deque

def read_n():
    return int(sys.stdin.readline())

def read_d():
    return [int(x) for x in sys.stdin.readline().split()]

def make_empty_capacity_matrix(size):
    return [[0] * size for _ in range(size)]

def make_empty_adjacency_list(size):
    return [[] for _ in range(size)]

def add_inf_edges(d, v, c, n):
    for i in range(1, n):
        if d[i-1] > 0:
            add_edge(v, c, i, n, float('inf'))
            add_edge(v, c, n, i, float('inf'))

def add_edge(v, c, a, b, cap):
    v[a].append(b)
    v[b].append(a)  # Maintain undirected edge for adjacency
    c[a][b] = cap
    c[b][a] = cap if c[b][a] == 0 else c[b][a]  # Don't overwrite if already set (possibly from inf)

def read_and_add_edges(num_edges, v, c):
    for _ in range(num_edges):
        add_edge_from_input(v, c)

def add_edge_from_input(v, c):
    a, b, p = [int(x) for x in sys.stdin.readline().split()]
    add_edge(v, c, a, b, p)

def bfs_layer_map(s, g, n, v, c):
    bfs_map = create_bfs_map(n)
    initialize_bfs(bfs_map, s)
    q = initialize_bfs_queue(s)
    bfs_traverse(q, bfs_map, v, c)
    return bfs_map

def create_bfs_map(n):
    return [-1] * n

def initialize_bfs(bfs_map, s):
    bfs_map[s] = 0

def initialize_bfs_queue(s):
    return deque([s])

def bfs_traverse(q, bfs_map, v, c):
    while q:
        x = q.popleft()
        process_bfs_neighbors(x, q, bfs_map, v, c)

def process_bfs_neighbors(x, q, bfs_map, v, c):
    for y in v[x]:
        if can_bfs_visit(x, y, bfs_map, c):
            assign_bfs_level(bfs_map, x, y)
            q.append(y)

def can_bfs_visit(x, y, bfs_map, c):
    return c[x][y] > 0 and bfs_map[y] < 0

def assign_bfs_level(bfs_map, x, y):
    bfs_map[y] = bfs_map[x] + 1

def update_flow(s, g, bfs_map, v, c):
    min_cap, path = find_augmenting_path(s, g, bfs_map, v, c)
    if min_cap == 0:
        return 0
    apply_augmenting_flow(path, min_cap, c)
    return min_cap

def find_augmenting_path(s, g, bfs_map, v, c):
    min_cap = float('inf')
    path = initialize_path(bfs_map[g])
    y = g
    for i in reversed(range(bfs_map[g])):
        path[i][1] = y
        found, x, cap = find_predecessor(y, i, v, c, bfs_map)
        if not found:
            return 0, None
        if cap < min_cap:
            min_cap = cap
        y = x
        path[i][0] = x
    return min_cap, path

def initialize_path(length):
    return [[None, None] for _ in range(length)]

def find_predecessor(y, level, v, c, bfs_map):
    for x in v[y]:
        if c[x][y] > 0 and bfs_map[x] == level:
            return True, x, c[x][y]
    return False, None, None

def apply_augmenting_flow(path, min_cap, c):
    for x, y in path:
        update_capacity(x, y, min_cap, c)

def update_capacity(x, y, min_cap, c):
    c[x][y] -= min_cap
    c[y][x] += min_cap

def dinic_main(s, g, n, v, c):
    f = 0
    while True:
        bfs_map = bfs_layer_map(s, g, n, v, c)
        if bfs_map[g] < 0:
            return f
        cap = update_flow(s, g, bfs_map, v, c)
        while cap > 0:
            f += cap
            cap = update_flow(s, g, bfs_map, v, c)

def main():
    n = read_n()
    d = read_d()
    cap_size = n + 1
    c = make_empty_capacity_matrix(cap_size)
    v = make_empty_adjacency_list(cap_size)
    add_inf_edges(d, v, c, n)
    read_and_add_edges(n - 1, v, c)
    print(dinic_main(0, n, cap_size, v, c))

main()