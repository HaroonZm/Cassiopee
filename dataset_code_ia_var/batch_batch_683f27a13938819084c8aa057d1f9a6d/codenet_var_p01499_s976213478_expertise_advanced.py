import sys
from functools import partial
from operator import mul
from math import prod

sys.setrecursionlimit(1 << 25)
INF = float('inf')
EPS = 1e-10
MOD = 10**9 + 7
DIRECTIONS_4 = [(-1,0), (0,1), (1,0), (0,-1)]
DIRECTIONS_8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

read_ints = lambda: list(map(int, sys.stdin.readline().split()))
read_ints0 = lambda: [x-1 for x in map(int, sys.stdin.readline().split())]
read_floats = lambda: list(map(float, sys.stdin.readline().split()))
read_strings = lambda: sys.stdin.readline().split()
read_int = lambda: int(sys.stdin.readline())
read_float = lambda: float(sys.stdin.readline())
read_input = input
print_flush = partial(print, flush=True)

def main():
    n, t = read_ints()
    a = sorted(map(read_int, range(n)))
    res, left = 1, 0
    for right, val in enumerate(a):
        while a[left] < val - t:
            left += 1
        res = (res * (right - left + 1)) % MOD
    return res

print(main())