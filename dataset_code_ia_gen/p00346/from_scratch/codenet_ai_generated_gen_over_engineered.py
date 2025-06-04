class Town:
    def __init__(self, id_):
        self.id = id_
        self.adjacent = {}

    def add_road(self, other, distance):
        self.adjacent[other] = distance


class RoadNetwork:
    def __init__(self, towns_count):
        self.towns = {i: Town(i) for i in range(1, towns_count + 1)}

    def add_road(self, s, t, d):
        self.towns[s].add_road(t, d)
        self.towns[t].add_road(s, d)

    def dijkstra(self, start):
        import heapq
        dist = {town_id: float('inf') for town_id in self.towns}
        dist[start] = 0
        hq = [(0, start)]
        while hq:
            current_dist, current_town = heapq.heappop(hq)
            if current_dist > dist[current_town]:
                continue
            for nxt, length in self.towns[current_town].adjacent.items():
                nd = current_dist + length
                if nd < dist[nxt]:
                    dist[nxt] = nd
                    heapq.heappush(hq, (nd, nxt))
        return dist


class RelayCourseCalculator:
    def __init__(self, network):
        self.network = network
        self.all_pairs_shortest_max = -1
        self.start_town = None
        self.goal_town = None
        self.distances = {}

    def compute_all_distances(self):
        # Precompute shortest paths from all towns
        for town_id in self.network.towns:
            self.distances[town_id] = self.network.dijkstra(town_id)

    def identify_max_shortest_path(self):
        max_dist = -1
        start, goal = None, None
        for i in self.network.towns:
            for j in self.network.towns:
                if i < j:
                    dist_ij = self.distances[i][j]
                    if dist_ij != float('inf') and dist_ij > max_dist:
                        max_dist = dist_ij
                        start, goal = i, j
        self.all_pairs_shortest_max = max_dist
        self.start_town = start
        self.goal_town = goal

    def find_one_shortest_path(self):
        # We find one shortest path from start to goal by Dijkstra with path reconstruction.
        import heapq

        prev = {town_id: None for town_id in self.network.towns}
        dist = {town_id: float('inf') for town_id in self.network.towns}
        dist[self.start_town] = 0
        hq = [(0, self.start_town)]
        while hq:
            current_dist, current_town = heapq.heappop(hq)
            if current_town == self.goal_town:
                break
            if current_dist > dist[current_town]:
                continue
            for nxt, length in self.network.towns[current_town].adjacent.items():
                nd = current_dist + length
                if nd < dist[nxt]:
                    dist[nxt] = nd
                    prev[nxt] = current_town
                    heapq.heappush(hq, (nd, nxt))

        # Reconstruct path
        path = []
        cur = self.goal_town
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        return path

    def towns_in_relay_course(self):
        if self.all_pairs_shortest_max == -1 or self.start_town is None or self.goal_town is None:
            raise RuntimeError("Max shortest path or start/goal not identified")
        path = self.find_one_shortest_path()
        return set(path)


class QuietTownFinder:
    def __init__(self, network):
        self.network = network
        self.course_towns = set()

    def compute(self):
        calc = RelayCourseCalculator(self.network)
        calc.compute_all_distances()
        calc.identify_max_shortest_path()
        self.course_towns = calc.towns_in_relay_course()

    def find_quiet_towns(self):
        quiet_towns = []
        for town_id in self.network.towns:
            if town_id not in self.course_towns:
                quiet_towns.append(town_id)
        return sorted(quiet_towns)


def main():
    import sys
    input = sys.stdin.readline

    N, R = map(int, input().split())
    network = RoadNetwork(N)
    for _ in range(R):
        s, t, d = map(int, input().split())
        network.add_road(s, t, d)

    finder = QuietTownFinder(network)
    finder.compute()
    quiet_towns = finder.find_quiet_towns()

    print(len(quiet_towns))
    for town in quiet_towns:
        print(town)


if __name__ == "__main__":
    main()