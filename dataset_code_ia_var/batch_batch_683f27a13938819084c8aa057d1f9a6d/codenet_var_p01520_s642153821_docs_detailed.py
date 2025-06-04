def find_first_divisible_clock(N, T, E, X):
    """
    Recherche l'indice (1-based) du premier élément dans X 
    qui divise au moins un élément de l'intervalle [T-E, T+E]. 
    Si aucun diviseur n'est trouvé, retourne -1.

    Args:
        N (int): Nombre d'éléments dans X
        T (int): Valeur centrale de l'intervalle
        E (int): Ecart autour de T à considérer
        X (list of int): Liste des diviseurs à tester

    Returns:
        int: L'indice 1-based du premier diviseur trouvé (ou -1 si aucun n'est trouvé)
    """
    # Construction de la plage de temps à vérifier : [T-E, T+E]
    time = [i for i in range(T - E, T + E + 1)]

    # Initialisation d'une variable pour stocker l'indice du diviseur trouvé
    clock = -2  # Si aucun diviseur trouvé, clock restera à -2

    # Parcourir chaque élément de X
    for i in range(len(X)):
        # Pour chaque valeur de temps dans la plage définie
        for j in range(len(time)):
            # Vérifier si la valeur time[j] est divisible par X[i]
            if time[j] % X[i] == 0:
                # Si oui, sauvegarder l'indice dans clock
                clock = X.index(X[i])  # On utilise l'index de X[i] dans X
                # Remarque : X.index(X[i]) sera en fait égal à i sauf s'il y a des doublons dans X
                # La boucle continue car on ne fait pas de break — seul le dernier trouvé sera retenu

    # Retourner l'indice en notation 1-based (ajouter 1), ou 0 si aucun n'a été trouvé (puisque -2+1 = -1)
    return clock + 1


if __name__ == "__main__":
    # Lecture des données d'entrée (N, T, E)
    N, T, E = map(int, input().split())
    # Lecture de la liste X (N entiers)
    X = list(map(int, input().split()))
    # Appel de la fonction principale et affichage du résultat
    print(find_first_divisible_clock(N, T, E, X))