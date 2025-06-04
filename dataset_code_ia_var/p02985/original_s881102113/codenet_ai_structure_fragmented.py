def read_input():
    N, K = map(int, input().split())
    return N, K

def read_edges(N):
    if N - 1:
        a, b = zip(*(map(int, input().split()) for _ in range(N - 1)))
        return a, b
    else:
        return (), ()

def build_graph(N, a, b):
    G = [set() for _ in range(N + 1)]
    for x, y in zip(a, b):
        G[x].add(y)
        G[y].add(x)
    return G

def create_visited(N):
    return [False for _ in range(N + 1)]

def init_queue():
    from heapq import heappush
    q = []
    heappush(q, (1, 1))
    return q

def process_node(G, v, q, ans, K, MOD):
    from heapq import heappush, heappop
    while q:
        i, c = heappop(q)
        X = get_unvisited_neighbors(G, v, i)
        ans = visit_neighbors(X, G, v, q, ans, K, MOD, c)
    return ans

def get_unvisited_neighbors(G, v, i):
    return {x for x in G[i] if not v[x]}

def visit_neighbors(X, G, v, q, ans, K, MOD, c):
    from heapq import heappush
    for l, j in enumerate(X):
        heappush(q, (j, 2))
        ans = update_answer(ans, K, c, l, MOD)
        v[j] = mark_visited()
    return ans

def update_answer(ans, K, c, l, MOD):
    return (ans * (K - c - l)) % MOD

def mark_visited():
    return True

def main():
    MOD = 10 ** 9 + 7
    N, K = read_input()
    a, b = read_edges(N)
    G = build_graph(N, a, b)
    q = init_queue()
    v = create_visited(N)
    ans = K
    set_root_visited(v)
    ans = process_node(G, v, q, ans, K, MOD)
    print(ans)

def set_root_visited(v):
    v[1] = True

main()