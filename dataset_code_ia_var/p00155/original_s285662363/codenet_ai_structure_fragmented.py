from heapq import heappush, heappop

INF = 10 ** 20

def read_n():
    return int(input())

def read_build_point():
    b, x, y = map(int, input().split())
    return b - 1, (x, y)

def build_points(n):
    points = [None] * n
    for _ in range(n):
        idx, pos = read_build_point()
        points[idx] = pos
    return points

def edge_cost(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def can_connect(cost):
    return cost <= 50

def make_edges(n, points):
    edges = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            c = edge_cost(points[i], points[j])
            if can_connect(c):
                edges[i].append((c, j))
                edges[j].append((c, i))
    return edges

def read_m():
    return int(input())

def read_query():
    s, g = map(int, input().split())
    return s - 1, g - 1

def init_costs(n, s):
    costs = [INF] * n
    costs[s] = 0
    return costs

def init_paths(n, s):
    paths = [[] for _ in range(n)]
    paths[s] = [s]
    return paths

def init_queue(s):
    return [(0, [s])]

def should_update(costs, to, new_cost):
    return costs[to] > new_cost

def update_costs(costs, to, val):
    costs[to] = val

def update_paths(paths, to, path):
    paths[to] = path

def dijkstra(n, edges, s, g):
    costs = init_costs(n, s)
    paths = init_paths(n, s)
    que = []
    for item in init_queue(s):
        heappush(que, item)
    while que:
        dist, path = heappop(que)
        last = path[-1]
        for cost, to in edges[last]:
            new_cost = dist + cost
            if should_update(costs, to, new_cost):
                update_costs(costs, to, new_cost)
                new_path = path + [to]
                update_paths(paths, to, new_path)
                heappush(que, (new_cost, new_path))
    return paths[g]

def output_path(path):
    print(*[x + 1 for x in path])

def output_NA():
    print("NA")

def handle_queries(n, edges, m):
    for _ in range(m):
        s, g = read_query()
        path = dijkstra(n, edges, s, g)
        if path:
            output_path(path)
        else:
            output_NA()

def main_loop():
    while True:
        n = read_n()
        if n == 0:
            break
        build_pts = build_points(n)
        edges = make_edges(n, build_pts)
        m = read_m()
        handle_queries(n, edges, m)

main_loop()