from typing import List, Tuple, Union
import heapq
import sys

class IslandNetwork:
    def __init__(self, n: int):
        self.n = n
        self.adj = [{} for _ in range(n + 1)]  # adjacency map: node -> {neighbor: cost}

    def update_route(self, c: int, d: int, e: int):
        # Add or update the cost for routes c->d and d->c with e if lower than existing
        # Because multiple ships can run the same route with different costs,
        # keep only the minimal cost for each direction.
        current_cd = self.adj[c].get(d, float('inf'))
        if e < current_cd:
            self.adj[c][d] = e
        current_dc = self.adj[d].get(c, float('inf'))
        if e < current_dc:
            self.adj[d][c] = e

    def shortest_path_cost(self, start: int, goal: int) -> int:
        # Dijkstra's algorithm to find minimal fare from start to goal
        dist = [float('inf')] * (self.n + 1)
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            current_cost, u = heapq.heappop(heap)
            if u == goal:
                return current_cost
            if current_cost > dist[u]:
                continue
            for v, cost in self.adj[u].items():
                new_cost = current_cost + cost
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, v))
        return -1

class InputParser:
    def __init__(self, input_stream):
        self.input_stream = input_stream

    def read_dataset(self) -> Union[Tuple[int, int, List[List[int]]], None]:
        header = ''
        while True:
            header = self.input_stream.readline()
            if header == '':
                return None
            header = header.strip()
            if header != '':
                break
        n, k = map(int, header.split())
        if n == 0 and k == 0:
            return None
        lines = []
        for _ in range(k):
            line = ''
            while True:
                line = self.input_stream.readline()
                if line == '':
                    break
                line = line.strip()
                if line != '':
                    break
            parts = list(map(int, line.split()))
            lines.append(parts)
        return (n, k, lines)

class TicketCenter:
    def __init__(self, n: int):
        self.network = IslandNetwork(n)
        self.queries: List[Tuple[int, int]] = []  # (a,b) orders in order
        self.responses: List[int] = []

    def process_command(self, command: List[int]):
        if command[0] == 1:
            _, c, d, e = command
            self.network.update_route(c, d, e)
        elif command[0] == 0:
            _, a, b = command
            cost = self.network.shortest_path_cost(a, b)
            self.responses.append(cost)

    def process_commands(self, commands: List[List[int]]):
        for cmd in commands:
            self.process_command(cmd)

    def get_responses(self) -> List[int]:
        return self.responses

class SophisticatedShipTravelSolution:
    """
    This class wraps the entire solution pipeline,
    anticipating future expansions like multi-modal transport, caching strategies etc.
    """

    def __init__(self, input_stream):
        self.parser = InputParser(input_stream)
        self.results_collector: List[List[int]] = []

    def solve_all_datasets(self):
        while True:
            dataset = self.parser.read_dataset()
            if dataset is None:
                break
            n, k, commands = dataset
            tc = TicketCenter(n)
            tc.process_commands(commands)
            self.results_collector.append(tc.get_responses())

    def output_results(self):
        # Output as specified without extra spaces or lines
        for responses in self.results_collector:
            for res in responses:
                print(res)

def main():
    solver = SophisticatedShipTravelSolution(sys.stdin)
    solver.solve_all_datasets()
    solver.output_results()

if __name__ == "__main__":
    main()