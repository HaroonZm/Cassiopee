# Définition d'une fonction appelée kesu qui va détecter et effacer des groupes connectés dans la grille
def kesu(x, s, c, h):
    # x est un tuple représentant les coordonnées (ligne, colonne) de la cellule courante
    # s est un ensemble qui contiendra toutes les coordonnées d'un groupe connecté trouvé jusqu'à présent
    # c est la couleur de la cellule de départ autour de laquelle on cherche le groupe à effacer
    # h est la hauteur de récursivité qui indique la profondeur d'appel de la fonction
    global n  # n est une variable globale utilisée pour stocker les cellules à supprimer

    # On regarde la cellule au-dessus (vers le haut, ligne -1)
    if (x[0] - 1, x[1]) not in s and a[x[0] - 1][x[1]] == c:
        # Si elle n'a pas déjà été visitée et qu'elle correspond à la même couleur c
        s.add((x[0] - 1, x[1]))  # On l'ajoute à l'ensemble du groupe
        kesu((x[0] - 1, x[1]), s, c, h + 1)  # Appel récursif avec la nouvelle cellule

    # On regarde la cellule en dessous (vers le bas, ligne +1)
    if (x[0] + 1, x[1]) not in s and a[x[0] + 1][x[1]] == c:
        s.add((x[0] + 1, x[1]))
        kesu((x[0] + 1, x[1]), s, c, h + 1)

    # On regarde la cellule à gauche (colonne -1)
    if (x[0], x[1] - 1) not in s and a[x[0]][x[1] - 1] == c:
        s.add((x[0], x[1] - 1))
        kesu((x[0], x[1] - 1), s, c, h + 1)

    # On regarde la cellule à droite (colonne +1)
    if (x[0], x[1] + 1) not in s and a[x[0]][x[1] + 1] == c:
        s.add((x[0], x[1] + 1))
        kesu((x[0], x[1] + 1), s, c, h + 1)

    # Si on est revenu à la profondeur initiale ET le groupe détecté est assez grand (plus de 3 cellules)
    if h == 0 and len(s) > 3:
        # On efface toutes les cellules du groupe du plateau en mettant leur valeur à "."
        for i in s:
            a[i[0]][i[1]] = "."
        # On ajoute ce groupe à l'ensemble global n (toutes les cellules à supprimer pour cette étape)
        n |= s

# Définition d'une fonction otosu qui fait tomber les pièces (effet de gravité vers le bas)
def otosu():
    # Parcours des lignes du bas vers le haut (sauf les bords, car ils servent de sentinelle)
    for i in range(1, 12)[::-1]:
        # Pour chaque colonne de jeu possible (hors bord gauche/droit)
        for j in range(1, 7):
            n = 0  # Compteur pour indiquer combien de fois la pièce est tombée
            # Tant qu'on ne sort pas du bas de la grille
            while i + n < 12:
                # Si la cellule à la position courante n'est pas vide (".") ET que celle en-dessous est vide
                if a[i + n][j] != "." and a[i + n + 1][j] == ".":
                    # Echange (permutation) de la cellule courante avec celle en-dessous
                    a[i + n][j], a[i + n + 1][j] = a[i + n + 1][j], a[i + n][j]
                    n += 1  # On regarde encore plus bas car la pièce vient de tomber d'un cran
                else:
                    break  # Sinon, on ne peut pas faire tomber la pièce, donc on quitte la boucle

# Boucle principale qui traite chaque test (chaque plateau d'entrée)
for _ in range(int(input())):
    # Construction du plateau a à partir des entrées de l'utilisateur
    # On construit d'abord une ligne du haut vide (bords) -- il y a 8 colonnes au total (6 jouables + 2 bords)
    a = [["." for _ in range(8)]]
    # Ensuite, on lit 12 lignes d'entrée, chaque ligne contenant 6 caractères (pour les 6 colonnes jouables)
    for ligne in range(12):
        # On ajoute un bord à gauche, puis les caractères de la ligne, puis un bord à droite
        a.append(["."] + list(input()) + ["."])
    # On ajoute alors une ligne du bas vide (bords)
    a += [["." for _ in range(8)]]

    rensa = 0  # Compteur pour le nombre de réactions en chaîne (combien de fois on efface des groupes)
    while 1:  # Boucle infinie qui ne s'arrête que quand aucune suppression n'est possible
        n = set()  # On initialise l'ensemble qui recueillera toutes les cellules effacées cette étape
        # On parcourt la grille (lignes 1 à 12 -- les lignes sans les bords)
        for i in range(1, 13):
            # On parcourt chaque colonne jouable (1 à 6, sans les bords)
            for j in range(1, 7):
                # Si la cellule contient une couleur jouable (parmi "R", "G", "B", "Y", "P")
                if a[i][j] in ("RGBYP"):
                    # On tente d'effacer un groupe connecté à partir de cette cellule
                    kesu((i, j), set(), a[i][j], 0)
        # Si aucun groupe n'a été supprimé durant cette étape : on arrête la boucle
        if n == set():
            break
        else:
            # Sinon, on augmente le compteur de réactions en chaîne
            rensa += 1
            # On traite les cellules spéciales "O" (bombes) qui explosent si adjacentes à une cellule supprimée
            for i in range(1, 13):
                for j in range(1, 7):
                    if a[i][j] == "O":
                        # Si l'une des cellules autour (haut, bas, gauche, droite) est dans les cellules effacées
                        if (i - 1, j) in n or (i + 1, j) in n or (i, j - 1) in n or (i, j + 1) in n:
                            a[i][j] = "."  # On efface aussi cette bombe en la remplaçant par "."

            # On fait redescendre les pièces tombées dans les trous (lignes vides)
            otosu()
    # A la fin, on affiche le nombre de réactions en chaîne qui ont eu lieu pour ce plateau
    print(rensa)