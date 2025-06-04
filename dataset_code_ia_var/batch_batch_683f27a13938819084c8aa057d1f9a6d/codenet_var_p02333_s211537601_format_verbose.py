import sys
import math
import itertools as itertools_module
from collections import deque as double_ended_queue

# Augmentation de la limite de récursion pour traiter des cas de grande taille
sys.setrecursionlimit(10000000)

# Constante pour le modulo
MODULO = 10 ** 9 + 7

# Lecture des entrées : nombre_total, nombre_choisi
nombre_total_elements, nombre_groupes = map(int, raw_input().split())

def calculer_factorielle(valeur):
    """
    Calcule la factorielle récursive de 'valeur'.
    """
    if valeur <= 1:
        return 1
    return calculer_factorielle(valeur - 1) * valeur

def calculer_puissance_modulo(base):
    """
    Calcule (base ** nombre_total_elements) % MODULO par multiplication successive.
    """
    resultat = 1
    for compteur_multiplication in range(nombre_total_elements):
        resultat = (resultat * base) % MODULO
    return resultat

# Somme cumulée du résultat intermédiaire
resultat_combine = 0

for cardinal_sous_ensemble in range(nombre_groupes - 1, 0, -1):

    # Calcul du coefficient binomial combiné avec une puissance
    coefficient_binomial = (calculer_factorielle(nombre_groupes) /
                           (calculer_factorielle(cardinal_sous_ensemble) * 
                            calculer_factorielle(nombre_groupes - cardinal_sous_ensemble)))

    terme_puissance = calculer_puissance_modulo(cardinal_sous_ensemble)

    terme_courant = coefficient_binomial * terme_puissance

    # Application du signe selon la parité de la différence
    if (cardinal_sous_ensemble - nombre_groupes) % 2 == 1:
        terme_courant *= -1

    resultat_combine += terme_courant

# Affichage du résultat final modulo la constante définie
print (calculer_puissance_modulo(nombre_groupes) + resultat_combine) % MODULO