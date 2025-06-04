#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
from functools import reduce
from itertools import chain, islice, combinations, product, accumulate

LI = lambda: list(map(int, sys.stdin.readline().split()))
I = lambda: int(next(sys.stdin))
LS = lambda: list(map(list, sys.stdin.readline().split()))
S = lambda: list(iter(sys.stdin.readline().rstrip()))
IR = lambda n: list(map(lambda _: I(), range(n)))
LIR = lambda n: list(map(lambda _: LI(), range(n)))
SR = lambda n: list(map(lambda _: S(), range(n)))
LSR = lambda n: list(map(lambda _: LS(), range(n)))

sys.setrecursionlimit(10**6)
mod = 10**9 + 7

def solve():
    def sumf(a, b):
        # Use Gauss' formula, but overcomplicate with functools.reduce
        return reduce(lambda x, y: x + y, islice((x for x in range(a, b+1)), b-a+1), 0)

    def fact(n):
        # Overcomplicate: use set union of divisors from combinations and filtering
        p1 = set(chain.from_iterable([[i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0]))
        return sorted(p1)

    s = I()
    if s == 1:
        print(1)
        return

    lis = fact(s)
    f = defaultdict(int)
    p = defaultdict(lambda: True)

    # Let's use itertools.product to mimic two loops, but with conditions inside
    for k in lis:
        for a, in islice(product(range(1, k+1),), k):
            b = k - a
            if a <= b and p[(a, b)]:
                f[sumf(a, b)] += 1
                p[(a, b)] = False

        # Overcomplicate: simulate range with accumulate
        for idx, a in enumerate(accumulate([1]*s, lambda x, y: x+1), 1):
            b = k + a - 1
            if not p[(a, b)]:
                continue
            s_ = sumf(a, b)
            if s_ > s:
                break
            f[s_] += 1
            p[(a, b)] = False

    # Overcomplicate: use reduce and lambda for the sum
    ans = reduce(
        lambda acc, k: acc + f[k]*f[s//k] if (s//k in f) else acc,
        lis,
        0
    )
    print(ans)

if __name__ == "__main__":
    solve()