from functools import reduce, partial
from operator import mul, or_, and_
import itertools

def deep_dfs(*pack):
    v, t, f, used, graph, path = pack
    return (
        f if v == t else next(
            (
                (
                    graph[v].__setitem__(to, graph[v][to] - d),
                    graph[to].__setitem__(v, graph[to][v] + d),
                    d
                )[-1]
                for to in sorted(graph[v], key=lambda x: -graph[v][x] + x)
                if not used[to] and graph[v][to] and not used.__setitem__(to, True)
                for d in [
                    deep_dfs(to, t, min(f, graph[v][to]), used, graph, path + [to])
                ] if d > 0
            ),
            0
        )
    )

def baroque_max_flow(s, t, graph):
    flow, q = 0, itertools.count()
    while True:
        used = [False] * len(graph)
        f = deep_dfs(s, t, float('inf'), used, graph, [s])
        flow += f
        if not (f and f != float('inf')):
            return flow

H, W = map(int, input().split())
raw = [input() for _ in range(H)]
a = list(map(list, raw))

blob = [{} for _ in range(H + W + 2)]

def set_edges(h, w, symbol):
    if symbol == 'o':
        blob[h].setdefault(H + w, 1)
        blob[H + w].setdefault(h, 1)
    elif symbol == 'S':
        for u, v in [(H + W, h), (H + W, H + w), (h, H + W), (H + w, H + W)]:
            blob[u][v] = blob[u].get(v, 0) + (float('inf') if u < v else 0)
    elif symbol == 'T':
        for u, v in [(H + W + 1, h), (H + W + 1, H + w), (h, H + W + 1), (H + w, H + W + 1)]:
            blob[u][v] = blob[u].get(v, 0) + (float('inf') if u > v else 0)

list(map(lambda x: list(map(lambda y:
    set_edges(x[0], y[0], y[1]), enumerate(a[x[0]]))),
    enumerate(a)
))

ans = baroque_max_flow(H + W, H + W + 1, blob)
print(-1 if ans == float('inf') else ans)