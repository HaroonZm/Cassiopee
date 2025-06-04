# Demande à l'utilisateur de saisir trois entiers séparés par des espaces (la hauteur H, la largeur W et le nombre de points N)
H, W, N = map(int, input().split())  # map() applique int() à chaque élément de la liste générée par input().split(), puis l'affecte aux variables H, W, N respectivement

# Initialise un dictionnaire vide qui sera utilisé pour stocker le nombre d'occurrences de chaque case centrale possible dans la grille
D = dict()  # Les clés seront des tuples (ligne, colonne) représentant les coordonnées d'une case centrale, les valeurs seront des nombres entiers

# Ces deux listes définissent les décalages relatifs aux coordonnées d'un voisinage 3x3 centré (incluant la case centrale elle-même)
da = [-1, -1, -1, 0, 0, 0, 1, 1, 1]  # Décalages pour les lignes ; -1, 0 ou 1 pour explorer autour d'une case
db = [-1, 0, 1, -1, 0, 1, -1, 0, 1]  # Décalages correspondants pour les colonnes

# Boucle sur le nombre de points noirs (N)
for i in range(N):
    # Pour chaque point, on lit deux entiers donnant la position (ligne a, colonne b) de ce point
    a, b = map(int, input().split())  # Récupère les coordonnées du point à traiter

    # Pour chaque voisin (et le centre) autour du point (a, b)
    for j in range(9):
        na = a + da[j]  # Calcule la ligne du voisin en ajoutant l'offset approprié
        nb = b + db[j]  # Calcule la colonne du voisin en ajoutant l'offset approprié

        # On s'assure que la case (na, nb) est bien à l'intérieur de la sous-grille centrale d'au moins 3x3 (les bords ne comptent pas)
        if 1 < na < H and 1 < nb < W:  # On vérifie que na et nb sont strictement supérieurs à 1 et strictement inférieurs à H et W
            # Si cette case centrale (na, nb) a déjà été comptée, on incrémente son compteur
            if (na, nb) in D:
                D[(na, nb)] += 1  # On ajoute 1 à la valeur déjà présente pour cette clé
            else:
                # Si la case n'a pas encore été rencontrée, on l'ajoute au dictionnaire avec une valeur initiale de 1
                D[(na, nb)] = 1

# Crée une liste de 10 zéros pour stocker le nombre de cases centrales ayant 0...9 points noirs dans leur voisinage respectif
ans = [0 for i in range(10)]  # ans[k] comptera le nombre de cases ayant exactement k points noirs dans leur voisinage 3x3

# Pour chaque case centrale qui a été rencontrée au moins une fois
for i in D:
    ans[D[i]] += 1  # On augmente le compteur du nombre de cases comportant D[i] voisins noirs

# Calcule le nombre total de cases centrales qui ont au moins un point noir dans leur voisinage 3x3 (somme des éléments 1 à 9 inclus)
tmp = sum(ans)  # La somme de ans, sauf qu'importe car ans[0] sera réassigné plus loin après

# Calcule le nombre de cases centrales (excluant les bords) qui n'ont aucun point noir dans leur voisinage 3x3
# Il y a (H-2)*(W-2) cases centrales au total, on retire celles déjà recensées avec au moins un point noir
ans[0] = (H - 2) * (W - 2) - tmp  # ans[0] contient le nombre de cases "vides"

# Affiche, pour chaque nombre k de 0 à 9, le nombre de cases centrales avec exactement k points noirs dans leur voisinage 3x3, une par ligne
for i in ans:
    print(i)  # Affiche le résultat pour chaque cas, sur une ligne séparée