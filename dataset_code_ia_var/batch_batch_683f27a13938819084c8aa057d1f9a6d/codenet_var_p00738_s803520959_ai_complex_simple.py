from functools import reduce, partial
from itertools import permutations, product, chain

def cross(c1, c2):
    return reduce(lambda acc, val: acc + val[0]*val[1], zip([c1.real, -c1.imag], [c2.imag, c2.real]), 0)

def dot(c1, c2):
    return sum(map(lambda x: x[0]*x[1], zip([c1.real, c1.imag], [c2.real, c2.imag])))

def ccw(p0, p1, p2):
    a, b = p1 - p0, p2 - p0
    x = cross(a, b)
    if x > 0:
        return 1
    if x < 0:
        return -1
    d = dot(a, b)
    if d < 0:
        return 1
    if abs(a) < abs(b):
        return -1
    return 0

def intersect(p1, p2, p3, p4):
    f = lambda a,b,c: ccw(a,b,c)
    verdict = all([
        reduce(lambda x, y: x*y <= 0, [f(p1,p2,p3), f(p1,p2,p4)]),
        reduce(lambda x, y: x*y <= 0, [f(p3,p4,p1), f(p3,p4,p2)])
    ])
    return verdict

def get_distance_sp(sp1, sp2, p):
    a, b = sp2 - sp1, p - sp1
    c, d = sp1 - sp2, p - sp2
    ops = [
        (lambda: abs(b), lambda: dot(a, b) < 0),
        (lambda: abs(d), lambda: dot(c, d) < 0),
        (lambda: abs(cross(a, b) / a), lambda: True)
    ]
    return next(op() for op, cond in ops if cond())

def solve():
    import sys
    from operator import itemgetter
    lines = sys.stdin.readlines()
    idx = 0
    while True:
        N = int(lines[idx])
        if not N: break
        sx, sy, ex, ey = map(int, lines[idx+1].split())
        sp, ep = complex(sx, sy), complex(ex, ey)
        subR = []
        for l in lines[idx+2:idx+2+N]:
            x1, y1, x2, y2, h = map(int, l.split())
            box = [
                complex(x1, y1), complex(x2, y1),
                complex(x2, y2), complex(x1, y2)
            ]
            edges = [ (box[i], box[(i+1)%4]) for i in range(4) ]
            intersections = any(intersect(sp, ep, a, b) for a, b in edges)
            ins_p1 = x1 <= sx <= x2 and y1 <= sy <= y2
            ins_p2 = x1 <= ex <= x2 and y1 <= ey <= y2
            if intersections or ins_p1 or ins_p2:
                print(0)
                break
            dists = list(chain(
                map(partial(get_distance_sp, sp, ep), box),
                (get_distance_sp(a, b, p)
                    for (a, b), p in product(edges, (sp, ep)))
            ))
            d = min(dists)
            subR.append( (d**2 + h**2) / (2*h) if h < d else d )
        else:
            print(min(subR))
        idx += 2 + N

solve()