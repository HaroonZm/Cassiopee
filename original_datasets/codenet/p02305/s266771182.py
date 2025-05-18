#!/usr/bin/env python3
# CGL_7_A: Circles - Intersection

from enum import Enum
from math import sqrt

class Relation(Enum):
    INCLUDED = 0
    INSCRIBED = 1
    INTERSECT = 2
    CIRCUMSCRIBED = 3
    NO_CROSS = 4

def circle_intersection(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    d = distance((x1, y1), (x2, y2))

    if d - (r1 + r2) > 1e-10:
        return Relation.NO_CROSS
    elif abs(d - (r1 + r2)) < 1e-10:
        return Relation.CIRCUMSCRIBED
    elif d - (r2 - r1) > 1e-10:
        return Relation.INTERSECT
    elif abs(d - (r2 - r1)) < 1e-10:
        return Relation.INSCRIBED
    else:
        return Relation.INCLUDED

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def run():
    c1 = [int(i) for i in input().split()]
    c2 = [int(i) for i in input().split()]

    if c1[2] > c2[2]:
        c1, c2 = c2, c1

    print(circle_intersection(c1, c2).value)

if __name__ == '__main__':
    run()