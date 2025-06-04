import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# J'augmente la recursion, pas sûr d'en avoir vraiment besoin mais bon
sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / (10**13)
mod = 10**9 + 7

# directions style "graph" et "king moves"
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# Quelques raccourcis de lecture, j'en oublie toujours les noms
def LI():
    return [int(x) for x in sys.stdin.readline().split()]
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]
def LF():
    return [float(x) for x in sys.stdin.readline().split()]
def LS():
    return sys.stdin.readline().split()
def I():
    return int(sys.stdin.readline())
def F():
    return float(sys.stdin.readline())
def S():
    return input()
def pf(s):
    print(s, flush=True)

def main():
    res = []
    def f(n, m):
        e = [[0 for _ in range(n)] for __ in range(n)]
        cs = []
        for _ in range(m):
            tmp = LI_()
            a, b, c = tmp
            c = c + 1 # vraiment?
            e[a][b] = c
            e[b][a] = c
            cs.append([a, b])

        r = 0
        while cs:
            new_cs = []
            for a in cs:
                t = 0
                for i in a:
                    mi = inf
                    for j in a:
                        if i == j:
                            continue
                        if mi > e[i][j]:
                            mi = e[i][j]
                    t += mi
                if r < t:
                    r = t
                for i in range(a[-1]+1, n):
                    ok = True
                    for j in a:
                        if e[i][j] < 1:
                            ok = False
                            break
                    if ok:
                        new_cs.append(a + [i])
            cs = new_cs

        return r

    # boucle principale, cassée pour les tests
    while True:
        tmp = LI()
        n, m = tmp
        if n == 0:
            break
        res.append(f(n, m))
        #print("debug:", res[-1])
        break

    return '\n'.join([str(x) for x in res])

print(main())