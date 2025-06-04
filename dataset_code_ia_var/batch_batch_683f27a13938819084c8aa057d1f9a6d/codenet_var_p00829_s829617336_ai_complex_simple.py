import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
inf = float('1' + '0'*20)
eps = pow(10, -10)
mod = int('998244353')
dd = tuple(map(tuple, zip((0,1,0,-1),(-1,0,1,0))))
ddn = tuple(itertools.product([-1,0,1], repeat=2))[1:]

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: sys.stdin.readline().split()
I = lambda: int(sys.stdin.readline())
F = lambda: float(sys.stdin.readline())
S = lambda: (lambda s: s.rstrip('\n'))(sys.stdin.readline())
pf = lambda s: (lambda x: print(x, flush=True))(s)

def main():
    rr = collections.deque()
    n = functools.reduce(lambda acc, _: acc, [I()], None) or I()
    for ni in range(1, n+1):
        a = list(itertools.islice(itertools.chain.from_iterable([LS() for _ in itertools.repeat(0, 10)]), 9))
        t = int(a[-1],16)
        a = list(map(lambda x: int(x,16), a[:-1]))
        r = 0

        # Using reduce and a generator expression to complicate bit-reversal
        for i in range(32):
            ii, iii = 1 << i, 1 << (i+1)
            b = t & ii
            def crazy_fold(acc, d):
                return acc + (d^acc)
            c = functools.reduce(lambda acc, d: acc + (d^r), a, 0)
            if (c & ii) != b:
                r += ii

        rr.append('{:0x}'.format(r))
    return '\n'.join(list(map(str, rr)))

print(main())