import sys
sys.setrecursionlimit(10**7)

def mex(s):
    m = 0
    while m in s:
        m += 1
    return m

import math

def grundy(n, m):
    # Calcul du Grundy number de la pile avec n biscuits et capacité m
    # Etats sont les nombres entre n et m
    # Deux opérations possibles: +1 (si <= m), *2 (si <= m)
    # Nous calculons de manière récursive les grundies
    # Optimisation: on utilise une DP avec mémo
    
    # Ici on utilise une approche itérative et cache
    
    stack = []
    cache = {}
    def dfs(x):
        if x > m:
            return 0
        if x == m:
            return 0
        if x in cache:
            return cache[x]
        s = set()
        if x+1 <= m:
            s.add(dfs(x+1))
        if x*2 <= m:
            s.add(dfs(x*2))
        g = mex(s)
        cache[x] = g
        return g
    return dfs(n)

input = sys.stdin.readline
K = int(input())
n_m = [tuple(map(int,input().split())) for _ in range(K)]

# Il y a 10^5 poches, m peut aller jusqu'à 10^18, calcul direct impossible.
# On remarque que les transformations ( +1 ou *2 ) forment un DAG d'états.
# Ce problème est connu et la valeur de grundy peut être calculée en trouvant le distance vers m en mouvements +1 ou *2 inverses (car l'analyse est équivalente).
# Une autre méthode reconnue est de remarquer que la pile se réduit en un game équivalent de pile de bijection.
# En fait, on peut calculer la distance minimale pour aller de n à m avec ces opérations. Puis, la grundy number correspond à la distance modulo something?
# Plus rigoureusement, d'après la théorie du jeu "Double or Increment", la grundy number est égale à la distance de n à m, où la distance est le nombre minimum d'opérations pour atteindre m depuis n.
# Cependant, ici l'état est le nombre de biscuits. L'ensemble des mouvements est +1 et *2, on peut calculer la distance minimum vers m.
# La grundy number est alors la "distance minimale" entre n et m sous ces opérations.
# On calcule la distance minimale de n vers m en BFS inversé (de m vers n) en opérations inverses:
#    opérations inverses: -1 (si > n), ou /2 (si divisible par 2)
# On calcule cette distance pour chaque poche.
# Le XOR des distances donne le résultat final.

from collections import deque

def dist_min(n,m):
    # calcule distance min de n à m en utilisant steps +1 et *2, c'est équivalent à distance min inverse de m à n avec -1 et /2 (si divisible)
    # n <= m
    visited = set()
    queue = deque()
    queue.append((m,0))
    visited.add(m)
    while queue:
        x,d = queue.popleft()
        if x == n:
            return d
        # on explore les états parents
        if x-1 >= n and (x-1) not in visited:
            visited.add(x-1)
            queue.append((x-1,d+1))
        if x%2 == 0 and (x//2) >= n and (x//2) not in visited:
            visited.add(x//2)
            queue.append((x//2,d+1))
    return 0  # pas possible théoriquement

xor_sum = 0
for n,m in n_m:
    d = 0
    # Pour éviter la queue trop grande car m peut être 10^18, BFS n'est pas faisable classique
    # On implémente une version optimisée :
    # la distance peut être calculée de façon récursive :
    # distance(n,m):
    # if n==m: return 0
    # si m < n return inf (pas possible)
    # sinon:
    # si m < 2*n:
    #   distance = m - n (increments only)
    # sinon:
    #   si m pair:
    #       distance = 1 + min(distance(n, m-1), distance(n, m//2))
    #   sinon:
    #       distance = 1 + distance(n, m-1)
    #
    # On peut mémoriser le résultat avec un dict pour éviter recréation
    
    memo = {}
    def f(n,m):
        if m == n:
            return 0
        if m < n:
            return 10**18
        if (n,m) in memo:
            return memo[(n,m)]
        if m < 2*n:
            memo[(n,m)] = m - n
            return memo[(n,m)]
        if m % 2 ==0:
            memo[(n,m)] = 1 + min(f(n,m-1), f(n,m//2))
            return memo[(n,m)]
        else:
            memo[(n,m)] = 1 + f(n,m-1)
            return memo[(n,m)]
    d = f(n,m)
    xor_sum ^= d

print("mo3tthi" if xor_sum != 0 else "tubuann")