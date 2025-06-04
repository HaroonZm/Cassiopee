import sys
from collections import deque

def read_n():
    return int(sys.stdin.readline())

def read_edge():
    return tuple(map(int, sys.stdin.readline().split()))

def create_edge_list(N):
    return [[] for _ in range(N)]

def add_edge(Edge, a, b):
    Edge[a].append(b)
    Edge[b].append(a)

def build_graph(N):
    Edge = create_edge_list(N)
    for _ in range(N-1):
        a, b = read_edge()
        a -= 1
        b -= 1
        add_edge(Edge, a, b)
    return Edge

def bfs_from_start_nodes(Edge, N, s):
    Q = deque(s)
    used = set(s)
    dist = [0]*N
    while Q:
        vn = Q.pop()
        for vf in Edge[vn]:
            if vf not in used:
                used.add(vf)
                dist[vf] = 1 + dist[vn]
                Q.appendleft(vf)
    return dist

def find_max_index(dist):
    return dist.index(max(dist))

def get_path_nodes(dists, diste, D, N):
    return [i for i in range(N) if dists[i] + diste[i] == D]

def initialize_table(N):
    return [1]*(N+5)

def update_mini_per_node(i, distp, dists, diste, mini):
    if distp[i] == 0:
        return mini
    fi = dists[i]
    if 2*distp[i] == fi:
        mini = max(mini, fi-1)
    else:
        mini = max(mini, fi)
    fi = diste[i]
    if 2*distp[i] == fi:
        mini = max(mini, fi-1)
    else:
        mini = max(mini, fi)
    return mini

def update_table_for_mini(table, mini):
    for i in range(mini+1):
        table[i] = 0

def set_base_table_values(table):
    table[1] = 1
    table[2] = 1

def update_table_after_D(table, D, N):
    for i in range(D+1, N+1):
        table[i] = 1

def get_output(table, N):
    return ''.join(map(str, table[1:N+1]))

def main():
    N = read_n()
    Edge = build_graph(N)
    dist0 = bfs_from_start_nodes(Edge, N, [0])
    st = find_max_index(dist0)
    dists = bfs_from_start_nodes(Edge, N, [st])
    en = find_max_index(dists)
    diste = bfs_from_start_nodes(Edge, N, [en])
    D = dists[en]
    path = get_path_nodes(dists, diste, D, N)
    distp = bfs_from_start_nodes(Edge, N, path)

    table = initialize_table(N)
    mini = 0
    for i in range(N):
        mini = update_mini_per_node(i, distp, dists, diste, mini)
    update_table_for_mini(table, mini)
    set_base_table_values(table)
    update_table_after_D(table, D, N)

    output = get_output(table, N)
    print(output)

main()