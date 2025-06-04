def min_cost_to_reach_last_stone(N, h_list):
    """
    Calcule le coût minimal pour atteindre la dernière pierre dans une séquence de pierres,
    en ne pouvant sauter que sur la pierre adjacente ou en sautant une pierre, le coût étant
    la différence absolue de hauteur entre les pierres sautées.

    Paramètres:
        N (int): Nombre total de pierres.
        h_list (list of int): Liste des hauteurs de chaque pierre.

    Retourne:
        int: Le coût minimal pour atteindre la dernière pierre.
    """
    # Initialisation de la liste dp pour mémoriser le coût minimal pour atteindre chaque pierre.
    # dp[i] représentera le coût minimal pour atteindre la pierre d'indice i.
    dp = [0] * N  # On initialise toutes les valeurs à 0, elles seront remplies ensuite.

    # Le coût pour atteindre la première pierre (indice 0) est toujours 0,
    # car c'est le point de départ.
    dp[0] = 0

    # Le coût pour atteindre la deuxième pierre (indice 1) est la différence absolue de hauteur
    # avec la première pierre, car il n'y a qu'une seule manière d'y arriver.
    dp[1] = abs(h_list[1] - h_list[0])

    # Remplissage de la table dp pour toutes les pierres suivantes.
    for i in range(2, N):
        # On peut arriver à la pierre i soit depuis la pierre i-1 soit depuis la pierre i-2 :
        # - Depuis i-1 : coût = dp[i-1] + abs(hauteur[i] - hauteur[i-1])
        # - Depuis i-2 : coût = dp[i-2] + abs(hauteur[i] - hauteur[i-2])
        # On prend le coût minimal entre les deux options.
        from_prev1 = dp[i-1] + abs(h_list[i] - h_list[i-1])
        from_prev2 = dp[i-2] + abs(h_list[i] - h_list[i-2])
        dp[i] = min(from_prev1, from_prev2)
    
    # Le coût minimal pour atteindre la dernière pierre est dp[N-1]
    return dp[N-1]

if __name__ == "__main__":
    # Lecture du nombre de pierres
    N = int(input())
    # Lecture et transformation de la liste des hauteurs de chaque pierre
    h_list = list(map(int, input().split()))
    # Calcul et impression du coût minimal pour atteindre la dernière pierre
    print(min_cost_to_reach_last_stone(N, h_list))