import sys
from math import hypot, sqrt

def input():
    return sys.stdin.readline().strip()

def list2d(a, b, c):
    return [[c] * b for _ in range(a)]

def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def ceil(x, y=1):
    return int(-(-x // y))

def INT():
    return int(input())

def MAP():
    return map(int, input().split())

def LIST():
    return list(map(int, input().split()))

def Yes():
    print('Yes')

def No():
    print('No')

def YES():
    print('YES')

def NO():
    print('NO')

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

def heron(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

x1, y1 = MAP()
x2, y2 = MAP()
x3, y3 = MAP()

a = hypot(x1 - x2, y1 - y2)
b = hypot(x2 - x3, y2 - y3)
c = hypot(x3 - x1, y3 - y1)

S = heron(a, b, c)
r = 2 * S / (a + b + c)

mx = max(a, b, c)
print(mx / (2 + mx / r))