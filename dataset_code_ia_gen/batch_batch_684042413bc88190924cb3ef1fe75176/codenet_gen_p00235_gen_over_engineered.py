from abc import ABC, abstractmethod
from typing import List, Tuple, Dict
import sys

class IBridge(ABC):
    @property
    @abstractmethod
    def island_a(self) -> int: pass

    @property
    @abstractmethod
    def island_b(self) -> int: pass

    @property
    @abstractmethod
    def traversal_time(self) -> int: pass

class Bridge(IBridge):
    def __init__(self, island_a: int, island_b: int, traversal_time: int):
        self._island_a = island_a
        self._island_b = island_b
        self._traversal_time = traversal_time

    @property
    def island_a(self) -> int:
        return self._island_a

    @property
    def island_b(self) -> int:
        return self._island_b

    @property
    def traversal_time(self) -> int:
        return self._traversal_time

class IIsland(ABC):
    @property
    @abstractmethod
    def id(self) -> int: pass

    @property
    @abstractmethod
    def adjacent_bridges(self) -> List[IBridge]: pass

    @abstractmethod
    def add_bridge(self, bridge: IBridge): pass

class Island(IIsland):
    def __init__(self, id: int):
        self._id = id
        self._adjacent_bridges: List[IBridge] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def adjacent_bridges(self) -> List[IBridge]:
        return self._adjacent_bridges

    def add_bridge(self, bridge: IBridge):
        self._adjacent_bridges.append(bridge)

class IWaterCity(ABC):
    @property
    @abstractmethod
    def islands(self) -> Dict[int, IIsland]: pass

    @property
    @abstractmethod
    def bridges(self) -> List[IBridge]: pass

    @abstractmethod
    def add_bridge(self, island_a: int, island_b: int, time: int): pass

class WaterCity(IWaterCity):
    def __init__(self, island_count: int):
        self._islands: Dict[int, IIsland] = {i: Island(i) for i in range(1, island_count + 1)}
        self._bridges: List[IBridge] = []

    @property
    def islands(self) -> Dict[int, IIsland]:
        return self._islands

    @property
    def bridges(self) -> List[IBridge]:
        return self._bridges

    def add_bridge(self, island_a: int, island_b: int, time: int):
        bridge = Bridge(island_a, island_b, time)
        self._bridges.append(bridge)
        self._islands[island_a].add_bridge(bridge)
        self._islands[island_b].add_bridge(bridge)

class IRescueOperation(ABC):
    @abstractmethod
    def compute_minimum_explosion_time(self) -> int: pass

class RescueOperation(IRescueOperation):
    def __init__(self, city: IWaterCity):
        self._city = city
        self._visited_edges = set()
        self._visited_nodes = set()

    def compute_minimum_explosion_time(self) -> int:
        # The problem reduces to calculating the minimum time to traverse all edges,
        # starting at node 1, and detonating edges adjacent to the current island instantly.
        #
        # The minimum time = sum of all edges * 2 - maximum distance from start node 1 to any leaf.
        # Because we must come back over every edge except those on the longest path to leaf, which can be left exploded last.

        total_bridge_time = sum(bridge.traversal_time for bridge in self._city.bridges)

        # Build adjacency list with times for Dijkstra or DFS
        adjacency = {i: [] for i in self._city.islands}
        for bridge in self._city.bridges:
            adjacency[bridge.island_a].append((bridge.island_b, bridge.traversal_time))
            adjacency[bridge.island_b].append((bridge.island_a, bridge.traversal_time))

        # We'll do a DFS from node 1 to find distances to all nodes and find the max distance to leaf (max path)
        def dfs(node: int, parent: int) -> int:
            max_dist = 0
            for (neighbor, dist) in adjacency[node]:
                if neighbor == parent:
                    continue
                current_dist = dfs(neighbor, node) + dist
                if current_dist > max_dist:
                    max_dist = current_dist
            return max_dist

        max_path_distance = dfs(1, -1)
        # Minimal time = 2 * total_bridge_time - max_path_distance
        result = 2 * total_bridge_time - max_path_distance
        return result

def parse_input_and_execute():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    results: List[int] = []
    while True:
        if idx >= len(input_lines):
            break
        n_line = input_lines[idx].strip()
        idx += 1
        if n_line == '0':
            break
        N = int(n_line)
        city = WaterCity(N)
        for _ in range(N - 1):
            a, b, t = map(int, input_lines[idx].strip().split())
            idx += 1
            city.add_bridge(a, b, t)
        operation = RescueOperation(city)
        results.append(operation.compute_minimum_explosion_time())
    for res in results:
        print(res)

if __name__ == "__main__":
    parse_input_and_execute()