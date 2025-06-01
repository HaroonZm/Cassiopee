import sys
sys.setrecursionlimit(10**7)

def sieve_spf(max_n):
    spf = [0] * (max_n + 1)
    spf[1] = 1
    for i in range(2, max_n + 1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i * i, max_n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1

def factorize(num, spf):
    factors = set()
    while num > 1:
        factors.add(spf[num])
        num //= spf[num]
    return factors

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)

    max_a = max(A)
    spf = sieve_spf(max_a)

    # Map from prime factor to index of first occurrence in A with this factor
    prime_to_index = {}

    uf = UnionFind(N)

    for i, val in enumerate(A):
        primes = factorize(val, spf)
        for p in primes:
            if p in prime_to_index:
                uf.union(i, prime_to_index[p])
            else:
                prime_to_index[p] = i

    # Group elements by their root parent
    groups = {}
    for i in range(N):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    # For each group, check if sorted elements match in terms of values in sorted list B
    for group in groups.values():
        original_vals = [A[i] for i in group]
        sorted_vals = [B[i] for i in group]
        if sorted(original_vals) != sorted_vals:
            print(0)
            return
    print(1)

if __name__ == "__main__":
    main()