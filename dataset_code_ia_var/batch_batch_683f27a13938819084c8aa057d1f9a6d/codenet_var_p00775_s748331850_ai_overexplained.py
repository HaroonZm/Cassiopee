# Importation de la fonction sqrt (racine carrée) du module math.
# Le module math contient des fonctions mathématiques standard, et sqrt calcule la racine carrée d'un nombre.
from math import sqrt

# Définition d'une fonction appelée inpl, qui ne prend pas d'argument.
# Cette fonction lit une ligne depuis l'entrée standard (input()), segmente la chaîne obtenue via .split() (qui découpe sur les espaces), applique à chaque morceau la fonction int (pour convertir chaque sous-chaîne en entier), puis rassemble tous ces entiers dans une liste via list().
# Cela permet d'obtenir facilement une liste d'entiers depuis une ligne de texte saisie par l'utilisateur.
def inpl():
    return list(map(int, input().split()))

# Lecture depuis l'entrée standard de deux entiers. La fonction inpl retourne une liste de deux entiers, qui sont affectés respectivement à R et N.
R, N = inpl()

# Démarre une boucle qui continue tant que la variable R (correspondant au rayon) est non nulle (si R vaut 0, la boucle s'arrête).
while R:
    # Création d'une liste H de 41 éléments, initialisée à zéro.
    # Cette liste va servir à stocker des hauteurs maximales pour des positions données, indexées de façon décalée.
    H = [0] * 41  # H[0] correspond à la position -20, ..., H[20] à position 0, ..., H[40] à position 20.

    # Initialisation de deux variables, r0 et l0, qui vont mémoriser des hauteurs maximales pour certains intervalles spéciaux.
    r0 = 0
    l0 = 0

    # Répète N fois (pour chaque obstacle à traiter).
    for _ in range(N):
        # Lit trois entiers : les positions gauche l, droite r, et la hauteur h de l'obstacle.
        l, r, h = inpl()

        # Si l < 0 et r >= 0, cela signifie que l'obstacle recouvre le zéro par la droite.
        # On met à jour l0 pour retenir la plus grande hauteur de ce genre d'obstacle.
        if l < 0 and r >= 0:
            l0 = max(l0, h)

        # Si l <= 0 et r > 0, l'obstacle recouvre le zéro par la gauche.
        # On met à jour r0 pareillement.
        if l <= 0 and r > 0:
            r0 = max(r0, h)

        # Ajustement des bornes gauche et droite pour exclure la position zéro sauf cas particuliers.
        # Si l <= 0, cela signifie que le point zéro est inclus dans le segment, donc on l'augmente de 1 pour l'exclure.
        l += (l <= 0)
        # Si r >= 0, cela veut dire que la position zéro est incluse, on la retire en diminuant r de 1.
        r -= (r >= 0)

        # Pour chaque position i du segment [l, r], on augmente de 1 l'indice de base (car la liste H est décalée).
        # (i ≠ 0 car le traitement du zéro est particulier plus loin)
        for i in range(l, r + 1):
            if i != 0:
                # On attribue à la position H décalée (i+20) la hauteur maximale rencontrée jusqu'à présent pour cette position.
                # Cela représente la plus grande hauteur sur ce segment.
                H[i + 20] = max(H[i + 20], h)

    # On met à jour la hauteur associée à la position zéro (c'est H[20]) comme étant le minimum de l0 et r0.
    # Cela gère le cas où le positionnement exact sur zéro doit prendre la plus petite des deux hauteurs "bordure" qui recouvrent zéro.
    H[20] = min(l0, r0)

    # Initialisation de la variable de résultat "ans" à 20.
    # Cela semble être une valeur suffisamment grande pour être réduite dans la suite.
    ans = 20

    # Parcours toutes les positions x comprises entre (-R + 1) inclus et (R - 1) inclus (suppose R > 0).
    for x in range(-R + 1, R):
        # Calcul du "temps" (ou de la hauteur minimale pour atteindre un point), ce qui dépend de R, de x et de la hauteur d'obstacle associée à x (obtenue par H[x+20]).
        # L'expression sqrt(R**2 - x**2) donne la hauteur du cercle d'équation x^2 + y^2 = R^2, donc R - sqrt(...) donne la "profondeur" verticale jusqu'à la surface.
        # Ensuite on ajoute la hauteur de l'obstacle présent en x.
        time = R - sqrt(R ** 2 - x ** 2) + H[x + 20]

        # On conserve la plus petite valeur de "time" rencontrée, dans ans.
        ans = min(ans, time)

    # Affiche la valeur minimale finale calculée.
    print(ans)

    # Relit deux nouveaux entiers pour la prochaine itération (prochain cas ou ensemble d'obstacles). Si R devient zéro, la boucle s'arrête.
    R, N = inpl()