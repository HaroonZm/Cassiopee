from typing import List, Tuple, Dict, Optional
import sys
import heapq

class Edge:
    def __init__(self, from_node: int, to_node: int, cost: int):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

    def __repr__(self):
        return f"Edge({self.from_node} -> {self.to_node}, cost={self.cost})"


class Graph:
    def __init__(self, n_nodes: int):
        self.n_nodes = n_nodes
        self.adj_list: Dict[int, List[Edge]] = {i: [] for i in range(1, n_nodes + 1)}

    def add_edge(self, a: int, b: int, cost: int):
        edge = Edge(a, b, cost)
        self.adj_list[a].append(edge)
        # Since routes are bidirectional (problem implies connecting two points), 
        # add both directions
        self.adj_list[b].append(Edge(b, a, cost))

    def get_neighbors(self, node: int) -> List[Edge]:
        return self.adj_list[node]


class SpecialTicketOptimizer:
    """
    Optimizer to compute the minimal cost path from node 1 to node n
    with the option of using exactly once a ticket that allows 2 consecutive
    edges to be free.
    """

    def __init__(self, graph: Graph):
        self.graph = graph
        self.n = graph.n_nodes

    def compute_min_cost(self) -> int:
        # Distances:
        # dist[node][ticket_used_flag] stores minimal cost
        # ticket_used_flag: 0 - not used yet, 1 - used
        dist = [[float('inf')] * 2 for _ in range(self.n + 1)]
        dist[1][0] = 0

        # Min-heap priority queue: entries are (cost_so_far, node, ticket_used_flag)
        pq = [(0, 1, 0)]

        while pq:
            cost_so_far, node, used = heapq.heappop(pq)

            if dist[node][used] < cost_so_far:
                continue

            if node == self.n:
                # Reached destination
                return cost_so_far

            # Regular edges relaxation without using ticket
            for edge1 in self.graph.get_neighbors(node):
                next_node = edge1.to_node
                next_cost = cost_so_far + edge1.cost

                if dist[next_node][used] > next_cost:
                    dist[next_node][used] = next_cost
                    heapq.heappush(pq, (next_cost, next_node, used))

            # If ticket not used, try using it: skip cost for 2 consecutive edges
            if used == 0:
                # We try all pairs of consecutive edges from current node:
                for edge1 in self.graph.get_neighbors(node):
                    mid_node = edge1.to_node
                    for edge2 in self.graph.get_neighbors(mid_node):
                        end_node = edge2.to_node
                        # The ticket covers cost of edge1 and edge2 = 0 cost for these two edges
                        # Only if this path (2 edges) doesn't go through destination in the middle
                        # Problem states:途中で目的地を通過しても、目的地にたどり着いたことにはなりません。
                        # So, can't treat mid_node == destination as reaching the destination
                        if mid_node == self.n or end_node == self.n:
                            # If the consecutive edges end in destination, it's allowed
                            # but the "途中で" phrase means if mid_node == destination, we cannot consider the trip ended at mid_node
                            # But if mid_node == destination, we are not arrived because the trip continues.
                            # The problem states passing through destination is not arrival,
                            # so it is allowed to use the ticket over edges including the destination as mid_node or end_node,
                            # but we cannot stop there; we must continue until last node == destination.
                            # Here, actually passing through (mid_node) == destination is allowed, but arrival means node == n.
                            # So no restriction to use edges with mid_node == n or end_node == n.
                            # Ticket can be used normally; destination can appear as intermediate nodes.

                            # This means no special skip check needed here.
                            pass

                        # Relax the cost: cost of these two edges is 0 with ticket
                        if dist[end_node][1] > cost_so_far:
                            dist[end_node][1] = cost_so_far
                            heapq.heappush(pq, (cost_so_far, end_node, 1))

        # According to problem statement, path always exist, but in fallback:
        return min(dist[self.n][0], dist[self.n][1])


class DatasetParser:
    """
    Parses the input datasets and yields Graph objects
    """

    def __init__(self, input_lines: List[str]):
        self.lines = input_lines
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Optional[Tuple[int, Graph]]:
        while self.index < len(self.lines):
            line = self.lines[self.index].strip()
            self.index += 1
            if line == "0 0":
                raise StopIteration

            if not line:
                continue

            parts = line.split()
            if len(parts) != 2:
                continue

            n, m = map(int, parts)
            if n == 0 and m == 0:
                raise StopIteration

            graph = Graph(n)
            count_edges = 0
            while count_edges < m and self.index < len(self.lines):
                edge_line = self.lines[self.index].strip()
                self.index += 1
                if not edge_line:
                    continue
                a, b, c = map(int, edge_line.split())
                graph.add_edge(a, b, c)
                count_edges += 1

            return n, graph

        raise StopIteration


def main():
    input_lines = sys.stdin.read().strip().split('\n')
    parser = DatasetParser(input_lines)

    for n, graph in parser:
        optimizer = SpecialTicketOptimizer(graph)
        result = optimizer.compute_min_cost()
        print(result)


if __name__ == "__main__":
    main()