class Edge:
    def __init__(self, to_vertex: int, cost: int):
        self.to_vertex = to_vertex
        self.cost = cost

class Vertex:
    def __init__(self, vertex_id: int):
        self.vertex_id = vertex_id
        self.children = []  # List[Edge]

    def add_child(self, child_vertex: int, cost: int):
        self.children.append(Edge(child_vertex, cost))

class Tree:
    def __init__(self, size: int):
        self.size = size
        self.vertices = [None] + [Vertex(i) for i in range(1, size + 1)]

    def add_edge(self, u: int, v: int, cost: int):
        self.vertices[u].add_child(v, cost)
        self.vertices[v].add_child(u, cost)

    def build_rooted_tree(self, root: int = 1):
        from collections import deque
        self.root = root
        self.parent = [0] * (self.size + 1)
        self.children = [[] for _ in range(self.size + 1)]
        self.edge_cost = [{} for _ in range(self.size + 1)]

        queue = deque([root])
        self.parent[root] = -1  # root has no parent
        visited = [False] * (self.size + 1)
        visited[root] = True

        while queue:
            u = queue.popleft()
            for edge in self.vertices[u].children:
                v = edge.to_vertex
                if not visited[v]:
                    visited[v] = True
                    self.parent[v] = u
                    self.children[u].append(v)
                    self.edge_cost[u][v] = edge.cost
                    queue.append(v)

class FractalTreeExpectationCalculator:
    def __init__(self, tree: Tree, p: float):
        self.tree = tree
        self.p = p
        # Memoization: expected cost starting DFS from node u's fractal tree
        self.memo = [-1.0] * (self.tree.size + 1)

    def expected_cost(self, u: int) -> float:
        # If already computed, return
        if self.memo[u] >= 0:
            return self.memo[u]

        # If leaf, no child => 0 cost
        if not self.tree.children[u]:
            self.memo[u] = 0.0
            return 0.0

        p = self.p
        expected = 0.0

        for c in self.tree.children[u]:
            cost_edge = self.tree.edge_cost[u][c]
            # Expected cost calculation from problem statement:
            # E(u) = sum over children c of p * (cost(u,c) + E(c) + E(u))
            # but because fractal tree T': each child's subtree repeats the same structure T.
            # So the recurrence is:
            # E(u) = sum_c p * (cost(u,c) + E(c) + E(u)) = sum_c p*(cost(u,c) + E(c)) + E(u)*sum_c p
            # Hence E(u)*(1 - sum_c p) = sum_c p *(cost(u,c) + E(c))
            # sum_c p = p * number_of_children
            # So:
            # E(u) = (sum_c p * (cost(u,c) + E(c))) / (1 - p * number_of_children)
            # Check denominator to avoid division by zero (if 1 - p*n == 0, unreachable in constraints)
            # We'll apply this after summing all children.

        n = len(self.tree.children[u])
        sum_p = self.p * n
        numerator = 0.0
        for c in self.tree.children[u]:
            cost_edge = self.tree.edge_cost[u][c]
            ec = self.expected_cost(c)
            numerator += self.p * (cost_edge + ec)

        if abs(1.0 - sum_p) < 1e-15:
            # edge case: denominator zero implies infinite expected value, 
            # but problem constraints ensure 0<=p<=1 and n<=N
            # To be safe, return large number
            self.memo[u] = float('inf')
            return float('inf')

        expected = numerator / (1.0 - sum_p)
        self.memo[u] = expected
        return expected

def main():
    import sys
    sys.setrecursionlimit(10**7)
    p = float(sys.stdin.readline())
    N = int(sys.stdin.readline())
    tree = Tree(N)
    for _ in range(N - 1):
        x, y, c = map(int, sys.stdin.readline().split())
        tree.add_edge(x, y, c)
    tree.build_rooted_tree(1)
    calculator = FractalTreeExpectationCalculator(tree, p)
    ans = calculator.expected_cost(1)
    print(ans)

if __name__ == "__main__":
    main()