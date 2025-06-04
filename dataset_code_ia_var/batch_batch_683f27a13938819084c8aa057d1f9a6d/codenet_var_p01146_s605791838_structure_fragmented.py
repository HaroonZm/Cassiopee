import sys
import heapq

def get_maxint():
    # Compatibility for Python 2 and 3
    try:
        return sys.maxint
    except AttributeError:
        return sys.maxsize

def initialize_distance_and_prev(num, start):
    maxint = get_maxint()
    dist = [maxint] * num
    prev = [maxint] * num
    dist[start] = 0
    return dist, prev

def push_to_queue(q, cost, node):
    heapq.heappush(q, (cost, node))

def pop_from_queue(q):
    return heapq.heappop(q)

def should_skip_node(dist, src, prov_cost, path):
    if dist[src] < prov_cost:
        return True
    if src not in path:
        return True
    return False

def process_neighbor(dist, prev, q, src, dest, edge_cost):
    if dist[dest] > dist[src] + edge_cost:
        dist[dest] = dist[src] + edge_cost
        push_to_queue(q, dist[dest], dest)
        prev[dest] = src

def process_all_neighbors(path, src, dist, prev, q):
    for dest, cost in path.get(src, []):
        process_neighbor(dist, prev, q, src, dest, cost)

def dijkstra_core(num, path, start, goal=None):
    dist, prev = initialize_distance_and_prev(num, start)
    q = []
    push_to_queue(q, 0, start)
    while len(q) != 0:
        prov_cost, src = pop_from_queue(q)
        if should_skip_node(dist, src, prov_cost, path):
            continue
        process_all_neighbors(path, src, dist, prev, q)
    if goal is not None:
        return get_path(goal, prev)
    else:
        return dist

def get_path(goal, prev):
    maxint = get_maxint()
    path = [goal]
    dest = goal
    while prev[dest] != maxint:
        path.append(prev[dest])
        dest = prev[dest]
    return list(reversed(path))

class Dijkstra(object):
    def dijkstra(self, num, path, start, goal=None):
        return dijkstra_core(num, path, start, goal)

    def get_path(self, goal, prev):
        return get_path(goal, prev)

def read_map_and_params():
    return map(int, raw_input().split())

def is_end_line(N):
    return N == 0

def read_list():
    return map(int, raw_input().split())

def make_edges_for_Ls(Ls, M, edge):
    for l in Ls:
        for i in xrange(M):
            key = l * (M + 1) + i
            if key not in edge:
                edge[key] = []
            edge[key].append((l * (M + 1) + i + 1, 1))

def ensure_edge_for_key(edge, key):
    if key not in edge:
        edge[key] = []

def process_K_lines(K, M, edge):
    for _ in xrange(K):
        s, g, c = map(int, raw_input().split())
        for i in xrange(c, M + 1):
            key_s = s * (M + 1) + i
            key_g = g * (M + 1) + i
            ensure_edge_for_key(edge, key_s)
            ensure_edge_for_key(edge, key_g)
            edge[key_s].append((g * (M + 1) + i - c, c))
            edge[key_g].append((s * (M + 1) + i - c, c))

def call_dijkstra(N, M, edge, A):
    num_vertices = N * (M + 1)
    start_vertex = A * (M + 1) + M
    return Dijkstra().dijkstra(num_vertices, edge, start_vertex)

def find_min_cost(cost, H, M):
    maxint = get_maxint()
    minCost = maxint
    for i in xrange(M + 1):
        idx = H * (M + 1) + i
        if cost[idx] < minCost:
            minCost = cost[idx]
    return minCost

def output_result(minCost):
    maxint = get_maxint()
    if minCost == maxint:
        print "Help!"
    else:
        print minCost

def main_loop():
    while True:
        N, M, L, K, A, H = read_map_and_params()
        if is_end_line(N):
            break
        Ls = read_list()
        edge = {}
        make_edges_for_Ls(Ls, M, edge)
        process_K_lines(K, M, edge)
        cost = call_dijkstra(N, M, edge, A)
        minCost = find_min_cost(cost, H, M)
        output_result(minCost)

main_loop()