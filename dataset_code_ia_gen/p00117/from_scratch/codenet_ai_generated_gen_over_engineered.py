from typing import Dict, List, Tuple, Protocol, runtime_checkable, Optional
import heapq


@runtime_checkable
class GraphInterface(Protocol):
    def add_edge(self, from_node: int, to_node: int, cost: int) -> None:
        ...

    def shortest_path(self, start: int, goal: int) -> Optional[int]:
        ...


class DirectedGraph:
    def __init__(self, num_nodes: int) -> None:
        self.num_nodes = num_nodes
        self.adj_list: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(1, num_nodes + 1)}

    def add_edge(self, from_node: int, to_node: int, cost: int) -> None:
        self.adj_list[from_node].append((to_node, cost))

    def shortest_path(self, start: int, goal: int) -> Optional[int]:
        dist = {node: float("inf") for node in self.adj_list}
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            current_dist, u = heapq.heappop(heap)
            if current_dist > dist[u]:
                continue
            if u == goal:
                return current_dist
            for v, cost in self.adj_list[u]:
                new_cost = current_dist + cost
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, v))
        return None


class BidirectionalGraph(GraphInterface):
    def __init__(self, num_nodes: int) -> None:
        self.forward_graph = DirectedGraph(num_nodes)
        self.reverse_graph = DirectedGraph(num_nodes)

    def add_bidirectional_edge(self, node_a: int, node_b: int, cost_ab: int, cost_ba: int) -> None:
        self.forward_graph.add_edge(node_a, node_b, cost_ab)
        self.forward_graph.add_edge(node_b, node_a, cost_ba)
        self.reverse_graph.add_edge(node_b, node_a, cost_ba)
        self.reverse_graph.add_edge(node_a, node_b, cost_ab)

    def add_edge(self, from_node: int, to_node: int, cost: int) -> None:
        # Unused in this context for one-way edge, but needed to comply with interface
        self.forward_graph.add_edge(from_node, to_node, cost)

    def shortest_path_forward(self, start: int, goal: int) -> Optional[int]:
        return self.forward_graph.shortest_path(start, goal)

    def shortest_path_backward(self, start: int, goal: int) -> Optional[int]:
        return self.forward_graph.shortest_path(start, goal)

    def shortest_path(self, start: int, goal: int) -> Optional[int]:
        # Default shortest_path method finds from start to goal on forward graph
        return self.forward_graph.shortest_path(start, goal)


class CarpenterRewardCalculator:
    def __init__(self, n: int, m: int, edges: List[Tuple[int, int, int, int]],
                 s: int, g: int, V: int, P: int) -> None:
        self.n = n
        self.m = m
        self.s = s
        self.g = g
        self.V = V
        self.P = P
        self.graph = BidirectionalGraph(n)
        for a, b, c, d in edges:
            self.graph.add_bidirectional_edge(a, b, c, d)

    def calculate_max_reward(self) -> int:
        cost_to_g = self.graph.shortest_path_forward(self.s, self.g)
        cost_to_s = self.graph.shortest_path_forward(self.g, self.s)
        if cost_to_g is None or cost_to_s is None:
            # No valid round trip path
            return - (self.P)
        total_travel_cost = cost_to_g + cost_to_s
        reward = self.V - self.P - total_travel_cost
        return reward


class InputParser:
    @staticmethod
    def parse_input() -> CarpenterRewardCalculator:
        import sys
        input_lines = sys.stdin.read().strip().splitlines()
        n = int(input_lines[0].strip())
        m = int(input_lines[1].strip())
        edges = []
        for i in range(m):
            line = input_lines[2 + i]
            # split by comma and convert to integer
            parts = list(map(int, line.split(',')))
            edges.append((parts[0], parts[1], parts[2], parts[3]))
        last_line = input_lines[2 + m]
        s, g, V, P = map(int, last_line.split(','))
        return CarpenterRewardCalculator(n, m, edges, s, g, V, P)


def main() -> None:
    calculator = InputParser.parse_input()
    result = calculator.calculate_max_reward()
    print(result)


if __name__ == "__main__":
    main()