import sys
from sys import stdin

input = stdin.readline

# Lire le nombre de points
nombre_points = int(input())

liste_sommes = []
liste_différences = []

for _ in range(nombre_points):
    coord_x, coord_y = map(int, input().split())
    somme_coords = coord_x + coord_y
    difference_coords = coord_x - coord_y
    liste_sommes.append(somme_coords)
    liste_différences.append(difference_coords)

valeur_min_somme = min(liste_sommes)
valeur_max_somme = max(liste_sommes)
valeur_min_difference = min(liste_différences)
valeur_max_difference = max(liste_différences)

meilleure_solution_1 = 0
meilleure_solution_2 = 0

for index in range(nombre_points):
    distance_1_option_1 = max(liste_sommes[index] - valeur_min_somme, liste_différences[index] - valeur_min_difference)
    distance_2_option_1 = max(valeur_max_somme - liste_sommes[index], valeur_max_difference - liste_différences[index])
    meilleure_solution_1 = max(meilleure_solution_1, min(distance_1_option_1, distance_2_option_1))

    distance_1_option_2 = max(liste_sommes[index] - valeur_min_somme, valeur_max_difference - liste_différences[index])
    distance_2_option_2 = max(valeur_max_somme - liste_sommes[index], liste_différences[index] - valeur_min_difference)
    meilleure_solution_2 = max(meilleure_solution_2, min(distance_1_option_2, distance_2_option_2))

print(min(meilleure_solution_1, meilleure_solution_2))