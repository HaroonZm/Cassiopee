def knapsack_max_value(N, W, wv):
    """
    Résout le problème du sac à dos où l'objectif est de maximiser la valeur totale 
    transportée sans dépasser le poids total spécifié.
    
    Ce problème correspond à la version pseudo-polynomiale utilisant la somme maximale de valeurs 
    possibles pour faire du 'DP' (programmation dynamique) indexé par la valeur.

    Paramètres
    ----------
    N : int
        Le nombre d'objets disponibles pour le sac à dos.
    W : int
        La capacité maximale (en poids) du sac à dos.
    wv : list of list of int
        La liste des N objets, chaque objet étant une liste de deux entiers [w, v] où
        w est son poids et v sa valeur.

    Retourne
    -------
    int
        La valeur maximale totale pouvant être atteinte sans dépasser la capacité W.
    """

    INF = 10**10  # Constante représentant l'infini (un nombre très élevé pour nos comparaisons).
    v_max = 10**5 # Supposée borne supérieure pour la somme des valeurs des objets.
    # Table de programmation dynamique:
    # dp[i][j] = poids minimal pour obtenir une valeur j avec les i premiers objets
    dp = [[INF] * (v_max + 1) for _ in range(N + 1)]

    # Cas de base : valeur 0 atteignable avec poids 0, sans objets
    dp[0][0] = 0

    # Variable stockant la meilleure valeur trouvée (sous la contrainte de poids)
    ans = 0

    # Parcours de chaque objet
    for i in range(N):
        # On parcourt toutes les valeurs possibles jusqu'à v_max
        for j in range(v_max + 1):
            # Si la valeur actuelle j est atteignable en ajoutant l'objet i
            if j >= wv[i][1]:
                # Deux choix : ne pas prendre l'objet (dp[i][j]) ou le prendre (ajouter son poids au poids minimal de valeur j-wv[i][1])
                dp[i+1][j] = min(dp[i][j], dp[i][j-wv[i][1]] + wv[i][0])
            else:
                # Cas où on ne peut pas atteindre la valeur j en ajoutant cet objet : on réplique la valeur précédente
                dp[i+1][j] = dp[i][j]
            # Si on a traité tous les objets et que le poids pour la valeur j reste dans la limite
            if i+1 == N and dp[i+1][j] <= W:
                # On met à jour la meilleure valeur trouvée
                ans = j
    return ans

def main():
    """
    Point d'entrée principal du programme.
    Lit les entrées depuis stdin (clavier), appelle la résolution du sac à dos et affiche la sortie.
    """
    # Lecture du nombre d'objets et de la capacité maximale du sac à dos
    N, W = map(int, input().split())
    wv = []
    # Lecture de la liste des objets (poids et valeur)
    for _ in range(N):
        wv.append(list(map(int, input().split())))
    # Calcul et affichage de la réponse via knapsack_max_value
    print(knapsack_max_value(N, W, wv))

# Si ce fichier est exécuté en tant que programme principal, on lance la fonction main
if __name__ == "__main__":
    main()