def find_earliest_index(n, t, e, a):
    """
    Trouve le plus petit index i (commençant à 1) tel que le temps maximum atteint par a[i]
    dans l'intervalle [t-e, t+e] ne dépasse pas t+e.

    Args:
        n (int): Le nombre d'éléments dans la liste 'a'.
        t (int): La valeur centrale de l'intervalle de temps.
        e (int): L'étendue de l'intervalle autour de 't'.
        a (list of int): La liste des valeurs à tester.

    Returns:
        int: L'index (1-based) du premier élément vérifiant la condition, ou -1 si aucun ne convient.
    """
    for i in range(n):
        # Calculer le nombre total de fois que a[i] rentre dans l'intervalle [t-e, t+e], moins 1
        x = (t - e - 1) // a[i]
        # Vérifier si le prochain multiple de a[i] dépasse l'intervalle maximal
        if (x + 1) * a[i] <= t + e:
            # Si la condition est respectée, retourner l'index (1-based)
            return i + 1
    # Si aucun index ne vérifie la condition, retourner -1
    return -1


def main():
    """
    Fonction principale du programme.
    Lit les entrées, appelle la fonction de recherche et affiche le résultat.
    """
    # Lecture des entrées utilisateur pour n, t, e
    n, t, e = map(int, input().split())
    # Lecture de la liste des valeurs a
    a = list(map(int, input().split()))
    # Appel de la fonction de recherche
    result = find_earliest_index(n, t, e, a)
    # Affichage du résultat
    print(result)


if __name__ == "__main__":
    main()