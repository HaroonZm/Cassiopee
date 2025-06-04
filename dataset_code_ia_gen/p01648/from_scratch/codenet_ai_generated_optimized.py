import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1]*n
        self.count = n
    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.p[b] = a
        self.sz[a] += self.sz[b]
        self.count -= 1
        return True

def can_build(edges, n, mid, median_index):
    dsu = DSU(n)
    # First, add edges with cost <= mid
    # To ensure median edge cost <= mid, we try to build spanning tree with enough edges <= mid
    count_small = 0
    # Sort edges by cost ascending
    # We'll try to pick edges cost <= mid first for MST
    chosen = []
    for c,s,t in edges:
        if c <= mid:
            if dsu.union(s, t):
                chosen.append(c)
                count_small += 1
    if dsu.count != 1:
        return False, []
    # chosen contains only edges <= mid; but the tree must have n-1 edges
    # If count_small < n-1, the MST includes edges > mid, so median may be higher than mid
    # Build full MST first here to test median
    return True, chosen

def solve():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        edges = []
        costs = set()
        for _ in range(m):
            s,t,c = map(int, input().split())
            s -= 1
            t -= 1
            edges.append((c,s,t))
            costs.add(c)
        edges.sort()
        costs = sorted(list(costs))
        median_index = (n-1)//2  # zero indexed median of edges in MST (n-1 edges)

        def can(med):
            dsu = DSU(n)
            count = 0
            # For median to be at most med, at least median_index + 1 edges must have cost <= med in spanning tree
            # Try to build MST adding edges with cost <= med first
            for c,s,t in edges:
                if c <= med:
                    if dsu.union(s,t):
                        count += 1
            if dsu.count != 1:
                # MST incomplete, try to add edges > med
                for c,s,t in edges:
                    if c > med:
                        if dsu.union(s,t):
                            count += 1
                    if dsu.count == 1:
                        break
            if dsu.count != 1:
                return False
            # Count edges with cost <= med in MST must be >= median_index + 1 
            # Because median of sorted edges of MST is the (median_index)-th edge (0-based)
            # If less edges <= med, median > med
            # However, above we didn't count how many edges of cost <= med are in final MST
            # So let's do MST construction to count that precisely.
            dsu = DSU(n)
            num_small = 0
            total = 0
            # MST with edges cost <= med first
            for c,s,t in edges:
                if c <= med:
                    if dsu.union(s,t):
                        num_small += 1
                        total += 1
            if dsu.count != 1:
                for c,s,t in edges:
                    if c > med:
                        if dsu.union(s,t):
                            total += 1
                        if dsu.count == 1:
                            break
            return num_small >= median_index+1

        left, right = 1, 1000
        while left < right:
            mid = (left+right)//2
            if can(mid):
                right = mid
            else:
                left = mid+1
        print(left)

if __name__ == "__main__":
    solve()