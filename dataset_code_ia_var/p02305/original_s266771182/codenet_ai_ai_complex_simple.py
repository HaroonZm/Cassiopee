from enum import Enum
from math import hypot
from functools import reduce
from operator import sub, add, abs as op_abs

class Relation(Enum):
    INCLUDED = 0
    INSCRIBED = 1
    INTERSECT = 2
    CIRCUMSCRIBED = 3
    NO_CROSS = 4

def circle_intersection(c1, c2):
    d = norm(vector(*c1[:2], *c2[:2]))
    radii = tuple(sorted((c1[2], c2[2])))
    rs = tuple(map(float, radii))
    s = [add(rs[0], rs[1]), sub(rs[1], rs[0])]
    e = 1e-10
    predicates = [
        lambda: d - s[0] > e,
        lambda: abs(d - s[0]) < e,
        lambda: d - s[1] > e,
        lambda: abs(d - s[1]) < e,
    ]
    results = [Relation.NO_CROSS, Relation.CIRCUMSCRIBED, Relation.INTERSECT, Relation.INSCRIBED, Relation.INCLUDED]
    idx = next((i for i, pred in enumerate(predicates) if pred()), len(results)-1)
    return results[idx]

def norm(v):
    return hypot(v[2]-v[0], v[3]-v[1])

def vector(x1, y1, x2, y2):
    return (x1, y1, x2, y2)

def run():
    parse = lambda: list(map(int, input().split()))
    circles = list(map(parse, range(2)))
    circles.sort(key=lambda c: c[2])
    [print(circle_intersection(*circles).value)]

if __name__ == '__main__':
    run()