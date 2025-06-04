class Town:
    def __init__(self, id_: int, visa_fee: int, altitude: int):
        self.id = id_
        self.visa_fee = visa_fee
        self.altitude = altitude

class Road:
    def __init__(self, start: Town, end: Town, cost: int):
        self.start = start
        self.end = end
        self.cost = cost

class Graph:
    def __init__(self, towns: list[Town]):
        self.towns = towns
        self.adj = {town.id: [] for town in towns}

    def add_road(self, road: Road):
        self.adj[road.start.id].append(road)

    def neighbors(self, town_id: int):
        return self.adj[town_id]

class TripPhase:
    ASCENDING = 'ascending'
    DESCENDING = 'descending'

class TripPlanner:
    def __init__(self, n: int, towns: list[Town], roads: list[Road]):
        self.n = n
        self.graph = Graph(towns)
        for road in roads:
            self.graph.add_road(road)

    class State:
        __slots__ = ['visited', 'town_id']
        def __init__(self, visited: frozenset[int], town_id: int):
            self.visited = visited
            self.town_id = town_id
        def __hash__(self):
            return hash((self.visited, self.town_id))
        def __eq__(self, other):
            return self.visited == other.visited and self.town_id == other.town_id

    def _can_travel(self, from_town: Town, to_town: Town, phase: str) -> bool:
        if phase == TripPhase.ASCENDING:
            # Return phase: prohibit ascending roads; allow descending or equal alt
            return to_town.altitude <= from_town.altitude
        else:
            # Go phase: prohibit descending roads; allow ascending or equal alt
            return from_town.altitude <= to_town.altitude

    def _min_cost_phase(self, start: int, end: int, phase: str) -> int:
        import heapq
        n = self.n
        towns = self.graph.towns
        graph = self.graph

        start_town = towns[start-1]
        end_town = towns[end-1]

        # Use Dijkstra with state (current town, frozenset of visited towns for visa fee)
        # To avoid exponential state space growth, keep track of best cost per (node, visited).
        initial_state = self.State(frozenset([start]), start)

        dist = {}
        dist[initial_state] = 0

        heap = [(0, initial_state)]

        while heap:
            curr_cost, state = heapq.heappop(heap)

            if state.town_id == end:
                return curr_cost

            if dist[state] < curr_cost:
                continue

            current_town = towns[state.town_id - 1]

            for road in graph.neighbors(state.town_id):
                neighbor = road.end
                # Check altitude constraint depending on phase
                if not self._can_travel(current_town, neighbor, phase):
                    continue

                # New visited towns set - if not visited, pay visa fee (except towns 1 and n)
                pay_visa = 0
                if neighbor.id not in state.visited and neighbor.id != 1 and neighbor.id != n:
                    pay_visa = neighbor.visa_fee

                new_visited = state.visited
                if neighbor.id not in new_visited:
                    new_visited = frozenset(set(new_visited) | {neighbor.id})

                new_cost = curr_cost + road.cost + pay_visa
                new_state = self.State(new_visited, neighbor.id)

                if new_state not in dist or new_cost < dist[new_state]:
                    dist[new_state] = new_cost
                    heapq.heappush(heap, (new_cost, new_state))

        return -1

    def minimum_total_cost(self) -> int:
        # Go phase: from 1 to n, prohibit descending roads (only ascending or equal)
        cost_go = self._min_cost_phase(1, self.n, TripPhase.DESCENDING)
        if cost_go == -1:
            return -1
        # Return phase: from n to 1, prohibit ascending roads (only descending or equal)
        cost_return = self._min_cost_phase(self.n, 1, TripPhase.ASCENDING)
        if cost_return == -1:
            return -1
        return cost_go + cost_return

class InputParser:
    def __init__(self):
        pass

    @staticmethod
    def parse_town_data(n: int, input_lines: list[str]) -> list[Town]:
        # First and last towns' data fixed
        towns = [Town(1, 0, 0)]
        # Next n-2 towns (2..n-1)
        for i in range(2, n):
            d, e = map(int, input_lines[i-2].split())
            towns.append(Town(i, d, e))
        towns.append(Town(n, 0, 1000))
        return towns

    @staticmethod
    def parse_roads(m: int, input_lines: list[str], towns: list[Town]) -> list[Road]:
        town_map = {town.id: town for town in towns}
        roads = []
        for line in input_lines:
            a, b, c = map(int, line.split())
            roads.append(Road(town_map[a], town_map[b], c))
        return roads

def main():
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip()]
    idx = 0
    while True:
        if idx >= len(lines):
            break
        n_m = lines[idx].split()
        idx += 1
        if n_m == ['0','0']:
            break
        n, m = map(int, n_m)
        # read town data (n-2 lines)
        town_data_lines = lines[idx:idx+n-2]
        idx += (n-2)
        towns = InputParser.parse_town_data(n, town_data_lines)
        # read road data (m lines)
        road_data_lines = lines[idx:idx+m]
        idx += m
        roads = InputParser.parse_roads(m, road_data_lines, towns)

        planner = TripPlanner(n, towns, roads)
        ans = planner.minimum_total_cost()
        print(ans)

if __name__ == '__main__':
    main()