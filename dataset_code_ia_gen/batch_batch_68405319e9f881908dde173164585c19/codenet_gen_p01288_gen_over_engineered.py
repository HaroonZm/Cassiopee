class Node:
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.children = []

class Tree:
    def __init__(self, n):
        self.nodes = [None] + [Node(i) for i in range(1, n + 1)]
        self.n = n
        self.marked = [False] * (n + 1)
        self.uf_parent = list(range(n + 1))  # Union-Find parent array for marked ancestors

    def add_edge(self, child_index, parent_index):
        self.nodes[child_index].parent = self.nodes[parent_index]
        self.nodes[parent_index].children.append(self.nodes[child_index])

    def find(self, x):
        # Find with path compression in Union-Find to get nearest marked ancestor
        if self.uf_parent[x] != x:
            self.uf_parent[x] = self.find(self.uf_parent[x])
        return self.uf_parent[x]

    def mark(self, v):
        # Mark node v and union with parent marked ancestor if exists
        self.marked[v] = True
        if v == 1:
            # root, self parent in union-find stays itself
            self.uf_parent[v] = v
        else:
            p = self.nodes[v].parent.index
            if self.marked[p]:
                self.uf_parent[v] = v
            else:
                # Link v to parent's nearest marked ancestor
                self.uf_parent[v] = self.find(p)

    def query(self, v):
        # returns index of nearest marked ancestor
        return self.find(v)

class InputProcessor:
    def __init__(self):
        pass

    def read_dataset(self):
        import sys
        for line in sys.stdin:
            if not line.strip():
                continue
            n, q = map(int, line.split())
            if n == 0 and q == 0:
                break
            yield n, q

    def read_tree_parents(self, n, input_lines):
        parents = []
        for _ in range(n - 1):
            pi = int(next(input_lines))
            parents.append(pi)
        return parents

    def read_operations(self, q, input_lines):
        ops = []
        for _ in range(q):
            parts = next(input_lines).split()
            ops.append((parts[0], int(parts[1])))
        return ops

class MarkedAncestorSolver:
    def __init__(self, n, parents, operations):
        self.tree = Tree(n)
        for i, p in enumerate(parents, start=2):
            self.tree.add_edge(i, p)
        self.operations = operations
        self.output_sum = 0

    def initialize(self):
        # Initially only root node(1) marked
        self.tree.marked[1] = True
        self.tree.uf_parent[1] = 1

    def solve(self):
        self.initialize()
        for op, v in self.operations:
            if op == 'M':
                self.tree.mark(v)
            else:  # op == 'Q'
                res = self.tree.query(v)
                self.output_sum += res
        return self.output_sum

def main():
    import sys
    input_lines = iter(sys.stdin.read().splitlines())
    ip = InputProcessor()
    while True:
        try:
            line = next(input_lines)
        except StopIteration:
            break
        if not line.strip():
            continue
        n, q = map(int, line.split())
        if n == 0 and q == 0:
            break
        parents = [int(next(input_lines)) for _ in range(n - 1)]
        operations = [next(input_lines).split() for _ in range(q)]
        operations = [(op, int(v)) for op, v in operations]
        solver = MarkedAncestorSolver(n, parents, operations)
        print(solver.solve())

if __name__ == '__main__':
    main()