from heapq import heappush, heappop

def read_input():
    N, M, X = map(int, input().split())
    T = [int(input()) for _ in range(N)]
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    return N, M, X, T, edges

def build_graph(N, edges):
    G = [[] for _ in range(N)]
    for A, B, D in edges:
        G[A-1].append((B-1, D))
        G[B-1].append((A-1, D))
    return G

def create_dist(N, X, INF=10**9):
    return [[INF] * (2*X + 1) for _ in range(N)]

def initial_state(X):
    return 0, 0, -X

def should_continue(dist, u, t, cost):
    return dist[u][t] < cost

def calculate_t1(t, d):
    if t > 0:
        return max(0, t - d)
    else:
        return min(0, t + d)

def forbidden_transition(t1, T_v):
    return (t1 < 0 and T_v == 2) or (t1 > 0 and T_v == 0)

def adjust_t1(T_v, t1, X):
    selector = [-X, t1, X]
    return selector[T_v]

def update_dist(dist, v, t1, cost, d):
    return cost + d < dist[v][t1]

def process_neighbors(u, t, cost, G, T, X, dist, que):
    for v, d in G[u]:
        t1 = calculate_t1(t, d)
        if forbidden_transition(t1, T[v]):
            continue
        t1 = adjust_t1(T[v], t1, X)
        if update_dist(dist, v, t1, cost, d):
            dist[v][t1] = cost + d
            heappush(que, (cost + d, v, t1))

def run_dijkstra(N, X, G, T, dist):
    queue = []
    start = initial_state(X)
    dist[start[1]][start[2]] = start[0]
    heappush(queue, start)
    while queue:
        cost, u, t = heappop(queue)
        if should_continue(dist, u, t, cost):
            continue
        process_neighbors(u, t, cost, G, T, X, dist, queue)

def find_answer(dist, N):
    return min(dist[N-1])

def main():
    N, M, X, T, edges = read_input()
    G = build_graph(N, edges)
    dist = create_dist(N, X)
    run_dijkstra(N, X, G, T, dist)
    print(find_answer(dist, N))

main()