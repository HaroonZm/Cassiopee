import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

sys.setrecursionlimit(100000)
input = sys.stdin.readline

def read_int():
    return int(input())

def read_int_n():
    return list(map(int, input().split()))

def read_float():
    return float(input())

def read_float_n():
    return list(map(float, input().split()))

def read_str():
    return input().strip()

def read_str_n():
    return list(map(str, input().split()))

def error_print(*args):
    print(*args, file=sys.stderr)

def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap

class Mod:
    def __init__(self, m):
        self.m = m

    def add(self, a, b):
        return (a + b) % self.m

    def sub(self, a, b):
        return (a - b) % self.m

    def mul(self, a, b):
        return ((a % self.m) * (b % self.m)) % self.m

    def div(self, a, b):
        return self.mul(a, pow(b, self.m-2, self.m))

    def pow(self, a, b):
        return pow(a, b, self.m)

@mt
def slv(N, S):
    if S[0] != 'B' or S[-1] != 'B':
        return 0

    LR = [''] * N * 2
    l = 0
    ans = 1
    M = Mod(10**9+7)
    for i in range(2*N):
        if S[i] == 'B':
            if l % 2 == 0:
                LR[i] = 'L'
                l += 1
            else:
                LR[i] = 'R'
                ans = M.mul(ans, l)
                l -= 1

        else:
            if l % 2 == 0:
                LR[i] = 'R'
                ans = M.mul(ans, l)
                l -= 1
            else:
                LR[i] = 'L'
                l += 1

    C = Counter(LR)
    if C['L'] != C['R']:
        return 0

    for i in range(1, N+1):
        ans = ans = M.mul(ans, i)

    return ans

def main():
    N = read_int()
    S = read_str()
    print(slv(N, S))

if __name__ == '__main__':
    main()