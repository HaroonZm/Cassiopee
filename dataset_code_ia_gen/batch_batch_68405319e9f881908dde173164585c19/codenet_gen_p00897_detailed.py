import sys
import heapq

def main():
    input = sys.stdin.readline

    while True:
        # Read the number of roads N, number of LPG stations M and tank capacity cap
        N, M, cap = map(int, input().split())
        if N == 0 and M == 0 and cap == 0:
            break  # end of all datasets

        # Read source and destination city names
        src, dest = input().split()

        # Map from city name to city index for easier processing
        city_index = {}
        idx_counter = 0

        def get_city_idx(city):
            nonlocal idx_counter
            if city not in city_index:
                city_index[city] = idx_counter
                idx_counter += 1
            return city_index[city]

        # Read road info and build graph as adjacency list
        # Each entry: city -> list of (neighbor, distance)
        graph = {}

        for _ in range(N):
            c1, c2, d = input().split()
            d = int(d)
            a = get_city_idx(c1)
            b = get_city_idx(c2)

            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, d))
            graph[b].append((a, d))

        # Read LPG stations
        lpg_stations = set()
        for _ in range(M):
            station_city = input().strip()
            lpg_stations.add(get_city_idx(station_city))

        source = get_city_idx(src)
        destination = get_city_idx(dest)

        # Add source and destination cities to graph if missing (to avoid KeyError)
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []

        # Tank capacity in liters,
        # the car consumes 1 liter per 10 km, so max travel distance without refuel:
        max_dist = cap * 10

        # Important:
        # The car can fill the tank completely at any LPG station or at the starting city (if it has LPG)
        # Also, at the destination, he can refill, so reaching dest with any fuel left is enough.
        # We use a Dijkstra-like search on state space (city, fuel_left)
        # Fuel_left is liters left in the tank (integer between 0 and cap)

        # We'll track distance traveled (total km) as the cost to minimize
        # The priority queue elements are (distance_so_far, city, fuel_left)

        # Initial state: at source city with full tank (cap liters)
        # Because if the source has LPG station or we start with full tank per problem statement
        # The problem states tank is full at start, so start with cap liters
        # initialize dp table: dict with keys (city, fuel_left) -> shortest distance found
        import collections

        dist = {}
        dist[(source, cap)] = 0

        pq = [(0, source, cap)]

        while pq:
            cur_dist, city, fuel = heapq.heappop(pq)

            if (city, fuel) not in dist or dist[(city, fuel)] < cur_dist:
                continue

            # If arrived at destination, output the distance and break
            if city == destination:
                print(cur_dist)
                break

            # If current city is LPG station, refill tank to full capacity
            # Refill option: if not already full, we can refill without cost (just reset fuel)
            # Only add new state if better
            if city in lpg_stations and fuel < cap:
                if (city, cap) not in dist or dist[(city, cap)] > cur_dist:
                    dist[(city, cap)] = cur_dist
                    heapq.heappush(pq, (cur_dist, city, cap))

            # Explore neighbors
            for nxt, d in graph[city]:
                # Check if can go from city to nxt with current fuel
                # distance d in km, 1 liter per 10 km -> liters_needed = ceil(d/10)
                # Problem states tank may reach exactly zero fuel at arrival, so:
                # liters_needed = ceil(d/10) ?
                # But distances are integer, consumption 1l/10km, so liters_needed = (d + 9)//10
                liters_needed = (d + 9) // 10  # ceiling division

                if liters_needed <= fuel:
                    new_fuel = fuel - liters_needed
                    new_dist = cur_dist + d
                    # Only push if better distance found for this state
                    if (nxt, new_fuel) not in dist or dist[(nxt, new_fuel)] > new_dist:
                        dist[(nxt, new_fuel)] = new_dist
                        heapq.heappush(pq, (new_dist, nxt, new_fuel))
        else:
            # If while loop ended without break - no path found
            print(-1)

if __name__ == "__main__":
    main()