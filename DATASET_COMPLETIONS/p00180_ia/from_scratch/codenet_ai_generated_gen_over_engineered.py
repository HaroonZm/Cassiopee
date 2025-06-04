class Bridge:
    def __init__(self, city1: int, city2: int, cost: int):
        self.city1 = city1
        self.city2 = city2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, a: int, b: int) -> bool:
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return False

        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            if self.rank[rootA] == self.rank[rootB]:
                self.rank[rootA] += 1
        return True

class Graph:
    def __init__(self, num_cities: int):
        self.num_cities = num_cities
        self.bridges = []

    def add_bridge(self, city1: int, city2: int, cost: int):
        self.bridges.append(Bridge(city1, city2, cost))

    def find_minimum_maintenance_cost(self) -> int:
        uf = UnionFind(self.num_cities)
        # Sort bridges based on cost for Kruskal's MST
        sorted_bridges = sorted(self.bridges)
        total_cost = 0
        edges_used = 0
        for bridge in sorted_bridges:
            if uf.union(bridge.city1, bridge.city2):
                total_cost += bridge.cost
                edges_used += 1
                if edges_used == self.num_cities - 1:
                    break
        return total_cost

class WaterDebunSolver:
    def __init__(self):
        self.graphs = []

    def parse_and_store_dataset(self, n: int, m: int, bridge_data: list):
        graph = Graph(n)
        for a, b, cost in bridge_data:
            graph.add_bridge(a, b, cost)
        self.graphs.append(graph)

    def solve_all(self):
        results = []
        for graph in self.graphs:
            results.append(graph.find_minimum_maintenance_cost())
        return results

def main():
    import sys

    solver = WaterDebunSolver()
    lines = iter(sys.stdin.read().strip().splitlines())

    while True:
        try:
            n, m = map(int, next(lines).split())
            if n == 0 and m == 0:
                break
            bridge_data = []
            for _ in range(m):
                a, b, cost = map(int, next(lines).split())
                bridge_data.append((a, b, cost))
            solver.parse_and_store_dataset(n, m, bridge_data)
        except StopIteration:
            break

    results = solver.solve_all()
    for res in results:
        print(res)

if __name__ == "__main__":
    main()