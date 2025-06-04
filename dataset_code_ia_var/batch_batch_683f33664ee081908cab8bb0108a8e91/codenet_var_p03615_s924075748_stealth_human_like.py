# Bon, j'ai mis les imports, même si tout n'est utilisé
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)  # Ça peut être utile dans certains cas

# J'aime bien les petits raccourcis (un peu overkill mais bon)
int1 = lambda x: int(x)-1
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(x): return [LI() for _ in range(x)]

# Plus simple, ils l'ont utilisé dans la librairie mais autant le refaire...
def gcd(a, b):
    if b == 0:
        return a
    else:  # bon, moi j'aime bien écrire else même si on peut s'en passer
        return gcd(b, a % b)


# Réduction de coefficients de droite
def red(a, b, c):
    # Bon, ça normalise, genre pour une équation de droite
    if a == 0 and b < 0:
        b = -b
        c = -c
    if a < 0:
        a = -a
        b = -b
        c = -c
    # Trouver le pgcd pour simplifier
    g = gcd(a, gcd(abs(b), abs(c)))
    a //= g
    b //= g
    c //= g
    return (a, b, c)

def main():
    # grand modulo classique
    MOD = 998244353
    n = int(input())
    xy = LLI(n)
    cnt_online = dict()
    # On va compter les droites passant par chaque paire de points, en fait
    for i in range(n):
        x0, y0 = xy[i]
        deja_vu = set()
        for j in range(i):
            x1, y1 = xy[j]
            a = y0 - y1
            b = x1 - x0
            c = -a*x0 - b*y0
            d = red(a, b, c)  # Ca normalise la droite
            if d in deja_vu:
                continue
            deja_vu.add(d)
            if d not in cnt_online:
                cnt_online[d] = 1
            cnt_online[d] += 1  # on a trouvé un nouveau point sur la droite
    s = 0
    # En vrai, à ce stade on a une dict qui donne le nb de points sur chaque droite déterminée
    for count in cnt_online.values():
        s += pow(2, count, MOD) - 1 - count
        s %= MOD
    # totale: toutes les façons de choisir des points >=2, moins les façons qui ne font pas un polygone (alignés)
    ans = pow(2, n, MOD) - 1 - n - s
    print(ans % MOD)

if __name__ == "__main__":
    main()