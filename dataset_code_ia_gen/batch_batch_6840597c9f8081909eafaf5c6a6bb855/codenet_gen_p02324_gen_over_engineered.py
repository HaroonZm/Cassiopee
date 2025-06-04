import sys
import heapq
from collections import defaultdict
from itertools import combinations

class Graph:
    def __init__(self, vertex_count):
        self.V = vertex_count
        self.adj = defaultdict(list)  # vertex -> list of (neighbor, weight)
        self.edges = []  # list of (u,v,w)
        self.degrees = [0]*self.V
    
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        self.edges.append((u, v, w))
        self.degrees[u] += 1
        self.degrees[v] += 1
    
    def total_edge_weight(self):
        return sum(w for _, _, w in self.edges)
    
    def odd_degree_vertices(self):
        return [v for v, d in enumerate(self.degrees) if d % 2 == 1]

class DijkstraSolver:
    def __init__(self, graph):
        self.graph = graph
        self.distances = {}

    def shortest_path(self, src):
        if src in self.distances:
            return self.distances[src]
        dist = [float('inf')] * self.graph.V
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            cd, u = heapq.heappop(heap)
            if cd > dist[u]:
                continue
            for v, w in self.graph.adj[u]:
                nd = cd + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        self.distances[src] = dist
        return dist

class PerfectMatchingSolver:
    def __init__(self, vertices, graph_distances):
        self.vertices = vertices
        self.n = len(vertices)
        self.distances = graph_distances
        self.memo = {}

    def min_weight_matching(self, used=0):
        if used == (1 << self.n) - 1:
            return 0
        if used in self.memo:
            return self.memo[used]
        # find first unmatched vertex
        first = 0
        while (used & (1 << first)) != 0:
            first += 1
        best = float('inf')
        for j in range(first + 1, self.n):
            if (used & (1 << j)) == 0:
                new_used = used | (1 << first) | (1 << j)
                cost = self.distances[self.vertices[first]][self.vertices[j]] + self.min_weight_matching(new_used)
                if cost < best:
                    best = cost
        self.memo[used] = best
        return best

class ChinesePostmanProblem:
    def __init__(self, vertex_count):
        self.graph = Graph(vertex_count)
        self.vertex_count = vertex_count
    
    def add_edge(self, u, v, w):
        self.graph.add_edge(u,v,w)
    
    def solve(self):
        total_weight = self.graph.total_edge_weight()
        odd_vertices = self.graph.odd_degree_vertices()
        if len(odd_vertices) == 0:
            # Eulerian circuit exists
            return total_weight
        
        # Compute all shortest paths between odd degree vertices
        dijkstra_solver = DijkstraSolver(self.graph)
        for v in odd_vertices:
            dijkstra_solver.shortest_path(v)
        # organize distances for perfect matching solver
        # distances[u][v] = shortest path dist between u,v
        distances = {}
        for u in odd_vertices:
            distances[u] = {}
            distu = dijkstra_solver.distances[u]
            for v in odd_vertices:
                distances[u][v] = distu[v]
        
        pm_solver = PerfectMatchingSolver(odd_vertices, distances)
        min_odd_pairing_cost = pm_solver.min_weight_matching()
        result = total_weight + min_odd_pairing_cost
        return result

def main():
    input = sys.stdin.read().strip().split()
    V, E = int(input[0]), int(input[1])
    cpp = ChinesePostmanProblem(V)
    idx = 2
    for _ in range(E):
        s, t, d = int(input[idx]), int(input[idx+1]), int(input[idx+2])
        idx += 3
        cpp.add_edge(s, t, d)
    answer = cpp.solve()
    print(answer)

if __name__ == "__main__":
    main()