def read_input():
    """
    Lit les dimensions du jardin (D, W) et la grille du jardin à partir de l'entrée standard.
    Retourne un tuple (D, W, garden) où :
        - D : Nombre de lignes du jardin,
        - W : Nombre de colonnes du jardin,
        - garden : Liste de listes d'entiers représentant les hauteurs de chaque case.
    """
    D, W = map(int, input().split())
    if (D, W) == (0, 0):
        return (0, 0, [])
    garden = []
    for _ in range(D):
        row = list(map(int, input().split()))
        garden.append(row)
    return D, W, garden

def max_water_trapped(D, W, garden):
    """
    Calcule le volume maximal d'eau pouvant être retenu par une sous-grille rectangulaire de taille au moins 3x3
    dans le jardin en fonction des contraintes.
    
    Args:
        D (int): Nombre de lignes du jardin.
        W (int): Nombre de colonnes du jardin.
        garden (list): Grille du jardin (liste de listes d'entiers).
        
    Returns:
        int: Le volume d'eau maximal qui peut être retenu dans une sous-grille donnée du jardin.
    """
    ans = 0  # Résultat final : volume maximal trouvé

    # Parcours toutes les paires possibles de colonnes en garantissant une largeur d'au moins 3
    for wi in range(W):
        for wj in range(wi+2, W):
            # Parcours toutes les paires possibles de lignes en garantissant une hauteur d'au moins 3
            for di in range(D):
                for dj in range(di+2, D):
                    edge_min = float("inf")  # Hauteur minimale sur le contour de la sous-grille
                    water_sum = 0            # Somme totale des hauteurs dans la zone intérieure (hors bordure)
                    count = 0                # Nombre de cases dans la zone intérieure
                    in_max = 0               # Valeur maximale à l'intérieur de la zone (hors bordure)

                    # Parcourir toutes les cases de la sous-grille sélectionnée
                    for w in range(wi, wj+1):
                        for d in range(di, dj+1):
                            # Si la case appartient au contour (bord)
                            if w in (wi, wj) or d in (di, dj):
                                # Mise à jour de la hauteur minimale du bord
                                edge_min = min(garden[d][w], edge_min)
                            else:
                                # Ajout des valeurs pour la zone intérieure
                                water_sum += garden[d][w]
                                in_max = max(in_max, garden[d][w])
                                count += 1

                    # Pour qu'un bassin existe, la hauteur du bord doit dépasser la hauteur intérieure la plus élevée
                    if edge_min > in_max:
                        # Calcul du volume d'eau maximal possible pour cette sous-grille
                        ans = max(ans, edge_min * count - water_sum)
    return ans

def main():
    """
    Programme principal : lit en boucle les configurations de jardin,
    calcule et affiche pour chacune le volume d'eau maximal pouvant être capturé.
    La boucle s'arrête à la saisie de '0 0'.
    """
    while True:
        D, W, garden = read_input()
        # Condition d'arrêt : fin de toutes les entrées
        if (D, W) == (0, 0):
            break
        ans = max_water_trapped(D, W, garden)
        print(ans)

# Exécution du programme principal
main()