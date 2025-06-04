import math
from functools import reduce
from collections import deque
import sys

# Augmenter la limite de récursion pour éviter une erreur dans certains cas extrêmes
sys.setrecursionlimit(10**7)

# Constante du modulo utilisée pour les calculs
MODULO_CONSTANT = 10**9 + 7

# Pré-calcul des factorielles modulo MODULO_CONSTANT
factorial_mod_table = [0] * 400020
factorial_mod_table[0] = 1
for factorial_index in range(1, len(factorial_mod_table)):
    factorial_mod_table[factorial_index] = (
        factorial_mod_table[factorial_index - 1] * factorial_index % MODULO_CONSTANT
    )

# Fonction pour lire une ligne d'entrée, la couper par espaces et convertir chaque élement en int
def lire_liste_entiers_depuis_ligne():
    return [int(element_chaine) for element_chaine in input().split(" ")]

# Fonction pour lire n lignes d'entrées, chacune étant convertie en int
def lire_liste_entiers_depuis_n_lignes(nombre_lignes):
    return [int(input()) for _ in range(nombre_lignes)]

# Fonction pour lire tout l'entrée (par espace ou retour à la ligne) et convertir en int (retourne un itérateur)
def lire_tous_les_entiers():
    return map(int, open(0).read().split())

# Fonction de log pour le debug, envoie vers la sortie d'erreur standard
def logger_debug(*valeurs_a_afficher):
    print("DEBUG:", *valeurs_a_afficher, file=sys.stderr)

# Fonction pour calculer l'inverse modulaire de x sous MODULO_CONSTANT
def calculer_inverse_modulaire(valeur):
    return pow(valeur, MODULO_CONSTANT - 2, MODULO_CONSTANT)

# Fonction pour calculer l'arrangement (n P k) modulo MODULO_CONSTANT
def arrangement_permutation_modulo(n_entiers, k_selectionnes):
    return factorial_mod_table[n_entiers] * calculer_inverse_modulaire(factorial_mod_table[n_entiers - k_selectionnes]) % MODULO_CONSTANT

# Fonction pour calculer la combinaison (n C k) modulo MODULO_CONSTANT
def combinaison_modulo(n_entiers, k_selectionnes):
    return arrangement_permutation_modulo(n_entiers, k_selectionnes) * calculer_inverse_modulaire(factorial_mod_table[k_selectionnes]) % MODULO_CONSTANT

# Lecture de la saisie standard : n = nombre d'éléments, k = nombre maximum autorisé
nombre_elements_total, nombre_maximum_autorise = lire_liste_entiers_depuis_ligne()

# Cas particulier : si k >= n-1, alors le résultat est une combinaison particulière
if nombre_maximum_autorise >= nombre_elements_total - 1:
    nombre_ensembles = combinaison_modulo(
        nombre_elements_total + nombre_elements_total - 1,
        nombre_elements_total
    ) % MODULO_CONSTANT
    print(nombre_ensembles)
    exit()

# Calcul du nombre total de façons de répartir les personnes dans les pièces (sous contraintes)
nombre_de_dispositions_possibles = 1

for nombre_pieces_vides in range(1, nombre_maximum_autorise + 1):
    facon_choisir_pieces_vides = combinaison_modulo(nombre_elements_total, nombre_pieces_vides)
    facon_repartir_personnes_restantes = combinaison_modulo(nombre_elements_total - 1, nombre_pieces_vides)
    nombre_de_dispositions_possibles += facon_choisir_pieces_vides * facon_repartir_personnes_restantes

resultat_final = nombre_de_dispositions_possibles % MODULO_CONSTANT
print(resultat_final)