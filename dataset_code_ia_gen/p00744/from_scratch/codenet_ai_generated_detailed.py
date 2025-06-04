import sys
import math
import threading

# Fonction pour factoriser un nombre en ses facteurs premiers (avec optimisation basique)
def prime_factors(n):
    factors = set()
    # Diviser par 2 autant que possible
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    # Diviser par les impairs
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.add(f)
            n //= f
        f += 2
    # Si reste >1 c'est un facteur premier
    if n > 1:
        factors.add(n)
    return factors

# Recherche augmentante pour trouver un couplage maximum dans un graphe bipartite
def try_match(u, adj, visited, matchR):
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            if matchR[v] == -1 or try_match(matchR[v], adj, visited, matchR):
                matchR[v] = u
                return True
    return False

def main():
    input_iter = iter(sys.stdin.read().split())
    while True:
        # Lecture des nombres de cartes bleues et rouges
        m = int(next(input_iter))
        n = int(next(input_iter))
        if m == 0 and n == 0:
            break

        blue_cards = [int(next(input_iter)) for _ in range(m)]
        red_cards = [int(next(input_iter)) for _ in range(n)]

        # On va construire un graphe bipartite où:
        # Chaque bleu est un noeud à gauche (0..m-1)
        # Chaque rouge est un noeud à droite (0..n-1)
        # Il y a une arête entre bleu i et rouge j si gcd(blue_cards[i], red_cards[j]) > 1

        # Pour accélérer, on peut pré-calculer les facteurs premiers de toutes cartes
        # Ensuite on peut comparer intersections de facteurs premiers pour décider de tester gcd
        # Mais de base on va faire un test gcd direct (possible car m,n <= 500, donc max 250000 tests)
        # Cela reste raisonnable.

        adj = [[] for _ in range(m)]
        for i in range(m):
            bi = blue_cards[i]
            for j in range(n):
                rj = red_cards[j]
                # Si gcd > 1 alors on peut connecter
                # math.gcd est efficace en python 3.5+
                if math.gcd(bi, rj) > 1:
                    adj[i].append(j)

        # Maintenant on cherche le couplage maximum pour optimiser le nombre de paires
        # Algorithme classique de matching bipartite: Recherche augmentante (Hungarian / Kuhn)

        matchR = [-1] * n  # match pour rouge j : indice du bleu i associé (-1 si aucun)

        result = 0
        for u in range(m):
            visited = [False] * n
            if try_match(u, adj, visited, matchR):
                result += 1

        print(result)

# Pour éviter RecursionError sur certains systèmes à cause de profondeur de récursion dans DFS de matching
sys.setrecursionlimit(10**7)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()