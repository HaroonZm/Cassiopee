import sys
from math import sqrt, hypot

def _hypot(p1, p2):
    return hypot(p2[0]-p1[0], p2[1]-p1[1])

def heron(p1, p2, p3):
    e1, e2, e3 = _hypot(p1, p2), _hypot(p2, p3), _hypot(p1, p3)
    z = (e1+e2+e3)/2
    return sqrt(z*(z-e1)*(z-e2)*(z-e3))

a = [tuple(map(float, l.split(","))) for l in sys.stdin]
result = 0
for p1, p2 in zip(a[1:], a[2:]):
    result += heron(a[0], p1, p2)
print(result)