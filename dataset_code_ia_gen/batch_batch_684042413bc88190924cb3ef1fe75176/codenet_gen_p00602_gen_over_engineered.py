class FibonacciModN:
    def __init__(self, n: int):
        self.n = n
        self.memo = { -1: 1, 0: 1 }
    
    def compute(self, i: int) -> int:
        if i in self.memo:
            return self.memo[i]
        self.memo[i] = (self.compute(i - 1) + self.compute(i - 2)) % self.n
        return self.memo[i]

class Node:
    def __init__(self, index: int, label: int):
        self.index = index
        self.label = label
    def __repr__(self):
        return f"Node(idx={self.index}, label={self.label})"

class DisjointSetUnion:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.count = size
    
    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x: int, y: int) -> None:
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
            elif self.rank[ry] < self.rank[rx]:
                self.parent[ry] = rx
            else:
                self.parent[ry] = rx
                self.rank[rx] += 1
            self.count -= 1

class FibonacciSetsSolver:
    N = 1001
    
    def __init__(self, V: int, d: int):
        self.V = V
        self.d = d
        self.fibo_mod = FibonacciModN(self.N)
        self.nodes = [Node(i, self.fibo_mod.compute(i)) for i in range(1, V+1)]
        self.dsu = DisjointSetUnion(V)
    
    def solve(self) -> int:
        # Sort nodes by label to optimize connectivity check
        self.nodes.sort(key=lambda node: node.label)
        
        # Since labels mod N are in range [0,N), and difference must be < d,
        # we only need to check neighborhood in sorted nodes by labels.
        
        for i in range(self.V):
            j = i + 1
            while j < self.V and self.nodes[j].label - self.nodes[i].label < self.d:
                self.dsu.union(self.nodes[i].index - 1, self.nodes[j].index - 1)
                j += 1
        
        return self.dsu.count

def main():
    import sys
    inputs = sys.stdin.read().strip().split('\n')
    for line in inputs:
        if not line.strip():
            continue
        V, d = map(int, line.split())
        solver = FibonacciSetsSolver(V, d)
        print(solver.solve())

if __name__ == "__main__":
    main()