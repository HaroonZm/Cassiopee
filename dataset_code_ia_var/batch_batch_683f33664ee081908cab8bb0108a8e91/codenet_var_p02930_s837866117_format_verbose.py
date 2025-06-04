# Lecture de la taille de la matrice carrée
taille_matrice = int(input())

# Initialisation de la matrice avec des valeurs None
matrice_distance_niveaux = [
    [None for _ in range(taille_matrice)] 
    for _ in range(taille_matrice)
]

def remplir_matrice_paires_selon_niveau(liste_indices, niveau_courant):
    if len(liste_indices) == 1:
        return

    sous_liste_indices_pairs = liste_indices[::2]
    sous_liste_indices_impairs = liste_indices[1::2]

    for indice_pair in sous_liste_indices_pairs:
        for indice_impair in sous_liste_indices_impairs:
            matrice_distance_niveaux[indice_pair][indice_impair] = niveau_courant
            matrice_distance_niveaux[indice_impair][indice_pair] = niveau_courant

    remplir_matrice_paires_selon_niveau(sous_liste_indices_pairs, niveau_courant + 1)
    remplir_matrice_paires_selon_niveau(sous_liste_indices_impairs, niveau_courant + 1)

# Remplissage initial de la matrice à partir de la liste d'indices
remplir_matrice_paires_selon_niveau(list(range(taille_matrice)), 1)

# Affichage ligne par ligne (triangulaire supérieure sans la diagonale principale)
for indice_ligne, ligne_valeurs in enumerate(matrice_distance_niveaux[:-1]):
    valeurs_a_afficher = ligne_valeurs[indice_ligne + 1:]
    print(*valeurs_a_afficher)