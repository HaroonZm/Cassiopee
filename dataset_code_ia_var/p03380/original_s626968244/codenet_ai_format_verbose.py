import bisect

# Lire le nombre d'éléments dans la liste
nombre_entiers = int(input())

# Lire la liste d'entiers et la trier par ordre croissant
liste_entiers = list(map(int, input().split()))
liste_entiers.sort()

# Extraire le plus grand élément
plus_grand_entier = liste_entiers[-1]

# Calculer les candidats potentiels pour le second élément (la moitié inférieure et supérieure)
demi_inferieure = plus_grand_entier // 2
demi_superieure = plus_grand_entier // 2 + 1

# Trouver les indices d'insertion à gauche pour les deux valeurs de la demi
indice_demi_inferieure = bisect.bisect_left(liste_entiers, demi_inferieure)
indice_demi_superieure = bisect.bisect_left(liste_entiers, demi_inferieure)

# Rassembler les indices à examiner pour trouver le meilleur candidat
indices_candidats = []

if liste_entiers[indice_demi_inferieure] != plus_grand_entier:
    indices_candidats.append(indice_demi_inferieure)

if liste_entiers[indice_demi_superieure] != plus_grand_entier:
    indices_candidats.append(indice_demi_superieure)

if indice_demi_inferieure > 0:
    if liste_entiers[indice_demi_inferieure - 1] != plus_grand_entier:
        indices_candidats.append(indice_demi_inferieure - 1)

if indice_demi_superieure > 0:
    if liste_entiers[indice_demi_superieure - 1] != plus_grand_entier:
        indices_candidats.append(indice_demi_superieure - 1)

if indice_demi_inferieure < nombre_entiers - 1:
    if liste_entiers[indice_demi_inferieure + 1] != plus_grand_entier:
        indices_candidats.append(indice_demi_inferieure + 1)

if indice_demi_superieure < nombre_entiers - 1:
    if liste_entiers[indice_demi_superieure + 1] != plus_grand_entier:
        indices_candidats.append(indice_demi_superieure + 1)

# Valeur cible : moitié (inférieure) du max
meilleur_candidat_valeur = plus_grand_entier // 2

# Initialiser l'indice du meilleur candidat
indice_meilleur_candidat = nombre_entiers - 1

# Parcourir tous les indices candidats uniques pour trouver celui le plus proche de la moitié
for indice in set(indices_candidats):
    if abs(meilleur_candidat_valeur - liste_entiers[indice]) <= abs(meilleur_candidat_valeur - liste_entiers[indice_meilleur_candidat]):
        indice_meilleur_candidat = indice
    if plus_grand_entier % 2 != 0:
        if abs(meilleur_candidat_valeur + 1 - liste_entiers[indice]) <= abs(meilleur_candidat_valeur + 1 - liste_entiers[indice_meilleur_candidat]):
            indice_meilleur_candidat = indice

# Afficher le plus grand entier et le candidat trouvé
print(str(plus_grand_entier) + " " + str(liste_entiers[indice_meilleur_candidat]))