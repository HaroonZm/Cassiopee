# Boucle principale : elle va s'exécuter un certain nombre de fois, chaque itération représente un "test" ou une opération indépendante
for _ in range(int(input())):
    # Lecture et conversion des coordonnées et dimensions du rectangle depuis l'entrée standard
    # input() lit une ligne de texte au clavier
    # split() découpe cette ligne en morceaux d'après les espaces
    # map(int, ...) convertit chaque morceau en entier
    # x = abscisse du coin inférieur gauche du rectangle
    # y = ordonnée du coin inférieur gauche du rectangle
    # w = largeur du rectangle (selon l'axe x)
    # h = hauteur du rectangle (selon l'axe y)
    x, y, w, h = map(int, input().split())

    # Initialisation du compteur qui sert à compter combien de points sont à l'intérieur ou sur le bord du rectangle
    c = 0

    # Deuxième boucle : on va demander combien de points on veut traiter dans ce test
    # Cette nouvelle entrée nous indique le nombre de points à considérer pour ce rectangle
    for _ in range(int(input())):
        # Lecture des coordonnées d'un point
        a, b = map(int, input().split())  # a = abscisse du point, b = ordonnée du point

        # Vérification si le point (a, b) est à l'intérieur OU sur le bord du rectangle
        # Le rectangle commence en (x, y), s'étend jusqu'à (x + w) selon l'axe x
        # et jusqu'à (y + h) selon l'axe y
        # On utilise les opérateurs de comparaison <= et >= pour inclure les bords
        if x <= a <= x + w and y <= b <= y + h:
            # Si la condition est vraie, le point est dans ou sur le rectangle, on incrémente le compteur
            c += 1

    # Affichage du résultat final pour ce "test" : combien de points étaient dans le rectangle
    print(c)