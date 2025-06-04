def knapsack_value_based(n, W, weights, values):
    """
    Résout le problème du sac à dos où la contrainte est la capacité totale en poids,
    et on cherche à maximiser la somme des valeurs des objets sélectionnés.

    Arguments :
        n (int): Nombre d'objets disponibles.
        W (int): Capacité maximale du sac à dos.
        weights (list[int]): Liste des poids des objets.
        values (list[int]): Liste des valeurs des objets.

    Retourne :
        int: La valeur maximale totale pouvant être obtenue sans dépasser la capacité W.
    """
    # Calcul de la somme maximale des valeurs (pour dimensionner le tableau DP)
    V = sum(values)

    # Initialisation du tableau de programmation dynamique.
    # dp[i][j] représente le poids minimal nécessaire pour atteindre la valeur totale j en utilisant les i premiers objets.
    dp = [[float('inf') for _ in range(V+1)] for _ in range(n+1)]
    # Initialisation de l'état de base : atteindre la valeur 0 avec 0 objet requiert 0 poids.
    dp[0][0] = 0

    # Remplissage du tableau DP
    for i in range(n):
        for j in range(V+1):
            # Si on prend l'objet i (sous condition que la valeur cible est atteignable),
            # on compare le poids en le prenant ou pas.
            if j - values[i] >= 0:
                dp[i+1][j] = min(
                    dp[i][j],                         # Ne pas prendre l'objet i
                    dp[i][j - values[i]] + weights[i] # Prendre l'objet i
                )
            else:
                # Impossible de prendre l'objet i si la valeur cible ne le permet pas
                dp[i+1][j] = dp[i][j]

    # Recherche de la valeur maximale atteignable sans dépasser la capacité W
    ans = 0
    for i in range(V+1):
        if dp[n][i] <= W:
            ans = i

    return ans

def main():
    """
    Fonction principale :
    Lit les entrées utilisateur, initialise les listes de poids et de valeurs,
    puis appelle la fonction de résolution du problème.
    Affiche la valeur optimale obtenue.
    """
    # Lecture de la première ligne : nombre d'objets et capacité du sac à dos
    n, W = map(int, input().split())

    # Initialisation des listes de poids et de valeurs
    weights = []
    values = []
    for _ in range(n):
        tmp_weight, tmp_value = map(int, input().split())
        weights.append(tmp_weight)
        values.append(tmp_value)

    # Appel de la fonction de résolution du sac à dos
    result = knapsack_value_based(n, W, weights, values)

    # Affichage du résultat optimal trouvé
    print(result)

# Appel de la fonction principale si le script est exécuté directement
if __name__ == "__main__":
    main()