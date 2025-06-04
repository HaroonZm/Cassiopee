import array
import functools
import itertools
import math
from fractions import Fraction
import os
import sys

DEBUG = os.environ.get('DEBUG', False)

def log(*k, **wa):
    if DEBUG:
        print(*k, **wa)

class Data:
    @staticmethod
    def take():
        return sys.stdin.readline().rstrip()
    @staticmethod
    def ints():
        return list(map(int, Data.take().split()))
    def __call__(self): return self.ints()

dat = Data()

def process(N, M, A, B):
    ends = {}
    idx = 0
    memo = [0 for _ in range(N+1)]
    C, starter, pointer, links = [], [], 0, {}
    lines = list(sorted(B))
    L, cnt, right = {}, [], 0

    for ind in range(1, N+1):
        while idx<M and lines[idx][0] == ind:
            l, r = lines[idx]
            if l not in links:
                links[l] = len(cnt)
                cnt.append(0)
                starter.append(l)
            cnt[links[l]] += 1
            if r not in ends:
                ends[r] = []
            ends[r].append(links[l])
            idx += 1
        lv = ind-1
        if pointer < len(cnt):
            lv = starter[pointer]-1
        memo[ind] = max(memo[ind-1], memo[lv]+A[ind-1])
        if ind in ends:
            for gi in ends[ind]: cnt[gi] -= 1
        while pointer < len(cnt) and cnt[pointer]==0:
            pointer+=1
    return memo[-1]

def start():
    fetch = Data()
    N, M = fetch.ints()
    A = fetch.ints()
    B = []
    for _ in range(M):
        B.append(tuple(fetch.ints()))
    res = process(N, M, A, B)
    print(res)

if __name__ == "__main__":
    start()