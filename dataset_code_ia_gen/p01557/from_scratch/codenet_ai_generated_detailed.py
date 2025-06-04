from collections import deque

def reverse_sort_min_operations(N, A):
    """
    Cette fonction calcule le nombre minimum d'opérations 'reverse(i, j)'
    nécessaires pour trier la permutation A en ordre croissant.
    Chaque opération consiste à inverser un segment contigu de la liste.

    Approche :
    - On modélise l'état par la permutation actuelle.
    - On utilise une recherche en largeur (BFS) pour explorer tous les états
      accessibles en appliquant une seule opération de reverse sur i,j.
    - On stocke les états déjà visités pour éviter des calculs redondants.
    - Quand on atteint la permutation triée, on renvoie le nombre d'opérations.

    Complexité :
    - N ≤ 10, donc au pire 10! ≈ 3.6 millions d'états, ce qui est faisable en BFS
      avec pruning et représentation efficace.
    """

    # L'état final trié
    target = tuple(sorted(A))
    start = tuple(A)

    # Si déjà trié, pas d'opérations nécessaires
    if start == target:
        return 0

    # Queue pour BFS, stocke tuple (état actuel, nombre d'opérations)
    queue = deque()
    queue.append((start, 0))

    # Ensemble pour mémoriser états visités
    visited = set()
    visited.add(start)

    while queue:
        current, steps = queue.popleft()
        # On génère tous les états obtenus en inversant tous segments possibles
        for i in range(N):
            for j in range(i, N):
                # inverser segment [i, j]
                new_lst = list(current)
                new_lst[i:j+1] = reversed(new_lst[i:j+1])
                new_state = tuple(new_lst)
                if new_state == target:
                    # On a trouvé l'état trié
                    return steps + 1
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
    # Théoriquement on ne devrait jamais atteindre ce point
    return -1

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    res = reverse_sort_min_operations(N, A)
    print(res)