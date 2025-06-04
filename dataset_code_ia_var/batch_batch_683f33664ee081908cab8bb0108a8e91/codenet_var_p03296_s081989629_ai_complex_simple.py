from functools import reduce
from itertools import groupby, tee, islice, chain
from operator import eq

n = int(input())
a = list(map(int, input().split()))

def pairwise(xs):
    a, b = tee(xs)
    next(b, None)
    return zip(a, b)

def tripletwise(xs):
    a, b, c = tee(xs, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)

def check(i):
    l = a[i-1] if i > 0 else None
    m = a[i]
    r = a[i+1] if i < len(a)-1 else None
    if l is not None and r is not None:
        if l != m and m != r:
            return 2, 0
        elif l == m == r:
            return 2, 1
        elif m == r:
            return 1, 0
        elif l == m:
            return 1, 1
    return 1, 0

indices = iter(range(1, n-1))
acc = [0, 1]
S = [0]

def recursive(i):
    if i >= n-1:
        return
    step, cnt = check(i)
    S[0] += cnt
    recursive(i+step)
recursive(1)

if n > 1 and a[-1] == a[-2]:
    S[0] += 1

print(S[0])