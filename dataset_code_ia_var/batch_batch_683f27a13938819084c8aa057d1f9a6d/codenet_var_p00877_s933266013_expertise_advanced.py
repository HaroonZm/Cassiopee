from functools import partial
from itertools import tee, islice, chain

def dot(c1, c2):
    return (c1.real * c2.real + c1.imag * c2.imag)

def cross(c1, c2):
    return (c1.real * c2.imag - c1.imag * c2.real)

def on_segment(p, a, b):
    v1, v2 = a - p, b - p
    return not cross(v1, v2) and dot(v1, v2) < 0

def ccw(p0, p1, p2):
    return cross(p1 - p0, p2 - p0) > 0

def intersect(p1, p2, p3, p4):
    d1, d2 = cross(p2-p1, p3-p1), cross(p2-p1, p4-p1)
    if not d1 and not d2:
        return dot(p1-p3, p2-p3) < 0 or dot(p1-p4, p2-p4) < 0
    d3, d4 = cross(p4-p3, p1-p3), cross(p4-p3, p2-p3)
    return d1*d2 <= 0 and d3*d4 <= 0

def monotone_chain(points):
    def build(seq):
        hull = []
        for p in seq:
            while len(hull) >= 2 and ccw(hull[-2], hull[-1], p):
                hull.pop()
            hull.append(p)
        return hull
    points = sorted(set(points), key=lambda c: (c.real, c.imag))
    upper = build(points)
    lower = build(points[::-1])
    return upper[:-1] + lower[:-1]

def contains(poly, pt):
    for a, b in pairwise_closed(poly):
        da, db = a-pt, b-pt
        cr = cross(da, db)
        if cr > 0 or (not cr and dot(da, db) > 0):
            return False
    return True

def string_to_complex(line):
    return complex(*map(int, line.split()))

def pairwise_closed(seq):
    # yields (a,b) for adjacent points, wrapping around
    a, b = tee(seq)
    yield from zip(a, chain(islice(b, 1, None), [next(a)]))

def solve():
    import sys
    lines = iter(sys.stdin.readlines())
    parse_pts = lambda it, n: [string_to_complex(next(it)) for _ in range(n)]
    while True:
        header = next(lines)
        n, m = map(int, header.split())
        if not n and not m:
            break
        pts1, pts2 = parse_pts(lines, n), parse_pts(lines, m)
        if n == 1 and m == 1:
            print('YES')
        elif n == 1 and m == 2:
            print('NO' if on_segment(pts1[0], *pts2) else 'YES')
        elif n == 2 and m == 1:
            print('NO' if on_segment(pts2[0], *pts1) else 'YES')
        elif n == 2 and m == 2:
            print('NO' if intersect(*pts1, *pts2) else 'YES')
        elif n == 1:
            cvx = monotone_chain(pts2)
            print('NO' if contains(cvx, pts1[0]) else 'YES')
        elif m == 1:
            cvx = monotone_chain(pts1)
            print('NO' if contains(cvx, pts2[0]) else 'YES')
        elif n == 2:
            cvx = monotone_chain(pts2)
            p1, p2 = pts1
            if contains(cvx, p1) or contains(cvx, p2):
                print('NO')
            else:
                for q1, q2 in pairwise_closed(cvx):
                    if intersect(p1, p2, q1, q2):
                        print('NO')
                        break
                else:
                    print('YES')
        elif m == 2:
            cvx = monotone_chain(pts1)
            p1, p2 = pts2
            if contains(cvx, p1) or contains(cvx, p2):
                print('NO')
            else:
                for q1, q2 in pairwise_closed(cvx):
                    if intersect(p1, p2, q1, q2):
                        print('NO')
                        break
                else:
                    print('YES')
        else:
            cvx1, cvx2 = monotone_chain(pts1), monotone_chain(pts2)
            if any(contains(cvx1, p) for p in cvx2):
                print('NO')
            elif any(contains(cvx2, p) for p in cvx1):
                print('NO')
            elif any(
                intersect(p1, p2, q1, q2)
                for p1, p2 in pairwise_closed(cvx1)
                for q1, q2 in pairwise_closed(cvx2)
            ):
                print('NO')
            else:
                print('YES')
solve()