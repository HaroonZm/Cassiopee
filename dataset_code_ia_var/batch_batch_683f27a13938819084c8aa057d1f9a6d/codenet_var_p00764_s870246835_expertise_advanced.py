from math import acos
from cmath import phase, rect
from functools import partial
from sys import stdin

def solve():
    input_iter = iter(stdin.readline, '')
    lim = 5000
    while True:
        n_s = next(input_iter)
        if not n_s:
            break
        n = int(n_s)
        if n == 0:
            break
        # Parse centers and radii as complex numbers
        centers_radii = [tuple(map(int, next(input_iter).split())) for _ in range(n)]
        points = []
        c0 = complex(*centers_radii[0][:2])
        r0 = centers_radii[0][2]
        points.append(c0)
        # Compute intersection points
        for (x, y, r1) in centers_radii[1:]:
            c1, r1 = complex(x, y), r1
            d = abs(c1 - c0)
            try:
                a = acos((r0 ** 2 + d ** 2 - r1 ** 2) / (2 * r0 * d))
            except ValueError:
                a = 0  # overlapping or tangent circles; fallback
            t = phase(c1 - c0)
            points.extend([c0 + rect(r0, t + a), c0 + rect(r0, t - a)])
            c0, r0 = c1, r1
        goal = c0
        g_idx = 2 * n - 1
        dist = [lim] * (2 * n)
        dist[0] = 0
        # Generate indices in pairs
        indices = ((i+1, i+2) for i in range(g_idx))
        # Advance search using generator expressions, cache phase 
        for (j, k), cp, d in zip(indices, points, dist):
            s1 = s2 = p_s1 = p_s2 = None
            z = enumerate(zip(points[j::2], points[k::2]), start=j)
            for l, (cp1, cp2) in z:
                t_s1 = cp1 - cp
                t_s2 = cp2 - cp
                if s1 is None or phase(s1 / t_s1) >= 0:
                    s1 = t_s1
                if s2 is None or phase(s2 / t_s2) <= 0:
                    s2 = t_s2
                if phase(s1 / s2) < 0:
                    break
                if p_s1 != s1:
                    dist[l] = min(dist[l], d + abs(s1))
                    p_s1 = s1
                if p_s2 != s2:
                    dist[l+1] = min(dist[l+1], d + abs(s2))
                    p_s2 = s2
            else:
                gs = goal - cp
                if (s1 is None and s2 is None) or (phase(s1 / gs) >= 0 and phase(s2 / gs) <= 0):
                    dist[g_idx] = min(dist[g_idx], d + abs(gs))
        print(dist[g_idx])

solve()