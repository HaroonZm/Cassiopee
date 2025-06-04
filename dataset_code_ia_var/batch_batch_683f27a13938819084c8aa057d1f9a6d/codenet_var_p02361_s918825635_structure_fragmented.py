from collections import defaultdict
from collections import deque
from sys import stdin

def read_first_line():
    line = stdin.readline()
    return line

def parse_first_line(line):
    return [int(x) for x in line.split(' ')]

def initialize_graph():
    return defaultdict(list)

def read_edge_line():
    line = stdin.readline()
    return line

def parse_edge_line(line):
    return [int(x) for x in line.split(' ')]

def add_edge_to_graph(G, s, t, w):
    G[s].append((t,w))
    return G

def initialize_distances(V):
    d = {}
    for i in range(V):
        set_distance_inf(d, i)
    return d

def set_distance_inf(d, i):
    d[i] = float('inf')

def set_distance_zero(d, R):
    d[R] = 0

def initialize_queue(R):
    return deque([(R)])

def get_neighbors(G, u):
    return G[u]

def need_relaxation(d, v0, u, w):
    return d[v0] > d[u] + w

def relax_distance(d, v0, u, w):
    d[v0] = d[u] + w

def enqueue(q, v0):
    q.append(v0)

def sp_build(G, R, V):
    d = initialize_distances(V)
    set_distance_zero(d, R)
    q = initialize_queue(R)
    process_queue(q, G, d)
    return d

def process_queue(q, G, d):
    while queue_not_empty(q):
        u = dequeue(q)
        process_neighbors(G, u, d, q)

def queue_not_empty(q):
    return bool(q)

def dequeue(q):
    return q.popleft()

def process_neighbors(G, u, d, q):
    for v in get_neighbors(G, u):
        try_relax_and_enqueue(d, v, u, q)

def try_relax_and_enqueue(d, v, u, q):
    v0, w = v
    if need_relaxation(d, v0, u, w):
        relax_distance(d, v0, u, w)
        enqueue(q, v0)

def output_distances(d, V):
    for k in range(V):
        print_distance(d, k)

def print_distance(d, k):
    if is_inf_distance(d, k):
        print_inf()
    else:
        print_value(d, k)

def is_inf_distance(d, k):
    return d[k] == float('inf')

def print_inf():
    print("INF")

def print_value(d, k):
    print(d[k])

def main():
    line = read_first_line()
    V, E, R = parse_first_line(line)
    G = initialize_graph()
    for case in range(E):
        edge_line = read_edge_line()
        s, t, w = parse_edge_line(edge_line)
        add_edge_to_graph(G, s, t, w)
    d = sp_build(G, R, V)
    output_distances(d, V)

main()