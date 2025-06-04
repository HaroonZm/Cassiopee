import sys
import heapq

def dijkstra(adj, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cur_d, u = heapq.heappop(heap)
        if dist[u] < cur_d:
            continue
        for v, cost in adj[u]:
            nd = cur_d + cost
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
        
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, c = map(int, input().split())
            adj[a].append((b, c))
            adj[b].append((a, c))

        # Read restaurants info
        rest_stations = []
        eat_times = []
        rest_map = dict()
        for i in range(l):
            j_i, e_i = map(int, input().split())
            rest_stations.append(j_i)
            eat_times.append(e_i)
            rest_map[j_i] = i

        # Distance from start to all stations
        dist_s = dijkstra(adj, s, n)

        # Distance from each restaurant station to all stations (to get return distances)
        dist_rest = []
        for r in rest_stations:
            dist_rest.append(dijkstra(adj, r, n))

        # For simplified TSP, we create a matrix dist between restaurants and from/to start
        # dist_s_rest[i]: distance from start to restaurant i
        dist_s_rest = [dist_s[r] for r in rest_stations]
        # dist_rest_s[i]: distance from restaurant i back to start
        dist_rest_s = [dist_rest[i][s] for i in range(l)]

        # dist_rest_rest[i][j]: distance from restaurant i to restaurant j
        dist_rest_rest = [[float('inf')] * l for _ in range(l)]
        for i in range(l):
            for j in range(l):
                if i == j:
                    dist_rest_rest[i][j] = 0
                else:
                    dist_rest_rest[i][j] = dist_rest[i][rest_stations[j]]

        # DP for TSP on restaurants:
        # dp[mask][i] = minimum time to finish eating at restaurants in 'mask', ending at restaurant i
        # We must account eating time at each restaurant
        # Time includes travel + eating

        dp = [[float('inf')] * l for _ in range(1 << l)]

        # Initialize dp with going from s to each restaurant i and eating there
        for i in range(l):
            if dist_s_rest[i] == float('inf'):
                continue
            cost = dist_s_rest[i] + eat_times[i]
            if cost + dist_rest_s[i] <= t:
                dp[1 << i][i] = cost

        for mask in range(1 << l):
            for u in range(l):
                if dp[mask][u] == float('inf'):
                    continue
                for v in range(l):
                    if mask & (1 << v):
                        continue
                    d = dist_rest_rest[u][v]
                    if d == float('inf'):
                        continue
                    nd = dp[mask][u] + d + eat_times[v]
                    # Check if we can return from v to s within time
                    if nd + dist_rest_s[v] <= t and nd < dp[mask | (1 << v)][v]:
                        dp[mask | (1 << v)][v] = nd

        ans = 0
        for mask in range(1 << l):
            for i in range(l):
                if dp[mask][i] == float('inf'):
                    continue
                # Check if this mask can be done within time (consider return to s)
                if dp[mask][i] + dist_rest_s[i] <= t:
                    cnt = bin(mask).count('1')
                    if cnt > ans:
                        ans = cnt
        print(ans)

if __name__ == "__main__":
    main()