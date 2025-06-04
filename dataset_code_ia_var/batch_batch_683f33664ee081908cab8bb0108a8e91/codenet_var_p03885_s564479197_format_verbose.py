import sys

import numpy as np

# Lecture des entrées standard avec des noms très explicites
standard_input = sys.stdin
input_readline_function = standard_input.readline
input_readlines_function = standard_input.readlines

# Augmentation de la limite de récursion
sys.setrecursionlimit(10 ** 7)

# Définition de la constante de modulo
modulus_modulo = 10 ** 9 + 7

# Lecture de la taille de la matrice binaire
binary_matrix_size = int(input_readline_function())

# Lecture et création de la matrice binaire
binary_matrix_lines = input_readlines_function()
binary_matrix = np.array([line.split() for line in binary_matrix_lines], np.int8)

def calculer_rang_matrice(matrice_a):
    if (matrice_a == 0).all():
        return 0

    indices_lignes_non_nuls = np.nonzero(matrice_a[:, 0])[0]

    if len(indices_lignes_non_nuls) == 0:
        return calculer_rang_matrice(matrice_a[:, 1:])

    indice_ligne_pivot = indices_lignes_non_nuls[0]
    ligne_pivot = matrice_a[indice_ligne_pivot].copy()
    matrice_a[indice_ligne_pivot] = matrice_a[0]
    matrice_a[0] = ligne_pivot
    matrice_a[1:] ^= matrice_a[1:, 0][:, None] * matrice_a[0][None, :]
    return 1 + calculer_rang_matrice(matrice_a[1:, 1:])

def produit_cumulatif_modulo(tableau_entree, modulo):
    taille_tableau = len(tableau_entree)
    dimension_racine = int(taille_tableau ** 0.5 + 1)
    tableau_redimensionne = np.resize(tableau_entree, dimension_racine ** 2).reshape(dimension_racine, dimension_racine)

    for colonne in range(1, dimension_racine):
        tableau_redimensionne[:, colonne] *= tableau_redimensionne[:, colonne - 1]
        tableau_redimensionne[:, colonne] %= modulo

    for ligne in range(1, dimension_racine):
        tableau_redimensionne[ligne] *= tableau_redimensionne[ligne - 1, -1]
        tableau_redimensionne[ligne] %= modulo

    return tableau_redimensionne.ravel()[:taille_tableau]

def puissance_modulaire(base, exposant, modulo):
    if exposant == 0:
        return 1
    resultat = puissance_modulaire(base, exposant // 2, modulo)
    resultat = (resultat * resultat) % modulo
    if exposant & 1:
        return (base * resultat) % modulo
    else:
        return resultat

rang_matrice_binaire = calculer_rang_matrice(binary_matrix)

# Préparation des puissances de 2 jusqu'à la taille maximale possible
tableau_puissances_de_2 = np.full(binary_matrix_size * binary_matrix_size + 100, 2, np.int64)
tableau_puissances_de_2[0] = 1
tableau_produit_cumulatif_puissances_de_2_modulo = produit_cumulatif_modulo(tableau_puissances_de_2, modulus_modulo)

tableau_g = np.zeros((binary_matrix_size + 1, binary_matrix_size + 1), np.int64)
for lignes in range(binary_matrix_size + 1):
    tableau_g[lignes, 1:] = tableau_produit_cumulatif_puissances_de_2_modulo[lignes] - tableau_produit_cumulatif_puissances_de_2_modulo[:binary_matrix_size]
tableau_g[:, 0] = 1
for colonne in range(1, binary_matrix_size + 1):
    tableau_g[:, colonne] *= tableau_g[:, colonne - 1]
    tableau_g[:, colonne] %= modulus_modulo

# Récupération de la diagonale de G
diagonale_g = np.diagonal(tableau_g)

# Calcul de la matrice inverse de G sur la diagonale modulo le modulus_modulo
matrice_d = tableau_g * puissance_modulaire(diagonale_g, modulus_modulo - 2, modulus_modulo)[None, :] % modulus_modulo

# Préparation de la matrice f
matrice_f = np.zeros((binary_matrix_size + 1, binary_matrix_size + 1), np.int64)
for lignes_matrice_f in range(binary_matrix_size + 1):
    matrice_f[lignes_matrice_f, :lignes_matrice_f + 1] = diagonale_g[:lignes_matrice_f + 1] * matrice_d[lignes_matrice_f, lignes_matrice_f::-1] % modulus_modulo

# Calcul des coefficients B et C
coefficient_b = matrice_d[binary_matrix_size] * matrice_f[binary_matrix_size] % modulus_modulo

coefficient_c = (
    matrice_d[binary_matrix_size, rang_matrice_binaire]
    * matrice_f[:, rang_matrice_binaire] % modulus_modulo
    * tableau_produit_cumulatif_puissances_de_2_modulo[binary_matrix_size * binary_matrix_size :: -binary_matrix_size] % modulus_modulo
)

# Calcul du résultat final A et la réponse finale
valeur_intermediaire_a = (coefficient_b[rang_matrice_binaire:binary_matrix_size + 1] * coefficient_c[rang_matrice_binaire:binary_matrix_size + 1] % modulus_modulo).sum() % modulus_modulo
reponse_finale = valeur_intermediaire_a * pow(int(coefficient_b[rang_matrice_binaire]), modulus_modulo - 2, modulus_modulo) % modulus_modulo

print(reponse_finale)