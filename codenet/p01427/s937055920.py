from collections import defaultdict
from math import atan2
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def gcd(m, n):
    while n:
        m, n = n, m % n
    return m
def solve():
    H, W = map(int, readline().split())

    MP = []
    MP.append([0]*(W+2))
    MP.extend([[0] + list(map(".#".index, readline().strip())) + [0] for i in range(H)])
    MP.append([0]*(W+2))

    R = defaultdict(int)
    for i in range(H+1):
        for j in range(W+1):
            if MP[i+1][j] != MP[i][j+1] or MP[i][j] == MP[i+1][j+1]:
                continue
            if MP[i][j] == MP[i][j+1]:
                v = 1
            else:
                v = -1
            x = j; y = H-i
            if x == 0:
                R[0, 1] += v
            elif y == 0:
                R[1, 0] += v
            else:
                g = gcd(x, y)
                R[x//g, y//g] += v
    *PS, = R.items()
    PS.sort(key = lambda p: atan2(p[0][1], p[0][0]), reverse=1)
    ans = 0; cur = 1
    for (x, y), v in PS:
        cur += v
        ans = max(ans, cur)
    write("%d\n" % ans)
solve()