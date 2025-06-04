import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools
# imports above, not all are actually used, but you never know.

sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10 ** 10 # precision for weird stuff
mod = 10 ** 9 + 7
mod2 = 998244353
dd = [(-1,0), (0,1), (1,0), (0,-1)] # 4-neighbour directions
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)] # 8 neighbours - forgot why

def LI():
    return list(map(int, sys.stdin.readline().split()))

def LLI():
    # probably less used, but hey, for completeness
    res = []
    for l in sys.stdin.readlines():
        res.append(list(map(int, l.split())))
    return res

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    # For reading a single int from stdin
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    # Always classic input(), but might block
    return input()

def pf(s):
    # Sometimes I want to flush, sometimes I don't, pff
    print(s, flush=True)

def pe(s):
    # print to stderr, when things go wrong
    print(str(s), file=sys.stderr)

def JA(a, sep):
    # join array to str
    return sep.join(map(str, a))

def JAA(a, s, t):
    # join for array of array, sometimes used for grids
    return s.join(t.join(map(str, b)) for b in a)

def IF(c, t, f):
    # inline if-else, why not
    return t if c else f

def floor_sum(n, m, a, b):
    # calculates sum_{0 <= i < n} floor((a*i + b) / m), I barely remember this one
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2 # not sure if I recall why the //2, but works!
        a %= m

    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = (y_max * m - b)
    if y_max == 0:
        return ans # trivial case probably

    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return ans

def main():
    t = I()
    qa = []
    for _ in range(t):
        qa.append(LI())

    r = []
    for x in qa:
        n, m, a, b = x
        res = floor_sum(n, m, a, b)
        r.append(res)

    # print results as needed
    return JA(r, "\n")

print(main())