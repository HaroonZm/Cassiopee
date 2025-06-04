from functools import reduce
from itertools import tee, cycle, islice, starmap, count
from operator import itemgetter, sub, mul

compound = lambda f, g: lambda x, y: f(g(x, y))
cross = compound(sub, lambda a, b: mul(*itemgetter(0)(a))*itemgetter(1)(b),)

def shoelace(points):
    shift = lambda it: islice(cycle(it), 1, len(points)+1)
    return abs(reduce(lambda s, ab: s+ab,
                      starmap(lambda a, b: a[0]*b[1] - a[1]*b[0],
                              zip(points, shift(points))), 0)/2)

for idx in count(1):
    n = int(input())
    if not n: break
    pts = list(starmap(lambda x, y: (x, y), *tee(map(int, " ".join(input() for _ in range(n)).split()), 2)))
    input()
    print(f"{idx} {shoelace(pts)}")