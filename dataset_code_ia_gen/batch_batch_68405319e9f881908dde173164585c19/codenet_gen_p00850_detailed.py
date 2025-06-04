# Programme pour calculer le nombre minimal d'opérations (multiplications/divisions)
# nécessaires pour calculer x^n à partir de x, en commençant à x (puissance 1).
# Opérations autorisées: multiplication et division entre nombres de la forme x^k
# avec k positif. On évite donc tout résultat intermédiaire avec exposant <= 0.
# Entrée: suite d'entiers n (1 <= n <= 1000), terminée par 0.
# Sortie: nombre minimal d'opérations pour chaque n.

import sys
from collections import deque

def minimal_operations(n_max):
    """
    Calcule le nombre minimal d'opérations pour tous n de 1 à n_max.
    Utilisation d'une recherche en largeur (BFS) sur les puissances atteignables.
    Chaque état est un exposant positif k (1 <= k <= 2*n_max) pour gérer les divisions.
    On commence par k=1 avec 0 opérations.

    A chaque étape, on peut combiner deux exposants déjà atteints (p, q) par multiplication:
        k = p + q
    Ou par division:
        k = p - q si k > 0
    On évite les exposants non positifs (car résultats doivent être x^k avec k>0).
    L'exploration est faite jusqu'à couvrir au moins 1..n_max.

    Renvoie une liste distance tel que distance[i] = minimal opérations pour x^i.
    """
    limit = 2 * n_max  # bornes pour éviter d'explorer trop loin
    dist = [float('inf')] * (limit + 1)
    dist[1] = 0  # x^1 est donné, 0 opérations

    # Pour accélérer, on stocke la liste des exposants déjà découverts
    known = [1]

    # Queue pour BFS: on traite les exposants découverts
    queue = deque([1])

    while queue:
        k = queue.popleft()
        # Pour chaque paire (k, m) où m est un exposant connu, tentons multiplication/division
        for m in known:
            nmul = k + m  # multiplication : exposant somme
            if nmul <= limit and dist[nmul] > dist[k] + 1:
                dist[nmul] = dist[k] + 1
                queue.append(nmul)
                known.append(nmul)
            ndiv = k - m  # division : exposant différence
            if ndiv > 0 and dist[ndiv] > dist[k] + 1:
                dist[ndiv] = dist[k] + 1
                queue.append(ndiv)
                known.append(ndiv)
    return dist

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    nums = [int(line) for line in input_lines]

    max_n = max(nums)
    if max_n == 0:
        return

    dist = minimal_operations(max_n)
    for n in nums:
        if n == 0:
            break
        # Affiche le résultat minimal pour chaque n
        print(dist[n])

if __name__ == "__main__":
    main()