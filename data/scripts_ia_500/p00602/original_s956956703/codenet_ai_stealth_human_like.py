import sys
sys.setrecursionlimit(10**7)  # Just in case of deep recursion
MOD = 1001
INF = 10**15  # Not really used here, but kept just in case

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n  # negative means root and size
    
    def find(self, x):
        # Find root of x with path compression
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])  # compress path
        return self.parents[x]
    
    def unite(self, x, y):
        # Union by size
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.parents[x_root] > self.parents[y_root]:  # x_root smaller size?
            x_root, y_root = y_root, x_root
        self.parents[x_root] += self.parents[y_root]
        self.parents[y_root] = x_root
    
    def same(self, x, y):
        # Check if in same group
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return -self.parents[self.find(x)]
    
    def roots(self):
        # Return list of all roots
        return [i for i, p in enumerate(self.parents) if p < 0]
    
    def group_count(self):
        return len(self.roots())

def solve(V, d, fib):
    uf = UnionFind(V)
    for i in range(V):
        for j in range(i+1, V):
            # Slightly arbitrary grouping condition
            if abs(fib[i] - fib[j]) < d:
                uf.unite(i, j)
    print(uf.group_count())

def main():
    fib = [0]*1005
    fib[0], fib[1] = 2, 3
    for i in range(2, 1005):
        fib[i] = (fib[i-1] + fib[i-2]) % MOD
    
    while True:
        try:
            line = input()
            if not line.strip():
                continue
            V, d = map(int, line.split())
            solve(V, d, fib)
        except EOFError:
            break  # Clean exit on no more inputs
        except Exception as e:
            # Catch-all, in case input is bad - normally not great, but anyway
            break

if __name__ == "__main__":
    main()