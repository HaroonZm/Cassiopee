class TaxiNetwork:
    class Town:
        def __init__(self, id_, cost, max_ride):
            self.id = id_
            self.cost = cost
            self.max_ride = max_ride
            self.adj = []

    class TaxiCompany:
        def __init__(self, town):
            self.town = town
            self.cost = town.cost
            self.max_ride = town.max_ride

    class RideSegment:
        # Represents a possible ride starting at a given town using its taxi company
        def __init__(self, start_town, reachable_towns):
            self.start_town = start_town
            self.reachable_towns = reachable_towns  # set of towns reachable within max_ride

    def __init__(self, n, k, town_specs, roads):
        self.n = n
        self.k = k
        self.towns = [None] + [self.Town(i, *town_specs[i-1]) for i in range(1, n+1)]
        for a, b in roads:
            self.towns[a].adj.append(b)
            self.towns[b].adj.append(a)
        self.taxi_companies = [None] + [self.TaxiCompany(self.towns[i]) for i in range(1, n+1)]

    def compute_all_reachable_segments(self):
        # For each town i, compute which towns can be reached using taxi i within max_ride roads
        self.ride_segments = [None]*(self.n+1)
        from collections import deque
        for i in range(1, self.n+1):
            max_r = self.taxi_companies[i].max_ride
            start = i
            visited = set()
            queue = deque()
            queue.append((start, 0))  # (current_node, distance)
            visited.add(start)
            while queue:
                node, dist = queue.popleft()
                if dist == max_r:
                    continue
                for nxt in self.towns[node].adj:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, dist+1))
            self.ride_segments[i] = self.RideSegment(start, visited)

    def minimum_total_cost(self):
        # Dijkstra over town states: cost to arrive at each town (via any combination)
        import heapq
        INF = 10**15
        dist = [INF]*(self.n+1)
        dist[1] = 0
        hq = [(0, 1)]  # (cost, town)
        while hq:
            cost, town = heapq.heappop(hq)
            if dist[town] < cost:
                continue
            if town == self.n:
                return cost
            # From current town, use taxi company corresponding to this town
            taxi_index = town
            segment = self.ride_segments[taxi_index]
            taxi_cost = self.taxi_companies[taxi_index].cost
            for reachable_town in segment.reachable_towns:
                new_cost = cost + taxi_cost
                if dist[reachable_town] > new_cost:
                    dist[reachable_town] = new_cost
                    heapq.heappush(hq, (new_cost, reachable_town))
        return dist[self.n]

def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    town_specs = [tuple(map(int, input().split())) for _ in range(N)]
    roads = [tuple(map(int, input().split())) for _ in range(K)]
    network = TaxiNetwork(N, K, town_specs, roads)
    network.compute_all_reachable_segments()
    print(network.minimum_total_cost())

if __name__ == "__main__":
    main()