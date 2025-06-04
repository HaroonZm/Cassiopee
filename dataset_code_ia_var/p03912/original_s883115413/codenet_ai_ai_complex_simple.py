from functools import reduce
from itertools import combinations_with_replacement, starmap, groupby
from operator import itemgetter, add

def inpl(): 
    return list(map(int, input().split()))

N, M = inpl()
X = sorted(inpl())

def deep_count(collection):
    return dict((k, len(list(g))) for k, g in groupby(sorted(collection)))

C = deep_count(X)

mod_group = lambda m: dict((i, sum(C.get(x,0) for x in C if x % M == i)) for i in range(M))
D = mod_group(M)
half_pairs = lambda c: dict((i, sum((C.get(x,0)//2) for x in C if x % M == i)) for i in range(M))
E = half_pairs(C)

def pairings(D, E):
    z = []
    paired = set()
    for i in range(1, (M+1)//2):
        j = M - i
        if i < j:
            x = min(D.get(i,0), D.get(j,0))
            y = sum(map(lambda a, b, c: min((a-b)//2, c), [D.get(i,0), x, E.get(i,0)])) + \
                sum(map(lambda a, b, c: min((a-b)//2, c), [D.get(j,0), x, E.get(j,0)]))
            z.append(x + y)
        elif i == j:
            z.append(D.get(i,0)//2)
    return sum(z)

def central(ans, D):
    return (ans + D.get(0,0)//2) if 0 in D else ans

final = reduce(lambda a,b: a+b, [pairings(D, E)], central(0,D))
print(final)