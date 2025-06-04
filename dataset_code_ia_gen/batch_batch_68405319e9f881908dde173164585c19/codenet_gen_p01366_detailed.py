import sys
import heapq

def main():
    input = sys.stdin.readline
    while True:
        # Read the number of cities N and roads M
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break

        # Graph representation: adjacency list
        # Each element: (neighbor, length, cost)
        graph = [[] for _ in range(N + 1)]
        edges = []

        for _ in range(M):
            u, v, d, c = map(int, input().split())
            graph[u].append((v, d, c))
            graph[v].append((u, d, c))
            edges.append((u, v, d, c))

        # Step 1: Use Dijkstra's algorithm from the capital (city 1)
        # to get shortest distance from capital to each city
        dist = [float('inf')] * (N + 1)
        dist[1] = 0
        pq = [(0, 1)]  # (distance, city)

        while pq:
            cur_dist, u = heapq.heappop(pq)
            if cur_dist > dist[u]:
                continue
            for v, length, cost in graph[u]:
                nd = cur_dist + length
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        # After this, dist[i] is the shortest distance from city 1 to city i

        # Step 2: Filter edges that can be on shortest paths from capital
        # Condition for edge (u,v) with length d:
        # It can appear in shortest paths if dist[u] + d == dist[v]
        # or dist[v] + d == dist[u].
        # We'll use these edges to build a subgraph where all shortest paths are preserved.

        shortest_path_edges = []  # To store edges that lie on at least one shortest path

        for u, v, d, c in edges:
            if dist[u] + d == dist[v] or dist[v] + d == dist[u]:
                # This edge could be on some shortest path from city 1
                shortest_path_edges.append((u, v, c))

        # Step 3: The required plan must connect all cities (graph is connected through shortest paths),
        # and distances from capital must not change => only edges in shortest_path_edges can be chosen.
        # We want a minimal cost subset that still connects all cities (spanning tree)
        # and keeps distances from capital unchanged.

        # The problem reduces to finding a Minimum Spanning Tree (MST) on the graph formed by shortest_path_edges.

        # Step 4: Build MST from edges in shortest_path_edges using Kruskal's algorithm

        # Union-Find data structure (Disjoint Set Union - DSU)
        parent = [i for i in range(N + 1)]
        rank = [0] * (N + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            if rank[a] < rank[b]:
                parent[a] = b
            else:
                parent[b] = a
                if rank[a] == rank[b]:
                    rank[a] += 1
            return True

        # Sort edges by cost
        shortest_path_edges.sort(key=lambda x: x[2])

        mst_cost = 0
        edges_used = 0
        for u, v, c in shortest_path_edges:
            if union(u, v):
                mst_cost += c
                edges_used += 1
                if edges_used == N - 1:
                    break

        # Output the total MST cost that satisfies constraints
        print(mst_cost)

if __name__ == "__main__":
    main()