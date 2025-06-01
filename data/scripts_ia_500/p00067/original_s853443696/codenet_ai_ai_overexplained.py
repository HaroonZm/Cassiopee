def fill(x, y, board):
    # Cette fonction prend en entrée trois arguments : 
    # x : coordonnée horizontale (colonne) de la cellule à traiter,
    # y : coordonnée verticale (ligne) de la cellule à traiter,
    # board : une matrice (liste de listes) représentant le plateau avec des cellules.
    # L'objectif est de « remplir » toutes les cellules connectées à la cellule (x, y)
    # ayant la valeur 1, en changeant leur valeur à 2.

    board[y][x] = 2
    # Modifier la cellule à la position (y, x) dans la matrice 'board' pour indiquer qu'elle est visitée.
    # On remplace 1 par 2 pour ne pas revisiter cette cellule.

    points = [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]
    # Créer une liste de points voisins à vérifier.
    # Chaque point est une liste [ligne, colonne].
    # On ajoute les points voisins directs dans les quatre directions : droite, gauche, bas, haut.

    if y == 0:
        points.remove([y-1, x])
    # Si la cellule est sur la première ligne (index 0),
    # le voisin du dessus ([y-1, x]) n'existe pas, il faut donc le retirer de la liste.

    elif y == 11:
        points.remove([y+1, x])
    # Si la cellule est sur la dernière ligne (index 11),
    # le voisin du dessous ([y+1, x]) n'existe pas, donc on le retire.

    if x == 0:
        points.remove([y, x - 1])
    # Si la cellule est sur la première colonne (index 0),
    # le voisin de gauche ([y, x-1]) n'existe pas,
    # donc on l'enlève de la liste des voisins à traiter.

    elif x == 11:
        points.remove([y, x + 1])
    # Si la cellule est sur la dernière colonne (index 11),
    # le voisin de droite ([y, x+1]) est inexistant,
    # on le supprime de la liste des voisins.

    for p in points:
        # Pour chaque point voisin p restant dans la liste,
        # qui est une liste [ligne, colonne]:

        if board[p[0]][p[1]] == 1:
            # Si la cellule voisine a la valeur 1 (non visitée, terre dans ce contexte),
            # on appelle récursivement la fonction fill sur cette cellule.
            # L'appel récursif va marquer cette cellule et ses voisins connectés.

            board = fill(p[1], p[0], board)
            # Notez que dans l'appel récursif, on passe x = p[1] et y = p[0]
            # car p est stocké sous la forme [ligne, colonne], 
            # alors que la fonction fill attend les paramètres dans l'ordre (x, y).

    return board
    # Après avoir marqué toutes les cellules connectées, retourner le plateau modifié.


while True:
    # Boucle infinie pour traiter plusieurs cas de test successivement.

    try:
        islands = [list(map(int, list(input()))) for i in range(12)]
        # Pour chaque itération, lire 12 lignes de l'entrée standard.
        # Chaque ligne est une chaîne de caractères représentant 12 chiffres ('0' ou '1').
        # Convertir cette chaîne en liste de chiffres entiers avec map(int, list(...)).
        # Le résultat est une liste de 12 listes (matrice 12x12), représentant l'île.

        ans = 0
        # Initialiser un compteur pour le nombre d'îles trouvées à zéro.

        for y in range(12):
            for x in range(12):
                # Parcourir chaque cellule du plateau en utilisant
                # deux boucles imbriquées : y pour les rangées (lignes),
                # x pour les colonnes.

                if islands[y][x] == 1:
                    # Lorsque l'on trouve une cellule avec la valeur 1,
                    # cela signifie que nous avons trouvé une nouvelle terre non visitée.

                    islands = fill(x, y, islands)
                    # Appeler la fonction fill pour marquer toute la terre connectée
                    # à cette cellule (y, x) en remplaçant les 1 par des 2,
                    # ce qui empêche de compter plusieurs fois la même île.

                    ans += 1
                    # Incrémenter le compteur d'îles, car une nouvelle île a été découverte.

        print(ans)
        # Afficher le nombre total d'îles trouvées dans le plateau.

        input()
        # Attendre une entrée supplémentaire (probablement pour mettre en pause avant le prochain test).
        # Cette ligne peut être utilisée pour séparer les tests.

    except:
        break
        # En cas d'exception (par exemple, fin de l'entrée standard),
        # quitter la boucle et terminer le programme.