#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys

def main():
    N = read_int()
    P = [Vec(*read_ints()) for _ in range(N)]
    Q = read_int()
    for _ in range(Q):
        x1, y1, x2, y2 = read_ints()
        print(solve(N, P, Vec(x1, y1), Vec(x2, y2)))

def solve(N, P, A, B):
    b = B - A
    P = [p - A for p in P]

    ccw = 0
    cw = 0
    for p in P:
        c = b.cross(p)
        if c >= 0:
            ccw += 1
        if c <= 0:
            cw += 1

    if ccw == N:
        return float(poly_area(P))
    if cw == N:
        return 0

    cross_points = []

    for i in range(N):
        j = (i + 1) % N
        p = P[i]
        q = P[j]
        qp = q - p

        cross_qp_b = qp.cross(b)
        if cross_qp_b == 0:
            continue
        k = Fraction(b.cross(p), cross_qp_b)
        if 0 < k <= 1:
            t = Fraction(p.cross(qp), b.cross(qp))
            cross_points.append((t, i, k))

    cross_points.sort()
    _, i1, k1 = cross_points[0]
    _, i2, k2 = cross_points[1]

    x1 = P[i1] + k1 * (P[(i1 + 1) % N] - P[i1])
    x2 = P[i2] + k2 * (P[(i2 + 1) % N] - P[i2])
    Q = [x2]
    j = (i2 + 1) % N
    while j != i1:
        Q.append(P[j])
        j = (j + 1) % N
    Q.append(P[i1])
    Q.append(x1)

    return float(poly_area(Q))

def poly_area(P):
    N = len(P)
    a = 0
    for i in range(1, N - 1):
        a += Fraction((P[i + 1] - P[i]).cross(P[0] - P[i + 1]), 2)
    return a

###############################################################################
# AUXILIARY FUNCTIONS

class Vec(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vec(self.x / scalar, self.y / scalar)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    def __idiv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self

    def __neg__(self):
        return Vec(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash('Vec', self.x, self.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def abs2(self):
        return self.x * self.x + self.y * self.y

    def __abs__(self):
        return math.sqrt(float(self.abs2()))

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

DEBUG = 'DEBUG' in os.environ

def inp():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(inp())

def read_ints():
    return [int(e) for e in inp().split()]

def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()