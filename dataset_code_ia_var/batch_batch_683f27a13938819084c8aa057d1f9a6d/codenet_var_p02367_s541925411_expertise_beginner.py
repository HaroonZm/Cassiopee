def solve():
    N, M = map(int, input().split())
    edges = []
    for i in range(N):
        edges.append([])
    for i in range(M):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    bridges, _ = get_lowlink(edges, M)
    result = []
    for a, b in bridges:
        if a < b:
            result.append((a, b))
        else:
            result.append((b, a))
    result.sort()
    for a, b in result:
        print(a, b)

def get_lowlink(edges, edge_num):
    import sys
    sys.setrecursionlimit(1000000)
    n = len(edges)
    order = [-1] * n
    low = [0] * n
    bridges = []
    articulations = []
    cnt = 0

    def dfs(v, parent, k):
        nonlocal cnt
        order[v] = k
        low[v] = k
        cnt += 1
        is_articulation = False
        for dest in edges[v]:
            if order[dest] == -1:
                dfs(dest, v, k + 1)
                if low[v] > low[dest]:
                    low[v] = low[dest]
                if order[v] < low[dest]:
                    bridges.append((v, dest))
                if order[v] <= low[dest]:
                    is_articulation = True
            elif dest != parent:
                if low[v] > order[dest]:
                    low[v] = order[dest]
        if v != 0 and is_articulation:
            articulations.append(v)

    dfs(0, -1, 0)
    return bridges, articulations

if __name__ == "__main__":
    solve()