import sys  # Le module sys permet d'interagir avec l'interpréteur Python (ex: lire les entrées, changer des paramètres système, etc.)
from operator import itemgetter  # itemgetter permet de créer une fonction qui extrait un élément à une position donnée d'une séquence
# Pour le PGCD (Plus Grand Commun Diviseur), on importe la fonction gcd du module fractions
from fractions import gcd
# Importation de fonctions mathématiques avancées pour arrondir vers le haut (ceil) et le bas (floor)
from math import ceil, floor
# Importation de deepcopy pour effectuer une copie réelle d'une structure (par opposition à une simple référence)
from copy import deepcopy
# accumulate permet de calculer les sommes cumulées d'une séquence
from itertools import accumulate
# Counter sert à compter les occurrences d’éléments dans une séquence, il retourne un objet spécial type dict
from collections import Counter
import math  # Importation du module math complémentaire pour d'autres opérations mathématiques
from functools import reduce  # reduce permet d'appliquer cumulativement une fonction à une séquence pour la réduire à une seule valeur

sys.setrecursionlimit(200000)  # Cette commande augmente la limite de récursion, utile pour éviter l’erreur "maximum recursion depth exceeded" lors de l’utilisation massive de la récursion

# Définition d'une version spéciale de la fonction input qui lit une ligne de l'entrée standard.
input = sys.stdin.readline  # readline() lit une ligne, incluant le caractère fin de ligne
# Fonctions personnalisées pour lire différents types d’entrées :
def ii():  # Cette fonction retourne un entier après avoir lu une ligne d'entrée, la convertit en int
    return int(input())

def mi():  # Cette fonction lit une ligne d'entrée, la découpe sur les espaces et convertit chaque élément en int, le tout sous forme de tuple
    return map(int, input().rstrip().split())

def lmi():  # Fait pareil que mi(), mais retourne une liste d’entiers au lieu d’un tuple
    return list(map(int, input().rstrip().split()))

def li():  # Lit une ligne, supprime les espaces de fin puis convertit la string en une liste de ses caractères (ex: "abc" ⇒ ['a', 'b', 'c'])
    return list(input().rstrip())

# Fonction de debug, qui affiche les valeurs passées en arguments sur la sortie d'erreur standard (sys.stderr).
# Utilisé pour le débogage afin de ne pas mélanger les sorties normales et celles du debug
def debug(*args, sep=" ", end="\n"):
    # Affiche uniquement si __debug__ est False (optimisation Python, normal=>True, donc debug non appelé sauf si l'interpréteur a été lancé avec l'option -O)
    print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None

# ==== Début du programme principal ====

# Lecture des dimensions de la grille (Hauteur H, Largeur W)
H, W = mi()  # Exemple : pour 3 4, H=3 et W=4

# Création de la grille S : liste contenant H lignes, chaque ligne étant une liste de caractères (ex: [['A','B'], ['C','B']]
S = [li() for i in range(H)]  # Pour chaque i de 0 à H-1, on lit une ligne et convertit en liste de caractères

ans = []  # Initialisation d’une liste vide qui va contenir les coordonnées de chaque cellule contenant un 'B'

# Parcours de la grille pour chercher chaque 'B'
for i in range(H):  # Parcours des lignes (0 à H-1)
    for j in range(W):  # Parcours des colonnes (0 à W-1)
        if S[i][j] == "B":  # Vérifie si la cellule (i,j) contient la lettre 'B'
            ans.append((i, j))  # Si oui, on ajoute les coordonnées (ligne, colonne) dans la liste ans

# On trie la liste ans en fonction de la somme des coordonnées (i+j) croissante
ans.sort(key=lambda x: x[0] + x[1])
debug(ans[-1])  # Affiche le dernier élément après tri, qui possède la plus grande somme ligne+colonne
debug(ans[0])   # Affiche le premier, qui a la plus petite somme

# On calcule la distance de Manhattan entre le 'B' le plus éloigné en bas à droite et celui le plus en haut à gauche
tmp = abs(ans[-1][0] - ans[0][0]) + abs(ans[-1][1] - ans[0][1])
# Cette distance correspond donc à la somme des différences d'indices entre deux points extrêmes

# Puis, on trie la liste ans avec une clé différente : on utilise (i + (W - j)), qui donne la priorité aux lignes du bas et aux colonnes de gauche
ans.sort(key=lambda x: x[0] + (W - x[1]))  # Ce tri permet d’examiner l’autre "diagonale"

debug(ans[-1])  # Affiche le dernier élément dans ce tri, donc le 'B' le plus éloigné selon cette métrique
debug(ans[0])   # Affiche le premier élément

# On recalcule la distance de Manhattan entre les points extrêmes dans ce nouvel ordre
tmp2 = abs(ans[-1][0] - ans[0][0]) + abs(ans[-1][1] - ans[0][1])

# Enfin, on affiche le maximum des deux distances calculées.
print(max(tmp, tmp2))  # max() retourne le plus grand des deux arguments.