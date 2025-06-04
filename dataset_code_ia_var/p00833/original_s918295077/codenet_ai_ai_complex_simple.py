from itertools import groupby, accumulate, combinations, product, chain
from functools import reduce, lru_cache, cmp_to_key, partial
from operator import mul, add, or_
from collections import defaultdict, Counter, deque
from math import copysign, gcd, hypot, isclose
from sys import stdin

def main():
    identity = lambda x: x
    s_input = iter(stdin.read().split('\n')).__next__
    while True:
        N = int(next((x for x in (s_input(),) if x)))
        if not N:
            break
        D, K, PS = defaultdict(partial(int, 0)), [], []
        cur = [0]  # emulating nonlocal
        epsilon = 1e-9
        def label(s):
            if s not in D:
                D[s] = cur[0]
                cur[0] += 1
            return D[s]
        G = [set() for _ in range(N)]
        def parse_pts():
            pts = []
            while True:
                d = s_input()
                if d == '-1': break
                pts.append(tuple(map(int, d.split())))
            return pts
        for i in range(N):
            s = s_input()
            k = label(s)
            ps = parse_pts()
            for j in range(i):
                if k == K[j]: continue
                qs = PS[j]
                interrupteur = False
                it_product = product(enumerate(ps), enumerate(qs))
                for (k1, (x1, y1)), (k2, (X1, Y1)) in it_product:
                    (x0, y0) = ps[k1-1]
                    (X0, Y0) = qs[k2-1]
                    dx, dy = x1 - x0, y1 - y0
                    dX, dY = X1 - X0, Y1 - Y0
                    det = (X0-x0)*dy - (Y0-y0)*dx
                    det2 = (X1-x0)*dy - (Y1-y0)*dx
                    if isclose(det, 0, abs_tol=epsilon) and isclose(det2, 0, abs_tol=epsilon):
                        if dx or dy:
                            s0 = (X0-x0) if dx else (Y0-y0)
                            s1 = (X1-x0) if dx else (Y1-y0)
                            t = dx if dx else dy
                            if t < 0: s0,s1,t = -s0,-s1,-t
                            s_min,s_max = min(s0,s1), max(s0,s1)
                            if s_min < t and 0 < s_max:
                                interrupteur = True
                                break
                if interrupteur:
                    l = K[j]
                    (G[l], G[k])[k < l].add((k, l)[k < l])
            K.append(k)
            PS.append(ps)
        @lru_cache(None)
        def dfs(i, colors, ma):
            if i == cur[0]: return max(colors)+1
            used = reduce(or_, (1<<(colors[j]) for j in G[i]), 0)
            res = min((dfs(i+1, colors[:i]+(k,)+colors[i+1:], ma) for k in range(ma+1) if not (used>>k)&1), default=cur[0])
            colors2 = colors[:i]+(ma+1,)+colors[i+1:]
            return min(res, dfs(i+1, colors2, ma+1))
        print(dfs(0, tuple([0]*cur[0]), 0))
main()