def fill(x, y, board):
    """
    Remplit récursivement (en profondeur) une région contiguë de '1' sur le plateau en la marquant comme '2'.
    Les régions sont déterminées à partir de la position (x, y).
    
    Args:
        x (int): Colonne de la cellule actuelle.
        y (int): Ligne de la cellule actuelle.
        board (list of list of int): Tableau 2D représentant la carte, où 1 signifie île, 0 signifie eau, et 2 une cellule déjà traitée.
    
    Returns:
        list of list of int: Le plateau après remplissage de la région connectée.
    """
    # Marquer la position actuelle comme visitée (2)
    board[y][x] = 2

    # Définir les positions voisines directes (haut, bas, gauche, droite)
    points = [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]

    # Éliminer les voisins invalide selon la position sur les bords
    if y == 0:
        # Pas de cellule au-dessus si sur le bord supérieur
        points.remove([y - 1, x])
    elif y == 11:
        # Pas de cellule en-dessous si sur le bord inférieur
        points.remove([y + 1, x])
    if x == 0:
        # Pas de cellule à gauche si sur le bord gauche
        points.remove([y, x - 1])
    elif x == 11:
        # Pas de cellule à droite si sur le bord droit
        points.remove([y, x + 1])

    # Pour chaque voisin valide, si c'est une île (1), lancer un remplissage depuis cette case
    for p in points:
        if board[p[0]][p[1]] == 1:
            board = fill(p[1], p[0], board)
    return board

while True:
    try:
        # Lecture de la grille d'îles (12 lignes, chaque ligne est une chaîne de 12 chiffres)
        islands = [list(map(int, list(input()))) for i in range(12)]
        ans = 0  # Compteur du nombre d'îles distinctes trouvées

        # Parcours de toute la grille
        for y in range(12):
            for x in range(12):
                # Si une île non encore traitée est trouvée
                if islands[y][x] == 1:
                    islands = fill(x, y, islands)  # Remplir toute l'île connectée
                    ans += 1                       # Incrémenter le nombre d'îles trouvées
        print(ans)  # Afficher le nombre d'îles

        input()  # Pause pour permettre à l'utilisateur d'entrer un jeu supplémentaire
    except:
        # Arrêter la boucle en cas d'erreur (EOF ou saisie incorrecte)
        break