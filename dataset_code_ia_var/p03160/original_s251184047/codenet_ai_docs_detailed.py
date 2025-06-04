def min_cost_to_reach_end(N, H):
    """
    Calcule le coût minimal pour atteindre la dernière marche d'un escalier, 
    en se basant sur un tableau de hauteurs. À chaque étape, il est possible 
    de passer à la marche suivante ou de sauter une marche. 
    Le coût pour sauter d'une marche à une autre est l'absolue différence de hauteur.

    Args:
        N (int): Le nombre de marches.
        H (list of int): La liste des hauteurs des marches.

    Returns:
        int: Le coût minimal pour arriver à la dernière marche.
    """
    BIG_NUM = 10 ** 18  # Valeur arbitrairement grande pour initialiser les coûts
    # Tableau pour stocker le coût minimal pour atteindre chaque marche
    # On prend N+10 pour éviter les erreurs d'indice lors des accès
    l = [BIG_NUM] * (N + 10)
    l[0] = 0  # Coût pour atteindre la première marche (départ) est 0

    # Parcours des marches à partir de la deuxième (indice 1)
    for i in range(1, N):
        # Coût en venant de la marche précédente
        cost_from_prev = l[i - 1] + abs(H[i] - H[i - 1])
        # Coût en venant de la marche avant la précédente
        # On vérifie que i-2 >= 0 pour éviter les accès hors limites
        if i >= 2:
            cost_from_prev_prev = l[i - 2] + abs(H[i] - H[i - 2])
        else:
            cost_from_prev_prev = BIG_NUM  # Impossible si i < 2

        # Le coût minimal pour atteindre la marche i
        l[i] = min(cost_from_prev, cost_from_prev_prev)

    return l[N - 1]  # Coût minimal pour atteindre la dernière marche

def main():
    """
    Fonction principale pour lire les entrées, traiter et afficher le résultat.
    """
    # Lecture du nombre de marches
    N = int(input())
    # Lecture des hauteurs des marches
    H = list(map(int, input().split()))

    # Calcul et affichage du coût minimal
    result = min_cost_to_reach_end(N, H)
    print(result)

# Appel du point d'entrée du programme
if __name__ == "__main__":
    main()