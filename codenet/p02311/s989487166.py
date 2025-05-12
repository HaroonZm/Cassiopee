#!/usr/bin/env python3
# CGL_7_G: Circles - Common Tangent

from math import acos, atan2, cos, hypot, isclose, pi, sin

def tangent_points(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2

    c1c2 = hypot(x2-x1, y2-y1)
    t0 = atan2(y2-y1, x2-x1)
    ps = []

    r1r2 = r1+r2
    if isclose(c1c2, r1r2):
        ps.append((x1 + r1*cos(t0), y1 + r1*sin(t0)))
    elif c1c2 > r1r2:
        t1 = acos(r1r2 / c1c2)
        ps.append((x1 + r1*cos(t0+t1), y1 + r1*sin(t0+t1)))
        ps.append((x1 + r1*cos(t0-t1), y1 + r1*sin(t0-t1)))

    r1r2 = r1-r2
    if isclose(c1c2, abs(r1r2)):
        if r1r2 > 0.0:
            t1 = 0.0
        else:
            t1 = pi
        ps.append((x1 + r1*cos(t0+t1), y1 + r1*sin(t0+t1)))
    elif c1c2 > abs(r1r2):
        if r1r2 > 0.0:
            t1 = acos(r1r2 / c1c2)
        else:
            t1 = pi - acos(-r1r2 / c1c2)
        ps.append((x1 + r1*cos(t0+t1), y1 + r1*sin(t0+t1)))
        ps.append((x1 + r1*cos(t0-t1), y1 + r1*sin(t0-t1)))

    return ps

def run():
    c1 = [int(i) for i in input().split()]
    c2 = [int(i) for i in input().split()]

    ps = tangent_points(c1, c2)

    for p in sorted(ps):
        print("{:.10f} {:.10f}".format(*map(eliminate_minus_zero, p)))

def eliminate_minus_zero(f):
    if isclose(f, 0.0, abs_tol=1e-9):
        return 0.0
    else:
        return f

if __name__ == '__main__':
    run()