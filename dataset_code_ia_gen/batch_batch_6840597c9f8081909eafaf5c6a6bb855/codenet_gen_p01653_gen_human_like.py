import sys
import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cd, u = heapq.heappop(heap)
        if dist[u] < cd:
            continue
        for v, w in graph[u]:
            nd = cd + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

def solve():
    input = sys.stdin.readline
    while True:
        N, M, S1, S2, T = map(str, input().split())
        if N == '0' and M == '0' and S1 == '0' and S2 == '0' and T == '0':
            break
        N, M, S1, S2, T = int(N), int(M), int(S1), int(S2), int(T)
        normal_graph = [[] for _ in range(N + 1)]
        magical_edges = []
        for _ in range(M):
            a, b, w = input().split()
            a, b = int(a), int(b)
            if w == 'x':
                # Store magical edges without length for now
                magical_edges.append((a, b))
            else:
                w = int(w)
                normal_graph[a].append((b, w))
                normal_graph[b].append((a, w))
        # We want to find for some x >= 0 the minimal |dist_S1_T(x) - dist_S2_T(x)|
        # where magical edges have length x, and normal edges have fixed length.
        # Approach:
        # We separate magical and normal edges.
        # We compute shortest distances from T to all nodes with magical edges set to length 0 and length 1.
        # The length from T to node v when magical edges have length x is:
        # dist_normal[v] + x * magic_edge_count_in_path
        # But the paths can vary, so we precompute base distances and counts of magical edges used to reach each node.
        # To do that, we run modified Dijkstra on reversed graph from T twice:
        # 1) With magical edges treated as length 0
        # 2) With magical edges treated as length 1
        # From these two we can get dist0 and dist1. 
        # Then the number of magical edges used in shortest path is dist1[v] - dist0[v]
        # Because difference between dist1 and dist0 gives how many magical edges are in the shortest path from v to T.
        # Since paths may not be unique, we will track minimal and maximal counts or at least one shortest path count
        # Here, we assume uniqueness or use dist1-dist0 as count.

        # Build reversed graphs for dist0 and dist1
        graph0 = [[] for _ in range(N + 1)]
        graph1 = [[] for _ in range(N + 1)]
        # Normal edges
        for u in range(1, N + 1):
            for v, w in normal_graph[u]:
                graph0[v].append((u, w))
                graph1[v].append((u, w))
        # Magical edges (length 0 in graph0, length 1 in graph1)
        for a, b in magical_edges:
            graph0[b].append((a, 0))
            graph0[a].append((b, 0))
            graph1[b].append((a, 1))
            graph1[a].append((b, 1))

        dist0 = dijkstra(N, graph0, T)
        dist1 = dijkstra(N, graph1, T)

        # For node v, number_of_magical_edges = dist1[v] - dist0[v]
        # Distance from v to T when magical edges have length x is dist0[v] + x * (dist1[v] - dist0[v])

        # For S1 and S2, dist_S1(x) = dist0[S1] + x * (dist1[S1] - dist0[S1])
        # dist_S2(x) = dist0[S2] + x * (dist1[S2] - dist0[S2])
        # difference D(x) = dist_S1(x) - dist_S2(x) = (dist0[S1] - dist0[S2]) + x * ((dist1[S1] - dist0[S1]) - (dist1[S2] - dist0[S2]))

        c0_1 = dist0[S1]
        c1_1 = dist1[S1]
        c0_2 = dist0[S2]
        c1_2 = dist1[S2]

        base = c0_1 - c0_2
        coeff = (c1_1 - c0_1) - (c1_2 - c0_2)

        # D(x) = base + coeff * x ; x >= 0 integer

        # We want to find min |D(x)| over x >= 0 integer

        if coeff == 0:
            # difference constant = base
            ans = abs(base)
        else:
            # |base + coeff * x| minimal
            # The expression is a line. The minimal absolute value occurs at x = -base/coeff (real).
            x_star = -base / coeff
            cand = []
            for x in [int(x_star), int(x_star)+1]:
                if x >= 0:
                    val = abs(base + coeff * x)
                    cand.append(val)
            # Also check boundary x=0 in case of negative x_star
            val0 = abs(base)
            cand.append(val0)
            ans = min(cand)
        print(ans)

if __name__ == "__main__":
    solve()