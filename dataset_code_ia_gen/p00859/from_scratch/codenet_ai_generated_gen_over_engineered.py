class Vertex:
    def __init__(self, id_):
        self.id = id_

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        return True

class Graph:
    def __init__(self, n):
        self.n = n
        self.vertices = [Vertex(i) for i in range(n)]
        self.edges = []

    def add_edge(self, a, b, w):
        self.edges.append(Edge(a, b, w))

    def _can_form_spanning_tree_within_edges(self, edges_subset):
        dsu = DisjointSet(self.n)
        edges_used = 0
        for edge in edges_subset:
            if dsu.union(edge.u, edge.v):
                edges_used += 1
                if edges_used == self.n - 1:
                    return True
        return False

    def find_min_slimness(self):
        if self.n < 2:
            return -1  # no spanning tree possible
        self.edges.sort(key=lambda e: e.w)
        edge_count = len(self.edges)
        INF = 10**9
        min_slimness = INF
        # We try all windows [i,j] over sorted edges where j>=i, looking if edges[i..j] contain a spanning tree
        j = 0
        dsu = DisjointSet(self.n)
        for i in range(edge_count):
            dsu = DisjointSet(self.n)
            edges_used = 0
            for k in range(i, edge_count):
                e = self.edges[k]
                if dsu.union(e.u, e.v):
                    edges_used += 1
                if edges_used == self.n - 1:
                    current_slimness = self.edges[k].w - self.edges[i].w
                    if current_slimness < min_slimness:
                        min_slimness = current_slimness
                    break
        return min_slimness if min_slimness != INF else -1

class SlimSpanProcessor:
    def __init__(self):
        self.graphs = []

    def parse_input(self, input_lines):
        idx = 0
        while idx < len(input_lines):
            line = input_lines[idx].strip()
            idx += 1
            if line == "0 0":
                break
            n, m = map(int, line.split())
            graph = Graph(n)
            for _ in range(m):
                a, b, w = map(int, input_lines[idx].split())
                idx += 1
                graph.add_edge(a-1, b-1, w)
            self.graphs.append(graph)

    def process(self):
        results = []
        for graph in self.graphs:
            results.append(graph.find_min_slimness())
        return results

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    processor = SlimSpanProcessor()
    processor.parse_input(lines)
    results = processor.process()
    for r in results:
        print(r)

if __name__ == "__main__":
    main()