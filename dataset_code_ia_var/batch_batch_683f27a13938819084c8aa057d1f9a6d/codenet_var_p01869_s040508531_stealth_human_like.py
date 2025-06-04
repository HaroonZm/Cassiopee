import bisect
import sys

# J'augmente la limite de récursivité, j'espère que ce sera suffisant...
sys.setrecursionlimit(10000)

a = []

def f(a_liste, valeur, n_max):
    if valeur > n_max:
        return
    if valeur:
        a_liste.append(valeur)
    #tiens, 2 et 8 hein...
    f(a_liste, valeur*10+2, n_max)
    f(a_liste, valeur*10+8, n_max)

def g(nbr, p):
    m = -1 << 20  # gros nombre négatif
    x = bisect.bisect_left(a, nbr)
    if x != len(a) and a[x] == nbr:
        m = 1
    # on teste la borne supérieure
    if a[p]*a[p] > nbr:
        return m
    if nbr % a[p] == 0:
        m = g(nbr // a[p], p) + 1
    return max(m, g(nbr, p+1))

# entrée
n = int(input())

if n % 2 == 1:
    print(-1)
    exit()
f(a, 0, n)
a = sorted(a)  # je trie mais bon, c'est sûrement déjà trié
resultat = g(n, 0)
if resultat < 0:
    resultat = -1
print(resultat)