def count_subarrays_with_unique_sum_xor(N, A):
    """
    Compte le nombre de sous-tableaux dans un tableau A de longueur N tels que,
    pour tout i <= l <= r < N, la somme des éléments de A[l:r+1] est égale à 
    leur opération XOR bit-à-bit.

    C'est équivalent à compter le nombre de sous-plages où aucun bit ne se répète.
    
    Args:
        N (int): La longueur du tableau.
        A (list of int): La liste des entiers à traiter.

    Returns:
        int: Le nombre de sous-tableaux respectant la propriété.
    """
    # ex : garde en mémoire la somme ET le xor actuel de la plage [i, j)
    ex = 0  # Somme / Xor actuel de la plage courante
    ans = 0  # Compteur de sous-tableaux valides
    j = 0    # Pointeur de fin de plage (exclusif)
    ex = 0   # Réinitialisé à 0 pour chaque nouveau début de sous-tableau

    for i in range(N):
        # Étend j aussi loin que l'invariant ex + A[j] == ex ^ A[j] est vérifié.
        # Cela signifie qu'aucun bit ne se "collisionne" quand on ajoute A[j].
        while j <= N-1 and ex + A[j] == ex ^ A[j]:
            ex += A[j]   # Met à jour la "somme xor" de la fenêtre
            j += 1       # Avance le pointeur de droite de la fenêtre
        
        # Pour la position i, le nombre de sous-tableaux valides est (j - i)
        ans += j - i

        # Avant de passer à i+1, on retire A[i] de la somme/xor courante.
        ex -= A[i]
    
    return ans


if __name__ == "__main__":
    # Lecture de l'entrée
    N = int(input())
    A = list(map(int, input().split()))

    # Appel de la fonction principale
    result = count_subarrays_with_unique_sum_xor(N, A)

    # Affichage du résultat
    print(result)