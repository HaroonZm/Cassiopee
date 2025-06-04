import sys
import heapq

def dijkstra(adj, start, n):
    # adj: adjacency list, start: start node, n: number of nodes
    dist = [[float('inf')] * 2 for _ in range(n + 1)]  # dist[node][ship_status]
    # ship_status: 0 = no ship, 1 = have ship
    dist[start][1] = 0  # start with the ship at port town z1
    pq = [(0, start, 1)]  # (cost, node, ship_status)

    while pq:
        cost, u, ship = heapq.heappop(pq)
        if dist[u][ship] < cost:
            continue
        for v, time, mode in adj[u]:
            # mode == 'L' => land route, ship presence not required
            # mode == 'S' => sea route, ship must be present
            if mode == 'L':
                # travel by land: ship stays as is
                new_ship = ship
            else:
                # sea route: requires ship at u to go
                if ship == 0:
                    continue  # no ship, can't go by sea
                # after travel by sea, ship is at v too
                new_ship = 1

            new_cost = cost + time
            
            # additionally, handle ship drop/return rules:
            # Actually, it's okay: traveling sea route keeps ship with carrier.
            # Traveling land keeps ship state the same (has ship or not).
            # If travelling land from a node that has ship, ship stays there (still with him),
            # from node without ship, no ship.
            # This matches problem's description.

            if dist[v][new_ship] > new_cost:
                dist[v][new_ship] = new_cost
                heapq.heappush(pq, (new_cost, v, new_ship))
    return dist

def main():
    input = sys.stdin.readline

    while True:
        line = input().strip()
        if not line:
            break
        N, M = map(int, line.split())
        if N == 0 and M == 0:
            break

        # Build graph with modes
        # adjacency list: node -> list of (neighbor, time, mode)
        adj = [[] for _ in range(N + 1)]
        for _ in range(M):
            x, y, t, sl = input().split()
            x = int(x)
            y = int(y)
            t = int(t)
            # undirected graph
            adj[x].append((y, t, sl))
            adj[y].append((x, t, sl))

        R = int(input())
        targets = list(map(int, input().split()))

        # Initial state: start at targets[0], with ship (1)
        # We must follow the given order strictly:
        # from targets[i] to targets[i+1], shortest path with ship state transition considered.

        total_time = 0
        current_pos = targets[0]
        # at start, ship is with Rito at current_pos (a port town for sure)
        current_ship_status = 1  # 1: have ship

        for i in range(R - 1):
            start = targets[i]
            goal = targets[i + 1]

            # Run dijkstra from start:
            dist = dijkstra(adj, start, N)

            # We want minimum cost to reach goal with any ship status
            # but last delivery at goal must be possible:
            # ship can be either with or without Rito depending on path,
            # but making delivery doesn't require ship, only traveling sea routes.
            # So we take min dist[goal][0], dist[goal][1]
            best = min(dist[goal][0], dist[goal][1])

            total_time += best

        print(total_time)

if __name__ == '__main__':
    main()