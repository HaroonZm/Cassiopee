# Demander à l'utilisateur de saisir un nombre entier qui sera attribué à la variable n
# Ceci déterminera combien de fois la boucle principale se répétera
n = int(input())

# Boucler n fois, c'est-à-dire exécuter le bloc suivant pour chaque cas de test donné
# "_" est un nom de variable valide, souvent utilisé lorsque la valeur de la variable n'est pas utilisée à l'intérieur de la boucle
for _ in range(n):
    # Demander à l'utilisateur de saisir quatre entiers séparés par un espace sur une seule ligne
    # Utilisation de input() pour obtenir la chaîne, split() pour séparer les différentes valeurs, puis map(int, ...) pour convertir chaque string en int
    # Cela représente le coin supérieur gauche (x1, y1) d'un rectangle, suivi de sa largeur (w) et de sa hauteur (h)
    x1, y1, w, h = map(int, input().split())

    # Calculer la coordonnée x du coin inférieur droit du rectangle
    # On l'obtient en ajoutant la largeur w à la coordonnée x du coin supérieur gauche x1
    x2 = x1 + w

    # Calculer la coordonnée y du coin inférieur droit du rectangle
    # On l'obtient en ajoutant la hauteur h à la coordonnée y du coin supérieur gauche y1
    y2 = y1 + h

    # Demander à l'utilisateur de saisir un entier qui représente le nombre de points à tester
    m = int(input())

    # Initialiser un compteur à zéro pour compter combien de points sont à l'intérieur du rectangle
    cnt = 0

    # Boucler exactement m fois, c'est-à-dire une fois pour chaque point à tester
    for _ in range(m):
        # Lire une ligne contenant deux entiers séparés, représentant les coordonnées x et y d'un point
        x, y = map(int, input().split())

        # Vérifier si le point (x, y) se trouve DANS le rectangle
        # On vérifie que la composante x du point est comprise entre x1 et x2 (bornes incluses)
        # On vérifie également que la composante y du point est comprise entre y1 et y2 (bornes incluses)
        # Les signes <= signifient "inférieur ou égal à" et "supérieur ou égal à", donc les bords du rectangle sont inclus
        if x1 <= x <= x2 and y1 <= y <= y2:
            # Si le point est à l'intérieur du rectangle, augmenter le compteur de 1
            cnt += 1

    # Après avoir vérifié tous les points pour ce rectangle, afficher le résultat
    # Cela affiche le nombre total de points qui se trouvent à l'intérieur du rectangle (y compris sur les bords)
    print(cnt)