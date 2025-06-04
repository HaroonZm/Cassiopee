from itertools import permutations
from math import acos, sin, cos, pi
import sys

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N = int(readline())
    R = [int(readline()) for i in range(N)]
    R.sort(reverse=True)

    ans = 0
    for l in range(3, N + 1):
        for rs in permutations(R[:l]):
            C = [rs[i] * rs[i - l + 1] for i in range(l)]
            if C.index(min(C)) != 0:
                continue

            left = 0
            right = pi + 1e-9
            while right - left > 1e-9:
                mid = (left + right) / 2
                s = mid
                cv = cos(mid)
                for i in range(1, l):
                    s += acos(C[0] * cv / C[i])
                if s > 2 * pi:
                    right = mid
                else:
                    left = mid
            if left < 1e-9:
                continue
            res = C[0] * sin(left)
            cv = cos(left)
            v2 = (C[0] * cos(left)) ** 2
            for i in range(1, l):
                res += (C[i] ** 2 - v2) ** 0.5
            ans = max(ans, res)
    ans /= 2
    write("%.16f\n" % ans)

solve()