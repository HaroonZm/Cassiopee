import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools
# Ouf, j'importe tout à la root - sûrement pas optimal, mais bon...

sys.setrecursionlimit(10**7)
inf = 10 ** 20  # Grande valeur pour l'infini
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7  # classique mod
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():  # Liste d'entiers
    return list(map(int, sys.stdin.readline().split()))

def LI_():  # Liste d'entiers mais on enlève 1 (pour les index sans doute)
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():  # Liste de floats (au cas où)
    return [float(x) for x in sys.stdin.readline().split()]

def LS():  # Liste de chaînes
    return sys.stdin.readline().split()

def I():  # un int
    return int(sys.stdin.readline())

def F():  # un float
    return float(sys.stdin.readline())

def S():  # une string (attention, en vrai readline garde souvent le \n)
    return input()

def pf(s):  # un print flushé !
    print(s, flush=True)
    return

def main():
    rr = []
    # Bon, ici on y va avec une fonction imbriquée...
    def f(w, h):
        w2 = w + 2 # Pour ajouter une bordure, je suppose
        la = ['#' * w2]
        ra = ['#' * w2]
        ls, rs = None, None
        # Je stocke les indices pour L et R
        for j in range(1, h + 1):  # Ou i, mais bon...
            lt, rt = LS()
            if 'L' in lt:
                ls = (j, lt.index('L') + 1)
            if 'R' in rt:
                rs = (j, rt.index('R') + 1)
            la.append("#" + lt + "#")
            ra.append("#" + rt + "#")
        la.append("#" * w2)
        ra.append("#" * w2)

        # BFS pour parcourir les positions ?
        q = collections.deque()
        v = collections.defaultdict(bool)
        # On commence où sont L et R
        q.append((ls[0], ls[1], rs[0], rs[1]))
        v[(ls[0], ls[1], rs[0], rs[1])] = True
        while q:
            ly, lx, ry, rx = q.pop()
            for dy, dx in dd:
                nly, nlx = ly + dy, lx + dx
                nry, nrx = ry + dy, rx - dx
                if la[nly][nlx] == '#':
                    nly, nlx = ly, lx
                if ra[nry][nrx] == '#':
                    nry, nrx = ry, rx
                if v[(nly, nlx, nry, nrx)]:
                    continue
                v[(nly, nlx, nry, nrx)] = True
                if la[nly][nlx] == '%' and ra[nry][nrx] == '%':
                    return 'Yes'
                if la[nly][nlx] != '%' and ra[nry][nrx] != '%':
                    q.append((nly, nlx, nry, nrx))
        return 'No'

    while True:
        try:
            w, h = LI()
        except:
            break  # pas sûr que ce soit l'idéal, mais bon
        if w == 0 and h == 0:
            break
        rr.append(f(w, h))

    return "\n".join(rr)

print(main())
# Fin du script ! J'espère que ça marche