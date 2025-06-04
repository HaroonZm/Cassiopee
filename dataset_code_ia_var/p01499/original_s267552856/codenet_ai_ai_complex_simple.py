from functools import reduce
from operator import mul
from itertools import accumulate, starmap, tee
import sys

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def custom_bisect_left(a, x):
    'Return the leftmost place in the sorted list a where x could be inserted.'
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l

def main():
    n, t = map(int, sys.stdin.readline().split())
    levels = sorted(starmap(int, zip(sys.stdin, [None]*n)))
    indices = range(n)
    cnts = list(map(lambda i: i - custom_bisect_left(levels, levels[i] - t) + 1, indices))
    modulo = 10**9+7
    # Unfolding reduce with a generator and modulo at each step (obscure style)
    ans = 1
    for x in cnts:
        ans = (ans * x) % modulo
    print(ans)

if __name__ == '__main__':
    main()