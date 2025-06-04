def is_in_triangle(px1, py1, px2, py2, px3, py3, x, y):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))
    A = area(px1, py1, px2, py2, px3, py3)
    A1 = area(x, y, px2, py2, px3, py3)
    A2 = area(px1, py1, x, y, px3, py3)
    A3 = area(px1, py1, px2, py2, x, y)
    return A == A1 + A2 + A3

import sys
input=sys.stdin.readline

n = int(input())
for _ in range(n):
    px1, py1, px2, py2, px3, py3, xk, yk, xs, ys = map(int, input().split())
    in_k = is_in_triangle(px1, py1, px2, py2, px3, py3, xk, yk)
    in_s = is_in_triangle(px1, py1, px2, py2, px3, py3, xs, ys)
    if in_k != in_s:
        print("OK")
    else:
        print("NG")