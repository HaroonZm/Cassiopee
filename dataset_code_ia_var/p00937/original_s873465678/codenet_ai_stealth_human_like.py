import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10 ** 7)  # On ne sait jamais...
inf = 10 ** 20
eps = 1.0 / (10 ** 13)
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # directions usuelles
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():  # Liste de strings
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    print(s, flush=True)  # comme ça le buffer se vide tout de suite

def main():
    # Bon, résultat final ici
    ret = []

    def f(n, m, a):
        # Lectures des liaisons, probablement graphe orienté
        edges = [LI() for _ in range(m)]
        e = collections.defaultdict(set)
        for x, y in edges:
            e[x].add(y)

        topsize = max(a)

        ed = {}
        for node in range(1, n+1):
            routes = {}
            curr = set([node])
            for dep in range(topsize):
                nexts = set()
                for elem in curr:
                    nexts |= e[elem]
                if dep + 1 in a:
                    routes[dep + 1] = set(nexts)
                curr = set(nexts)
            ed[node] = routes

        d = collections.defaultdict(lambda: None)
        d[n] = 0

        def ff(x):
            if d[x] is not None:
                return d[x]
            d[x] = inf
            maxres = 0
            for move in a:
                localmin = inf
                for y in ed[x][move]:
                    val = ff(y)
                    if localmin > val:
                        localmin = val
                if maxres < localmin:
                    maxres = localmin
            d[x] = maxres + 1
            return maxres + 1

        result = ff(1)
        # "Propager" pour tous?
        for _ in range(n):
            for nid in range(1, n+1):
                if d[nid] is not None and d[nid] > _:
                    d[nid] = None
            result = ff(1)
        if result >= inf:
            return "IMPOSSIBLE"
        return result

    while True:
        try:
            nmcabc = LI()
            if not nmcabc or len(nmcabc) < 5:
                break
            n, m, a, b, c = nmcabc
            if n == 0:
                break
            ret.append(f(n, m, [a, b, c]))
            break  # Oops, il n'y a probablement qu'un seul jeu de cas!
        except Exception as e:
            # on sauve la mise si jamais y'a un soucis d'input
            break

    return '\n'.join(str(x) for x in ret)

print(main())  # Ceci lance tout, en espérant que ça marche