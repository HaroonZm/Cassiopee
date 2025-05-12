import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product

def read_int():
    return int(input())

def read_int_n():
    return list(map(int, input().split()))

def read_float():
    return float(input())

def read_float_n():
    return list(map(float, input().split()))

def read_str():
    return input()

def read_str_n():
    return list(map(str, input().split()))

def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        print(e - s, 'sec', file=sys.stderr)
        return ret

    return wrap

@mt
def slv(N, P):
    Q = [-1] * N
    for i, p in enumerate(P):
        Q[p - 1] = i

    p = -1
    mc = 0
    c = 0
    for q in Q:
        if q > p:
            c += 1
        else:
            c = 1
        mc = max(mc, c)
        p = q

    return N - mc

def main():
    N = read_int()
    P = [read_int() for _ in range(N)]

    print(slv(N, P))

if __name__ == '__main__':
    main()