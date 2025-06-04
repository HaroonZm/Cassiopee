import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 10**9 + 7

def mod_pow(base, exp, mod):
    result = 1
    cur = base % mod
    while exp > 0:
        if exp & 1:
            result = result * cur % mod
        cur = cur * cur % mod
        exp >>= 1
    return result

class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            self.par[a] = b
        else:
            self.par[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1
        return True

while True:
    N,M = map(int,input().split())
    if N == 0 and M == 0:
        break
    dsu = DSU(N)
    for _ in range(M):
        a,b = map(int,input().split())
        dsu.union(a-1,b-1)
    # Count number of connected components
    comp_set = set()
    for i in range(N):
        comp_set.add(dsu.find(i))
    c = len(comp_set)

    # Answer is 2^(N-c) * (c+1) mod
    # Explanation:
    # Each connected component can have all attributes light or darkness except one attribute per component that must be
    # partitioned specially for transitions
    # The formula derived from the problem combinatorics is pow(2, N - c) * (c+1)
    ans = mod_pow(2, N - c, MOD) * (c+1) % MOD
    print(ans)