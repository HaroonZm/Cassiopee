import sys
sys.setrecursionlimit(10**7)

def edmonds(root, n, edges):
    INF = 10**15
    total_cost = 0
    while True:
        in_edge = [INF] * n
        pre = [-1] * n
        for u, v, w in edges:
            if w < in_edge[v] and v != root:
                in_edge[v] = w
                pre[v] = u
        for i in range(n):
            if i != root and in_edge[i] == INF:
                # no arborescence possible
                return None
        total_cost += sum(in_edge[i] for i in range(n) if i != root)
        # detect cycles
        vis = [-1]*n
        id = [-1]*n
        cycle_num = 0
        for i in range(n):
            v = i
            while v != root and vis[v] != i and id[v] == -1:
                vis[v] = i
                v = pre[v]
            if v != root and id[v] == -1:
                u = pre[v]
                while u != v:
                    id[u] = cycle_num
                    u = pre[u]
                id[v] = cycle_num
                cycle_num += 1
        if cycle_num == 0:
            break
        for i in range(n):
            if id[i] == -1:
                id[i] = cycle_num
                cycle_num += 1
        new_edges = []
        for u, v, w in edges:
            u_id = id[u]
            v_id = id[v]
            if u_id != v_id:
                w -= in_edge[v]
                new_edges.append((u_id, v_id, w))
        n = cycle_num
        root = id[root]
        edges = new_edges
    return total_cost

def main():
    import sys
    input = sys.stdin.readline
    V, E, r = map(int, input().split())
    edges = []
    for _ in range(E):
        s, t, w = map(int, input().split())
        edges.append((s, t, w))
    res = edmonds(r, V, edges)
    print(res if res is not None else 0)

if __name__ == '__main__':
    main()