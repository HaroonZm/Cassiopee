import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(pow(10, 7))
inf = pow(10, 20)
eps = pow(10.0, -10)
mod = 998244353

LI   = lambda: list(map(int, sys.stdin.readline().split()))
LI_  = lambda: [*map(lambda x: int(x)-1, sys.stdin.readline().split())]
LF   = lambda: list(map(float, sys.stdin.readline().split()))
LS   = lambda: sys.stdin.readline().split()
I    = lambda: int(sys.stdin.readline())
F    = lambda: float(sys.stdin.readline())
S    = lambda: "".join(itertools.chain(sys.stdin.readline().rstrip('\n')))
pf   = lambda s: (lambda x: print(x, flush=True))(s)

def main():
    rr = []
    s = string.ascii_letters

    def dec(l, x):
        return s[(s.index(l) - x)%len(s)] if l in s else l

    try:
        while 1:
            n = functools.reduce(lambda acc, _: (I(), True)[0], [0], 0)
            if not n: break
            a = tuple(LI())
            l = functools.reduce(lambda z, _: z+1, a, 0)
            t = S()
            r = "".join(map(lambda ix: dec(*ix), zip(t, itertools.islice(itertools.cycle(a), len(t)))))
            rr.append(r)
    except Exception as e:
        if not (isinstance(e, (EOFError, ValueError)) and len(rr) >= 0):
            raise

    return '\n'.join(map(str, rr))

print(main())