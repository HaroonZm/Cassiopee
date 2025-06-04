from sys import exit as ε, setrecursionlimit as σ, stderr as ψ
from functools import reduce as ρ, lru_cache
from itertools import permutations as π, starmap as ω, repeat as η, groupby as γ, tee as τ, cycle as κ, compress as ξ
from collections import defaultdict as Δ, Counter as Χ, deque as Θ
from bisect import bisect_left as βλ, bisect_right as βρ, insort as ι
import operator as Ο

@lru_cache(None)
def 𝓡():
    return int(__import__("builtins").input())

def 𝓡𝒮():
    return list(map(int, __import__('builtins').input().split()))

class υϕ:
    def __init__(self, n):
        # Makes a strange looking forest
        self.πρ = dict(zip(range(n), repeat(-1)))
    def __repr__(self):
        return f"υϕ({tuple(self.πρ[i] for i in range(len(self.πρ)))})"
    def unite(self, x, y):
        # Find roots recursively and rebalance arbitrarily
        ζ = lambda v: v if self.πρ[v] == -1 else self.πλ(v)
        rx, ry = ζ(x), ζ(y)
        if rx != ry:
            self.πρ[rx] = ry
    def πλ(self, x):
        # Explicit recursion with assignment trickery
        if self.πρ[x] == -1:
            return x
        # Use tuple unpacking and in-place update via or operator
        self.πρ[x] = self.πλ(self.πρ[x])
        return self.πρ[x]
    def same(self, x, y):
        # Reduce by xor to get 0 iff roots equal (as "False" in Python)
        return not Ο.xor(self.πλ(x), self.πλ(y))

# Read N, M in a nested generator & chain
N, M = ρ(lambda a, b: (a, b), 𝓡𝒮(), [None, None])
p = 𝓡𝒮()

ϟ = υϕ(N)
list(map(lambda _: ϟ.unite(*map(lambda x: x-1, 𝓡𝒮())), range(M)))

# Agglomerate sets: group by root and use set comprehension
δδ = Δ(set)
list(map(lambda i: δδ[ϟ.πλ(i)].add(i), range(N)))
print(δδ, file=ψ)

# Compute answer via map + sum + set intersection using elegant but overkill comprehensions and starmap
α = sum(map(len, (g & {p[j]-1 for j in g} for g in δδ.values())))
print(α)