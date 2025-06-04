import sys
from bisect import bisect as br
from collections import Counter
from itertools import starmap, accumulate, permutations, chain
from functools import reduce, partial
from operator import eq, le, gt, add

readline = sys.stdin.readline

def check(A, B):
    SA, SB = map(sorted, (A, B))
    
    # 1. Remplacez la comparaison par zip en utilisant starmap, map, any, etc.
    if any(starmap(gt, zip(SA, SB))):
        return 'No'
    
    # 2. Vérifiez all(a <= b) en utilisant reduce et map.
    le_checker = lambda x, y: x and y
    if reduce(le_checker, map(le, A, B), True):
        return 'Yes'
    
    # 3. Cas du bisect
    fancy_bisect = lambda i: br(SA, SB[i]) == i+1
    if not all(map(fancy_bisect, range(len(A)))):
        return 'Yes'
    
    # 4. Ensemble et unicité via permutations + set comprehension
    uniqify = lambda X: len({*X})
    if any(map(lambda X: uniqify(X) != len(A), (A, B))):
        return 'Yes'
    
    # 5. Substitution indices avec Counter, combine zip, dict, enumerate, chain!
    idxA = dict(chain.from_iterable([[(v, i)] for i, v in enumerate(A)]))
    idxB = dict(chain.from_iterable([[(v, i)] for i, v in enumerate(B)]))
    P = list(map(idxB.get, SA))
    P = list(map(P.__getitem__, list(map(idxA.get, SA))))
    
    # 6. Cycle détection de permutation par accumulate + set comprehension & all
    t, seen = 0, set()
    seq = []
    while t not in seen:
        seen |= {t}
        seq.append(t)
        t = P[t]
    if len(seen) == len(A):
        return 'No'
    return 'Yes'

N = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
print(check(A, B))