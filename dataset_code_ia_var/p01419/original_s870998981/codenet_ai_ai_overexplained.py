#!/usr/bin/env python

# Importation du module deque de la bibliothèque collections 
# (utile pour les files d'attente efficaces, bien que non utilisé directement dans ce script)
from collections import deque

# Importation du module itertools et on lui donne l'alias 'it'
# (facilite l'utilisation de fonctions itératives avancées, mais il n'est pas utilisé directement ici)
import itertools as it

# Importation du module sys qui fournit des fonctions pour interagir avec l'interpréteur Python
import sys

# Modification de la limite de récursion maximale pour permettre à Python 
# d'effectuer plus d'appels de fonctions récursifs avant d'arrêter avec une erreur
sys.setrecursionlimit(1000000)

# Demande à l'utilisateur de saisir trois entiers séparés par des espaces via raw_input()
# map applique la fonction int à chaque partie pour obtenir trois entiers
R, C, M = map(int, raw_input().split())
# R = nombre de lignes de la grille
# C = nombre de colonnes de la grille
# M = nombre de points d'intérêt à traiter

# Initialisation d'une liste vide qui stockera les lignes de la carte
S = []

# Initialisation des listes vides qui stockeront les coûts de temps, d'allumage et d'extinction pour chaque case
t_cost = []
on_cost = []
off_cost = []

# Boucle pour lire R lignes décrivant la carte avec des caractères (par exemple '.' ou '#')
for loop in range(R):
    hoge = raw_input()  # Lecture d'une ligne représentant une ligne de la carte
    S.append(hoge)      # Ajoute cette ligne à la liste S

# Boucle pour lire R lignes de coûts de temps pour chaque case
for loop in range(R):
    hoge = map(int, raw_input().split())  # Convertit chaque valeur de la ligne saisie en entier
    t_cost.append(hoge)                   # Ajoute la liste des coûts de temps pour cette ligne à t_cost

# Boucle pour lire les coûts d'allumage pour chaque case
for loop in range(R):
    hoge = map(int, raw_input().split())
    on_cost.append(hoge)

# Boucle pour lire les coûts d'extinction pour chaque case
for loop in range(R):
    hoge = map(int, raw_input().split())
    off_cost.append(hoge)

# Création d'un dictionnaire m qui associe à chaque coordonnée (x, y) une liste vide
# Ce dictionnaire stocke les instants où la case (x, y) est visitée lors du trajet
m = {}
# Création d'un dictionnaire used permettant de savoir si une case a déjà été visitée durant une recherche
used = {}

# Double boucle imbriquée pour parcourir toutes les cases de la grille
for y in range(R):            # Parcourt chaque ligne grâce à l'index y
    for x in range(C):        # Parcourt chaque colonne grâce à l'index x
        # Associe à chaque case (x, y) une liste vide dans m (pour y stocker les étapes (temps) où la case est visitée)
        m[(x, y)] = []

# Définition d'une fonction récursive func pour trouver un chemin de (x, y) à (gx, gy)
# x, y = coordonnées actuelles
# gx, gy = coordonnées de la destination
# step = nombre d'étapes depuis le début
def func(x, y, gx, gy, step):
    # Si on sort de la grille (condition d'arrêt de la récursion pour éviter IndexError)
    if x < 0 or y < 0 or x >= C or y >= R:
        return False
    # Si la case (x, y) a déjà été visitée durant cette recherche, on s'arrête ici
    if (x, y) in used:
        return False
    # On indique que la case (x, y) est visitée à l'étape 'step' (pour éviter les boucles infinies)
    used[(x, y)] = step
    # Si la case est un mur ('#'), on s'arrête ici (on ne peut pas la traverser)
    if S[y][x] == '#':
        return False
    # Si on a atteint la destination
    if x == gx and y == gy:
        # On ajoute à la liste de ce point le nombre d'étapes effectuées pour arriver ici
        m[(x, y)].append(step)
        return True  # Succès de la recherche de chemin
    # Variable ret qui indique si l'une des directions conduit à la destination
    ret = False
    # Appel récursif dans 4 directions : gauche, droite, haut, bas
    ret = (ret or func(x - 1, y, gx, gy, step + 1))   # à gauche
    ret = (ret or func(x + 1, y, gx, gy, step + 1))   # à droite
    ret = (ret or func(x, y - 1, gx, gy, step + 1))   # en haut
    ret = (ret or func(x, y + 1, gx, gy, step + 1))   # en bas
    # Si un chemin a été trouvé à partir de cette case, on note à quelle étape on y est passé
    if ret:
        m[(x, y)].append(step)
    # Retourne si un chemin vers la destination existe depuis (x, y)
    return ret

# Lecture de la position de départ : sy, sx (ordinairement (ligne, colonne))
sy, sx = map(int, raw_input().split())

# Initialisation du compteur d'étapes (nombre d'étapes cumulées depuis le point de départ)
cnt = 0

# Boucle pour chaque transition entre points d'intérêt, moins un car on commence déjà sur le premier point d'intérêt
for loop in range(M - 1):
    # Lecture de la prochaine cible (gy, gx)
    gy, gx = map(int, raw_input().split())
    # Réinitialisation du dictionnaire used pour cette nouvelle recherche
    used = {}
    # Appel de func pour trouver un chemin depuis la position courante (sx, sy) jusqu'à la cible (gx, gy)
    func(sx, sy, gx, gy, cnt)
    # Mise à jour du compteur d'étapes : on retire le dernier temps enregistré pour la nouvelle position
    cnt = m[(gx, gy)].pop()
    # Mise à jour de la position courante pour la prochaine itération
    sx, sy = gx, gy

# Après la boucle, on ajoute le compteur d'étapes final à la liste des instants passés sur la dernière case visitée
m[(gx, gy)].append(cnt)

# Initialisation de la variable de somme finale
ans = 0

# Double boucle parcourant chaque case de la grille pour calculer le coût total du parcours
for y in range(R):
    for x in range(C):
        # t est le coût de temps associé à la case (y, x)
        t = t_cost[y][x]
        # on est le coût d'allumage de la case (y, x)
        on = on_cost[y][x]
        # off est le coût d'extinction de la case (y, x)
        off = off_cost[y][x]
        # lst est la liste des instants où la case (x, y) a été foulée
        lst = m[(x, y)]
        # Si la liste n'est pas vide, cela signifie que la case a été traversée au moins une fois
        if len(lst) > 0:
            # Ajoute les coûts fixes d'allumage et d'extinction (payés une seule fois par case visitée)
            ans += on + off
        # Parcourt tous les intervalles successifs de passage sur cette case
        for i in range(len(lst) - 1):
            t1 = lst[i]     # instant d'entrée précédent
            t2 = lst[i + 1] # instant d'entrée suivant
            # On paie soit les coûts fixes, soit le coût de maintenance au temps passé entre deux passages consécutifs, le moins cher des deux
            ans += min(on + off, t * (t2 - t1))
# Affiche le coût total minimum obtenu par la stratégie suivie
print ans