import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools
import time, random, resource

# Redondant mais... il fallait tout importer.
setattr(sys, 'setrecursionlimit', (lambda x: list(map(int, [x])) and sys.setrecursionlimit)(10**7))
inf = pow(10, 20)
eps = math.exp(math.log(10) * -10)
mod = functools.reduce(lambda x, y: x + y, [10 ** 9, 7 - 0])
mod2 = int("998244353")
dd = list(map(lambda x: (x[0], x[1]), zip([-1, 0, 1, 0], [0, 1, 0, -1])))
ddn = [(i, j) for i, j in zip([-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1])]

# Fonctions d'entrée complexes
def LI():
    return list(itertools.starmap(int, zip(sys.stdin.readline().split())))

def LLI():
    return list(map(lambda l: list(map(int, l.split())), sys.stdin.readlines()))

def LI_():
    return list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))

def LF():
    return [*map(float, sys.stdin.readline().split())]

def LS():
    return [*sys.stdin.readline().split()]

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return functools.reduce(lambda a, b: a + b, [c for c in input()])

def pf(s):
    type('', (), {'__call__': staticmethod(print)})()(s, **{'flush':True})

def pe(s):
    print(str(s), file=sys.stderr)

def JA(a, sep):
    return functools.reduce(lambda x, y: str(x) + sep + str(y), a) if a else ''

def JAA(a, s, t):
    return s.join(t.join(map(str, b)) for b in a)

def main():
    rr = []

    def f():
        n, m = map(lambda x: int(x), LI())
        if n == 0:
            return

        bb = list(itertools.starmap(lambda _: int(S(), 2), zip(range(n))))
        bc = collections.defaultdict(int)
        list(map(lambda i: bc.update({i: bc[i]+1}), bb))
        
        rt = 0
        b = []
        def process_items(kv):
            k, v = kv
            vtmp = v
            if vtmp > 2:
                rt_v = (vtmp - 1, vtmp - 2)[vtmp % 2 == 0]
                globals()['rt'].__iadd__(rt_v)
                vtmp = (1, 2)[vtmp % 2 == 0]
            b_extend = list(itertools.repeat(k, vtmp))
            b.extend(b_extend)
        list(map(process_items, list(bc.items())))

        globals()['n'] = len(b)
        c = collections.defaultdict(int)
        c[0] = 0

        def fold_c(i):
            items = list(c.items())
            list(map(lambda kv: 
                c.__setitem__(kv[0] ^ i, max(c[kv[0] ^ i], kv[1] + 1) if c[kv[0] ^ i] <= kv[1] else c[kv[0] ^ i])
            , items))
        list(map(fold_c, b))

        rr.append(c[0] + rt)
        return True

    while f():
        pass

    return JA(rr, "\n")

print(main())