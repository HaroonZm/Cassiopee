from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

q = input()
for loop in range(q):
    x0, y0, x1, y1 = map(int, raw_input().split())
    n = input()
    ls = []
    for i in range(n):
        x2, y2, x3, y3, o, l = map(int, raw_input().split())
        flag = (o + l) % 2
        a1 = y1 - y0
        b1 = x0 - x1
        c1 = x0 * (y1 - y0) - y0 * (x1 - x0)
        a2 = y3 - y2
        b2 = x2 - x3
        c2 = x2 * (y3 - y2) - y2 * (x3 - x2)
        det = a1 * b2 - b1 * a2
        if det == 0:
            dx = x2 - x0
            dy = y2 - y0
            if dx * a1 + dy * b1 != 0:
                pass
            elif max(x0, x1) < min(x2, x3) or max(x2, x3) < min(x0, x1) or max(y0, y1) < min(y2, y3) or max(y2, y3) < min(y0, y1):
                pass
            else:
                p = [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]
                for i in range(4):
                    for j in range(4):
                        if p[i] == p[j]:
                            ls.append((p[i], flag))
            continue
        xdet = c1 * b2 - c2 * b1
        ydet = c2 * a1 - c1 * a2
        if min(x0, x1)*det <= xdet <= max(x0, x1)*det and min(y0, y1)*det <= ydet <= max(y0, y1)*det and min(x2, x3)*det <= xdet <= max(x2, x3)*det and min(y2, y3)*det <= ydet <= max(y2, y3)*det:
            detf = float(det)
            ls.append( ((xdet / detf, ydet / detf), flag) )
    ls.sort()
    ans = 0
    for i in range(len(ls) - 1):
        if ls[i][1] != ls[i + 1][1]:
            ans += 1
    print ans