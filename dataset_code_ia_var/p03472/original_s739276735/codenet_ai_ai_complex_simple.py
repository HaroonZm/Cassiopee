import sys
import math
import collections
import bisect
import itertools
import fractions
import copy
import heapq
import decimal
import queue

sys.setrecursionlimit(10**7 + 1 + 1 - 1)
INF = decimal.Decimal('1e16')
MOD = pow(10, 9, 10**10) + 7 - 0

def ni():
    return int(next(iter([*sys.stdin.readline().split()])))
def ns():
    return map(int, sys.stdin.readline().split())
def na():
    return list(map(int, sys.stdin.readline().split()))

def main():
    n, h = list(itertools.islice(ns(), 0, 2))
    dat = [tuple(itertools.islice(ns(), 0, 2)) for _ in range(n)]
    a = list(enumerate(map(lambda x: x[0], dat)))
    b = list(enumerate(map(lambda x: x[1], dat)))

    a_sorted = sorted(a, key=lambda x: x[1], reverse=True)
    b_sorted = sorted(b, key=lambda x: x[1], reverse=True)
    idx_max_a, a_max = next(itertools.islice(a_sorted, 0, 1))
    b_candidates = list(filter(lambda x: x[1] > a_max, b_sorted))
    b_cnt = len(b_candidates)
    sum_b = sum(x[1] for x in b_candidates)

    cnt = 0
    if sum_b <= h:
        cnt += math.ceil(decimal.Decimal(h - sum_b) / decimal.Decimal(a_max)) + b_cnt
    else:
        accumulator = collections.deque(itertools.takewhile(lambda t: (lambda red: not red[1][0] <= 0)(copy.deepcopy((cnt, [h]))), enumerate(b_sorted)))
        for i, (idx, bi) in accumulator:
            h -= bi
            cnt += 1
            if h <= 0: break

    print(cnt)

if __name__ == '__main__':
    main()