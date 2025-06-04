import sys
import math
from collections import deque, defaultdict, Counter
from itertools import accumulate, combinations, permutations, product
from heapq import heappush, heappop
from functools import reduce, lru_cache
from decimal import Decimal
from operator import itemgetter

sys.setrecursionlimit(10**7)

input = lambda: sys.stdin.readline().rstrip('\n')

def printe(*args): print("##", *args, file=sys.stderr)
def printl(li): print(*li, sep="\n") if li else None

def argsort(seq, return_sorted=False):
    inds = sorted(range(len(seq)), key=seq.__getitem__)
    if return_sorted:
        return inds, [seq[i] for i in inds]
    return inds

alp2num = lambda c, cap=False: ord(c) - (65 if cap else 97)
num2alp = lambda i, cap=False: chr(i + (65 if cap else 97))

def matmat(A, B):
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

def matvec(M, v):
    return [sum(m * v_i for m, v_i in zip(M_row, v)) for M_row in M]

def T(M):
    return [list(col) for col in zip(*M)]

binr = lambda x: format(x, 'b')

def bitcount(x):
    x -= (x >> 1) & 0x5555555555555555
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x += x >> 8
    x += x >> 16
    x += x >> 32
    return x & 0x7f

def solve_intervals(S, N, base):
    import heapq
    # Use negative for max-heap effect with heapq
    ls = [-l * base + i for i, (l, r) in enumerate(S)]
    rs = [r * base + i for i, (l, r) in enumerate(S)]
    heapq.heapify(ls)
    heapq.heapify(rs)

    dset = set()
    cur = 0
    tot = 0
    f = False
    # use fast local variable aliasing
    heappop = heapq.heappop
    while ls and rs:
        while ls:
            l, i = divmod(heappop(ls), base)
            l = -l
            if i in dset:
                dset.remove(i)
            elif cur < l:
                tot += l - cur
                dset.add(i)
                cur = l
                break
            else:
                f = True
                break
        if f:
            break
        while rs:
            r, i = divmod(heappop(rs), base)
            if i in dset:
                dset.remove(i)
            elif cur > r:
                tot += cur - r
                cur = r
                dset.add(i)
                break
            else:
                f = True
                break
        if f:
            break
    tot += abs(cur)
    return tot

def main():
    MOD = 10**9 + 7
    N = int(input())
    S = [tuple(map(int, input().split())) for _ in range(N)]
    base = N

    # Prebuild heaps (copy avoided by fresh recomputation)
    tot1 = solve_intervals(S, N, base)
    # For reversed initial order, swap l/r in the logic:
    S_rev = [(l, r) for l, r in S]
    # Simply swap the while loop order
    def solve_reverse(S, N, base):
        import heapq
        ls = [-l * base + i for i, (l, r) in enumerate(S)]
        rs = [r * base + i for i, (l, r) in enumerate(S)]
        heapq.heapify(ls)
        heapq.heapify(rs)

        dset = set()
        cur = 0
        tot = 0
        f = False
        heappop = heapq.heappop
        while ls and rs:
            while rs:
                r, i = divmod(heappop(rs), base)
                if i in dset:
                    dset.remove(i)
                elif cur > r:
                    tot += cur - r
                    cur = r
                    dset.add(i)
                    break
                else:
                    f = True
                    break
            if f:
                break
            while ls:
                l, i = divmod(heappop(ls), base)
                l = -l
                if i in dset:
                    dset.remove(i)
                elif cur < l:
                    tot += l - cur
                    dset.add(i)
                    cur = l
                    break
                else:
                    f = True
                    break
            if f:
                break
        tot += abs(cur)
        return tot

    tot2 = solve_reverse(S, N, base)

    print(max(tot1, tot2))

if __name__ == "__main__":
    main()