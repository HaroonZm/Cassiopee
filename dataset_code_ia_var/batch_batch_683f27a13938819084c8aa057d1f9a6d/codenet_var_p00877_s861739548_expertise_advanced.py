import sys
import math
from operator import itemgetter
from functools import partial, lru_cache

sys.setrecursionlimit(10_000_000)
INF = float('inf')
EPS = 1e-13
MOD = 10**9 + 7
DIRECTIONS_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTIONS_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [x - 1 for x in map(int, sys.stdin.readline().split())]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def pf(s): print(s, flush=True)

@lru_cache(maxsize=None)
def ccw(a, b, c):
    ax, ay = b[0] - a[0], b[1] - a[1]
    bx, by = c[0] - a[0], c[1] - a[1]
    cross = ax * by - ay * bx
    if cross > 0: return 1
    if cross < 0: return -1
    dot = ax * bx + ay * by
    sq_a = ax * ax + ay * ay
    sq_b = bx * bx + by * by
    if dot < 0: return 2
    if sq_a < sq_b: return -2
    return 0

def convex_hull(points):
    points = sorted(set(map(tuple, points)))
    if len(points) <= 2:
        return points[:]
    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def _kosa(a1, a2, b1, b2):
    (x1, y1), (x2, y2) = a1, a2
    (x3, y3), (x4, y4) = b1, b2
    t1 = (x1 - x2) * (y3 - y1) + (y1 - y2) * (x1 - x3)
    t2 = (x1 - x2) * (y4 - y1) + (y1 - y2) * (x1 - x4)
    return t1 * t2 < 0

def kosa(a1, a2, b1, b2): return _kosa(a1, a2, b1, b2) and _kosa(b1, b2, a1, a2)

def dist_p2(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def distance3(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    ax, ay = x2 - x1, y2 - y1
    bx, by = x3 - x1, y3 - y1
    denominator = ax * ax + ay * ay
    dot = ax * bx + ay * by
    if denominator == 0:
        return dist_p2(p1, p3)
    r = dot / denominator
    if r <= 0:
        return dist_p2(p1, p3)
    if r >= 1:
        return dist_p2(p2, p3)
    proj = (x1 + r * ax, y1 + r * ay)
    return dist_p2(proj, p3)

def are_convex_hulls_separate(h1, h2):
    n1, n2 = len(h1), len(h2)
    for a, b in zip(h1, h1[1:] + h1[:1]):
        for c in h2:
            if distance3(a, b, c) < EPS:
                return False
        for i in range(n2):
            if n2 > 1 and kosa(a, b, h2[i], h2[(i+1)%n2]):
                return False
    for a, b in zip(h2, h2[1:] + h2[:1]):
        for c in h1:
            if distance3(a, b, c) < EPS:
                return False
    return True

def main():
    results = []
    input_iter = iter(sys.stdin.readline, '')
    while True:
        try:
            n_m_line = next(input_iter)
            if not n_m_line.strip():
                continue
            n, m = map(int, n_m_line.strip().split())
            if n == 0:
                break

            a = [tuple(map(int, next(input_iter).split())) for _ in range(n)]
            b = [tuple(map(int, next(input_iter).split())) for _ in range(m)]

            hull_union = convex_hull(a + b)
            a_on_hull = any(p in a for p in hull_union)
            b_on_hull = any(p in b for p in hull_union)
            if not (a_on_hull and b_on_hull):
                results.append('NO')
                continue

            hull_a = convex_hull(a)
            hull_b = convex_hull(b)

            if are_convex_hulls_separate(hull_a, hull_b):
                results.append('YES')
            else:
                results.append('NO')
        except StopIteration:
            break

    return '\n'.join(results)

print(main())