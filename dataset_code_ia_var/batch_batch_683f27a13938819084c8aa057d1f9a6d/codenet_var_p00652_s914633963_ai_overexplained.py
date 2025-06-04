# AOJ 1067 Cutting a Chocolate
# Code Python3 réécrit avec commentaires extrêmement détaillés
# Explication de chaque ligne et concept, même des notions basiques

from bisect import bisect_left  # Importe la fonction bisect_left du module bisect pour la recherche dichotomique dans une liste triée

while True:  # Boucle sans fin, sera arrêtée par un break dès que la condition de fin de l'entrée est rencontrée
    # Lecture d'une ligne d'entrée utilisateur, contenant cinq entiers séparés par des espaces
    # map(int, ...) convertit chaque élément en entier
    n, m, w, h, S = map(int, input().split())
    if n == 0:  # Condition de terminaison : si n vaut 0, on sort de la boucle
        break

    m = m + 1  # Incrémente m de 1. Ceci est nécessaire car on ajoutera un segment "virtuel" pour encadrer les segments existants
    wh2 = 2 * (w * h)  # Calcule 2 * (w * h) et stocke dans wh2. w et h sont la largeur et la hauteur du rectangle
    S = wh2 - 2 * S  # Met à jour S comme étant wh2 - 2*S, une transformation propre à l'énoncé du problème

    # tbl contiendra les segments de coupe, initialisé avec un segment [0, 0, 0] (correspond au bord gauche)
    tbl = [[0, 0, 0]]  # tbl est une liste de listes représentant les coupes (l, r, r-l)
    s = [0]  # s est une liste des surfaces cumulées à chaque segment, initialisée avec 0

    # Boucle sur les coupes (de 1 à m-1) pour lire leurs bornes gauche et droite
    for i in range(1, m):  # Pour chaque coupe
        l, r = map(int, input().split())  # Lecture de deux entiers : position gauche (l) et droite (r) de la coupe
        tbl.append([l, r, r - l])  # Ajout du segment sous forme d'une liste [l, r, r-l] dans tbl
        s.append((l + r) * w)  # Surface cumulée ajoutée à s. (l+r)*w représente le "poids" de cette coupe

    p = []  # p sera la liste des points, c'est-à-dire les raisins (ou "points d'intérêt" du problème)

    # Lecture des coordonnées des n raisins
    for i in range(n):  # Pour chaque raisin
        x, y = map(float, input().split())  # Lecture de deux float : coordonnées x et y du raisin
        p.append((y, x))  # On ajoute le tuple (y, x) à la liste. Note : y est inséré avant x pour faciliter le tri ultérieur

    # Gestion des cas particuliers
    if S == 0:
        print(n)  # Si la surface S à couvrir est 0, alors tous les raisins sont inclus (aucun n'est omis)
        continue  # Passe à la prochaine entrée
    elif S == wh2:
        print(0)  # Si S est la surface totale, on en enlève tous
        continue  # Passe à la prochaine entrée

    # Trie les raisins p selon la coordonnée y, puis x. p est maintenant trié par la hauteur
    p.sort()

    j = 1  # Initialisation de l'indice j pour les segments
    a = [0] * m  # a est une liste de taille m, remplie de zéros. À l'indice j, a[j] comptera le nombre de raisins dans [j]-ième segment

    # Boucle pour chaque raisin déjà trié par y, x
    for i in range(n):
        y, x = p[i]  # Extraction des coordonnées y et x du i-ème raisin

        # Cette boucle détermine dans quel segment le raisin (x, y) se trouve
        while True:  # Boucle jusqu'à ce que le segment correct soit trouvé
            # Calcul de y1 : la bordure inférieure du segment j-1 à la coordonnée x
            y1 = tbl[j - 1][2] * x / w + tbl[j - 1][0]
            # Calcul de y2 : la bordure supérieure du segment j à la coordonnée x
            y2 = tbl[j][2] * x / w + tbl[j][0]
            # Si y1 < y < y2, c'est que le point (x, y) se trouve dans le segment j
            if y1 < y:
                if y < y2:
                    break  # Segment trouvé, on sort de la boucle while
                j += 1  # Sinon, on avance d'un segment vers la droite
            else:
                j -= 1  # Sinon, on recule d'un segment vers la gauche

        a[j] += 1  # Incrémente le compteur de raisins du segment j

    # À présent, on effectue une somme cumulative de a
    for i in range(1, m):  # Pour chaque segment à partir du deuxième
        a[i] += a[i - 1]  # Incrémente a[i] par a[i-1]. Après cette boucle, a[j] = nb de raisins dans les segments 1 à j inclus

    # Recherche dichotomique pour trouver l’indice j où s[j] >= S (mais le plus petit possible)
    j = bisect_left(s, S, 0, m)  # Recherche de la première position dans s où s[j] >= S
    if s[j] != S:  # Si s[j] n'est pas exactement égal à S, on se met sur la zone précédente
        j -= 1  # On décrémente j pour rester dans la partie admissible

    ans = a[j]  # ans reçoit la valeur du nombre max de raisins dans la surface de taille S initiale
    i = 1  # i est l’indice de début de la fenêtre mobile pour trouver un sous-segment optimal

    # Parcours de tous les sous-segments "coulissants" pour maximiser le nombre de raisins dans une surface <= S
    while j + 1 < m:
        j += 1  # On déplace la fenêtre à droite
        # On déplace i (le début du segment) tant que la surface couverte excède S
        while s[j] - s[i] > S:
            i += 1  # On avance i pour ramener la surface sous la contrainte
        # Mise à jour du maximum de raisins dans un segment de surface admissible
        ans = max(ans, a[j] - a[i])

    # Affichage du résultat final : n - ans est le nombre minimal de raisins à retirer pour obtenir une part ne contenant pas plus de S de surface
    print(n - ans)  # Affiche le résultat, c'est-à-dire le nombre minimal de raisins à retirer