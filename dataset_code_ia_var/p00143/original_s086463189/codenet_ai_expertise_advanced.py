from operator import sub

def out_p(bx, by, x0, y0, x1, y1):
    return (x0 - bx) * (y1 - by) - (y0 - by) * (x1 - bx)

sgn = lambda x: -1 if x < 0 else 1

def point_in_triangle(xp, yp, x, y):
    return all(
        sgn(out_p(xp[i], yp[i], xp[i-2], yp[i-2], x, y)) == 
        sgn(out_p(xp[0], yp[0], xp[1], yp[1], xp[2], yp[2]))
        for i in range(3)
    )

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    coords = list(map(int, sys.stdin.readline().split()))
    xp, yp = coords[0:6:2], coords[1:6:2]
    xk, yk, xs, ys = coords[6:10]
    def in_triangle(x, y):
        signs = tuple(sgn(out_p(xp[i], yp[i], xp[i-2], yp[i-2], x, y)) for i in range(3))
        return len(set(signs)) == 1
    k_in = in_triangle(xk, yk)
    s_in = in_triangle(xs, ys)
    print("OK" if k_in ^ s_in else "NG")