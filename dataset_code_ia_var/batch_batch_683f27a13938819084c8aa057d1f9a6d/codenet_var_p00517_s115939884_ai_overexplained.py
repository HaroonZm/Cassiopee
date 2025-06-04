# Lecture de trois entiers depuis l'entrée standard, séparés par des espaces
# - w : largeur ou limite maximale possible pour la coordonnée x
# - h : hauteur ou limite maximale possible pour la coordonnée y
# - n : nombre total de points à traiter (le premier point est le point de départ)
w, h, n = map(int, input().split())

# Création d'une liste vide pour stocker les coordonnées (x, y) de chaque point
dist = []

# Boucle sur une plage de taille 'n' (c'est-à-dire que la boucle s'exécutera 'n' fois)
for _ in range(n):
    # Lecture d'une ligne d'entrée contenant deux entiers séparés par des espaces
    # Affectation de ces valeurs à x et y à l'aide de map et split
    x, y = map(int, input().split())
    # Ajout du couple (x, y) à la liste 'dist' sous forme de sous-liste
    dist.append([x, y])

# Retrait du premier point de la liste 'dist' à l'aide de la méthode pop(0)
# Ceci supprime et renvoie l'élément à l'index 0, à savoir le point de départ
start = dist.pop(0)

# Extraction des coordonnées x et y du point de départ pour initialiser x1 et y1
x1, y1 = start

# Initialisation du compteur à zéro; ce compteur va servir à compter le nombre total d'étapes effectuées
cnt = 0

# Parcours de tous les points restants dans 'dist'
for d in dist:
    # Extraction des coordonnées cibles x2 et y2 pour ce point
    x2, y2 = d
    # Boucle infinie pour déplacer (x1, y1) vers (x2, y2) étape par étape
    while 1:
        # Si le point courrant (x1, y1) a atteint le point cible (x2, y2),
        # la boucle s’arrête à l’aide de break
        if x1 == x2 and y1 == y2:
            break

        # Incrémentation du compteur à chaque étape de déplacement
        cnt += 1
        # Si les deux coordonnées courantes sont strictement inférieures aux coordonnées cibles :
        # Cela signifie que l’on peut se déplacer diagonalement en (x, y)
        if x1 < x2 and y1 < y2:
            x1 += 1   # Incrémenter x1 pour se rapprocher de x2
            y1 += 1   # Incrémenter y1 pour se rapprocher de y2
        # Si x est déjà aligné mais pas y : il faut augmenter y pour atteindre y2
        elif x1 == x2 and y1 < y2:
            y1 += 1   # Incrémenter y1 jusqu'à atteindre y2
        # Si on se trouve à droite du point cible mais en dessous de lui
        elif x1 > x2 and y1 < y2:
            # S'il est encore possible d'augmenter y sans dépasser la limite supérieure h
            if y1 != h:
                y1 += 1 # Incrémenter y1 si possible
            else:
                x1 -= 1 # Sinon, décrémenter x1 pour s'approcher de x2
        # Si y est aligné mais x doit encore être augmenté
        elif x1 < x2 and y1 == y2:
            x1 += 1    # Incrémenter x1
        # Si y est aligné mais x doit être diminué
        elif x1 > x2 and y1 == y2:
            x1 -= 1    # Décrémenter x1
        # Maintenant, si y doit être décrémenté et x augmenté
        elif x1 < x2 and y1 > y2:
            # Vérifie si l'on peut décrémenter y1 sans passer en dessous de zéro
            if y1 != 0:
                y1 -= 1 # Décrémenter y1
            else:
                x1 += 1 # Sinon, incrémenter x1
        # Si x est aligné mais y doit être décrémenté
        elif x1 == x2 and y1 > y2:
            y1 -= 1    # Décrémenter y1
        # Si les deux coordonnées sont supérieures aux cibles, on se rapproche diagonalement vers le coin en haut à gauche
        elif x1 > x2 and y1 > y2:
            x1 -= 1    # Décrémenter x1
            y1 -= 1    # Décrémenter y1

# Lorsque toutes les étapes sont terminées, afficher la valeur finale du compteur cnt
print(cnt)