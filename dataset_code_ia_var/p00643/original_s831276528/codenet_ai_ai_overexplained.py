from heapq import heappush, heappop  # Importation des fonctions heappush et heappop du module heapq pour gérer la file de priorité

while True:  # Boucle infinie qui permettra de traiter plusieurs jeux de données jusqu'à la condition d'arrêt
    h, w = map(int, input().split())  # Lecture du nombre de lignes (h) et du nombre de colonnes (w) de la grille, entrée par l'utilisateur
    if h == 0:  # Condition d'arrêt : si le nombre de lignes est égal à 0 (indiqué par l'utilisateur), on s'arrête
        break  # Quitte la boucle infinie, donc le programme s'arrête ici

    # Construction de la grille ('mp'), avec une bordure de -1 tout autour pour simplifier la gestion des bords
    mp = []
    for _ in range(h):
        # Lecture d'une ligne de la grille, chaque valeur convertie en int
        # Ajout d'un -1 au début et à la fin de chaque ligne pour marquer les bords
        row = list(map(int, input().split()))
        mp.append([-1] + row + [-1])
    # Ajout d'une ligne de -1 en haut et en bas de la grille pour compléter la bordure
    mp.insert(0, [-1] * (w + 2))  # Ligne de -1 au début (haut)
    mp.append([-1] * (w + 2))     # Ligne de -1 à la fin (bas)

    # Lecture de la position de départ (sy, sx) et d'arrivée (gy, gx)
    sy, sx = map(int, input().split())  # Position de départ, indices d'origine 0, colonne puis ligne
    gy, gx = map(int, input().split())  # Position d'arrivée, mêmes remarques
    # Décalage de +1 sur les indices pour compenser la bordure noire ajoutée autour de la grille
    sy += 1
    sx += 1
    gy += 1
    gx += 1

    # Initialisation de la file de priorité min-heap avec l'état initial du dé (position et orientation)
    que = []  # La priorité ici sera donnée par la pénalité accumulée
    # Les valeurs concernant le dé : top, south, east représentent le chiffre sur le dessus, au sud, et à l'est du dé
    # Le dé est initialement orienté avec 'top'=1, 'south'=2, 'east'=3
    heappush(que, (0, sx, sy, 1, 2, 3))  # On commence avec une pénalité de 0

    # Dictionnaire servant à mémoriser le coût minimum pour atteindre chaque configuration (position + orientation du dé)
    dic = {}
    # Clé : (x, y, top, south, east) ; valeur : coût minimal pour atteindre cet état
    dic[(sx, sy, 1, 2, 3)] = 0

    # Directions dans lesquelles le dé peut rouler : droite, haut, gauche, bas (dx, dy)
    vec = (
        (1, 0),   # Vers la droite
        (0, -1),  # Vers le haut
        (-1, 0),  # Vers la gauche
        (0, 1)    # Vers le bas
    )

    # Fonction pour calculer la nouvelle orientation du dé après un mouvement
    # On suppose ici un dé conventionnel où les faces opposées s'additionnent à 7
    def spin(top, south, east, direct):
        # direct est un tuple (dx, dy) indiquant la direction du mouvement
        if direct == (1, 0):  # Roule vers la droite
            # Le dessus devient opposé de east, le sud reste, l'est devient top
            return 7 - east, south, top
        if direct == (0, -1):  # Roule vers le haut
            # Le dessus devient sud, le sud devient opposé de top, l'est reste
            return south, 7 - top, east
        if direct == (-1, 0):  # Roule vers la gauche
            # Le dessus devient est, le sud reste, l'est devient opposé de top
            return east, south, 7 - top
        if direct == (0, 1):  # Roule vers le bas
            # Le dessus devient opposé de sud, le sud devient top, l'est reste
            return 7 - south, top, east

    # Boucle principale utilisant l'algorithme de Dijkstra pour trouver le chemin minimal
    while que:  # Tant qu'il reste des états à explorer dans la file de priorité
        # On extrait l’état avec la pénalité (poids) minimale
        pena, x, y, top, south, east = heappop(que)

        # Condition d'arrivée : si la position actuelle correspond à celle demandée, on affiche la pénalité
        if (x, y) == (gx, gy):
            print(pena)  # Affichage du coût minimal pour atteindre la destination avec le dé dans une quelconque orientation
            break        # On arrête ce scénario et passe au suivant

        # On regarde toutes les directions dans lesquelles on peut déplacer le dé
        for dx, dy in vec:
            nx, ny = x + dx, y + dy  # Calcul du voisin : nouvelle position possible du dé après le mouvement

            if mp[ny][nx] == -1:
                # Si la case d'arrivée est en dehors de la grille (c'est-à-dire sur la bordure de -1), on ignore ce mouvement
                continue

            # On calcule la nouvelle orientation du dé après avoir bougé dans cette direction
            new_top, new_south, new_east = spin(top, south, east, (dx, dy))

            # Calcul du nouveau coût (penalité) pour arriver à cette case
            # La règle est : ajout du poids de la case multiplié par (7 - face sur le dessus après le roulement)
            # (7 - new_top) inversant la face -> sur un dé, faces opposées = 7
            new_pena = pena + (7 - new_top) * mp[ny][nx]

            # Si cette nouvelle configuration (position + orientation du dé) n'a pas encore été visitée,
            # on l'ajoute au dictionnaire avec la pénalité trouvée, sinon on l'ignore (Dijkstra ne revisitera pas un état déjà optimisé)
            if (nx, ny, new_top, new_south, new_east) not in dic:
                dic[(nx, ny, new_top, new_south, new_east)] = new_pena  # On enregistre le coût pour cet état
                heappush(que, (new_pena, nx, ny, new_top, new_south, new_east))  # On ajoute ce nouvel état à explorer plus tard