from collections import defaultdict, deque
from bisect import bisect

# Lecture des dimensions du rectangle et du nombre de murs
largeur_rect, hauteur_rect, nombre_murs = map(int, input().split())

# Lecture des coordonnées des murs
liste_murs = [list(map(int, input().split())) for _ in range(nombre_murs)]

# Initialisation des ensembles de coordonnées uniques
ensemble_abscisses = set([0, largeur_rect])
ensemble_ordonnees = set([0, hauteur_rect])

# Collecte de toutes les positions de murs pour discrétisation
for x_debut, y_debut, x_fin, y_fin in liste_murs:
    ensemble_abscisses.add(x_debut)
    ensemble_abscisses.add(x_fin)
    ensemble_ordonnees.add(y_debut)
    ensemble_ordonnees.add(y_fin)

liste_abscisses_discretes = sorted(ensemble_abscisses)
liste_ordonnees_discretes = sorted(ensemble_ordonnees)

def generer_mapping_discretisation(liste_coordonnees):
    mapping_discret = {}
    indice_courant = 0
    for valeur in liste_coordonnees:
        mapping_discret[valeur] = indice_courant
        indice_courant += 2
    taille_grille = indice_courant - 1
    return mapping_discret, taille_grille

mapping_abscisses, taille_grille_abscisse = generer_mapping_discretisation(liste_abscisses_discretes)
mapping_ordonnees, taille_grille_ordonnee = generer_mapping_discretisation(liste_ordonnees_discretes)

# Grille de murs (1 = mur, 0 = ouvert)
grille_murs = [[0] * taille_grille_abscisse for _ in range(taille_grille_ordonnee)]
# Grille de composantes connexes
grille_composante = [[-1] * taille_grille_abscisse for _ in range(taille_grille_ordonnee)]

# Marquer les bords de la grille comme des murs
for ord_index in range(taille_grille_ordonnee):
    grille_murs[ord_index][0] = 1
    grille_murs[ord_index][taille_grille_abscisse - 1] = 1
for abs_index in range(taille_grille_abscisse):
    grille_murs[0][abs_index] = 1
    grille_murs[taille_grille_ordonnee - 1][abs_index] = 1

# Placement des murs dans la grille
for x1, y1, x2, y2 in liste_murs:
    if x1 == x2:  # Mur vertical
        if y1 > y2:
            y1, y2 = y2, y1
        abs_discret = mapping_abscisses[x1]
        ord_discret_debut = mapping_ordonnees[y1]
        ord_discret_fin = mapping_ordonnees[y2]
        for ordonne in range(ord_discret_debut, ord_discret_fin + 1):
            grille_murs[ordonne][abs_discret] = 1
    else:  # Mur horizontal
        if x1 > x2:
            x1, x2 = x2, x1
        abs_discret_debut = mapping_abscisses[x1]
        abs_discret_fin = mapping_abscisses[x2]
        ord_discret = mapping_ordonnees[y1]
        for abscisse in range(abs_discret_debut, abs_discret_fin + 1):
            grille_murs[ord_discret][abscisse] = 1

# Directions pour le BFS (haut, gauche, bas, droite)
directions_voisinage = [(-1, 0), (0, -1), (1, 0), (0, 1)]
file_exploration = deque()
nombre_composantes = 0

# Détection des composantes connexes dans la grille (BFS)
for ord_index in range(taille_grille_ordonnee):
    for abs_index in range(taille_grille_abscisse):
        if grille_murs[ord_index][abs_index] == 1 or grille_composante[ord_index][abs_index] != -1:
            continue
        grille_composante[ord_index][abs_index] = nombre_composantes
        file_exploration.append((abs_index, ord_index))
        while file_exploration:
            courant_x, courant_y = file_exploration.popleft()
            for dx, dy in directions_voisinage:
                voisin_x = courant_x + dx
                voisin_y = courant_y + dy
                if grille_murs[voisin_y][voisin_x] == 1 or grille_composante[voisin_y][voisin_x] != -1:
                    continue
                grille_composante[voisin_y][voisin_x] = nombre_composantes
                file_exploration.append((voisin_x, voisin_y))
        nombre_composantes += 1

# Construction du graphe des composantes connexes adjacentes
infini = 10 ** 9
graphe_composantes = [[] for _ in range(nombre_composantes)]
for ord_index in range(1, taille_grille_ordonnee - 1):
    for abs_index in range(1, taille_grille_abscisse - 1):
        composante_gauche = grille_composante[ord_index][abs_index - 1]
        composante_droite = grille_composante[ord_index][abs_index + 1]
        if composante_gauche != -1 and composante_droite != -1 and composante_gauche != composante_droite:
            graphe_composantes[composante_gauche].append(composante_droite)
            graphe_composantes[composante_droite].append(composante_gauche)
        composante_haut = grille_composante[ord_index - 1][abs_index]
        composante_bas = grille_composante[ord_index + 1][abs_index]
        if composante_haut != -1 and composante_bas != -1 and composante_haut != composante_bas:
            graphe_composantes[composante_haut].append(composante_bas)
            graphe_composantes[composante_bas].append(composante_haut)

# Traitement des requêtes
nombre_requetes = int(input())
for _ in range(nombre_requetes):
    depart_x, depart_y, arrivee_x, arrivee_y = map(int, input().split())
    position_x_depart = (bisect(liste_abscisses_discretes, depart_x) - 1) * 2 + 1
    position_y_depart = (bisect(liste_ordonnees_discretes, depart_y - 1) - 1) * 2 + 1
    position_x_arrivee = (bisect(liste_abscisses_discretes, arrivee_x) - 1) * 2 + 1
    position_y_arrivee = (bisect(liste_ordonnees_discretes, arrivee_y) - 1) * 2 + 1

    assert grille_composante[position_y_depart][position_x_depart] != -1
    assert grille_composante[position_y_arrivee][position_x_arrivee] != -1

    indice_composante_depart = grille_composante[position_y_depart][position_x_depart]
    indice_composante_arrivee = grille_composante[position_y_arrivee][position_x_arrivee]
    file_bfs = deque([indice_composante_depart])
    tableau_distances = [-1] * nombre_composantes
    tableau_distances[indice_composante_depart] = 0

    while file_bfs:
        composante_courante = file_bfs.popleft()
        distance_courante = tableau_distances[composante_courante]
        for composante_voisine in graphe_composantes[composante_courante]:
            if tableau_distances[composante_voisine] != -1:
                continue
            tableau_distances[composante_voisine] = distance_courante + 1
            file_bfs.append(composante_voisine)
    print(tableau_distances[indice_composante_arrivee])