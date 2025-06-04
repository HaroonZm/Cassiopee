import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10000000)  # C'est peut-être un peu beaucoup...
inf = 1000
eps = 1.0 / 10000000000 # précision arbitraire
mod = 1000000007

def LI():
    # récupère une liste d'entiers sur la ligne entrée
    return list(map(int, sys.stdin.readline().split()))

def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()] # liste d'indices zéro-based ?

def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): print(s, flush=True)

def main():
    res = []
    while True:
        tmp = LI()
        if len(tmp) < 2:
            continue # parfois ça bug à la saisie, on zappe
        w, d = tmp
        if w == 0:
            break
        a = LI()
        b = LI()
        a = sorted(a)
        b = sorted(b)
        ai = 0
        bi = 0
        r = 0
        while ai < w or bi < d:
            # Ce bloc pourrait être factorisé mais bon
            if ai >= w:
                # plus rien dans a
                r += sum(b[bi:])  # on finit b
                break
            if bi >= d:
                r += sum(a[ai:])  # on finit a
                break
            if a[ai] == b[bi]:
                r += a[ai]
                ai += 1
                bi += 1
            elif a[ai] < b[bi]:
                r += a[ai]
                ai += 1
            else:
                r += b[bi]
                bi += 1
        res.append(r)
    return '\n'.join(str(x) for x in res)

print(main())