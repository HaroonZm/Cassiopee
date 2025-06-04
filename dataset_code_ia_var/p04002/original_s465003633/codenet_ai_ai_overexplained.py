# Définition d'une fonction anonyme (lambda) f qui, lorsqu'elle est appelée, lit une ligne depuis l'entrée standard (input()),
# sépare cette ligne en utilisant les espaces comme séparateur (split()), puis applique la fonction int() à chaque élément.
# Cela retourne donc un objet map dont chaque élément est un entier provenant de la saisie utilisateur.
f = lambda: map(int, input().split())

# Appel de la fonction f pour lire trois entiers à la suite depuis l'entrée,
# qui seront affectés respectivement aux variables h, w et n.
# h : hauteur de la grille
# w : largeur de la grille
# n : nombre de points à lire ensuite
h, w, n = f()

# Initialisation de la liste c, qui va contenir le nombre de grilles 3x3 contenant exactement k points marqués (avec k de 0 à 9).
# (h-2)*(w-2) correspond au nombre total possible de sous-grilles 3x3 complètement contenues dans la grille h x w.
# C'est-à-dire, les sous-grilles qui ne débordent pas du cadre.
# [0]*9 crée une liste de neuf zéros pour les compteurs de 1 à 9 points.
c = [(h-2)*(w-2)] + [0]*9

# Initialisation d'un dictionnaire d vide.
# Ce dictionnaire servira à compter, pour chaque sous-grille 3x3 (identifiée par ses coordonnées en haut à gauche), 
# combien de points marqués elle contient.
d = {}

# Début d'une boucle while, qui va tourner n fois, afin de traiter chacun des n points donnés.
while n:
    # On décrémente n de 1 à chaque itération pour progresser dans la boucle.
    n -= 1

    # Lecture depuis l'entrée standard de deux entiers x et y, correspondant à la position d'un point marqué.
    x, y = f()

    # Pour chaque point marqué à la position (x, y), ce point peut appartenir à jusqu'à 9 sous-grilles 3x3 différentes.
    # On parcourt ainsi les 9 positions de sous-grilles potentielles autour du point marqué.
    # La variable i va de 0 à 8 pour représenter ces 9 configurations.
    for i in range(9):

        # Calcul des coordonnées (a) du coin supérieur gauche de la sous-grille 3x3 actuellement considérée.
        # i%3 donne le décalage horizontal de -1, 0 ou 1 ; i//3 donne le décalage vertical.
        # Le but est de "balayer" toutes les sous-grilles 3x3 contenues dans la grille et contenant (x, y).
        a = (x + i % 3, y + i // 3)

        # Condition : on vérifie que la sous-grille considérée (dont le coin supérieur gauche est a) est entièrement
        # contenue dans la grille. On veut que : 
        # - la coordonnée a[0] (x de la sous-grille) soit comprise strictement entre 1 et h-2 (donc 2 < a[0] <= h)
        # - la coordonnée a[1] (y de la sous-grille) soit comprise strictement entre 1 et w-2 (donc 2 < a[1] <= w)
        # Correction: en fait les bornes sont telles que h >= a[0] > 2 et w >= a[1] > 2
        if h >= a[0] > 2 < a[1] <= w:
            # On utilise le tuple a comme clé dans le dictionnaire d.
            # d.get(a, 0) récupère pour cette sous-grille son compteur actuel (défaut 0 si clé absente).
            # On incrémente ce compteur de 1 pour signaler qu'il y a un point marqué supplémentaire dans la sous-grille.
            d[a] = d.get(a, 0) + 1

            # On met à jour la liste c pour refléter cette modification:
            # On réduit de 1 le compteur pour le nombre de sous-grilles ayant "précédemment" d[a]-1 points marqués.
            c[d[a] - 1] -= 1

            # On augmente de 1 le compteur pour le nombre de sous-grilles ayant "maintenant" d[a] points marqués.
            c[d[a]] += 1

# A la fin de toutes les insertions, on affiche la liste c comme une série d'entiers séparés par des espaces.
# Chacun correspond au nombre de sous-grilles 3x3 contenant 0, 1, ... jusqu'à 9 points marqués.
print(*c)