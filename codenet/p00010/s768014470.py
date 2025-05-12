from math import acos
from math import sin

def ang(ax, ay, ox, oy, bx, by):
    oax, oay = ax - ox, ay - oy
    obx, oby = bx - ox, by - oy
    r1, r2 = oax ** 2 + oay ** 2, obx ** 2 + oby ** 2
    return acos((oax * obx + oay * oby) / (r1 * r2) ** 0.5)

def circumcircle(x1, y1, x2, y2, x3, y3):
    s2A = sin(2 * ang(x3, y3, x1, y1, x2, y2))
    s2B = sin(2 * ang(x1, y1, x2, y2, x3, y3))
    s2C = sin(2 * ang(x2, y2, x3, y3, x1, y1))
    px = (s2A * x1 + s2B * x2 + s2C * x3) / (s2A + s2B + s2C) + 0.
    py = (s2A * y1 + s2B * y2 + s2C * y3) / (s2A + s2B + s2C) + 0.
    r = (((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5) / (2 * sin(ang(x2, y2, x1, y1, x3, y3))) + 0.
    return px, py, r

n = int(input())
for i in range(n):
    print("{0[0]:.3f} {0[1]:.3f} {0[2]:.3f}".format(
          circumcircle(*tuple(map(float, input().split())))))