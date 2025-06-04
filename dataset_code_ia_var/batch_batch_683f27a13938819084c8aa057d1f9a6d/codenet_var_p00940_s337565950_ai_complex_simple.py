import sys
from functools import reduce
from itertools import accumulate, chain, product
from operator import add, sub

read = sys.stdin.readline
writ = sys.stdout.write

def solve():
    P,R,T = map(int, read().split())
    Lx = tuple(map(int, read().split()))
    RxS = [tuple(map(int, read().split())) for _ in range(P)]
    LG = [tuple(map(int, input().split())) for _ in range(T)]

    prev = [-1]
    K = [[0]*R for _ in range(P)]

    def updateK(lim, sense=1):
        """ Apply updates on K and L according to LG and direction. """
        op_idx = slice(prev[0]+1, lim+1) if sense==1 else slice(lim+1, prev[0]+1)
        for p, r in map(LG.__getitem__, range(*op_idx.indices(T))):
            K[p-1][r-1] += (1 if sense==1 else -1)
            Ln[r-1] -= (1 if sense==1 else -1)
    
    def check(t):
        Ln[:] = origL[:]
        sense = 1 if prev[0] < t else -1
        updateK(t, sense)
        Us = set()
        rej = lambda i: any(RxS[i][j] - K[i][j] > max(Ln[j],0) for j in range(R))
        stream = lambda: filter(lambda i: i not in Us and not rej(i), range(P))
        while True:
            F = tuple(stream())
            if not F: break
            Us.update(F)
            for j in range(R):
                Ln[j] += sum(K[i][j] for i in F)
        prev[0] = t
        return len(Us) == P

    origL = list(Lx)
    Ln = [x for x in Lx]

    # Fancy binary search
    rng = lambda: (0, T)
    bounds = list(rng())
    while bounds[0]+1 < bounds[1]:
        mid = (sum(bounds)//2)
        if check(mid): bounds[0] = mid
        else: bounds[1] = mid
    writ("-1\n" if bounds[1]==T else f"{bounds[1]+1}\n")
solve()