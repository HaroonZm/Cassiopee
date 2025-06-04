#!/usr/bin/env python

# Importation du module 'deque' à partir de la bibliothèque 'collections'
# 'deque' est une structure de données optimisée pour ajouter/supprimer des éléments aux deux extrémités.
from collections import deque
# Importation du module 'itertools' sous l'alias 'it', pour des outils d'itération avancée
import itertools as it
# Importation du module 'sys' pour manipuler des éléments spécifiques au système, comme stdin et la récursion
import sys
# Importation du module 'math', pour les fonctions mathématiques diverses, bien que non utilisé ici
import math

# Augmentation de la limite de récursion maximale pour éviter les erreurs de récursion en profondeur.
# Par défaut, la limite est d'environ 1000. Ici, elle est fixée à 10 millions pour permettre des appels récursifs profonds.
sys.setrecursionlimit(10000000)

# Lecture d'une valeur depuis l'entrée standard (input utilisateur)
# Cette valeur représente le nombre de boucles principales à exécuter.
LOOP = input()
# Parcours d'un certain nombre de boucles principales, déterminées par la variable LOOP
for loop in range(LOOP):
    # Initialisation d'une liste vide. Cette liste va représenter le plateau de jeu Puyo.
    puyo = []
    # La grille de jeu contient 12 lignes
    for i in range(12):
        # Lecture d'une ligne depuis l'entrée utilisateur (version Python 2 : raw_input())
        # On convertit la chaîne obtenue en une liste de caractères pour permettre l'accès individuel aux cellules
        puyo.append(list(raw_input()))

    # Boucle principale des effondrements et suppressions de groupes, appelée jusqu'à 20 fois maximum
    for cnt in range(20):
        # Initialisation d'une matrice 'used' indiquant si une cellule a déjà été visitée lors de la recherche de groupes
        # Elle a autant de lignes que la grille (12) et chaque ligne a 6 colonnes (6 cellules dans chaque ligne).
        used = [[False] * 6 for i in range(12)]
        
        # Définition d’une fonction récursive pour compter la taille des groupes contigus d’une même couleur
        def func(y, x, c):
            # Test de sortie : vérifie si la position (y, x) est en dehors des bornes de la grille
            if y < 0 or x < 0 or y >= 12 or x >= 6:
                # Si oui, retourne 0 car il n’y a plus rien à compter
                return 0
            # Teste si la cellule n'est pas de la couleur recherchée ou si elle a déjà été visitée
            if puyo[y][x] != c or used[y][x]:
                # Si oui, retourne 0 car ce n’est pas un nouveau puyo à compter
                return 0
            # Marque la cellule comme visitée pour éviter de la compter plusieurs fois dans le même groupe
            used[y][x] = True
            # Initialisation du compteur local, commence à 1 car la cellule actuelle est du bon type et non visitée
            ret = 1
            # Ajout récursif de la taille des groupes voisins dans les 4 directions cardinales
            ret += func(y - 1, x, c)  # Haut
            ret += func(y + 1, x, c)  # Bas
            ret += func(y, x - 1, c)  # Gauche
            ret += func(y, x + 1, c)  # Droite
            # Retourne la taille totale trouvée pour ce groupe connecté
            return ret

        # Définition d’une fonction récursive pour effacer (mettre à '.') tous les puyos d’une couleur connectée, à partir de (y, x)
        def erase(y, x, c):
            # Vérification des bordures de la grille
            if y < 0 or x < 0 or y >= 12 or x >= 6:
                # Si la position est invalide, on n'efface rien
                return
            # Si la cellule contient un 'O', alors elle est transformée en '.'
            if puyo[y][x] == 'O':
                puyo[y][x] = '.'
                return
            # Si la cellule ne correspond pas à la couleur attendue, on n'efface rien
            if puyo[y][x] != c:
                return
            # Efface la cellule courante, la remplaçant par '.'
            puyo[y][x] = '.'
            # Appel récursif pour effacer toutes les cellules connectées (dans les 4 directions cardinales)
            erase(y - 1, x, c)  # Haut
            erase(y + 1, x, c)  # Bas
            erase(y, x - 1, c)  # Gauche
            erase(y, x + 1, c)  # Droite

        # Déclaration et initialisation de la variable flag à True
        # Ce flag servira à détecter si, lors de cette itération, il n'y a plus rien à effacer
        flag = True

        # Parcourt chaque cellule du plateau pour rechercher des groupes à supprimer
        for i in range(12):  # Parcourt toutes les lignes du plateau
            for j in range(6):  # Parcourt toutes les colonnes de la ligne
                # Si la cellule fait partie des couleurs principales (R, G, B, Y, P)
                if puyo[i][j] in "RGBYP":
                    # Appel de la fonction func pour obtenir la taille du groupe connecté à cette cellule
                    num = func(i, j, puyo[i][j])
                    # Si la taille du groupe est d'au moins 4, on l'efface
                    if num >= 4:
                        # Indique qu'un effacement a été réalisé, on n'a pas encore fini
                        flag = False
                        # Appel à la fonction erase pour supprimer tous les puyos du groupe connecté
                        erase(i, j, puyo[i][j])

        # Simule la chute de tous les puyos après les suppressions.
        # On le fait jusqu’à 50 fois au maximum pour s’assurer que tout est bien descendu.
        for t in range(50):
            # On parcourt de la deuxième ligne à la dernière
            for i in range(1, 12):
                # Pour chaque colonne de la grille
                for j in range(6):
                    # Si la cellule courante (i,j) est vide ('.')
                    if puyo[i][j] == '.':
                        # On échange cette cellule avec la cellule du dessus (i-1, j).
                        # Cela simule un effet de gravité où les puyos au-dessus tombent vers le bas.
                        puyo[i][j], puyo[i - 1][j] = puyo[i - 1][j], puyo[i][j]
        # Si le flag est toujours à True, c’est qu’aucun groupe n’a été supprimé lors de ce passage
        if flag:
            # On affiche le nombre d’itérations effectuées avant qu'il n’y ait plus rien à effacer
            print cnt
            # On arrête la boucle, le jeu est terminé pour ce plateau
            break