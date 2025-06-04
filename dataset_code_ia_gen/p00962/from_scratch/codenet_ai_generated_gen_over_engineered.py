import sys
import heapq

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_forward = [[] for _ in range(n + 1)]
        self.adj_reverse = [[] for _ in range(n + 1)]

    def add_edge(self, u, v, w, idx):
        # Store edges separately forward and backward
        self.adj_forward[u].append((v, w, idx))
        self.adj_reverse[v].append((u, w, idx))

class ShortestPathFinder:
    def __init__(self, graph):
        self.graph = graph
        self.n = graph.n
        self.dist_from_start = [float('inf')] * (self.n + 1)
        self.dist_to_end = [float('inf')] * (self.n + 1)

    def dijkstra(self, start, adj):
        dist = [float('inf')] * (self.n + 1)
        dist[start] = 0
        hq = [(0, start)]
        while hq:
            d, u = heapq.heappop(hq)
            if d > dist[u]:
                continue
            for v, w, _ in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(hq, (nd, v))
        return dist

    def compute(self):
        # Distances from start (1) using original edges
        self.dist_from_start = self.dijkstra(1, self.graph.adj_forward)
        # Distances to end (2) using reversed edges (for paths ending at 2)
        self.dist_to_end = self.dijkstra(2, self.graph.adj_reverse)

class ExperimentEvaluator:
    def __init__(self, graph, spfinder):
        self.graph = graph
        self.spfinder = spfinder
        self.n = graph.n
        self.m = 0
        # Will store edges as tuples (a,b,c)
        self.edges = []
        # Will store minimal shortest distance before experiment
        self.original_dist = self.spfinder.dist_from_start[2]

    def register_edges(self, edges):
        self.edges = edges
        self.m = len(edges)

    def evaluate_day(self, i):
        a, b, c = self.edges[i]
        d = self.original_dist

        dist_from_start = self.spfinder.dist_from_start
        dist_to_end = self.spfinder.dist_to_end

        # We consider the experiment reversing edge i: from (a->b) to (b->a)

        # 1) Check if shortest path unchanged:
        # shortest path is d originally, from 1 to 2

        # 2) Check if new shortest path can be shorter by using the reversed edge:
        # shortest path candidate with reversed edge:
        # dist_from_start[b] + c + dist_to_end[a]
        cand = dist_from_start[b] + c + dist_to_end[a]

        # 3) Check if new shortest path can be longer or no route if we exclude edge (a->b) original?
        # Since original shortest path uses some edges, if the reversed edge is on the shortest path,
        # its reversal may break it, possibly making path longer or none.

        # Instead of full recomputation, use:
        # If original shortest path > cand => HAPPY
        # if original shortest path == cand => SOSO
        # if cand > d or no path => SAD (including if cand infinite)
        # But also if reversing edge breaks original shortest path and no better alternative exists, SAD.

        if cand < d:
            return "HAPPY"
        elif cand == d:
            return "SOSO"
        else:
            # Possibly no improvement, check if original shortest path used this edge a->b
            # To detect usage of edge i on some shortest path, check:
            # Whether dist_from_start[a] + c + dist_to_end[b] == d

            # Because edge i is a->b with length c, if it lies on the shortest path,
            # the path passing through edge i will have distance:
            # dist_from_start[a] + c + dist_to_end[b]

            use = (dist_from_start[a] + c + dist_to_end[b]) == d

            if use:
                # Since reversal removes edge i in original direction, and alternative route was longer or none,
                # it's SAD
                return "SAD"
            else:
                # edge i not on shortest path, reversing doesn't increase length
                # means shortest path doesn't change
                return "SOSO"

class PizzaDeliveryExperiment:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.graph = None
        self.edges = []

    def parse_input(self):
        input = sys.stdin.readline
        self.n, self.m = map(int, input().split())
        self.edges = []
        self.graph = Graph(self.n)
        for i in range(self.m):
            a, b, c = map(int, input().split())
            self.edges.append((a, b, c))
            self.graph.add_edge(a, b, c, i+1)

    def run(self):
        # 1) compute shortest paths for original graph
        spfinder = ShortestPathFinder(self.graph)
        spfinder.compute()

        evaluator = ExperimentEvaluator(self.graph, spfinder)
        evaluator.register_edges(self.edges)

        # Evaluate each day
        out = []
        for i in range(self.m):
            res = evaluator.evaluate_day(i)
            out.append(res)
        print("\n".join(out))


def main():
    experiment = PizzaDeliveryExperiment()
    experiment.parse_input()
    experiment.run()

if __name__ == "__main__":
    main()