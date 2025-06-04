import sys
import heapq

def solve():
    input = sys.stdin.readline
    while True:
        # Read n (number of islands) and k (number of subsequent lines)
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            # End of all data sets
            break

        # Initialize adjacency list to store graph edges.
        # For each island, we keep list of (neighbor, cost) pairs.
        graph = [[] for _ in range(n + 1)]

        # List to store the queries (orders) that require answers
        queries = []

        # We'll process lines one by one. For any new ship route,
        # we add routes to the graph.
        # For queries (orders), we run shortest path using current graph.

        for _ in range(k):
            data = list(map(int, input().split()))
            if data[0] == 0:
                # Order query: 0 a b
                a, b = data[1], data[2]
                queries.append((a, b))
            else:
                # New ship route: 1 c d e
                c, d, e = data[1], data[2], data[3]
                # Since multiple ships can operate between same islands,
                # we add edges without removing old ones.
                graph[c].append((d, e))
                graph[d].append((c, e))

        # For each query order, compute the minimum fare using Dijkstra
        # from departure island to destination island in current graph.

        for a, b in queries:
            # Implement Dijkstra algorithm

            # distance array - initialize with a large number
            dist = [float('inf')] * (n + 1)
            dist[a] = 0
            # min-heap for exploration: (cost, island)
            heap = [(0, a)]

            while heap:
                cost, island = heapq.heappop(heap)
                # If this cost is already larger than recorded, skip
                if dist[island] < cost:
                    continue
                # If we reached destination, can break early
                if island == b:
                    break
                # Relax edges from current island
                for nxt, w in graph[island]:
                    new_cost = cost + w
                    if dist[nxt] > new_cost:
                        dist[nxt] = new_cost
                        heapq.heappush(heap, (new_cost, nxt))

            # Print the result: -1 if unreachable, else minimum cost
            if dist[b] == float('inf'):
                print(-1)
            else:
                print(dist[b])

if __name__ == "__main__":
    solve()