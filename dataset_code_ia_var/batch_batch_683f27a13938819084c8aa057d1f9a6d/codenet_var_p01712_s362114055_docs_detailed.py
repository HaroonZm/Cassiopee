def read():
    """
    Lit une ligne d'entrée standard, divise par les espaces et convertit chaque élément en entier.

    Returns:
        list: Liste d'entiers lus depuis l'entrée standard.
    """
    return list(map(int, input().split()))

while True:
    try:
        # Lecture du nombre de bases, de la largeur et de la hauteur depuis l'entrée.
        n, w, h = read()

        # Initialisation de la liste des bases, chaque base étant un triplet (x, y, r).
        bases = [(0, 0, 0)] * n
        for i in range(n):
            # Lecture des coordonnées x, y et du rayon w de la base i.
            bases[i] = read()
    except:
        # Fin de l'entrée ou erreur, sortie de la boucle principale.
        break

    # --------- Test de couverture horizontale (selon l'axe x) -------------
    res1 = True  # Résultat du test de couverture de la largeur
    # Pour chaque base, on calcule son intervalle de couverture sur l'axe x : [x-w, x+w]
    intervals_x = sorted([(x - w, x + w) for x, y, w in bases], key=lambda lr: lr[0])
    ls, rs = zip(*intervals_x)  # Sépare les bornes gauche et droite

    x = 0  # “Frontière” courante couverte
    for l, r in zip(ls, rs):
        # Vérifie si la prochaine couverture commence avant ou à la fin de la zone déjà couverte
        res1 &= (l <= x)
        # Étend la zone couverte jusqu'à la fin de l'intervalle courant si possible
        x = max(x, r)
    # Vérifie que l'extrémité droite de la zone (w) est également couverte
    res1 &= (w <= x)

    # --------- Test de couverture verticale (selon l'axe y) -------------
    res2 = True  # Résultat du test de couverture de la hauteur
    # Pour chaque base, on calcule son intervalle de couverture sur l'axe y : [y-w, y+w]
    intervals_y = sorted([(y - w, y + w) for x, y, w in bases], key=lambda lr: lr[0])
    ls, rs = zip(*intervals_y)  # Sépare les bornes gauche et droite

    x = 0  # “Frontière” courante couverte
    for l, r in zip(ls, rs):
        # Vérifie si la prochaine couverture commence avant ou à la fin de la zone déjà couverte
        res2 &= (l <= x)
        # Étend la zone couverte jusqu'à la fin de l'intervalle courant si possible
        x = max(x, r)
    # Vérifie que l'extrémité supérieure de la zone (h) est également couverte
    res2 &= (h <= x)

    # Affiche "Yes" si la zone [0, w] ou [0, h] est complètement couverte, sinon "No"
    print("Yes" if res1 or res2 else "No")