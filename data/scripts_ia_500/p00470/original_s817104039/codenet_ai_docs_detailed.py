def count_paths():
    """
    Lit plusieurs cas de dimensions (largeur w et hauteur h) depuis l'entrée standard,
    calcule et affiche pour chaque cas le nombre de chemins spécifiques modulo 100000.
    Le programme s'arrête lorsque w et h sont tous deux nuls.

    Le calcul utilise une programmation dynamique avec un tableau 3D `dp` où:
        - La première dimension (0 à 3) représente quatre états différents de direction/transitions.
        - Les autres dimensions représentent les coordonnées y (hauteur) et x (largeur) dans une grille.

    Etats dans dp:
        0: transition de direction "up" à "up"
        1: transition de direction "up" à "right"
        2: transition de direction "right" à "up"
        3: transition de direction "right" à "right"

    La logique compte les chemins possibles avec ces contraintes de changement de direction.
    """

    while True:
        # Lecture de deux entiers w (largeur) et h (hauteur) séparés par un espace
        w, h = map(int, raw_input().split())

        # Condition d'arrêt : lorsque w et h sont simultanément zéro
        if w | h == 0:
            break

        # Initialisation d'un tableau 3D dp avec 4 couches pour les états,
        # et (h+1) x (w+1) pour les positions sur la grille.
        # Chaque valeur est initialisée à zéro.
        dp = [[[0] * (w + 1) for _ in xrange(h + 1)] for _ in xrange(4)]

        # Initialisation des cas de base pour commencer les chemins
        # dp[0][1][0] = 1 signifie qu'on a une position verticale atteinte
        # dp[3][0][1] = 1 signifie qu'on a une position horizontale atteinte
        dp[0][1][0] = 1  # Etat up->up à la position (y=1,x=0)
        dp[3][0][1] = 1  # Etat right->right à la position (y=0,x=1)

        # Parcours de toutes les positions valides de la grille
        for y in xrange(h):
            for x in xrange(w):
                # Mise à jour des états possibles en fonction des transitions

                # Prolonge un chemin en allant vers le haut (up->up) 
                # en additionnant les chemins qui continuent verticalement 
                # ou qui viennent d'un virage (right->up)
                dp[0][y + 1][x] += dp[0][y][x] + dp[2][y][x]

                # Prolonge un chemin avec un changement de direction de up->right
                dp[1][y][x + 1] += dp[0][y][x]

                # Prolonge un chemin avec un changement de direction de right->up
                dp[2][y + 1][x] += dp[3][y][x]

                # Prolonge un chemin en allant vers la droite (right->right)
                # en additionnant les chemins qui continuent horizontalement
                # ou qui viennent d'un virage (up->right)
                dp[3][y][x + 1] += dp[1][y][x] + dp[3][y][x]

        # Somme des chemins possibles dans les 4 états, position en bas à droite (h-1,w-1)
        # Modulo 100000 pour éviter les nombres trop grands
        result = sum(dp[i][h - 1][w - 1] for i in xrange(4)) % 100000

        # Affichage du résultat pour ce cas
        print result

# Appel de la fonction principale
count_paths()