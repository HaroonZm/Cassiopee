def count_mutual_pairs(n, a):
    """
    Compte le nombre de paires mutuelles réciproques dans le tableau a.
    Une paire mutuelle existe si pour les indices i et j, on a a[i] = j+1 et a[j] = i+1.
    Chaque paire est comptée deux fois (une fois pour i et une fois pour j), donc le résultat final est divisé par 2.

    Args:
        n (int): Nombre d'éléments dans le tableau.
        a (list): Liste d'entiers, indices commencent à 0, valeurs comprises entre 1 et n.

    Returns:
        int: Nombre de paires mutuelles distinctes.
    """
    ans = 0  # Compteur des paires réciproques trouvées
    # Parcourt chaque élément du tableau
    for i in range(n):
        # Vérifie si l'élément pointé par a[i]-1 pointe vers i+1 (réciprocité)
        if a[a[i]-1] == i+1:
            ans += 1  # Incrémente le compteur si condition satisfaite
    # Chaque paire a été comptée deux fois, donc on divise le compteur par 2
    return ans // 2

if __name__ == "__main__":
    # Lecture de la taille du tableau depuis l'entrée standard
    n = int(input())
    # Lecture et conversion des éléments du tableau depuis l'entrée standard
    a = list(map(int, input().split()))
    # Affiche le résultat c'est-à-dire le nombre de paires mutuelles distinctes
    print(count_mutual_pairs(n, a))