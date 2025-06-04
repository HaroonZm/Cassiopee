class MagicCircleRealizabilityChecker:
    class Edge:
        def __init__(self, u: int, v: int):
            self.u = u
            self.v = v

    class Graph:
        def __init__(self, n: int):
            self.vertex_count = n
            self.adj = [[] for _ in range(n + 1)]

        def add_edge(self, u: int, v: int):
            self.adj[u].append(v)
            self.adj[v].append(u)

    class BipartiteChecker:
        def __init__(self, graph):
            self.graph = graph
            self.colors = [None] * (graph.vertex_count + 1)
            self.is_bipartite = True

        def check(self):
            for v in range(1, self.graph.vertex_count + 1):
                if self.colors[v] is None:
                    self._dfs(v, 0)
                    if not self.is_bipartite:
                        return False
            return True

        def _dfs(self, v, c):
            self.colors[v] = c
            for nv in self.graph.adj[v]:
                if self.colors[nv] is None:
                    self._dfs(nv, 1 - c)
                    if not self.is_bipartite:
                        return
                elif self.colors[nv] == c:
                    self.is_bipartite = False
                    return

    class CompleteSubgraphDetector:
        def __init__(self, graph):
            self.graph = graph
            self.visited = [False] * (graph.vertex_count + 1)

        def has_k5(self):
            # Checking for K5 is complex in huge graphs, but we rely on:
            # K5 is not planar => the problem asks about 1D line embeddability
            # We'll use a heuristic: if there's a complete subgraph with 5 vertices (K5),
            # it must be detected.
            # Detecting K5 naively is expensive: O(n^5) impossible on input sizes.
            # Instead, for sophistication and future extension,
            # we prepare a high-level function, but here do a special check:
            # We'll implement an abstraction; actual detection skipped (not feasible).
            return False  # Placeholder in this implementation

        def _find_complete_subgraph(self, k):
            # Placeholder for future extension:
            # sophisticated algorithm to find Kk subgraph if needed
            pass

    class CompleteBipartiteSubgraphDetector:
        def __init__(self, graph):
            self.graph = graph

        def has_k33(self):
            # Same complexity issue: detecting K3,3 explicitly is complicated
            # We'll rely on a future-extension placeholder.
            return False  # Placeholder in this implementation

    @staticmethod
    def can_be_drawn_on_line(n: int, edges: list) -> bool:
        # Step 1: Build graph abstraction
        graph = MagicCircleRealizabilityChecker.Graph(n)
        for u, v in edges:
            graph.add_edge(u, v)

        # Step 2: Check if graph is linear (path graphs or unions of paths)
        # In 1D line embeddability, the graph must be a linear forest:
        # each connected component is a path (no node degree > 2 and no cycles)

        # We'll decompose to connected components and check conditions
        used = [False] * (n + 1)

        def dfs_check_path(v, parent):
            used[v] = True
            deg = len(graph.adj[v])
            if deg > 2:
                # vertex with degree more than 2 => can't embed on a line
                return False
            for nx in graph.adj[v]:
                if not used[nx]:
                    if not dfs_check_path(nx, v):
                        return False
                elif nx != parent:
                    # cycle detected
                    return False
            return True

        for vertex in range(1, n + 1):
            if not used[vertex]:
                if not dfs_check_path(vertex, -1):
                    return False

        # Step 3: Actually the above suffices for line embeddability: disjoint paths or isolated points

        return True

    def process_dataset(self, n: int, m: int, edges: list) -> str:
        if self.can_be_drawn_on_line(n, edges):
            return "yes"
        else:
            return "no"

def main():
    import sys
    checker = MagicCircleRealizabilityChecker()
    lines = (line.rstrip('\n') for line in sys.stdin)
    while True:
        try:
            line = next(lines)
        except StopIteration:
            break
        if line.strip() == "":
            continue
        if line == "0 0":
            break
        n, m = map(int, line.split())
        edges = []
        for _ in range(m):
            u, v = map(int, next(lines).split())
            edges.append((u, v))
        print(checker.process_dataset(n, m, edges))

if __name__ == "__main__":
    main()