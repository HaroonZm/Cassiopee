import sys

import numpy as np

# Constantes globales
MODULO = 10 ** 9 + 7
MAX_DIMENSION = 301
RECURSION_LIMIT = 10 ** 7

# Configuration de l'environnement
sys.setrecursionlimit(RECURSION_LIMIT)

# Fonctions d'entrée
lecture_ligne = sys.stdin.readline
lecture_toutes_les_lignes = sys.stdin.readlines

# Lecture de la taille de la matrice
taille_matrice = int(lecture_ligne())

# Lecture et conversion de la matrice d'entrée en une matrice numpy d'entiers 8 bits
matrice_coefficients = np.array(
    [ligne.split() for ligne in lecture_toutes_les_lignes()],
    dtype=np.int8
)

def calculer_rang_sur_champ_binaire(matrice):
    """
    Calcule récursivement le rang d'une matrice sur le champ binaire (GF(2)).
    """
    if (matrice == 0).all():
        return 0

    ligne_non_nulle = np.nonzero(matrice[:, 0])[0]
    if len(ligne_non_nulle) == 0:
        return calculer_rang_sur_champ_binaire(matrice[:, 1:])

    indice_pivot = ligne_non_nulle[0]
    ligne_temporaire = matrice[indice_pivot].copy()
    matrice[indice_pivot] = matrice[0]
    matrice[0] = ligne_temporaire

    matrice[1:] ^= matrice[1:, 0][:, None] * matrice[0][None, :]
    return 1 + calculer_rang_sur_champ_binaire(matrice[1:, 1:])

rang_matrice = calculer_rang_sur_champ_binaire(matrice_coefficients)

# Pré-calcul des puissances de 2 modulo MODULO
puissances_de_deux_modulo = np.ones(MAX_DIMENSION, dtype=np.int64)
for exposant in range(1, MAX_DIMENSION):
    puissances_de_deux_modulo[exposant] = (
        puissances_de_deux_modulo[exposant - 1] * 2
    ) % MODULO

# Initialisation et remplissage du tableau de programmation dynamique
# dp[n, m, d] : nombre de façons de choisir m vecteurs dans un espace de dimension n pour engendrer un espace de dimension d
tableau_prog_dynamique = np.zeros((MAX_DIMENSION, MAX_DIMENSION, MAX_DIMENSION), dtype=np.int64)
tableau_prog_dynamique[:, 0, 0] = 1

for nombre_vecteurs in range(1, MAX_DIMENSION):
    tableau_prog_dynamique[:, nombre_vecteurs, :nombre_vecteurs] += (
        tableau_prog_dynamique[:, nombre_vecteurs - 1, :nombre_vecteurs] * puissances_de_deux_modulo[:nombre_vecteurs]
    ) % MODULO
    tableau_prog_dynamique[:, nombre_vecteurs, 1:nombre_vecteurs + 1] += (
        tableau_prog_dynamique[:, nombre_vecteurs - 1, 0:nombre_vecteurs] *
        (puissances_de_deux_modulo[:, None] - puissances_de_deux_modulo[None, 0:nombre_vecteurs])
    ) % MODULO
    tableau_prog_dynamique[:, nombre_vecteurs, :] %= MODULO

# Calcul du nombre total de façons possibles pour obtenir un rang donné
nombre_moyens_obtenir_rang = 0
for dimension_intermediaire in range(rang_matrice, taille_matrice + 1):
    nombre_moyens_obtenir_rang += (
        tableau_prog_dynamique[taille_matrice, taille_matrice, dimension_intermediaire] *
        tableau_prog_dynamique[taille_matrice, dimension_intermediaire, rang_matrice] % MODULO *
        pow(2, taille_matrice * (taille_matrice - dimension_intermediaire), MODULO) % MODULO
    )
nombre_moyens_obtenir_rang %= MODULO

# Calcul de l'inverse modulaire pour normaliser la réponse
inverse_modulaire_nombre_ensembles = pow(
    int(tableau_prog_dynamique[taille_matrice, taille_matrice, rang_matrice]),
    MODULO - 2,
    MODULO
)

# Résultat final
reponse_finale = nombre_moyens_obtenir_rang * inverse_modulaire_nombre_ensembles % MODULO

print(reponse_finale)