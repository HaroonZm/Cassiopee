import heapq
import sys

def read_input():
    return sys.stdin.readline()

def parse_first_line(line):
    return map(int, line.split())

def create_empty_edges(n):
    return ([[] for _ in range(n)], [[] for _ in range(n)])

def encode_edge(cost, v):
    return cost * (10 ** 6) + v

def decode_edge(e):
    return e // (10 ** 6), e % (10 ** 6)

def add_bidirectional_edge(edge, u, v, cost):
    edge[u].append(encode_edge(cost, v))
    edge[v].append(encode_edge(cost, u))

def process_edges_input(edge1, edge2, n, m):
    for _ in range(m):
        u, v, a, b = map(int, read_input().split())
        add_bidirectional_edge(edge1, u - 1, v - 1, a)
        add_bidirectional_edge(edge2, u - 1, v - 1, b)

def initialize_dijkstra(n, s):
    d = [float("inf")] * n
    used = [True] * n
    d[s] = 0
    used[s] = False
    return d, used

def push_initial_edges_to_heap(edge, s, edgelist):
    for e in edge[s]:
        heapq.heappush(edgelist, e)

def process_adjacent_edges(edge, minedge_v, edgelist, used, minedge_cost):
    for e in edge[minedge_v]:
        e_cost, e_v = decode_edge(e)
        if used[e_v]:
            heapq.heappush(edgelist, encode_edge(e_cost + minedge_cost, e_v))

def dijkstra_heap(edge, s, n):
    d, used = initialize_dijkstra(n, s)
    edgelist = []
    push_initial_edges_to_heap(edge, s, edgelist)
    while edgelist:
        minedge = heapq.heappop(edgelist)
        minedge_cost, minedge_v = decode_edge(minedge)
        if not used[minedge_v]:
            continue
        d[minedge_v] = minedge_cost
        used[minedge_v] = False
        process_adjacent_edges(edge, minedge_v, edgelist, used, minedge_cost)
    return d

def sum_distances(d1, d2, n):
    return [d1[i] + d2[i] for i in range(n)]

def update_min_right_to_left(d, n):
    for i in range(n-1):
        d[-i-2] = min(d[-i-2], d[-i-1])

def print_results(d):
    for dd in d:
        print(10 ** 15 - dd)

def main():
    input_line = read_input()
    n, m, s, t = parse_first_line(input_line)
    edge1, edge2 = create_empty_edges(n)
    process_edges_input(edge1, edge2, n, m)
    d1 = dijkstra_heap(edge1, s - 1, n)
    d2 = dijkstra_heap(edge2, t - 1, n)
    d = sum_distances(d1, d2, n)
    update_min_right_to_left(d, n)
    print_results(d)

main()