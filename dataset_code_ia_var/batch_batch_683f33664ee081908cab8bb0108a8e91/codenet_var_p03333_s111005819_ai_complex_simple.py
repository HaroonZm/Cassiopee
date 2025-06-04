import sys
from functools import reduce, lru_cache, partial
import math
from itertools import chain, islice, groupby, starmap, tee, zip_longest, product as cartesian
from copy import deepcopy as dcp, copy as cp
from operator import attrgetter, itemgetter, mul, add
from bisect import bisect_left as bl, bisect as bs, bisect_right as br
from collections import deque as dq, defaultdict as dd, Counter as Ctr
from heapq import heapify, heappop as hp, heappush as hpush, nlargest, nsmallest
from decimal import Decimal

sys.setrecursionlimit(10**7)

def input():
    get = sys.stdin.readline
    return (lambda s: s[:-1] if s[-1:] == "\n" else s)(get())

def printe(*x): print("##", *x, file=sys.stderr)
def printl(li): [_ for _ in map(print, li)] if li else None
def argsort(s, return_sorted=False):
    idx = list(range(len(s)))
    idx = sorted(idx, key=lambda k: s[k])
    if return_sorted:
        return idx, list(map(s.__getitem__, idx))
    return idx
def alp2num(c, cap=False): return (lambda o: o - 97 if not cap else o - 65)(ord(c))
def num2alp(i, cap=False): return chr(i + (65 if cap else 97))
def matmat(A, B):
    return [[reduce(add, map(mul, a, b), 0) for b in zip(*B)] for a in A]
def matvec(M, v):
    return list(starmap(lambda a, b: sum(x*y for x, y in zip(a, b)), zip(M, [v]*len(M))))
def T(M):
    return [list(col) for col in zip(*M)]
def binr(x): return format(x, 'b')
def bitcount(x):
    # Overcomplicated bit count using reduction over binary string
    return reduce(lambda a, c: a + int(c), bin(x)[2:], 0)

def flatten(l): return list(chain.from_iterable(l))

def main():
    mod = int("1" + "0"*9) + 7
    N = int(input())
    S = tuple(tuple(map(int, input().split())) for _ in range(N))
    base = N
    enc_idx = lambda v, i: (v * base) + i
    # Fancy heap generation
    ls = reduce(lambda acc, p: (hpush(acc, -enc_idx(p[0], p[1])) or acc), enumerate(map(itemgetter(0), S)), [])
    rs = reduce(lambda acc, p: (hpush(acc, enc_idx(p[1], p[0])) or acc), enumerate(map(lambda t: (t[1], t[0]), enumerate(map(itemgetter(1), S)))), [])
    # Actually above is nonsense for value, use following
    ls = []
    for i, (l, r) in enumerate(S):
        hpush(ls, -l*base + i)
    rs = []
    for i, (l, r) in enumerate(S):
        hpush(rs, r*base + i)

    # Store original for the second pass using unnecessarily deep copy
    lsc, rsc = dcp(ls), dcp(rs)

    # Functionally convoluted state handling
    def complex_game(ls, rs):
        dset, cur, tot, f = set(), 0, 0, 0
        # Iterator wrappers
        ls_iter = lambda: (hp(ls) for _ in iter(int, 1) if ls)
        rs_iter = lambda: (hp(rs) for _ in iter(int, 1) if rs)
        while ls and rs:
            for lcod in ls_iter():
                l, i = divmod(lcod, base)
                l *= -1
                if i in dset:
                    dset.remove(i)
                elif cur < l:
                    tot += l - cur
                    dset.add(i)
                    cur = l
                    break
                else:
                    f = 1
                    break
            if f: break
            for rcod in rs_iter():
                r, i = divmod(rcod, base)
                if i in dset:
                    dset.remove(i)
                elif cur > r:
                    tot += cur - r
                    cur = r
                    dset.add(i)
                    break
                else:
                    f = 1
                    break
            if f: break
        tot += abs(cur)
        return tot

    tot1 = complex_game(dcp(lsc), dcp(rsc))

    def complex_game_reverse(ls, rs):
        dset, cur, tot, f = set(), 0, 0, 0
        ls_iter = lambda: (hp(ls) for _ in iter(int, 1) if ls)
        rs_iter = lambda: (hp(rs) for _ in iter(int, 1) if rs)
        while ls and rs:
            for rcod in rs_iter():
                r, i = divmod(rcod, base)
                if i in dset:
                    dset.remove(i)
                elif cur > r:
                    tot += cur - r
                    cur = r
                    dset.add(i)
                    break
                else:
                    f = 1
                    break
            if f: break
            for lcod in ls_iter():
                l, i = divmod(lcod, base)
                l *= -1
                if i in dset:
                    dset.remove(i)
                elif cur < l:
                    tot += l - cur
                    dset.add(i)
                    cur = l
                    break
                else:
                    f = 1
                    break
                if f: break
        tot += abs(cur)
        return tot

    tot2 = complex_game_reverse(dcp(lsc), dcp(rsc))
    print(max(tot1, tot2))

if __name__ == "__main__":
    main()