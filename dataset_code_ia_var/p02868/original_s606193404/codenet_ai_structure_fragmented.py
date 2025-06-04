import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop, heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')

def I():
    return int(sys.stdin.readline())

def LI():
    return list(map(int, sys.stdin.readline().split()))

def get_input_values():
    n, m = LI()
    return n, m

def make_empty_graph(n):
    return [[] for _ in range(n)]

def append_previous_edges(edges, n):
    def append_for_index(i):
        edges[i].append((i-1, 0))
    for i in range(1, n):
        append_for_index(i)

def read_edge():
    return LI()

def add_input_edges(edges, m):
    def process_one_edge():
        l, r, c = read_edge()
        edges[l-1].append((r-1, c))
    for _ in range(m):
        process_one_edge()

def init_dist(n, s):
    d = [inf]*n
    d[s] = 0
    return d

def init_heap(s):
    return [(0, s)]

def update_distance(d, t, new_dist):
    d[t] = new_dist

def should_continue(d, v, c):
    return d[v] < c

def process_neighbor(d, v, t, cost, h):
    if d[v] + cost < d[t]:
        update_distance(d, t, d[v] + cost)
        heappush(h, (d[t], t))

def process_vertex(h, d, graph):
    c, v = heappop(h)
    if should_continue(d, v, c):
        return
    for t, cost in graph[v]:
        process_neighbor(d, v, t, cost, h)

def run_heap(h, d, graph):
    while h:
        process_vertex(h, d, graph)

def dijkstra(s, graph, n):
    d = init_dist(n, s)
    h = init_heap(s)
    run_heap(h, d, graph)
    return d

def output_result(d):
    if d[-1] == inf:
        print(-1)
    else:
        print(d[-1])

def main():
    n, m = get_input_values()
    edges = make_empty_graph(n)
    append_previous_edges(edges, n)
    add_input_edges(edges, m)
    d = dijkstra(0, edges, n)
    output_result(d)

if __name__ == "__main__":
    main()