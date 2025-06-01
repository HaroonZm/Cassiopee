while True:
    # Lecture du nombre de blocs à traiter
    n = input()
    # Conversion en entier pour la comparaison avec 0
    n = int(n)
    # Condition d'arrêt de la boucle principale
    if n == 0:
        break
    
    # Hauteur maximale de la zone de jeu
    hmax = 7500
    # Lecture des blocs : chaque bloc est défini par trois valeurs d'entrée
    # d : direction (1 pour horizontal, autre pour vertical)
    # p : taille du bloc (nombre de cases occupées)
    # q : position de départ sur la ligne ou colonne (1-indexé)
    block = [list(map(int, input().split())) for _ in range(n)]
    
    # Initialisation du champ de jeu comme une grille à 2 dimensions
    # 5 colonnes fixes, hauteur hmax cases (initialement remplies de 0)
    field = [[0] * 5 for _ in range(hmax)]
    # Hauteur actuelle effective où les blocs sont placés
    h = 0

    for d, p, q in block:
        if d == 1:
            # Placement d'un bloc horizontal
            # On descend du haut vers le bas afin de trouver la ligne d'atterrissage
            for li in range(h, -2, -1):
                # On vérifie si la zone sur la ligne li aux colonnes q-1 jusqu'à q+p-2 est libre (toutes 0)
                # Ou si on est arrivé sous la grille (li == -1)
                if field[li][q - 1:q + p - 1] != [0] * p or li == -1:
                    # On place le bloc à la ligne juste au-dessus
                    field[li + 1][q - 1:q + p - 1] = [1] * p
                    # Mise à jour de la hauteur effective maximale utilisée
                    h = max(h, li + 2)
                    break
        else:
            # Placement d'un bloc vertical
            # Recherche la ligne la plus basse où placer ce bloc verticalement
            for li in range(h, -2, -1):
                # On vérifie si la case à la colonne q-1 et ligne li est occupée ou si li est hors bord
                if field[li][q - 1] != 0 or li == -1:
                    # On place le bloc verticalement de li+1 à li+p (dans la colonne q-1)
                    for i in range(p):
                        field[li + i + 1][q - 1] = 1
                    # Mise à jour de la hauteur effective
                    h = max(h, li + 1 + p)
                    break
        
        # Nettoyage des lignes complètes (remplies de 1) et lignes vides après chaque placement
        i = 0
        while True:
            # Si la ligne i est complètement remplie (5 colonnes à 1)
            if field[i] == [1] * 5:
                del field[i]  # On supprime cette ligne (descente de toutes lignes supérieures)
                h -= 1        # On réduite la hauteur effective d'une ligne
            # Si la ligne est complètement vide, on arrête la vérification des lignes suivantes
            elif field[i] == [0] * 5:
                break
            else:
                # Ligne ni pleine ni vide : on continue à la ligne suivante
                i += 1

    # Calcul et affichage du nombre total de cases occupées dans la grille jusqu'à la hauteur h
    total_occupied = sum(sum(field[li]) for li in range(h))
    print(total_occupied)