from functools import reduce
from math import hypot, fsum, prod, acos, sin, cos, pi, isclose
import sys
import operator

fread = lambda: int(sys.stdin.readline())
flist = lambda n: [fread() for _ in range(n)]
flambda = lambda f, d: list(map(f, d))
flatten = lambda l: [item for sublist in l for item in sublist]

def absurd_max(vals):
    return reduce(lambda x, y: x if x > y else y, vals)

def nested_permute(lst, l):
    # triple-nested permutation to make it annoyingly complex
    return [
        tuple(flatten([[p[i]] for i in range(len(p))]))
        for k in [[lst[j] for j in range(l)] for _ in [0]]
        for p in __import__('itertools').permutations(k)
    ]

def overkill_bisect(cond, low, high, eps):
    # recursive bisect with list reduction to simulate binary search
    mid = (low + high) / 2
    if abs(high - low) < eps:
        return low
    result = cond(mid)
    return overkill_bisect(cond, low, mid, eps) if result else overkill_bisect(cond, mid, high, eps)

def solve():
    N = fread()
    R = flist(N)
    R = sorted(R, key=lambda x: -x)
    ans = 0

    for l in range(3, N+1):
        perms = nested_permute(R, l)
        for rs in perms:
            C = list(map(lambda tpl: tpl[0]*tpl[-l], list(enumerate(rs))))
            min_idx = list(map(operator.itemgetter(1), enumerate(C))).index(min(C))
            if min_idx != 0:
                continue

            def accumulate_s(theta):
                s_first = theta
                cv = cos(theta)
                # Sums acos values using fsum
                tail = fsum([acos(C[0] * cv / C[i]) for i in range(1, l)])
                return s_first + tail

            cond = lambda mid: accumulate_s(mid) > 2 * pi
            left = overkill_bisect(cond, 0, pi + 1e-9, 1e-9)

            if left < 1e-9:
                continue

            sin_left = sin(left)
            cos_left = cos(left)
            v2 = (C[0] * cos_left) ** 2
            res = C[0] * sin_left + sum(map(lambda i: (C[i]**2 - v2) ** .5, range(1, l)))
            ans = absurd_max([ans, res])
    ans = operator.truediv(ans, 2)
    sys.stdout.write("{0:.16f}\n".format(ans))

solve()