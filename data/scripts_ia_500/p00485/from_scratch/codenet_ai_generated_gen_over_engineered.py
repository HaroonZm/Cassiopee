class Graph:
    class Node:
        __slots__ = ['id', 'edges']
        def __init__(self, id):
            self.id = id
            self.edges = []

    class Edge:
        __slots__ = ['start', 'end', 'length']
        def __init__(self, start, end, length):
            self.start = start
            self.end = end
            self.length = length

    def __init__(self, n):
        self.nodes = [self.Node(i) for i in range(n)]
        self.edges = []

    def add_edge(self, a, b, l):
        edge = self.Edge(a, b, l)
        self.nodes[a].edges.append(edge)
        self.nodes[b].edges.append(edge)
        self.edges.append(edge)


import sys
import math
import heapq


class DistanceCalculator:
    def __init__(self, graph, malls):
        self.graph = graph
        self.malls = malls
        self.n = len(self.graph.nodes)
        self.distances = [math.inf] * self.n

    def multi_source_dijkstra(self):
        queue = []
        for m in self.malls:
            self.distances[m] = 0
            heapq.heappush(queue, (0, m))
        while queue:
            dist, node = heapq.heappop(queue)
            if self.distances[node] < dist:
                continue
            for edge in self.graph.nodes[node].edges:
                neighbor = edge.end if edge.start == node else edge.start
                nd = dist + edge.length
                if self.distances[neighbor] > nd:
                    self.distances[neighbor] = nd
                    heapq.heappush(queue, (nd, neighbor))

    def get_max_min_distance_on_road(self):
        max_dist = 0.0
        for edge in self.graph.edges:
            d_start = self.distances[edge.start]
            d_end = self.distances[edge.end]
            l = edge.length
            # The function f(x) = min(d_start + x, d_end + (l - x)) is "V"-shaped and minimal at some x.
            # Objective: maximize minimal distance from malls along edge.
            # The maximal minimal distance along edge is (d_start + d_end + l)/2
            edge_max = (d_start + d_end + l) / 2.0
            if edge_max > max_dist:
                max_dist = edge_max
        return max_dist


class JOIShoppingInKingdom:
    def __init__(self):
        self.graph = None
        self.malls = []

    def read_input(self):
        input = sys.stdin.readline
        N, M, K = map(int, input().split())
        self.graph = Graph(N)
        for _ in range(M):
            a, b, l = map(int, input().split())
            self.graph.add_edge(a - 1, b - 1, l)
        self.malls = [int(input()) - 1 for _ in range(K)]

    def solve(self):
        calculator = DistanceCalculator(self.graph, self.malls)
        calculator.multi_source_dijkstra()
        max_dist = calculator.get_max_min_distance_on_road()
        # round as requested
        print(round(max_dist))


def main():
    problem = JOIShoppingInKingdom()
    problem.read_input()
    problem.solve()


if __name__ == "__main__":
    main()