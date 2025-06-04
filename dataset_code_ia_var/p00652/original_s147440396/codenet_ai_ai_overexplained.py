# Ce code résout le problème 1067 "Cutting a Chocolate" de l'AOJ.
# Il est écrit pour Python 3. L'auteur original est bal4u.

from bisect import bisect_left  # Importe une fonction utile pour les recherches binaires dans les listes triées.

while True:  # Boucle infinie pour traiter de multiples cas de tests, jusqu'à ce qu'une condition d'arrêt soit rencontrée.
    # Lit une ligne de l'entrée standard, la divise en entiers, puis les assigne aux variables respectives.
    n, m, w, h, S = map(int, input().split())
    
    if n == 0:
        break  # Condition d'arrêt : si le nombre de points 'n' est 0, sort de la boucle.
    
    # Incrémente 'm' de 1 (le nombre de sections horizontales).
    m = m + 1
    
    # Calcule deux fois l'aire totale du rectangle de chocolat.
    wh2 = 2 * (w * h)
    
    # Met à jour la valeur 'S' en soustrayant deux fois la surface d'intérêt à l'aire totale du rectangle.
    # Cela permet d'obtenir une valeur représentant la différence par rapport à la surface cible.
    S = wh2 - 2 * S

    # Initialise une table 'tbl' contenant les informations sur chaque bande horizontale.
    # Chaque élément de 'tbl' est une liste : [limite gauche, limite droite, nombre de points contenus, largeur de la bande]
    tbl = [[0, 0, 0, 0]]  # Commence par une bande fictive pour simplifier les indices plus tard.

    # Initialise la liste 's' qui va servir à stocker, pour chaque bande horizontale, la somme des limites gauche et droite multipliée par la largeur.
    # Cette liste sera utilisée pour effectuer une recherche binaire.
    s = [0]

    # Remplit 'tbl' et 's' avec les informations sur les bandes horizontales, à l'exception de la première bande fictive.
    for i in range(1, m):
        l, r = map(int, input().split())  # Lit les limites gauche et droite de la bande actuelle.
        tbl.append([l, r, 0, r - l])      # Ajoute à 'tbl' une bande : [gauche, droite, 0 point au départ, largeur].
        s.append((l + r) * w)             # Ajoute à 's' la somme (limite gauche + droite) multipliée par la largeur totale.

    p = []  # Liste vide pour stocker les coordonnées des points.

    for i in range(n):
        x, y = map(float, input().split())  # Lit les coordonnées (x, y) du point i.
        p.append((x, y))                    # Ajoute ce point à la liste 'p'.

    # Trie la liste des points d'abord par leur coordonnée 'y', puis par 'x' en cas d'égalité.
    p.sort(key=lambda x: (x[1], x[0]))

    j = 1  # Initialise l'indice de la bande horizontale à tester lors de l'affectation des points.

    # Parcourt tous les points, un par un.
    for i in range(n):
        x, y = p[i]  # Récupère les coordonnées x et y du i-ème point.
        while True:  # Boucle pour trouver dans quelle bande appartient le point courant.
            # Calcule la position verticale du point projetée sur la bande précédente (j-1).
            y1 = tbl[j - 1][3] * x / w + tbl[j - 1][0]
            # Calcule la position verticale du point projetée sur la bande actuelle (j).
            y2 = tbl[j][3] * x / w + tbl[j][0]
            if y1 < y:
                if y < y2:
                    break  # Si y1 < y < y2, alors le point est dans la bande j.
                j += 1    # Sinon, le point est encore plus haut, test la bande suivante.
            else:
                j -= 1    # Sinon, on est trop haut, revient à la bande précédente.
        tbl[j][2] += 1    # Incrémente le compteur de points pour la bande 'j' correspondante.

    # Calcule cumulativement le nombre de points contenus dans chaque bande, en ajoutant à chaque bande le total de la précédente.
    for i in range(1, m):
        tbl[i][2] += tbl[i - 1][2]

    # Cas particulier : si S == 0, cela signifie que la surface d'intérêt est identique à la surface initiale du rectangle
    if S == 0:
        print(n)  # Tous les points sont au bon endroit.
        continue  # Passe au prochain cas de test.
    elif S == wh2:  # Autre cas particulier : la surface requise est exactement identique à la surface totale du rectangle multipliée par deux ; il n'est pas possible d'inclure aucun point.
        print(0)    # Aucun point dans la zone.
        continue    # Passe au prochain cas de test.

    # Recherche binaire pour trouver l'indice 'j' tel que s[j] >= S, dans la liste 's' de 0 à m-1.
    j = bisect_left(s, S, 0, m)

    # Ajuste j si s[j] > S, pour trouver l'intervalle approprié.
    if s[j] != S:
        j -= 1

    # Initialise la réponse avec le nombre total de points dans le segment trouvé (tbl[j][2]).
    ans = tbl[j][2]
    i = 1  # Indice de départ pour la fenêtre glissante.

    # Lance une boucle pour explorer les intervalles valides qui couvrent exactement la surface requise S.
    while j + 1 < m:
        j += 1  # Passe à l'intervalle suivant à droite.
        # Incrémente i pour déplacer la fenêtre à droite, tant que la surface couverte dépasse la surface cible S.
        while s[j] - s[i] > S:
            i += 1
        # Met à jour 'ans' pour garder le maximum de points dans une surface S.
        ans = max(ans, tbl[j][2] - tbl[i][2])

    # Le résultat final est le nombre de points qui ne peuvent pas être inclus dans la zone de surface maximale valant S.
    print(n - ans)  # Affiche la réponse pour le cas de test courant.