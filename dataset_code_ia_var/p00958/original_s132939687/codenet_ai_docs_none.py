from fractions import Fraction
import os
import sys
import math

def main():
    M = read_int()
    A = [Vec(*read_ints()) for _ in range(M)]
    print(solve(M, A))

def solve(M, A):
    D = [[None] * M for _ in range(M)]
    last_did = 0
    did_map = {}
    for i in range(M):
        for j in range(i + 1, M):
            v = A[j] - A[i]
            if v.y < 0 or (v.y == 0 and v.x < 0):
                v = -v
            c = Fraction(v.x ** 2, v.abs2())
            if v.x < 0:
                c = -c
            if c not in did_map:
                did_map[c] = last_did
                did = last_did
                last_did += 1
            else:
                did = did_map[c]
            D[i][j] = did
            D[j][i] = did

    used = [False] * M
    m = {}
    best = 0

    def rec(i):
        nonlocal best
        while i < M and used[i]:
            i += 1
        if i == M:
            s = 0
            for c in m.values():
                s += c * (c - 1) // 2
            best = max(best, s)
            return

        used[i] = True
        for j in range(i + 1, M):
            if used[j]:
                continue
            used[j] = True
            d = D[i][j]
            if d not in m:
                m[d] = 1
            else:
                m[d] += 1
            rec(i + 1)
            m[d] -= 1
            if m[d] == 0:
                del m[d]
            used[j] = False
        used[i] = False

    rec(0)
    return best

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
        return hash(('Vec', self.x, self.y))

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