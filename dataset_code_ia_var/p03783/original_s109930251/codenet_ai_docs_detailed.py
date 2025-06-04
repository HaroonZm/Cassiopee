def main():
    """
    Lit l'entrée, traite une séquence de paires d'intervalles (l, r), 
    et résout un problème d'agrégation via deux tas à l'aide d'une logique spécifique, 
    en calculant et affichant le résultat final.
    L'algorithme utilise deux heaps pour maintenir la structure d'ensemble de points 
    sous contraintes, et accumule les coûts nécessaires pour synchroniser les bornes.
    """
    import sys
    import heapq

    # Lecture du nombre d'intervalles
    N = int(input())

    # Lecture des paires (l, r) pour chaque intervalle
    P = [list(map(int, input().split())) for _ in range(N)]

    INF = 10 ** 18  # Constante pour représenter l'infini (non utilisé ici mais gardé pour référence)

    # Initialisation de Left heap (L) et Right heap (R)
    # On stocke des valeurs négatives pour simuler un max-heap avec heapq (qui est un min-heap par défaut)
    l0, r0 = P[0]
    L = [-l0 + 1]  # Tas des bornes gauches, valeurs négatives pour max-heap
    R = [l0 - 1]   # Tas des bornes droites

    # s et t représentent les décalages accumulés vers la gauche et vers la droite
    s = t = 0

    res = 0  # Variable pour accumuler le coût total

    # On traite chaque transition entre intervalles consécutifs
    for i in range(N - 1):
        l0, r0 = P[i]
        l1, r1 = P[i + 1]

        # S et t accumulent la variation entre intervalles
        s += (r1 - l1)
        t += (r0 - l0)

        # Cas 1 : le point souhaité est dans la fenêtre contrainte autorisée
        if -s - L[0] <= l1 - 1 <= t + R[0]:
            heapq.heappush(L, -l1 + 1 - s)
            heapq.heappush(R, l1 - 1 - t)
        
        # Cas 2 : le point souhaité est trop à gauche, il faut le déplacer
        elif l1 - 1 < -s - L[0]:
            heapq.heappush(L, -l1 + 1 - s)
            heapq.heappush(L, -l1 + 1 - s)
            p = -heapq.heappop(L) - s
            heapq.heappush(R, p - t)
            res += (p - (l1 - 1))  # On accumule le coût de déplacement
        
        # Cas 3 : le point souhaité est trop à droite, il faut le déplacer
        elif t + R[0] < l1 - 1:
            heapq.heappush(R, l1 - 1 - t)
            heapq.heappush(R, l1 - 1 - t)
            p = heapq.heappop(R) + t
            heapq.heappush(L, -p - s)
            res += (l1 - 1 - p)   # On accumule le coût de déplacement

    # Affichage du résultat final
    print(res)


if __name__ == "__main__":
    main()