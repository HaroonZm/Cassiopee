from heapq import heappush, heappop

def read_graph_parameters():
    return map(int, input().split())

def initialize_edges(num_nodes):
    return [[] for _ in range(num_nodes)]

def read_edge():
    return map(int, input().split())

def adjust_index(u):
    return u - 1

def add_edge(edges, u, v, w):
    edges[u].append((v, w))
    edges[v].append((u, w))

def read_start_end_query():
    return map(int, input().split())

def dijkstra_initialize(num_nodes, start):
    INF = 10 ** 20
    dist = [INF] * num_nodes
    dist[start] = 0
    parents = [[] for _ in range(num_nodes)]
    que = []
    heappush(que, (0, start))
    return dist, parents, que, INF

def dijkstra_update_neighbors(edges, dist, parents, que, score, node):
    for to, w in edges[node]:
        if dist[to] > score + w:
            dist[to] = score + w
            parents[to] = {node}
            heappush(que, (score + w, to))
        elif dist[to] == score + w:
            parents[to].add(node)

def dijkstra_run(edges, num_nodes, start):
    dist, parents, que, INF = dijkstra_initialize(num_nodes, start)
    while que:
        score, node = heappop(que)
        dijkstra_update_neighbors(edges, dist, parents, que, score, node)
    return dist, parents

def on_shortest_path_check(c, d, dist_from_a, parents, mem):
    if c == d:
        return True
    if d in mem:
        return False
    mem.add(d)
    if dist_from_a[c] >= dist_from_a[d]:
        return False
    for parent in parents[d]:
        if on_shortest_path_check(c, parent, dist_from_a, parents, mem):
            return True
    return False

def read_query():
    return map(int, input().split())

def check_nodes_on_shortest_path(c, d, dist_from_a, dist_from_b, shortest, parents):
    cond1 = dist_from_a[c] + dist_from_b[c] == shortest
    cond2 = dist_from_a[d] + dist_from_b[d] == shortest
    cond3 = on_shortest_path_check(c, d, dist_from_a, parents, set())
    return cond1 and cond2 and cond3

def process_queries(q, dist_from_a, dist_from_b, shortest, parents):
    for _ in range(q):
        c, d = read_query()
        c = adjust_index(c)
        d = adjust_index(d)
        if check_nodes_on_shortest_path(c, d, dist_from_a, dist_from_b, shortest, parents):
            print("Yes")
        else:
            print("No")

def main():
    s, r = read_graph_parameters()
    edges = initialize_edges(s)
    for _ in range(r):
        u, v, w = read_edge()
        u = adjust_index(u)
        v = adjust_index(v)
        add_edge(edges, u, v, w)
    a, b, q = read_start_end_query()
    a = adjust_index(a)
    b = adjust_index(b)
    dist_from_a, parents = dijkstra_run(edges, s, a)
    dist_from_b, _ = dijkstra_run(edges, s, b)
    shortest = dist_from_a[b]
    process_queries(q, dist_from_a, dist_from_b, shortest, parents)

main()