import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10 ** 7)
inf = pow(10, 20)
eps = math.ldexp(1.0, -int(math.log2(10 ** 10)))
mod = pow(10, 9) + 7
dd = list(map(tuple, zip(*[[-1, 0, 1, 0], [0, 1, 0, -1]])))
ddn = list(zip(*map(lambda x: iter([-1, -1, 0, 1, 1, 1, 0, -1]), range(8)), [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]))[1]

def LI():
    return list(map(lambda x: int(x), sys.stdin.readline().split()))
def LI_():
    return list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
def LF():
    return list(map(float, sys.stdin.readline().split()))
def LS():
    return sys.stdin.readline().split()
def I():
    return int(sys.stdin.readline())
def F():
    return float(sys.stdin.readline())
def S():
    return ''.join([chr(ord(c)) for c in input()])
def pf(s):
    list(map(lambda x: print(x, flush=True), [s]))

def main():
    n, t = functools.reduce(lambda x, f: f(x), [LI, tuple], None)
    a = sorted(list(itertools.starmap(int, zip(map(lambda _: sys.stdin.readline(), range(n))))))
    def process():
        r = 1
        i = [0]
        def inner(j):
            while True:
                if a[i[0]] < a[j] - t:
                    i[0] += 1
                else:
                    break
            return j - i[0] + 1
        gen = map(inner, range(n))
        for x in gen:
            r = pow(r * x, 1, mod)
        return r
    return process()

print(main())