import sys
import collections

def can_assign(m, edges, n, low, high):
    # Construct a flow network to check if an orientation exists
    # such that each student's indegree (received gifts) is between low and high
    #
    # We use a circulation with demands approach:
    # For each student:
    #   demand = low
    # Each edge (friend pair) is assigned direction in flow network from u to v or v to u
    # We want to choose directions to satisfy demands
    #
    # Build graph:
    # S - super source
    # T - super sink
    # For each edge:
    #   Introduce an edge node, connect S->edge node (capacity 1) (each edge must be assigned)
    #   edge node -> u and edge node -> v capacity 1, direction chosen by flow
    # For each student node:
    #   connect student -> T with capacity (high - low)
    #
    # total demand = m * low, total flow = m
    #
    # If max flow equals m, feasible assignment exists.

    S = 0
    T = 1
    # nodes: S=0, T=1, edge nodes: 2..m+1, student nodes: m+2 .. m+1+n
    # total nodes = 2 + m + n
    size = 2 + m + n

    graph = [[] for _ in range(size)]

    def add_edge(u, v, cap):
        graph[u].append([v, cap, len(graph[v])])
        graph[v].append([u, 0, len(graph[u]) - 1])

    # Add edges from S to edge nodes with capacity 1
    for i in range(m):
        add_edge(S, 2 + i, 1)
    # Add edges from student nodes to T with capacity high - low
    for i in range(n):
        add_edge(2 + m + i, T, high - low)

    # For each edge node i corresponds to friendship pair edges[i]=(u,v)
    # Add edges from edge node to u node and v node with capacity 1
    # selecting direction means flow goes from edge node to student node
    for i, (u, v) in enumerate(edges):
        u_node = 2 + m + (u - 1)
        v_node = 2 + m + (v - 1)
        edge_node = 2 + i
        add_edge(edge_node, u_node, 1)
        add_edge(edge_node, v_node, 1)

    # Now check if max flow is m
    # max flow implementation (Dinic)
    level = [0]*size
    iter = [0]*size

    def bfs():
        for i in range(size):
            level[i] = -1
        level[S] = 0
        queue = collections.deque([S])
        while queue:
            u = queue.popleft()
            for i,(v,c,rev) in enumerate(graph[u]):
                if c > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[T] != -1

    def dfs(u, flow):
        if u == T:
            return flow
        for i in range(iter[u], len(graph[u])):
            v, c, rev = graph[u][i]
            if c > 0 and level[u] < level[v]:
                d = dfs(v, min(flow, c))
                if d > 0:
                    graph[u][i][1] -= d
                    graph[v][rev][1] += d
                    return d
            iter[u] += 1
        return 0

    flow = 0
    while bfs():
        iter = [0]*size
        f = dfs(S, 10**9)
        while f > 0:
            flow += f
            f = dfs(S, 10**9)
    return flow == m


def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = input()
            if line == '':
                return
        n, m = map(int, line.strip().split())
        if n == 0 and m == 0:
            break
        edges = []
        for _ in range(m):
            while True:
                l = input()
                if l.strip() != '':
                    break
            u,v = map(int, l.strip().split())
            edges.append((u,v))

        # Binary search for minimal difference (h - l)
        # l and h in [0, m]
        left, right = 0, m
        best_diff = m + 1
        best_l = -1
        best_h = -1
        # For minimal difference, for fixed difference d,
        # try all l from 0 to m - d to find feasible with that diff
        # Among those, choose max l.

        for d in range(m+1):
            found = False
            cur_l = -1
            cur_h = -1
            for l in range(m - d +1):
                h = l + d
                if can_assign(m, edges, n, l, h):
                    found = True
                    cur_l = l
                    cur_h = h
                    # since want max l for this diff, continue checking
            if found:
                best_diff = d
                best_l = cur_l
                best_h = cur_h
                break
        print(best_l, best_h)

if __name__ == "__main__":
    main()