import math
import sys
import itertools
import numpy as np

# Lecture de l'entier à partir de l'entrée standard
nombre_entrees_utilisateur = int(input())

nombre_groupes = 0

# Recherche du plus petit entier 'i' tel que i*(i-1)//2 == nombre_entrees_utilisateur
for groupe_candidat in range(2, 1000):
    nombre_paires_possible = groupe_candidat * (groupe_candidat - 1) // 2
    if nombre_entrees_utilisateur == nombre_paires_possible:
        nombre_groupes = groupe_candidat
        break

if nombre_groupes >= 2:
    print("Yes")
else:
    print("No")

if nombre_groupes >= 1:
    print(nombre_groupes)
    # Initialisation d'une matrice pour stocker les indices de chaque groupe
    indices_groupes = [ [0] * (nombre_groupes - 1) for _ in range(nombre_groupes) ]
    compteur_element = 1

    for indice_groupe in range(nombre_groupes):
        print(nombre_groupes - 1, end=" ")
        # Remplir le début de la ligne avec des valeurs précédemment attribuées
        for indice_element_precedent in range(indice_groupe):
            indices_groupes[indice_groupe][indice_element_precedent] = indices_groupes[indice_element_precedent][indice_groupe - 1]
            print(indices_groupes[indice_groupe][indice_element_precedent], end=" ")
        # Remplir le reste de la ligne avec de nouvelles valeurs croissantes
        for indice_nouvel_element in range(indice_groupe, nombre_groupes - 1):
            indices_groupes[indice_groupe][indice_nouvel_element] = compteur_element
            compteur_element += 1
            print(indices_groupes[indice_groupe][indice_nouvel_element], end=" ")
        print("")