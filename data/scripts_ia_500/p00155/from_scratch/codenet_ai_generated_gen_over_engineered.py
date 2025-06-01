from typing import List, Tuple, Dict, Optional
import sys
import math


class Building:
    def __init__(self, number: int, x: int, y: int):
        self.number = number
        self.x = x
        self.y = y

    def distance_to(self, other: "Building") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


class Graph:
    def __init__(self, buildings: List[Building], max_rope_length: float):
        self.buildings = buildings
        self.max_rope_length = max_rope_length
        self.index_by_number = {b.number: i for i, b in enumerate(buildings)}
        self.adj_list = self._build_adjacency()

    def _build_adjacency(self) -> List[List[int]]:
        adjacency = [[] for _ in range(len(self.buildings))]
        for i, b1 in enumerate(self.buildings):
            for j, b2 in enumerate(self.buildings):
                if i != j and b1.distance_to(b2) <= self.max_rope_length:
                    adjacency[i].append(j)
        return adjacency

    def shortest_path(self, start_number: int, goal_number: int) -> Optional[List[int]]:
        start_idx = self.index_by_number.get(start_number)
        goal_idx = self.index_by_number.get(goal_number)
        if start_idx is None or goal_idx is None:
            return None

        # BFS to find shortest path
        from collections import deque
        queue = deque([start_idx])
        visited = [False] * len(self.buildings)
        prev = [None] * len(self.buildings)
        visited[start_idx] = True

        while queue:
            current = queue.popleft()
            if current == goal_idx:
                break
            for neighbor in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    prev[neighbor] = current
                    queue.append(neighbor)

        if not visited[goal_idx]:
            return None

        # reconstruct path
        path_idx = []
        at = goal_idx
        while at is not None:
            path_idx.append(at)
            at = prev[at]
        path_idx.reverse()
        return [self.buildings[i].number for i in path_idx]


class Dataset:
    def __init__(self, buildings: List[Building], queries: List[Tuple[int, int]]):
        self.buildings = buildings
        self.queries = queries
        self.graph = Graph(buildings, 50)

    def solve(self) -> List[str]:
        results = []
        for start, goal in self.queries:
            path = self.graph.shortest_path(start, goal)
            if path is None:
                results.append("NA")
            else:
                results.append(" ".join(map(str, path)))
        return results


class InputProcessor:
    def __init__(self, lines: List[str]):
        self.lines = lines
        self.index = 0

    def _read_line(self) -> str:
        line = self.lines[self.index].strip()
        self.index += 1
        return line

    def _read_int(self) -> int:
        return int(self._read_line())

    def _read_buildings(self, n: int) -> List[Building]:
        buildings = []
        for _ in range(n):
            b_str = self._read_line()
            b_num, x, y = map(int, b_str.split())
            buildings.append(Building(b_num, x, y))
        # normalize building list by number in ascending order to avoid confusion
        buildings.sort(key=lambda b: b.number)
        return buildings

    def _read_queries(self, m: int) -> List[Tuple[int, int]]:
        queries = []
        for _ in range(m):
            s, g = map(int, self._read_line().split())
            queries.append((s, g))
        return queries

    def parse_datasets(self) -> List[Dataset]:
        datasets = []
        while True:
            if self.index >= len(self.lines):
                break
            n_line = self.lines[self.index].strip()
            if n_line == '0':
                break
            n = int(n_line)
            self.index += 1
            buildings = self._read_buildings(n)
            m = int(self._read_line())
            queries = self._read_queries(m)
            datasets.append(Dataset(buildings, queries))
        return datasets


def main():
    stdin_lines = [line.rstrip('\n') for line in sys.stdin]
    processor = InputProcessor(stdin_lines)
    datasets = processor.parse_datasets()

    for dataset in datasets:
        results = dataset.solve()
        for line in results:
            print(line)


if __name__ == "__main__":
    main()