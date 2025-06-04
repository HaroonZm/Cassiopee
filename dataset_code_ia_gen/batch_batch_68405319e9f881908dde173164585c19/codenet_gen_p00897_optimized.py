import sys
import heapq

input = sys.stdin.readline

while True:
    N, M, cap = map(int, input().split())
    if N == 0 and M == 0 and cap == 0:
        break
    src, dest = input().split()

    city_id = {}
    def get_id(name):
        if name not in city_id:
            city_id[name] = len(city_id)
        return city_id[name]

    edges = [[] for _ in range(2 * N + 2 * M + 10)]  # enough size
    # Read roads
    for _ in range(N):
        c1, c2, d = input().split()
        d = int(d)
        id1 = get_id(c1)
        id2 = get_id(c2)
        edges[id1].append((id2, d))
        edges[id2].append((id1, d))

    stations = set()
    for _ in range(M):
        s = input().strip()
        stations.add(get_id(s))

    if src not in city_id or dest not in city_id:
        print(-1)
        continue
    start = city_id[src]
    end = city_id[dest]

    # BFS/Dijkstra on state: (city, fuel)
    # Each edge consumes fuel equal to distance. Can refuel to full tank at stations at any time, including start and end.
    # Since capacity ≤ 200, keep fuel from 0 to cap inclusive.
    # Init dist array
    dist = [ [float('inf')] * (cap + 1) for _ in range(len(city_id)) ]
    # Start with full tank at src (tank always full at start)
    dist[start][cap] = 0
    hq = [(0, start, cap)]

    while hq:
        cost, city, fuel = heapq.heappop(hq)
        if city == end:
            print(cost)
            break
        if dist[city][fuel] < cost:
            continue
        # Refuel if city is a station (tank full)
        if city in stations and fuel < cap:
            if dist[city][cap] > cost:
                dist[city][cap] = cost
                heapq.heappush(hq, (cost, city, cap))
        # Move to neighbors if fuel allows
        for nxt, d in edges[city]:
            if d <= fuel:
                nfuel = fuel - d
                ncost = cost + d
                if dist[nxt][nfuel] > ncost:
                    dist[nxt][nfuel] = ncost
                    heapq.heappush(hq, (ncost, nxt, nfuel))
    else:
        # no break -> no path
        print(-1)