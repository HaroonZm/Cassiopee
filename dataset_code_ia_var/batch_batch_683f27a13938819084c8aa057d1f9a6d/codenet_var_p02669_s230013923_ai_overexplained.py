import sys  # Importe le module système pour manipuler certains aspects du système d'exécution Python
INF = 1 << 60  # Définition d'une très grande valeur (équivalent à l'infini pour cette utilisation) en décalant 1 de 60 bits à gauche (équivalent à 2^60)
MOD = 10**9 + 7  # Définition d'un modulo souvent utilisé dans les compétitions, ici 1000000007
# MOD = 998244353  # Une autre valeur de modulo courante, commentée ici au cas où
sys.setrecursionlimit(2147483647)  # Change la limite maximale de récursion à une très grande valeur (2^31-1), évite les erreurs de récursion profonde
input = lambda:sys.stdin.readline().rstrip()  # Redéfinit la fonction 'input' pour lire une ligne de l'entrée standard sans le saut de ligne à la fin
from functools import lru_cache  # Importe l'outil lru_cache pour mémoïser les appels de fonction et optimiser la récursion

def resolve():  # Définition de la fonction principale qui encapsule toute la logique du programme
    for _ in range(int(input())):  # Boucle sur le nombre de tests à traiter, convertit la première entrée en entier
        # Lecture de 5 entiers sur une ligne, les valeurs sont séparées par des espaces
        n, a, b, c, d = map(int, input().split())

        # Définition de la fonction DFS (Depth First Search) avec mémoïsation pour ne pas recalculer les mêmes états
        @lru_cache(None)  # On active la mémoire cache sans limiter le nombre d'éléments stockés
        def dfs(k):
            # Cas de base : si k vaut 0 (c'est-à-dire qu'il n'y a plus rien à traiter)
            if k == 0:
                return 0  # Aucun coût car il n'y a rien à faire
            # Cas de base : si k vaut 1 (cas minimal significatif)
            if k == 1:
                return d  # Le coût pour traiter un élément est 'd'

            # Au début, on initialise la variable 'res' au coût de traiter chaque unité individuellement (c'est la solution naïve)
            res = k * d

            # On itère sur chaque opération possible : division par 2, 3 ou 5 avec leur coût respectif a, b ou c
            for p, cost in zip([2, 3, 5], [a, b, c]):
                # On divise k par p pour obtenir le quotient q et le reste r
                q, r = divmod(k, p)
                # Si k est divisible par p (reste 'r' égal à 0)
                if r == 0:
                    # On compare et garde le minimum : coût de diviser + coût récursif
                    res = min(res, dfs(q) + cost)
                else:
                    # Si k n'est PAS divisible par p, il y a deux possibilités :
                    # 1. On diminue k jusqu'au multiple inférieur de p (donc on enlève r éléments : coût r*d)
                    #    puis on applique l'opération et on continue récursivement
                    res = min(res, dfs(q) + cost + d * r)
                    # 2. On augmente k jusqu'au multiple supérieur de p (ajouter p-r éléments : coût (p - r)*d)
                    #    puis on applique l'opération et on continue récursivement
                    res = min(res, dfs(q + 1) + cost + d * (p - r))
            # Après avoir testé toutes les possibilités, on retourne le coût minimal trouvé
            return res

        # On affiche la réponse pour cette instance (valeur minimale calculée par dfs)
        print(dfs(n))

# Appel de la fonction principale pour démarrer le traitement
resolve()