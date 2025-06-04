# Importation des modules standards Python avec alias ou importations spécifiques
# (Bien que non utilisés dans le code ci-dessous, ces imports font partie de l'en-tête standard fourni)
from math import gcd  # Importation de la fonction 'gcd' pour calculer le plus grand commun diviseur
from collections import Counter, deque, defaultdict  # Importation d'outils de collections utiles : Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge  # Fonctions pour les files de priorité (tas)
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort  # Fonctions de recherche/insertions sur listes triées
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement  # Fonctions d'itérations, produits et combinaisons

# Le code principal commence ici

# Lecture d'un nombre entier depuis l'entrée standard, en utilisant la fonction input().
# input() attend que l'utilisateur saisisse une ligne au clavier, renvoie une chaîne de caractères,
# et int() convertit cette chaîne de caractères en un nombre entier.
n = int(input())  # n est le nombre d'unités de longueur (souvent la taille d'un carré ou d'une grille)

# Lecture d'un deuxième nombre entier représentant la hauteur de quelque chose (par exemple un rectangle à placer dans une grille)
h = int(input())  # h est la hauteur du bloc ou rectangle à placer

# Lecture d'un troisième nombre entier représentant la largeur (par exemple d'un rectangle à placer dans la grille)
w = int(input())  # w est la largeur du bloc ou rectangle à placer

# Calcul du nombre de placements possibles d'un rectangle de taille h*w dans un carré (ou matrice) de n*n
# Pour chaque position (i, j) telle que le rectangle complet rentre dans les limites du carré,
# on a (n-h+1) choix pour la coordonnée verticale (lignes), et (n-w+1) choix pour l'horizontale (colonnes)
# On multiplie donc les deux nombres pour obtenir le nombre total de placements possibles.
resultat = (n - h + 1) * (n - w + 1)  # Subtraction pour le nombre de positions possibles, +1 car les indices commencent à 0

# Affichage du résultat calculé ci-dessus dans la sortie standard.
# print() permet d'afficher des informations à l'utilisateur ou d'exporter les résultats du programme.
print(resultat)  # Affiche le nombre total de possibilités