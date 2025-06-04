class GraphDiameterOptimizer:
    class DiameterConstraint:
        def __init__(self, n: int, d: int):
            self.n = n
            self.d = d
            self.validate()

        def validate(self):
            if not (2 <= self.n <= 10**9):
                raise ValueError("n must be between 2 and 10^9")
            if not (1 <= self.d <= self.n - 1):
                raise ValueError("d must be between 1 and n-1")

    class GraphProperties:
        def __init__(self, n: int):
            self.n = n

        def max_edges_complete_graph(self) -> int:
            # Maximum edges in a simple undirected graph with n vertices: C(n, 2) = n*(n-1)//2
            return self.n * (self.n - 1) // 2

        def max_edges_for_diameter_one(self) -> int:
            # Diameter 1 means complete graph
            return self.max_edges_complete_graph()

    class DiameterOneGraphBuilder:
        def __init__(self, n):
            self.n = n

        def max_edges(self):
            # Complete graph
            return self.n * (self.n - 1) // 2

    class DiameterGreaterThanOneGraphBuilder:
        def __init__(self, n, d):
            self.n = n
            self.d = d

        def build_max_edges(self) -> int:
            # We create a path of length d (with d+1 vertices)
            # The remaining vertices are connected to one of the endpoints to maintain diameter d
            # The maximum edges = 
            # edges in path (d)
            # + edges between the remaining vertices (remaining_vertices choose 2)
            # + edges connecting remaining vertices to endpoint (remaining_vertices)
            remaining = self.n - (self.d + 1)

            edges_path = self.d
            edges_remaining_complete = remaining * (remaining - 1) // 2 if remaining > 1 else 0
            edges_connecting = remaining

            total_edges = edges_path + edges_remaining_complete + edges_connecting
            return total_edges

    def __init__(self, n: int, d: int):
        self.constraint = self.DiameterConstraint(n, d)
        self.n = n
        self.d = d
        self.graph_properties = self.GraphProperties(n)

    def compute(self) -> int:
        if self.d == 1:
            builder = self.DiameterOneGraphBuilder(self.n)
            return builder.max_edges()
        else:
            builder = self.DiameterGreaterThanOneGraphBuilder(self.n, self.d)
            return builder.build_max_edges()

def main():
    import sys
    input_line = sys.stdin.readline().strip()
    if not input_line:
        return
    n_str, d_str = input_line.split()
    n, d = int(n_str), int(d_str)
    optimizer = GraphDiameterOptimizer(n, d)
    ans = optimizer.compute()
    print(ans)

if __name__ == "__main__":
    main()