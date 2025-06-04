import sys

def main(N, L, A):
    """
    Détermine s'il est possible de faire une séquence d'opérations de couplage
    d'une liste d'entiers A (longueur N) telle que pour au moins une paire 
    consécutive, la somme des deux éléments soit supérieure ou égale à L.
    Si possible, imprime "Possible" suivi de l'ordre dans lequel effectuer les couplages.
    Sinon, imprime "Impossible".

    Args:
        N (int): Le nombre d'éléments dans la liste A.
        L (int): Le seuil minimum pour la somme de deux éléments consécutifs.
        A (List[int]): La liste des entiers représentant la taille des éléments.

    Returns:
        None. Affiche directement le résultat sur la sortie standard.
    """
    # Cherche la première paire consécutive (A[i], A[i+1]) dont la somme >= L
    for i in range(N - 1):
        if A[i] + A[i + 1] >= L:
            break
    else:
        # Si aucune paire ne satisfait la condition, la tâche est impossible
        print('Impossible')
        return

    print('Possible')

    # Affiche les indices (1-based) à utiliser avant d'atteindre la paire trouvée
    for j in range(N - 1):
        if j == i:
            break
        print(j + 1)

    # Traite les éléments après la paire trouvée en ordre décroissant d'indices
    for j in range(N - 2, -1, -1):
        if j == i:
            break
        print(j + 1)
    
    # Affiche enfin l’indice (1-based) de la paire trouvée, correspondant à l'endroit où 
    # se produira le couplage décisif
    print(i + 1)

if __name__ == '__main__':
    # Utilise la lecture rapide depuis l'entrée standard
    input = sys.stdin.readline
    # Lit N (taille) et L (seuil)
    N, L = map(int, input().split())
    # Lit la liste d'entiers A
    A = list(map(int, input().split()))
    # Appelle la fonction principale avec les paramètres lus
    main(N, L, A)