import sys
sys.setrecursionlimit(10**7)

def main():
    V = int(sys.stdin.readline().strip())
    graph = [sys.stdin.readline().strip() for _ in range(V)]

    # Union-Find (Disjoint Set Union) implementation
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
            self.components = n  # Track number of connected components
        
        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]  # Path compression
                x = self.parent[x]
            return x
        
        def unite(self, x, y):
            x_root = self.find(x)
            y_root = self.find(y)
            if x_root == y_root:
                return False
            if self.size[x_root] < self.size[y_root]:
                x_root, y_root = y_root, x_root
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.components -= 1
            return True
        
        def same(self, x, y):
            return self.find(x) == self.find(y)

    uf = UnionFind(V)

    # Build connected components from input
    for i in range(V):
        for j in range(i+1, V):
            if graph[i][j] == 'Y':
                uf.unite(i, j)

    # Since the original graph is disconnected, uf.components >= 2

    # The game moves consist in adding edges between distinct components,
    # so each move reduces number of components by one.
    # Player who makes the graph connected (components = 1) loses.

    # Initial number of moves possible = uf.components - 1,
    # because to connect all components, at least that many edges are needed.

    # Players alternate moves:
    # If the number of moves (uf.components - 1) is odd, first player (Taro) wins, else second player (Hanako) wins.

    # Explanation:
    # This is because the player forced to do the last move (connecting the graph) loses.
    # So apply normal parity logic on the number of moves.

    if (uf.components - 1) % 2 == 1:
        print("Taro")
    else:
        print("Hanako")

if __name__ == '__main__':
    main()