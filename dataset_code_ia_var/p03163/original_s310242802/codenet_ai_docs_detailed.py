from collections import defaultdict

def knapsack(N, W, WV):
    """
    Résout le problème du sac à dos 0/1 avec N objets et une capacité maximale W.
    
    Args:
        N (int): Le nombre d'objets à choisir
        W (int): La capacité maximale du sac à dos
        WV (list of list or tuple): Une liste de paires [poids, valeur] pour chaque objet
    
    Returns:
        int: La valeur maximale totale que l'on peut obtenir sans dépasser la capacité W
    """
    # Dictionnaire pour mémoriser la meilleure (valeur maximale) atteignable pour chaque poids total.
    # dp[poids total] = valeur maximale pour ce poids total parmi toutes les combinaisons considérées
    dp = defaultdict(int)
    
    # Le cas de base : il est possible d'obtenir une valeur de 0 avec un poids total de 0.
    dp[0] = 0

    # Parcours de chaque objet donné sous forme de (w, v) = (poids, valeur)
    for w, v in WV:
        # Création d'une liste temporaire des états actuels du dictionnaire
        # Ceci est nécessaire pour éviter de modifier le dictionnaire 'dp' pendant l'itération
        for current_weight, current_value in list(dp.items()):
            # On vérifie si on peut ajouter l'objet courant sans dépasser la capacité du sac à dos
            if current_weight + w <= W:
                # Mise à jour du dictionnaire pour ce nouveau poids atteint :
                # - Soit on ne prend pas l'objet et on garde la valeur précédente
                # - Soit on prend l'objet et on met à jour avec la valeur obtenue
                dp[current_weight + w] = max(dp[current_weight + w], current_value + v)
    
    # Recherche de la valeur maximale atteignable pour un poids total inférieur ou égal à W
    return max(dp.values())

def main():
    """
    Fonction principale pour lire l'entrée et afficher la solution du problème du sac à dos.
    """
    # Lecture du nombre d'objets et de la capacité du sac à dos
    N, W = map(int, input().split())
    WV = []
    
    # Lecture des paires poids et valeur pour chaque objet
    for _ in range(N):
        WV.append(list(map(int, input().split())))
    
    # Appel de la fonction knapsack et affichage du résultat
    print(knapsack(N, W, WV))

if __name__ == "__main__":
    main()