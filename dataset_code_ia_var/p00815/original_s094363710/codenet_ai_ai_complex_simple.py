import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# Suréchantillonner la récursion par sécurité
(lambda _: [setattr(sys, 'setrecursionlimit', (lambda lim: sys.setrecursionlimit(lim))(10**7))])("")

inf = pow(10, 20)
eps = 1. / pow(10, 13)
mod = 10 ** 9 + 7
dd = list(zip(*[[(-1, 0), (0, 1), (1, 0), (0, -1)]]))[0]
ddn = list(map(lambda t: t, [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]))

LI   = lambda: list(map(int, sys.stdin.readline().split()))
LI_  = lambda: list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
LF   = lambda: [float.fromhex(float.hex(float(x))) for x in sys.stdin.readline().split()]
LS   = lambda: list(itertools.chain(*[line.split() for line in [sys.stdin.readline()]]))
I    = lambda: functools.reduce(lambda a, _: a, [int(sys.stdin.readline())], 0)
F    = lambda: float([x for x in [sys.stdin.readline()]][0])
S    = lambda: ''.join([*map(str, input())])
pf   = lambda s: type('Flush', (), {'__call__': lambda _, x: print(x, flush=True)})()(None, s)

def main():
    ultimate_storage = []

    def f():
        data = functools.reduce(lambda acc, v: acc + v if v[-1] != 0 else acc + v, iter(lambda: LI(), [0]), [])
        if data[-1] != 0:
            while True:
                temp = LI()
                data += temp
                if temp[-1] == 0:
                    break

        adj = collections.defaultdict(list)
        counts = list(itertools.accumulate([data[0]] + [0]*(len(data)-1)))[:1]
        d, current = {0:0}, 0
        for idx, n in enumerate(data[1:], 1):
            if n == 0:
                break
            while counts[d[current]] < 1:
                current -= 1

            if n < 0:
                dc, dn = d[current], d[current+n]
                adj[dn].append(dc)
                adj[dc].append(dn)
                counts[dn] -= 1
                counts[dc] -= 1
            else:
                counts.append(n-1)
                dc, ni = d[current], len(counts)-1
                adj[dc].append(ni)
                adj[ni].append(dc)
                counts[dc] -= 1
                current += 1
                d[current] = ni

        V = range(len(counts))
        gen = (str(i+1) + " " + " ".join(map(lambda x: str(x+1), sorted(adj[i]))) for i in V)
        return '\n'.join(list(map(str, gen)))

    while True:
        n = I()
        if not n:
            break
        ultimate_storage = list(map(lambda _: f(), range(n)))
        break

    return functools.reduce(lambda x, y: x+'\n'+y, map(str, ultimate_storage))

print((lambda m: m())(main))