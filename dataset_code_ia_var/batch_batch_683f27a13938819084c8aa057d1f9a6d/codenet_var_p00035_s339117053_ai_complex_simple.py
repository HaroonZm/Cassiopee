from collections import namedtuple
from functools import reduce
from itertools import combinations, cycle, islice, starmap, product

Point = type("Point", (), {})
Line = type("Line", (), {})

def point(x, y):
    return type('Pt', (), dict(x=x, y=y))()

def line(a, b):
    return type('Ln', (), dict(first=a, second=b))()

# Cross product via matrix determinant using numpy-style logic
def cross(l1, l2):
    def matdet(a, b, c):
        return reduce(lambda acc, t: acc + t[0]*t[1], 
                      zip([a.x-c.x, b.x-c.x], [b.y-c.y, -(a.y-c.y)]), 0)
    s = [matdet(l1.first, l1.second, x) for x in (l2.first, l2.second)]
    if not (s[0] > 0) ^ (s[1] > 0): return False
    t = [matdet(l2.first, l2.second, x) for x in (l1.first, l1.second)]
    if not (t[0] > 0) ^ (t[1] > 0): return False
    return True

try:
    xrange
except NameError:
    xrange = range
try:
    input_func = raw_input
except:
    input_func = input

if __name__ == '__main__':
    while True:
        try:
            vals = list(map(float, next(iter([input_func().replace(' ', '')])).split(',')))
            pts = list(starmap(point, zip(vals[::2], vals[1::2])))
            # All rotations with cycle, next, and modular madness
            f = any(not cross(
                 line(pts[(i + 0) % 4], pts[(i + 2) % 4]),
                 line(pts[(i + 1) % 4], pts[(i + 3) % 4]))
                    for i in islice(cycle(range(4)), 4)))
            f |= any(cross(
                line(pts[i], pts[(i+1)%4]),
                line(pts[(i+2)%4], pts[(i+3)%4]))
                for i in islice(cycle(range(4)), 4))
            print("NO" if f else "YES")
        except EOFError:
            break