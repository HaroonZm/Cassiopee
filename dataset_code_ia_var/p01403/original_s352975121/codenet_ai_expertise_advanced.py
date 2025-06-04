import sys
import math
from itertools import accumulate

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

MOD = 10 ** 9 + 7
INF = float('inf')


def list2d(a, b, c):
    return [[c] * b for _ in range(a)]


def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]


def list4d(a, b, c, d, e):
    return [[[[e] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]


def ceil(x, y=1):
    return -(-x // y)


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST(N=None):
    if N is None:
        return list(MAP())
    return [INT() for _ in range(N)]


def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


N = 10 ** 6 + 1

# Optimized Euler's Totient Table using advanced features
phi = [i for i in range(N + 1)]
for i in range(2, N + 1):
    if phi[i] == i:
        phi_slice = phi[i:N+1:i]
        phi[i:N+1:i] = [val - val // i for val in phi_slice]

phi[0] = 1  # By problem convention

ans = list(accumulate(phi))

for _ in range(INT()):
    a = INT()
    print(ans[a])