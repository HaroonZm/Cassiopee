import sys

# Importation du module sys qui permet d'interagir avec le système, notamment pour arrêter le programme avec sys.exit()

# Lecture de l'entrée utilisateur
# input() lit une ligne de texte entrée par l'utilisateur sous forme de chaîne de caractères
# .split() sépare cette chaîne en une liste de sous-chaînes à chaque espace
# map(int, ...) transforme chaque sous-chaîne en entier
# list(...) convertit l'objet map en liste
x, y = list(map(int, input().split()))

# Initialisation d'un compteur à 1, ce compteur sera utilisé pour suivre le nombre d'itérations ou d'étapes effectuées
cnt = 1

# Initialisation des deux listes xy et xy2 représentant des coordonnées dans un plan 2D.
# xy est initialisé à [0,0], il représente le coin inférieur gauche d'un rectangle
# xy2 est initialisé à [1,1], il représente le coin supérieur droit du même rectangle.
xy = [0, 0]
xy2 = [1, 1]

# Condition vérifiant si le point (x,y) donné en entrée est contenu dans le rectangle initial défini par xy (coin inférieur gauche)
# et xy2 (coin supérieur droit). Le test utilise 'x >= xy[0]' et 'x < xy2[0]' pour s'assurer que x est dans l'intervalle [xy[0], xy2[0]),
# De même pour la coordonnée y entre xy[1] et xy2[1].
if xy[0] <= x < xy2[0] and xy[1] <= y < xy2[1]:
    # Si la condition est vraie, on imprime la valeur du compteur actuel (1)
    print(cnt)
    # On arrête le programme immédiatement pour ne pas exécuter le reste du code inutilement
    sys.exit(0)

# Boucle infinie (while 1 est équivalent à while True)
# Cette boucle va s'exécuter indéfiniment jusqu'à rencontrer un break ou un sys.exit()
while 1:
    # On applique une modification aux coordonnées des coins du rectangle
    # En fonction du reste de la division euclidienne du compteur cnt par 4,
    # le programme modifie de façon alternée les coordonnées pour élargir ou déplacer le rectangle

    # Si cnt mod 4 égale 1
    if cnt % 4 == 1:
        # On agrandit la coordonnée maximale en x (bord haut droit) en ajoutant la hauteur du rectangle actuel (xy2[1] - xy[1])
        # Cela déplace la limite maximale de x vers la droite d'une distance égale à la hauteur actuelle du rectangle
        xy2[0] += xy2[1] - xy[1]

    # Si cnt mod 4 égale 2
    elif cnt % 4 == 2:
        # On agrandit la coordonnée maximale en y (bord haut droit) en ajoutant la largeur du rectangle actuel (xy2[0] - xy[0])
        # Cela déplace la limite maximale de y vers le haut d'une distance égale à la largeur actuelle du rectangle
        xy2[1] += xy2[0] - xy[0]

    # Si cnt mod 4 égale 3
    elif cnt % 4 == 3:
        # On réduit la coordonnée minimale en x (bord bas gauche) en soustrayant la hauteur actuelle du rectangle
        # Cela déplace la limite minimale de x vers la gauche d'une distance égale à la hauteur actuelle du rectangle
        xy[0] -= xy2[1] - xy[1]

    # Si cnt mod 4 égale 0
    elif cnt % 4 == 0:
        # On réduit la coordonnée minimale en y (bord bas gauche) en soustrayant la largeur actuelle du rectangle
        # Cela déplace la limite minimale de y vers le bas d'une distance égale à la largeur actuelle du rectangle
        xy[1] -= xy2[0] - xy[0]

    # Après avoir modifié les limites du rectangle, on vérifie à nouveau si le point (x,y) est dans ce nouveau rectangle
    # Le test est toujours la même condition d'inclusion: x dans [xy[0], xy2[0]) et y dans [xy[1], xy2[1])
    if xy[0] <= x < xy2[0] and xy[1] <= y < xy2[1]:
        # Si le point est dans le rectangle, on imprime un nombre calculé à partir de cnt modulo 3 plus 1
        # Cela donne toujours un entier parmi {1, 2, 3}
        print((cnt % 3) + 1)
        # On sort de la boucle infinie forçant la fin du programme
        break

    # On incrémente le compteur cnt de 1 pour passer à l'itération suivante
    cnt += 1