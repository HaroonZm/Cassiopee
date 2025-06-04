import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# Bon, je mets la limite haute, "au cas où"
sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7

# Directions (carrées et diagonales, on ne sait jamais)
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Les raccourcis d'input qui me font gagner 3 secondes (en fait, j’hésite à garder tout)
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()    # Pas utilisé je crois ici
def pf(s): return print(s, flush=True) # bon, mais pf vraiment ?

def main():
    results = []

    # Alors ça, c'est le cœur du problème
    def fight(n):
        h = []
        for _ in range(n):    # les HP
            h.append(I())
        highest = max(h)
        m = I()
        ms = []
        ma = []
        zero_flag = False
        for _ in range(m):
            stuff = LS()
            # bon, je rale : pas de décomposition idiot proof là-dessus, ça peut planter si pas le bon input
            nama, mp, target, damage = stuff
            mp = int(mp)
            damage = int(damage)
            if damage == 0:
                continue  # lol, pas besoin d'attaque qui tape rien
            if mp == 0:
                zero_flag = True
                continue  # gratos? On gagne
            if target == 'All':
                ma.append((mp, damage))
            else:
                ms.append((mp, damage))

        if zero_flag:  # si gratos qui tape
            return 0

        # Pour chaque monstre, dp sur les dégâts maximaux atteignables
        ds = [inf] * (highest+1)
        ds[0] = 0

        # Les spells single
        for mp, dmg in ms:
            for i in range(dmg, highest+1):
                if ds[i] > mp + ds[i-dmg]:
                    ds[i] = mp + ds[i-dmg]
            if dmg < 2:
                continue
            t = min(ds[-dmg+1:]) # bon, j’espère que l'indice colle
            if ds[-1] > t + mp:
                ds[-1] = t + mp

        # Pour attaque de zone (tous les monstres)
        da = [inf] * (highest+1)
        da[0] = 0
        for mp, dmg in ma:
            for i in range(dmg, highest+1):
                if da[i] > mp + da[i-dmg]:
                    da[i] = mp + da[i-dmg]
            if dmg < 2:
                continue
            t = min(da[-dmg+1:])
            if da[-1] > t + mp:
                da[-1] = t + mp

        # Un genre de "descente": on force que chaque case est la meilleure possible ou mieux
        for i in range(highest-1, -1, -1):
            if ds[i] > ds[i+1]:
                ds[i] = ds[i+1]
            if da[i] > da[i+1]:
                da[i] = da[i+1]

        min_total = result = inf
        for i in range(highest, -1, -1):
            if min_total <= da[i]:
                continue
            min_total = temp = da[i]
            for hi in h:
                if hi > i:
                    temp += ds[hi-i]
            if result > temp:
                result = temp
        return result

    # Loop principal qui lit tous les cas
    while True:
        n = I()
        if n == 0:
            break
        results.append(fight(n))

    # Je retourne au lieu d’imprimer dans le main (c’est discutable, mais bon)
    return "\n".join(map(str, results))

print(main())