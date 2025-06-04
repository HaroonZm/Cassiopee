import sys
from functools import lru_cache
from itertools import takewhile

sys.setrecursionlimit(10**7)
INF = float('inf')
EPS = 1e-13
MOD = 10**9 + 7
DIR4 = [(-1,0),(0,1),(1,0),(0,-1)]
DIR8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def pf(s): print(s, flush=True)

def main():
    results = []

    def solve(n, m):
        a = [int(S(), 2) for _ in range(m)]
        if not a: return 0
        max_bits = max(a).bit_length()
        bit_masks = [1 << i for i in range(max_bits)]

        @lru_cache(maxsize=None)
        def recur(bitset):
            vals = [x for x in bitset if x is not None]
            if len(vals) < 2:
                return 0

            res = INF
            for mask in bit_masks:
                group1 = tuple(x for x in vals if x & mask)
                group2 = tuple(x for x in vals if not x & mask)
                if not group1 or not group2: continue
                d = max(recur(group1), recur(group2)) + 1
                if d < res:
                    res = d
            return res

        # Tuplify input for hashable cache key
        return recur(tuple(a))

    while True:
        n, m = LI()
        if n == 0:
            break
        results.append(solve(n, m))

    return '\n'.join(map(str, results))

print(main())