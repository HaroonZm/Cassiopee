class PropositionGraph:
    def __init__(self, n: int):
        self.n = n
        self._implications = [[False] * n for _ in range(n)]
        for i in range(n):
            self._implications[i][i] = True  # Each proposition implies itself
    
    def add_implication(self, a: int, b: int):
        self._implications[a - 1][b - 1] = True

    def compute_transitive_closure(self):
        # Warshall's algorithm for transitive closure
        for k in range(self.n):
            for i in range(self.n):
                if self._implications[i][k]:
                    for j in range(self.n):
                        if self._implications[k][j]:
                            self._implications[i][j] = True

    def are_equivalent(self, x: int, y: int) -> bool:
        # x implies y and y implies x
        return self._implications[x - 1][y - 1] and self._implications[y - 1][x - 1]

class EquivalenceClassCollector:
    def __init__(self, graph: PropositionGraph):
        self.graph = graph
        self.n = graph.n
        self._equivalence_classes = None
        self._representatives = None

    def _find_equivalence_classes(self):
        # Using a union-find inspired grouping via equivalences
        parent = list(range(self.n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x,y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.graph.are_equivalent(i+1, j+1):
                    union(i,j)

        clusters = {}
        for i in range(self.n):
            p = find(i)
            clusters.setdefault(p, []).append(i+1)
        
        self._equivalence_classes = clusters
        self._representatives = [0] * self.n
        for rep, members in clusters.items():
            for m in members:
                self._representatives[m-1] = rep
        return clusters
    
    def get_equivalence_class(self, proposition: int):
        if self._equivalence_classes is None:
            self._find_equivalence_classes()
        rep = self._representatives[proposition - 1]
        return self._equivalence_classes[rep]

class InputParser:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.implications = []

    def parse(self):
        first_line = input().strip()
        self.n, self.m = map(int, first_line.split())
        for _ in range(self.m):
            a, b = map(int, input().strip().split())
            self.implications.append((a,b))

class OutputFormatter:
    def __init__(self):
        pass
    
    def format_and_print(self, equiv_collector: EquivalenceClassCollector):
        for i in range(1, equiv_collector.n + 1):
            eq_class = equiv_collector.get_equivalence_class(i)
            print(" ".join(map(str, sorted(eq_class))))

class PropositionEquivalenceSolver:
    def __init__(self):
        self.input_parser = InputParser()
        self.graph = None
        self.equiv_collector = None
        self.output_formatter = OutputFormatter()

    def solve(self):
        self.input_parser.parse()
        self.graph = PropositionGraph(self.input_parser.n)
        for a,b in self.input_parser.implications:
            self.graph.add_implication(a,b)
        self.graph.compute_transitive_closure()
        self.equiv_collector = EquivalenceClassCollector(self.graph)
        self.output_formatter.format_and_print(self.equiv_collector)

if __name__ == "__main__":
    solver = PropositionEquivalenceSolver()
    solver.solve()