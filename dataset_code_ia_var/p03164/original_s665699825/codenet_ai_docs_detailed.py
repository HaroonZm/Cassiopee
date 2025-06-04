import numpy as np

def knapsack_max_value(num_items, max_weight, items):
    """
    Calcule la valeur maximale pouvant être obtenue avec des objets soumis à une contrainte de poids,
    en utilisant l'algorithme du sac à dos basé sur la valeur, optimisé via un tableau dynamique.

    Args:
        num_items (int): Nombre total d'objets à considérer.
        max_weight (int): Poids total maximal autorisé.
        items (List[Tuple[int, int]]): Liste de tuples (poids, valeur) pour chaque objet.

    Returns:
        int: La valeur maximale atteignable sans dépasser la contrainte de poids.
    """

    # Définition de la valeur maximale possible par objet et du nombre total de valeurs possibles
    v_max = 1000               # Hypothèse : valeur maximale pour un objet (connu d'après contrainte du problème)
    num_v = v_max * num_items  # Valeur maximale possible atteignable par combinaison des objets

    # INF agit comme une valeur impossible (plus grande que n'importe quel poids réalisable)
    INF = 10**9 + 1

    # Initialisation du tableau dynamique :
    # dp[v] : poids minimal nécessaire pour atteindre une valeur v
    dp = np.full(num_v + 1, INF, dtype=int)
    dp[0] = 0  # Il faut 0 de poids pour atteindre une valeur 0 (cas de base)

    # Parcours de chaque objet pour mettre à jour dp
    for wn, vn in items:
        # On parcourt dp de la droite vers la gauche pour éviter de compter un même objet plusieurs fois
        dp[vn:] = np.minimum(dp[vn:], dp[:-vn] + wn)

    # Recherche de la plus grande valeur réalisable (en partant du maximum) sous la contrainte de poids
    for i in range(len(dp) - 1, -1, -1):
        if dp[i] <= max_weight:
            return i  # Valeur maximale pour laquelle le poids reste admissible
    # Si aucune valeur atteignable, retour 0 par défaut
    return 0

def main():
    """
    Fonction principale qui lit l'entrée utilisateur, prépare les données et affiche la solution du sac à dos.
    """

    # Lecture du nombre d'objets et du poids maximal
    n, w = map(int, input().split())
    items = []

    # Lecture des n lignes suivantes (poids, valeur)
    for _ in range(n):
        wn, vn = map(int, input().split())
        items.append((wn, vn))

    # Calcul et affichage de la valeur optimale
    res = knapsack_max_value(n, w, items)
    print(res)

# Exécution du programme principal si ce script est lancé directement
if __name__ == "__main__":
    main()