import heapq
import math

def read_graph_input():
    nvertices, nedges, s = map(int, input().split())
    Adj = initialize_adjacency_list(nvertices)
    fill_edges(Adj, nedges)
    return nvertices, Adj, s

def initialize_adjacency_list(nvertices):
    return [[] for _ in range(nvertices)]

def fill_edges(Adj, nedges):
    for _ in range(nedges):
        add_edge(Adj)

def add_edge(Adj):
    u, v, w = map(int, input().split())
    Adj[u].append((v, w))

def initialize_distances(nvertices, s):
    d = [float('inf')] * nvertices
    set_source_distance(d, s)
    return d

def set_source_distance(d, s):
    d[s] = 0

def initialize_priority_queue(s):
    return [(0, s)]

def process_priority_queue(Q, Adj, d):
    while not is_priority_queue_empty(Q):
        w, u = pop_queue(Q)
        if not should_continue(d, u, w):
            relax_neighbors(u, Adj, d, Q)

def is_priority_queue_empty(Q):
    return not Q

def pop_queue(Q):
    return heapq.heappop(Q)

def should_continue(d, u, w):
    return d[u] < w

def relax_neighbors(u, Adj, d, Q):
    for v, cost in get_neighbors(Adj, u):
        if is_shorter_path(d, u, v, cost):
            update_distance(d, v, d[u] + cost)
            push_to_queue(Q, d[v], v)

def get_neighbors(Adj, u):
    return Adj[u]

def is_shorter_path(d, u, v, cost):
    return d[u] + cost < d[v]

def update_distance(d, v, value):
    d[v] = value

def push_to_queue(Q, value, v):
    heapq.heappush(Q, (value, v))

def print_distances(d):
    for cost in d:
        print_distance(cost)

def print_distance(cost):
    if math.isinf(cost):
        print("INF")
    else:
        print(cost)

def main():
    nvertices, Adj, s = read_graph_input()
    d = initialize_distances(nvertices, s)
    Q = initialize_priority_queue(s)
    process_priority_queue(Q, Adj, d)
    print_distances(d)

main()