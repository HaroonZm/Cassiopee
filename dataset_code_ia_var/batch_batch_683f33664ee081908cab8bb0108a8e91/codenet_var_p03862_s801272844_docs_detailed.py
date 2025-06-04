def compute_min_reduction_operations(N, x, A):
    """
    Calcule le nombre minimum d'opérations nécessaires pour réduire la valeur de chaque élément 
    d'une liste transformée B afin qu'aucun élément ne dépasse la valeur x.
    Les opérations consistant à réduire B[i] s'appliquent également à B[i+1] lorsque i < N.
    
    Args:
        N (int): Le nombre d'éléments dans la liste d'entrée A.
        x (int): La valeur maximale autorisée pour chaque élément de la nouvelle liste B.
        A (List[int]): Liste d'entiers de taille N représentant la séquence initiale.
        
    Returns:
        int: Nombre total d'opérations de réduction effectuées.
    """

    # Construction de la liste transformée B à partir de A.
    # B[0] est simplement le premier élément de A.
    B = [A[0]]
    # Pour les indices de 0 à N-2, ajouter la somme des éléments successifs de A.
    for i in range(N - 1):
        B.append(A[i] + A[i + 1])
    # Le dernier élément de B est le dernier élément de A.
    B.append(A[-1])

    # Initialisation du compteur d'opérations de réduction.
    ans = 0

    # Parcours de tous les éléments de B pour s'assurer qu'aucun ne dépasse x.
    for i in range(N + 1):
        # Si la valeur actuelle de B[i] est supérieure à x,
        # il faut la réduire et appliquer le même montant au B[i+1] suivant si besoin.
        if B[i] > x:
            # Quantité à réduire pour atteindre x.
            a = B[i] - x
            ans += a  # Incrémenter le compteur d'opérations.
            B[i] -= a  # Réduire l'élément courant.
            # Réduire également l'élément suivant si nous ne sommes pas à la fin de la liste B.
            if i < N:
                B[i + 1] -= a

    return ans

if __name__ == "__main__":
    # Lecture des entrées utilisateur.
    # N : taille de la liste A, x : valeur max souhaitée
    N, x = map(int, input().split())
    # Liste initiale à traiter
    A = list(map(int, input().split()))
    # Calcul du résultat final en appelant la fonction principale
    print(compute_min_reduction_operations(N, x, A))