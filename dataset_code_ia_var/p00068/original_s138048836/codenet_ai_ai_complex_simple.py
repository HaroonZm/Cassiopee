from sys import stdin
from functools import reduce
from itertools import repeat, islice, chain, starmap, tee, permutations

def norm(v): 
    return sum(map(lambda x: x**2, v))**0.5

def unit(v): 
    n = norm(v)
    return list(map(lambda x: x/n, v)) if n else v

def cos_angle(u, v):
    return (sum(map(lambda x, y: x*y, u, v)) / (norm(u)*norm(v))) if norm(u)*norm(v) else 0

def next_point(points, p, direction, cmp_op):
    idx = [i for i in range(len(points)) if points[i][1] >= p[1] and points[i]!=p]
    if not idx: return None
    candidates = [points[i] for i in idx]
    v_base = [1, 0] if direction == "r" else [-1, 0]
    vlist = [[q[0]-p[0], q[1]-p[1]] for q in candidates]
    cosines = list(starmap(lambda v: v[0]/norm(v) if norm(v) else -2 if direction == "r" else 2, zip(vlist)))
    composite = list(zip(candidates, cosines))
    reducer = (lambda a,b: a if cmp_op(a[1], b[1]) else b)
    return reduce(reducer, composite)[0] if composite else None

def hull(points, direction):
    import operator as op
    cmp_op = op.ge if direction=="r" else op.le
    p = points[0]
    output = [p]
    lookup = set()
    while p!=points[-1]:
        q = next_point(points, p, direction, cmp_op)
        output.append(q)
        p = q
    return output

def chunk(n, iterable):
    it = iter(iterable)
    return list(islice(it, n))

while True:
    line = next(stdin).strip()
    if not line:
        continue
    n = int(line)
    if n==0:
        break
    d = list(starmap(lambda a,b: [float(a), float(b)], *tee((s for s in (l.strip().split(",") for l in islice(stdin, n))), 1)))
    d.sort(key=lambda x: x[1])
    h1 = hull(d, "r")
    h2 = hull(d, "l")
    print(len(d) - ( len(h1 + h2) - 2))