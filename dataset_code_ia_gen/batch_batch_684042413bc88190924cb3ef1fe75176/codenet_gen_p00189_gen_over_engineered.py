from typing import List, Tuple, Dict
import heapq


class Town:
    def __init__(self, id_: int):
        self.id = id_

    def __repr__(self):
        return f"Town({self.id})"


class Road:
    def __init__(self, town1: Town, town2: Town, cost: int):
        self.town1 = town1
        self.town2 = town2
        self.cost = cost

    def connects(self, town_a: Town, town_b: Town) -> bool:
        return (self.town1.id == town_a.id and self.town2.id == town_b.id) or \
               (self.town1.id == town_b.id and self.town2.id == town_a.id)

    def __repr__(self):
        return f"Road({self.town1.id}, {self.town2.id}, cost={self.cost})"


class OfficeNetwork:
    def __init__(self):
        self.towns: Dict[int, Town] = {}
        self.roads: List[Road] = []

    def add_road(self, a: int, b: int, cost: int) -> None:
        if a not in self.towns:
            self.towns[a] = Town(a)
        if b not in self.towns:
            self.towns[b] = Town(b)
        road = Road(self.towns[a], self.towns[b], cost)
        self.roads.append(road)

    def get_town_ids(self) -> List[int]:
        return sorted(self.towns.keys())

    def shortest_paths_from(self, start_id: int) -> Dict[int, int]:
        # Dijkstra's algorithm for shortest paths
        dist = {tid: float('inf') for tid in self.towns}
        dist[start_id] = 0
        queue = [(0, start_id)]
        adjacency = self._build_adjacency()
        while queue:
            current_dist, current = heapq.heappop(queue)
            if current_dist > dist[current]:
                continue
            for neighbor, cost in adjacency[current]:
                ndist = current_dist + cost
                if ndist < dist[neighbor]:
                    dist[neighbor] = ndist
                    heapq.heappush(queue, (ndist, neighbor))
        return dist

    def _build_adjacency(self) -> Dict[int, List[Tuple[int, int]]]:
        adjacency: Dict[int, List[Tuple[int, int]]] = {tid: [] for tid in self.towns}
        for road in self.roads:
            adjacency[road.town1.id].append((road.town2.id, road.cost))
            adjacency[road.town2.id].append((road.town1.id, road.cost))
        return adjacency


class ConvenienceEvaluator:
    def __init__(self, network: OfficeNetwork):
        self.network = network

    def evaluate(self) -> Tuple[int, int]:
        min_town_id = -1
        min_sum = float('inf')
        for town_id in self.network.get_town_ids():
            dist_map = self.network.shortest_paths_from(town_id)
            total_cost = sum(dist_map.values())
            if total_cost < min_sum or (total_cost == min_sum and town_id < min_town_id):
                min_sum = total_cost
                min_town_id = town_id
        return min_town_id, min_sum


class InputParser:
    def __init__(self, input_lines: List[str]):
        self.lines = input_lines
        self.index = 0

    def next_int(self) -> int:
        while self.index < len(self.lines):
            line = self.lines[self.index].strip()
            self.index += 1
            if line:
                return int(line)
        return 0

    def next_road_data(self, n: int) -> List[Tuple[int,int,int]]:
        roads = []
        for _ in range(n):
            line = self.lines[self.index].strip()
            self.index += 1
            a_str,b_str,c_str = line.split()
            roads.append((int(a_str), int(b_str), int(c_str)))
        return roads


class SolutionController:
    def __init__(self, raw_input: str):
        self.raw_input = raw_input
        self.parser = InputParser(self.raw_input.splitlines())

    def process(self):
        while True:
            n = self.parser.next_int()
            if n == 0:
                break
            roads = self.parser.next_road_data(n)
            network = OfficeNetwork()
            for a, b, c in roads:
                network.add_road(a, b, c)
            evaluator = ConvenienceEvaluator(network)
            town_id, total_cost = evaluator.evaluate()
            print(town_id, total_cost)


def main():
    import sys
    raw = sys.stdin.read()
    controller = SolutionController(raw)
    controller.process()


if __name__ == "__main__":
    main()