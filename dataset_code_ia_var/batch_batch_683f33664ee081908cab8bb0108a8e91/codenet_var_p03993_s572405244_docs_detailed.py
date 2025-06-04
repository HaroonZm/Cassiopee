def count_mutual_pairs(N, a):
    """
    Compte le nombre de paires mutuellement préférées dans la liste a.

    Une paire (i, j) est considérée comme mutuellement préférée si a[i] = j+1 et a[j] = i+1.
    Chaque paire est comptée une seule fois (i.e., (i, j) ≡ (j, i), i ≠ j).

    Args:
        N (int): Nombre d'éléments dans la liste.
        a (List[int]): Liste d'entiers représentant les préférences (indices 1-based).

    Returns:
        int: Nombre de paires mutuelles.
    """
    cnt = 0  # Initialise le compteur de paires mutuelles
    for i in range(N):
        # Vérifie si l'élément pointé par a[i] pointe lui aussi vers i+1
        # a[i]-1 car les indices dans a sont 1-based alors que Python utilise des indices 0-based
        if a[a[i] - 1] == i + 1:
            cnt += 1  # Incrémente le compteur si la symétrie est trouvée
    return cnt // 2  # Chaque paire est comptée deux fois, on divise donc par 2


def main():
    """
    Point d'entrée principal du programme.
    Lit l'entrée de l'utilisateur, traite les données et affiche le résultat.
    """
    # Lecture du nombre d'éléments dans la liste
    N = int(input())
    # Lecture de la liste de préférences et conversion en entiers
    a = list(map(int, input().split()))
    # Appel de la fonction pour compter les paires mutuelles et affichage du résultat
    print(count_mutual_pairs(N, a))


if __name__ == "__main__":
    main()