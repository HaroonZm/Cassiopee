from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

def in_sec(a, b, c):
    return min(a, b) <= c <= max(a, b)

q = input()

for loop in range(q):
    x0, y0, x1, y1 = map(int, raw_input().split())
    n = input()
    ls = []
    for i in range(n):
        x2, y2, x3, y3, o, l = map(int, raw_input().split())
        flag = (o + l) % 2
        a1, b1, c1 = [y1 - y0, x0 - x1, x0 * (y1 - y0) - y0 * (x1 - x0)]
        a2, b2, c2 = [y3 - y2, x2 - x3, x2 * (y3 - y2) - y2 * (x3 - x2)]
        det = a1 * b2 - b1 * a2
        if det == 0:
            dx, dy = [x2 - x0, y2 - y0]
            if dx * a1 + dy * b1 != 0:
                pass
            elif max(x0, x1) < min(x2, x3) or max(x2, x3) < min(x0, x1) \
                or max(y0, y1) < min(y2, y3) or max(y2, y3) < min(y0, y1):
                pass
            else:
                p = [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]
                ls += [(p[i], flag) for i in range(4) for j in range(4) if p[i] == p[j]]
            continue
        xdet = c1 * b2 - c2 * b1
        ydet = c2 * a1 - c1 * a2
        if in_sec(det * x0, det * x1, xdet) and in_sec(det * y0, det * y1, ydet) \
            and in_sec(det * x2, det * x3, xdet) and in_sec(det * y2, det * y3, ydet):
            det = float(det)
            ls += [((xdet / det, ydet / det), flag)]
    ls.sort()
    ans = 0
    for i in range(len(ls) - 1):
        if ls[i][1] != ls[i + 1][1]:
            ans += 1
    print ans