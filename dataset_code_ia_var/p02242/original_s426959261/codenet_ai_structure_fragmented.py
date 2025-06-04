from collections import namedtuple

def create_edge_namedtuple():
    return namedtuple('Edge', ('fr', 'to', 'cost'))

def get_infinity():
    return 1e9

def initialize_distance_list(n, start, inf):
    dists = [inf for _ in range(n)]
    dists[start] = 0
    return dists

def initialize_bellman_ford_vars(n, start, inf):
    dists = initialize_distance_list(n, start, inf)
    return dists

def relax_edges(edges, dists, inf):
    updated = False
    for e in edges:
        if can_relax_edge(e, dists, inf):
            perform_edge_relaxation(e, dists)
            updated = True
    return updated

def can_relax_edge(e, dists, inf):
    return dists[e.fr] != inf and dists[e.fr] + e.cost < dists[e.to]

def perform_edge_relaxation(e, dists):
    dists[e.to] = dists[e.fr] + e.cost

def should_continue(updated):
    return updated

def bellman_ford(n, start, edges):
    inf = get_infinity()
    dists = initialize_bellman_ford_vars(n, start, inf)
    while True:
        updated = relax_edges(edges, dists, inf)
        if not should_continue(updated):
            break
    return dists

def initialize_dijkstra_dists(n, inf):
    dists = [inf for _ in range(n)]
    dists[0] = 0
    return dists

def initialize_determined_list(n):
    return [False for _ in range(n)]

def dijkstra_select_vertex(n, dists, determined, inf):
    v, min_d = -1, inf
    for i in range(n):
        if skip_dijkstra_vertex(determined, i):
            continue
        if dists[i] < min_d:
            v, min_d = i, dists[i]
    return v

def skip_dijkstra_vertex(determined, i):
    return determined[i]

def dijkstra_update_determined(determined, v):
    determined[v] = True

def dijkstra_relax_neighbors(n, v, costs, determined, dists):
    for i in range(n):
        if skip_dijkstra_neighbor(determined, costs, v, i):
            continue
        dists[i] = attempt_dijkstra_relax(dists, costs, v, i)

def skip_dijkstra_neighbor(determined, costs, v, i):
    return determined[i] or costs[v][i] == -1

def attempt_dijkstra_relax(dists, costs, v, i):
    return min(dists[i], dists[v] + costs[v][i])

def dijkstra(n, costs):
    inf = get_infinity()
    dists = initialize_dijkstra_dists(n, inf)
    determined = initialize_determined_list(n)
    while True:
        v = dijkstra_select_vertex(n, dists, determined, inf)
        if v == -1:
            break
        dijkstra_update_determined(determined, v)
        dijkstra_relax_neighbors(n, v, costs, determined, dists)
    return dists

def read_n():
    return int(input())

def initialize_matrix(n):
    return [[-1 for _ in range(n)] for _ in range(n)]

def initialize_edges():
    return []

def parse_node_input():
    return list(map(int, input().split()))

def parse_edges_for_node(i, fs, m, es, Edge):
    ne = fs[1]
    for j in range(ne):
        v = fs[2 + 2 * j]
        c = fs[2 + 2 * j + 1]
        m[i][v] = c
        es.append(Edge(i, v, c))

def read_edges_and_matrix(n, m, es, Edge):
    for i in range(n):
        fs = parse_node_input()
        parse_edges_for_node(i, fs, m, es, Edge)

def print_distances(d):
    for (i, di) in enumerate(d):
        print(i, di)

def main():
    Edge = create_edge_namedtuple()
    n = read_n()
    m = initialize_matrix(n)
    es = initialize_edges()
    read_edges_and_matrix(n, m, es, Edge)
    # d = bellman_ford(n, 0, es)
    d = dijkstra(n, m)
    print_distances(d)

main()