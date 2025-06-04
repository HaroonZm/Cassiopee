def read_input():
    """
    Lit la première ligne d'entrée pour obtenir la hauteur et la largeur, puis lit les lignes suivantes pour former la grille.

    Returns:
        tuple: un tuple contenant:
            - h (int): la hauteur de la grille.
            - w (int): la largeur de la grille.
            - squares (list): une liste de listes représentant la grille de caractères.
    """
    # Lire la hauteur et la largeur à partir de l'entrée standard
    h, w = [int(i) for i in input().split()]
    # Lire les lignes suivantes pour remplir la matrice de caractères
    squares = [list(input()) for _ in range(h)]
    return h, w, squares

def count_special_positions(h, w, squares):
    """
    Compte le nombre de positions spéciales dans la grille selon la règle définie par la logique du code original.

    La logique est :
        - Pour chaque case de la grille contenant un autre caractère que 'I' ou 'O', 
        on multiplie le nombre de 'I' trouvés plus bas dans la colonne correspondante par
        le nombre de 'O' trouvés plus à droite sur la même ligne, pour cette ligne.

    Args:
        h (int): hauteur de la grille.
        w (int): largeur de la grille.
        squares (list): la grille de caractères.

    Returns:
        int: le nombre total de positions spéciales selon la règle.
    """
    ans = 0  # Compteur global pour la réponse
    h_cnts = [0] * w  # Compteur des 'I' rencontrés dans chaque colonne
    # Parcours des lignes de bas en haut
    for i in reversed(range(0, h)):
        o_cnt = 0  # Compteur de 'O' dans la ligne courante, de droite à gauche
        # Parcours des colonnes de droite à gauche
        for j in reversed(range(0, w)):
            if squares[i][j] == 'I':
                # Incrémente le compteur d''I' pour la colonne j
                h_cnts[j] += 1
            elif squares[i][j] == 'O':
                # Incrémente le compteur d''O' pour la ligne courante
                o_cnt += 1
            else:
                # Ajoute au total le produit des 'I' en dessous dans la colonne et des 'O' à droite dans la ligne
                ans += h_cnts[j] * o_cnt
    return ans

def main():
    """
    Fonction principale contrôlant la lecture des entrées, le calcul et l'affichage du résultat.
    """
    # Récupération des entrées utilisateur
    h, w, squares = read_input()
    # Calcul du résultat selon la règle
    ans = count_special_positions(h, w, squares)
    # Affichage du résultat
    print(ans)

# Lancement du programme
if __name__ == "__main__":
    main()