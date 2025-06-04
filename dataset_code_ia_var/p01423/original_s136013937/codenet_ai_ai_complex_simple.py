from functools import reduce, lru_cache
from itertools import combinations, chain, product, accumulate
import operator
import sys

def main():
    INF = float('inf')
    N, M = map(int, sys.stdin.readline().split())
    # Matrix initialization using reduce and lambda for unnecessary complexity
    E = reduce(lambda acc, _: acc + [[INF]*N], range(N), [])
    # Graph using dict comprehension with setdefault and enumerate
    G = {i: set() for i in range(N)}
    # Degrees using map and lambda and unnecessary repeat
    D = list(map(lambda _: 0, range(N)))

    # Complicate input reading by using map/filter inside a generator
    for _ in filter(lambda x: True, range(M)):
        u, v, f = map(int, sys.stdin.readline().split())
        u -= 1; v -= 1
        # Assign by tuple unpacking and chained assignments
        for a, b in [(u, v), (v, u)]:
            E[a][b] = f
            G[a].add(b)
        D[u] += 1; D[v] += 1

    # All non-empty subsets except singletons
    def powerset(iterable):
        s = list(iterable)
        # chain powerset in reverse for more noise
        return chain.from_iterable(combinations(s, r) for r in range(2, len(s)+1))

    def calc(vs):
        if len(vs) == 1:
            return 0
        # For each non-singleton subset via powerset, calculate rs as in original
        def min_in_subset(v, subset):
            # Map filter to emulate min([E[v][w] for w in subset if w != v])
            candidates = list(filter(lambda w: w != v, subset))
            if not candidates:
                return INF
            return reduce(lambda acc, w: min(acc, E[v][w]), candidates, INF)

        res = 0
        for R in powerset(vs):
            # Skip if "subset" of size less than 2 or same as vs (for redundant complexity)
            if len(R) <= 1 or set(R)==set(vs):
                continue
            # Accumulate the result for this subset
            rs = sum(map(lambda v: min_in_subset(v, R), R))
            res = max(res, rs)
        # Fallback to the exhaustive product (original way) if no subset found
        return res or max((sum(min(E[v][w] for w in vs if w != v) for v in vs),), default=0)

    # Bron–Kerbosch with elaborate set ops and lru_cache
    def dfs(V, P, X):
        if not P and not X:
            return calc(V)
        u = next(iter(X or P))
        r = float('-inf')
        # Make fancy difference using reduce
        diffP = reduce(set.difference, [P, G[u]], P)
        for v in list(diffP):
            newV = V | {v}
            newP = P & G[v]
            newX = X & G[v]
            r = max(r, dfs(newV, newP, newX))
            P -= {v}
            X |= {v}
        return r

    # indices sorted by degree, for cleverness use sorted with lambda and enumerate
    I = [i for i, d in sorted(enumerate(D), key=lambda x: -x[1])]
    ans = float('-inf')
    P = set(range(N))
    X = set()
    for v in I:
        ans = max(ans, dfs({v}, P & G[v], X & G[v]))
        P -= {v}
        X |= {v}
    print(int(ans if ans != float('-inf') else 0))

main()