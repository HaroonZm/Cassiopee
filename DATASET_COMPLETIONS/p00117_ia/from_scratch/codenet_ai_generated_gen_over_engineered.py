from typing import Dict, List, Tuple, Protocol, Optional
import heapq


class Town(Protocol):
    id: int


class Road:
    def __init__(self, from_town: int, to_town: int, cost_forward: int, cost_backward: int):
        self.from_town = from_town
        self.to_town = to_town
        self.cost_forward = cost_forward
        self.cost_backward = cost_backward

    def __repr__(self):
        return f"Road({self.from_town}->{self.to_town}, fwd={self.cost_forward}, bwd={self.cost_backward})"


class Graph:
    def __init__(self, n_towns: int):
        self.n = n_towns
        self.adj_forward: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(1, n_towns + 1)}
        self.adj_backward: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(1, n_towns + 1)}

    def add_road(self, road: Road):
        # Add forward edge
        self.adj_forward[road.from_town].append((road.to_town, road.cost_forward))
        # Add backward edge
        self.adj_backward[road.to_town].append((road.from_town, road.cost_backward))

    def shortest_path(self, start: int, direction: str = 'forward') -> Dict[int, int]:
        if direction == 'forward':
            adj = self.adj_forward
        elif direction == 'backward':
            adj = self.adj_backward
        else:
            raise ValueError(f"Unknown direction: {direction}")

        dist = {node: float('inf') for node in adj}
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            current_dist, u = heapq.heappop(heap)
            if dist[u] < current_dist:
                continue
            for v, cost in adj[u]:
                cost_through_u = current_dist + cost
                if cost_through_u < dist[v]:
                    dist[v] = cost_through_u
                    heapq.heappush(heap, (cost_through_u, v))
        return dist


class CarpenterRewardCalculator:
    def __init__(self, graph: Graph, s: int, g: int, V: int, P: int):
        self.graph = graph
        self.s = s  # Starting town
        self.g = g  # Mountain village town
        self.V = V  # Money received from lord
        self.P = P  # Cost of pillar

    def calculate_max_reward(self) -> int:
        # Calculate shortest path from s to g (going toward mountain village)
        dist_forward = self.graph.shortest_path(self.s, direction='forward')
        # Calculate shortest path from g back to s (return trip)
        dist_backward = self.graph.shortest_path(self.g, direction='backward')

        forward_cost = dist_forward.get(self.g, float('inf'))
        backward_cost = dist_backward.get(self.s, float('inf'))

        total_transport_cost = forward_cost + backward_cost

        if total_transport_cost == float('inf'):  # no route found
            return -self.P  # cannot even get pillar, lose pillar cost in reward calculation

        reward = self.V - self.P - total_transport_cost
        # Reward can be negative if costs exceed money received
        return reward


def parse_road(line: str) -> Road:
    # Input line: 'a,b,c,d'
    parts = line.strip().split(',')
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])
    d = int(parts[3])
    return Road(a, b, c, d)


class InputReader:
    def __init__(self):
        self.n: Optional[int] = None
        self.m: Optional[int] = None
        self.roads: List[Road] = []
        self.s: Optional[int] = None
        self.g: Optional[int] = None
        self.V: Optional[int] = None
        self.P: Optional[int] = None

    def read_input(self):
        self.n = int(input().strip())
        self.m = int(input().strip())
        for _ in range(self.m):
            line = input().strip()
            self.roads.append(parse_road(line))
        last_line = input().strip()
        s_str, g_str, V_str, P_str = last_line.split(',')
        self.s = int(s_str)
        self.g = int(g_str)
        self.V = int(V_str)
        self.P = int(P_str)


class Application:
    def __init__(self):
        self.input_reader = InputReader()

    def run(self):
        self.input_reader.read_input()
        graph = Graph(self.input_reader.n)
        for road in self.input_reader.roads:
            graph.add_road(road)
        calculator = CarpenterRewardCalculator(
            graph,
            self.input_reader.s,
            self.input_reader.g,
            self.input_reader.V,
            self.input_reader.P,
        )
        reward = calculator.calculate_max_reward()
        print(reward)


if __name__ == "__main__":
    Application().run()