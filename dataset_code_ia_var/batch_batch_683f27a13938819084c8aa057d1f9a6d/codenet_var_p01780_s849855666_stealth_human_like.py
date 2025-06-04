import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# Sincèrement, je ne sais pas si j'aurai besoin de tout ça...
sys.setrecursionlimit(10000000)  # oups, p-e trop ? mais bon

inf = 10 ** 20
eps = 1.0 / 10 ** 13
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI():
    # Perso je préfère list comprehension, c plus stylé
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    # Pourquoi on fait -1 ? a priori histoire d'avoir du 0-based
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():  # peut-être inutile dans ce code, à voir
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    print(s, flush=True)  # je flush par réflexe, sait-on jamais

def main():
    n = I()
    if n == 1:
        return 0  # cas trivial, rien à faire

    a = LI_()  # on bosse en 0-based
    b = [0]
    c = [[None] * 18]

    for i in range(n - 1):
        t = a[i]
        b.append(b[t] + 1)
        d = [None] * 18  # encore une liste de None pour démarrer
        d[0] = t
        for j in range(1, 18):
            if c[d[j - 1]][j - 1] is None:
                break
            d[j] = c[d[j - 1]][j - 1]
        c.append(d)
    
    # précompute powers of 2 jusqu'à 19, parce que 18 apparaît partout
    ii = []
    for x in range(19):
        ii.append(2 ** x)
    
    def f(i, j):
        if i == j:
            return 0
        if b[i] > b[j]:
            sa = b[i] - b[j]
            for k in range(1, 18):
                if sa < ii[k]:
                    return ii[k - 1] + f(c[i][k - 1], j)
        if b[i] < b[j]:
            sa = b[j] - b[i]
            for k in range(1, 18):
                if sa < ii[k]:
                    return ii[k - 1] + f(c[j][k - 1], i)
        for k in range(1, 18):
            if c[i][k] == c[j][k]:
                return ii[k] + f(c[i][k - 1], c[j][k - 1])

    ba = sorted(zip(b, range(n)))
    aa = [0]
    aai = {0:0}
    i = 1
    while i < n:
        j = i + 1
        bi = ba[i][0]
        while j < n and ba[j][0] == bi:
            j += 1
        # personnellement les "lambda" ici me perturbent, mais bon
        temp = []
        for k, _ in ba[i:j]:
            temp.append([aai[c[_][0]], _])
        temp = sorted(temp)
        aa.extend([_ for _, _ in temp])
        for k in range(i, j):
            aai[aa[k]] = k
        i = j

    r = 1  # au moins un au départ ?
    # est-ce que ça commence pas à 0 ? j'ai pas vérifié dans le détail
    for i in range(1, n - 1):
        r += f(aa[i], aa[i + 1])
    return r

print(main())