from __future__ import annotations
from typing import List, Dict, Tuple, Optional, Iterator
from collections import deque
import math


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_to(self, other: Point2D) -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


class Building:
    __slots__ = ('number', 'location')

    def __init__(self, number: int, location: Point2D):
        self.number = number
        self.location = location


class Graph:
    def __init__(self, buildings: List[Building], max_jump_distance: float):
        self.buildings = buildings
        self.max_jump_distance = max_jump_distance
        self.adjacency: Dict[int, List[int]] = {}
        self._build_graph()

    def _build_graph(self):
        # Initialize adjacency list
        self.adjacency = {b.number: [] for b in self.buildings}
        # Build edges for buildings within max_jump_distance
        n = len(self.buildings)
        for i in range(n):
            for j in range(i + 1, n):
                b1 = self.buildings[i]
                b2 = self.buildings[j]
                dist = b1.location.distance_to(b2.location)
                if dist <= self.max_jump_distance:
                    self.adjacency[b1.number].append(b2.number)
                    self.adjacency[b2.number].append(b1.number)

    def shortest_path(self, start: int, goal: int) -> Optional[List[int]]:
        if start == goal:
            return [start]
        # BFS to find shortest path in unweighted graph
        queue = deque([start])
        visited = {start}
        parent: Dict[int, int] = {}

        while queue:
            current = queue.popleft()
            for neighbor in self.adjacency.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    if neighbor == goal:
                        # reconstruct path
                        path = [goal]
                        while path[-1] != start:
                            path.append(parent[path[-1]])
                        path.reverse()
                        return path
                    queue.append(neighbor)
        return None


class SpiderManJourneySolver:
    MAX_JUMP_DISTANCE = 50.0

    def __init__(self):
        self.datasets: List[Tuple[List[Building], List[Tuple[int, int]]]] = []

    def parse_input(self, input_iter: Iterator[str]) -> None:
        while True:
            line = next(input_iter).strip()
            if line == '0':
                break
            n = int(line)
            buildings: List[Building] = []
            for _ in range(n):
                bi, xi, yi = map(int, next(input_iter).strip().split())
                buildings.append(Building(bi, Point2D(xi, yi)))
            m = int(next(input_iter).strip())
            moves: List[Tuple[int, int]] = []
            for _ in range(m):
                si, gi = map(int, next(input_iter).strip().split())
                moves.append((si, gi))
            self.datasets.append((buildings, moves))

    def solve_all(self) -> List[List[Optional[List[int]]]]:
        results: List[List[Optional[List[int]]]] = []
        for buildings, moves in self.datasets:
            graph = Graph(buildings, self.MAX_JUMP_DISTANCE)
            dataset_results = []
            for start, goal in moves:
                path = graph.shortest_path(start, goal)
                dataset_results.append(path)
            results.append(dataset_results)
        return results

    def format_output(self, results: List[List[Optional[List[int]]]]) -> str:
        output_lines: List[str] = []
        for dataset_result in results:
            for path in dataset_result:
                if path is None:
                    output_lines.append("NA")
                else:
                    output_lines.append(' '.join(map(str, path)))
        return '\n'.join(output_lines)


def main():
    import sys
    input_iter = iter(sys.stdin)
    solver = SpiderManJourneySolver()
    solver.parse_input(input_iter)
    results = solver.solve_all()
    print(solver.format_output(results))


if __name__ == '__main__':
    main()