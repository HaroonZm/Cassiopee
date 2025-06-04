import sys
import heapq

def dijkstra(n, graph, start):
    # Compute shortest distances from start to all stations using Dijkstra's algorithm
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if dist[u] < d:
            continue
        for v, cost in graph[u]:
            nd = d + cost
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

def main():
    input = sys.stdin.readline
    while True:
        n, m, l, s, t = map(int, input().split())
        if n == 0 and m == 0 and l == 0 and s == 0 and t == 0:
            break

        # Build the graph, adjacency list with (neighbor, cost)
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append((b, c))
            graph[b].append((a, c))

        # Restaurants info: station and eating time
        rest_stations = []
        eat_times = []
        rest_idx_map = dict()  # station -> index 0..l-1
        for i in range(l):
            j_i, e_i = map(int, input().split())
            rest_idx_map[j_i] = i
            rest_stations.append(j_i)
            eat_times.append(e_i)

        # Compute shortest distances from s to all stations
        dist_from_s = dijkstra(n, graph, s)
        # Compute shortest distances from all stations to s (reverse graph)
        # For that, build reversed graph:
        reverse_graph = [[] for _ in range(n + 1)]
        for u in range(1, n+1):
            for v, cost in graph[u]:
                reverse_graph[v].append((u, cost))
        dist_to_s = dijkstra(n, reverse_graph, s)

        # Precompute shortest distances between all restaurants
        # For i in 0..l-1, compute dist from rest_stations[i] to all stations
        dist_rest_to_all = []
        for i in range(l):
            dist_rest_to_all.append(dijkstra(n, graph, rest_stations[i]))

        # Precompute travel times between restaurants: dist from j-th restaurant to k-th restaurant
        dist_rest_to_rest = [[float('inf')] * l for _ in range(l)]
        for i in range(l):
            for j in range(l):
                dist_rest_to_rest[i][j] = dist_rest_to_all[i][rest_stations[j]]

        # Now we want to find the maximum number of restaurants visited 
        # starting from s, then visiting some subset in some order, and 
        # returning to s, so that total travel + eating time <= t

        # Use bit DP over subsets of restaurants
        # dp[mask][i] = minimal time to start at s, visit restaurants in 'mask', 
        # ending at restaurant i (i in mask)
        # We'll initialize with INF, and update by transitions

        INF = float('inf')
        dp = [[INF] * l for _ in range(1 << l)]

        # Initialization: try visiting one restaurant directly from s and eating there
        for i in range(l):
            to_rest = dist_from_s[rest_stations[i]]
            back = dist_to_s[rest_stations[i]]
            if to_rest == float('inf') or back == float('inf'):
                continue
            cost = to_rest + eat_times[i] + back
            if cost <= t:
                dp[1 << i][i] = to_rest + eat_times[i]  # time spent before finishing at i

        # Iterate over subsets and update dp
        for mask in range(1 << l):
            for i in range(l):
                if not (mask & (1 << i)):
                    continue
                if dp[mask][i] == INF:
                    continue
                # Try to add a new restaurant j not in mask
                for j in range(l):
                    if mask & (1 << j):
                        continue
                    travel = dist_rest_to_rest[i][j]
                    if travel == float('inf'):
                        continue
                    new_time = dp[mask][i] + travel + eat_times[j]
                    # Need to check if can return to s after visiting j within t
                    back = dist_to_s[rest_stations[j]]
                    if back == float('inf'):
                        continue
                    if new_time + back <= t:
                        new_mask = mask | (1 << j)
                        if new_time < dp[new_mask][j]:
                            dp[new_mask][j] = new_time

        # Find max number of visited restaurants with any ending restaurant i
        ans = 0
        for mask in range(1 << l):
            # count bits in mask
            cnt = bin(mask).count('1')
            for i in range(l):
                if dp[mask][i] < INF:
                    if cnt > ans:
                        ans = cnt

        print(ans)


if __name__ == "__main__":
    main()