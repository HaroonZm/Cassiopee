import sys
import itertools
from operator import itemgetter
from functools import partial, lru_cache

readline = sys.stdin.readline
write = sys.stdout.write

def cross3(p0, p1, q0):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = q0
    return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)

def cross_point(p0, p1, q0, q1):
    x0, y0 = p0; x1, y1 = p1
    x2, y2 = q0; x3, y3 = q1
    dx0, dy0 = x1 - x0, y1 - y0
    dx1, dy1 = x3 - x2, y3 - y2
    s = (y0-y2)*dx1 - (x0-x2)*dy1
    sm = dx0*dy1 - dy0*dx1
    if sm < 0:
        return - (x0*sm + s*dx0), - (y0*sm + s*dy0), -sm
    return x0*sm + s*dx0, y0*sm + s*dy0, sm

def solve():
    N, M = map(int, readline().split())
    PSS = [[tuple(map(int, readline().split())) for _ in range(int(readline()))] for _ in range(N)]
    QS = list(map(tuple, map(int, readline().split())) for _ in range(M))
    LS = [((x0, y0), (x1, y1)) for PS in PSS for (x0, y0) in PS for (x1, y1) in QS]

    @lru_cache(maxsize=None)
    def check(p, q, r):
        p0 = (p, q)
        PS_scaled = [[(x * r, y * r) for x, y in PS] for PS in PSS]
        good = 0
        scaled_QS = [(x * r, y * r) for x, y in QS]
        for q0 in scaled_QS:
            for PS in PS_scaled:
                cyclic_P = itertools.chain([PS[-1]], PS)
                pairs = zip(cyclic_P, PS)
                for p1, q1 in pairs:
                    C0, C1 = cross3(p0, q0, p1), cross3(p0, q0, q1)
                    D0, D1 = cross3(p1, q1, p0), cross3(p1, q1, q0)
                    if C0 * C1 < 0 and D0 * D1 < 0:
                        break
                else:
                    continue
                break
            else:
                good += 1
        return good

    ans = 0
    for (p0, p1), (q0, q1) in itertools.combinations(LS, 2):
        x, y, r = cross_point(p0, p1, q0, q1)
        if r != 0:
            ans = max(ans, check(x, y, r))
    write(f"{ans}\n")

solve()