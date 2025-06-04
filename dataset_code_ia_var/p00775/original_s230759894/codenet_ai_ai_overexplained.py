#!/usr/bin/env python

# Importation de toutes les fonctions du module math (par exemple : sqrt, etc.)
from math import *

# Boucle principale infinie, tant que l'utilisateur ne décide pas d'arrêter
while True:
    # Lecture de deux entiers sur une ligne, séparés par un espace
    # raw_input() lit l'entrée de l'utilisateur sous forme de chaîne de caractères
    # split() découpe la chaîne en morceaux selon les espaces
    # map(int, ...) convertit chacun des morceaux en un entier
    # On assigne ces deux entiers à r (le rayon) et n (le nombre de descriptions de murs)
    r, n = map(int, raw_input().split())

    # Si la valeur de r vaut zéro, on arrête la boucle avec "break"
    # On suppose que cela sert de condition d'arrêt pour le programme
    if r == 0:
        break

    # Création d'un dictionnaire (type mappage, ici nommé "m")
    # Ce dictionnaire servira à stocker la hauteur maximale pour chaque abscisse entière de -50 à 49 incluse
    m = {}
    # Pour chaque entier i allant de -50 inclus à 50 exclus
    for i in range(-50, 50):
        # On initialise la hauteur maximum à zéro pour chaque position associée à i
        m[i] = 0

    # On fait une boucle sur le nombre n : cela correspond à traiter n murs/segments
    for loop in range(n):
        # Lecture de trois entiers : x1 (début du mur), x2 (fin du mur non inclus), h (hauteur du mur)
        x1, x2, h = map(int, raw_input().split())
        # Pour chaque abscisse entière comprise entre x1 inclus et x2 exclus
        for i in range(x1, x2):
            # On met à jour dans le dictionnaire m à la position i, la hauteur maximale
            # Cela compare la hauteur déjà présente (m[i]) et celle du nouveau mur (h)
            m[i] = max(m[i], h)

    # Initialisation de la variable ans à 100
    # Cela va contenir la valeur minimale finale à afficher
    ans = 100

    # Première boucle : pour chaque valeur entière i entre -r inclus et 0 exclus
    for i in range(-r, 0):
        # Calcul du reste/rem (c'est un nom de variable) pour cette abscisse i
        # r est le rayon donné
        # (i + 1) est le décalage de l'abscisse 
        # sqrt(r * r - (i + 1) * (i + 1)) calcule la racine carrée de (r^2 - (i+1)^2)
        # Donc r - sqrt(...) donne une sorte de hauteur relative
        # On y ajoute la hauteur du mur à la position i, contenue dans le dictionnaire m
        rem = r - sqrt(r * r - (i + 1) * (i + 1)) + m[i]
        # On garde à chaque itération la plus petite valeur de rem obtenue, en la comparant à ans
        ans = min(rem, ans)

    # Deuxième boucle : pour chaque valeur entière i entre 0 inclus et r exclus
    for i in range(0, r):
        # Calcul similaire à la boucle précédente, mais cette fois sans le +1
        rem = r - sqrt(r * r - i * i) + m[i]
        # Mise à jour éventuelle de la plus petite valeur
        ans = min(rem, ans)

    # Affichage de la valeur finale (la plus petite trouvée), sans retour à la ligne supplémentaire
    print ans