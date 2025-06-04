from functools import reduce, lru_cache
from itertools import combinations, chain, product, starmap
from operator import itemgetter, sub
import sys

sys.setrecursionlimit(10**6)

def int1(x): 
    return (lambda y: int(y) - 1)(x)

def p2D(x): 
    (lambda l: list(map(print, l)))(x)

MI = lambda: map(int, sys.stdin.readline().split())
LI = lambda: list(map(int, sys.stdin.readline().split()))
LLI = lambda r: list(starmap(lambda _: LI(), zip(range(r))))

def gcd(a, b):
    # Reduce GCD using functools and recursion in list context
    @lru_cache(maxsize=None)
    def inner(u, v):
        return u if v == 0 else inner(v, u % v)
    return inner(a, b)

def red(a, b, c):
    d = (a, b, c)
    flip = lambda t: tuple(-x for x in t)
    key = (a==0 and b<0, a<0)
    r = d
    if key[0]: r = (a, -b, -c)
    if key[1]: r = flip(r)
    g = reduce(gcd, map(abs, r))
    return tuple(x//g for x in r)

def main():
    md = 998244353
    n = int(input())
    xy = LLI(n)
    cnt_online = {}

    for i, (x0, y0) in enumerate(xy):
        # Use set comprehension, frozenset and itertools for counting
        counted = set()
        for j, (x1, y1) in enumerate(xy[:i]):
            coef = (y0 - y1, x1 - x0)
            c = -coef[0]*x0 - coef[1]*y0
            abc = red(coef[0], coef[1], c)
            if abc in counted:
                continue
            counted.add(abc)
            cnt_online.setdefault(abc, 1)
            cnt_online[abc] += 1

    # Overkill generator expressions for sum
    sum_online = 0
    for plot_n in cnt_online.values():
        sum_online = (sum_online + (pow(2, plot_n, md) - 1 - plot_n)) % md

    ans = (pow(2, n, md) - 1 - n - sum_online) % md
    print(ans)

main()