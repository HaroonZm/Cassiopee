def bomb(y, x, a):
    # La fonction 'bomb' modifie une grille 'a' en remplaçant certaines cellules par '0' à partir d'une position donnée (y, x).
    # 'y' est l'indice de la ligne (axe vertical) dans la grille, 'x' est l'indice de la colonne (axe horizontal).
    # 'a' est une liste de listes représentant la grille, chaque élément est un caractère.
    
    a[y][x] = '0'  
    # La cellule à la position (y, x) dans la grille 'a' est modifiée pour contenir le caractère '0'.
    # Cela signifie que ce point est "explosé" ou "marqué" d'une certaine façon.
    
    # Création d'une liste 'b' contenant des couples [dx, dy], où dx et dy représentent des décalages horizontaux et verticaux.
    # Ces décalages représentent les positions autour du point actuel qui doivent être vérifiées.
    # On considère ici les positions situées à 1, 2 ou 3 cases à droite, gauche, en haut ou en bas (pas en diagonale).
    b = [[-3, 0], [-2, 0], [-1, 0], [1, 0], [2, 0], [3, 0],
         [0, -3], [0, -2], [0, -1], [0, 1], [0, 2], [0, 3]]
    
    # Parcours de chacun des décalages dans 'b'.
    for dx, dy in b:
        # Calcul des nouvelles coordonnées en ajoutant le décalage aux coordonnées actuelles.
        # On vérifie ensuite que ces nouvelles coordonnées sont valides, c'est-à-dire qu'elles restent dans la grille de taille 8x8.
        # 0 <= x + dx < 8 garantit que la colonne est dans l'intervalle autorisé (de 0 à 7).
        # 0 <= y + dy < 8 garantit que la ligne est dans l'intervalle autorisé (de 0 à 7).
        # On ajoute 0 et compare avec 8 car les indices vont de 0 à 7 sur une grille de 8 lignes et 8 colonnes.
        # Enfin, on vérifie que la cellule cible dans la grille 'a' contient le caractère '1'.
        if 0 <= x + dx < 8 and 0 <= y + dy < 8 and a[y + dy][x + dx] == '1':
            # Si toutes ces conditions sont remplies, on appelle récursivement la fonction 'bomb'
            # avec la nouvelle position (y + dy, x + dx) pour continuer à "exploser" à partir de là.
            bomb(y + dy, x + dx, a)

    # Une fois toutes les explosions autour de la position initiale traitées, on retourne la grille modifiée.
    return a

# Le bloc suivant traite plusieurs jeux de données en fonction d'un nombre donné en entrée.
for i in range(int(input())):
    # On lit une ligne d'entrée qui n'est pas utilisée ici (probablement une ligne vide ou un séparateur entre données).
    input()
    # On construit la grille 'a' en lisant 8 lignes successives.
    # Chaque ligne est transformée en liste de ses caractères (grâce à list(input())).
    # La variable 'a' sera donc une liste de 8 listes, chacune contenant 8 caractères.
    a = [list(input()) for _ in range(8)]
    
    # Lecture des coordonnées 'x' et 'y' en entrée, données comme des entiers.
    x = int(input())
    y = int(input())

    # Appel de la fonction 'bomb' avec les coordonnées ajustées de 1 vers 0 pour correspondre aux indices Python (0-based).
    bomb(y - 1, x - 1, a)
    
    # Affichage de l'en-tête du jeu de données, en affichant le numéro commençant à 1.
    print('Data %d:' % (i+1))
    
    # Pour chaque ligne de la grille résultante, on imprime la ligne sous forme de chaîne de caractères sans espaces.
    # Le *x décompose la liste en éléments individuels pour 'print', sep='' enlève les espaces entre les caractères.
    [print(*x, sep='') for x in a]