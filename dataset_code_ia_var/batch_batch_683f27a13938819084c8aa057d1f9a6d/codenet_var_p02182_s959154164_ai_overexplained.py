#!usr/bin/env python3

# Importation des modules nécessaires
from collections import defaultdict, deque  # defaultdict pour les dictionnaires avec valeur par défaut, deque pour les files efficaces
from heapq import heappush, heappop         # heappush et heappop pour gérer des files de priorité (tas/min-heap)
import sys                                  # Module système pour gérer les entrées/sorties, etc.
import math                                 # Module pour les fonctions mathématiques courantes (pas utilisé ici)
import bisect                               # Module pour la recherche dans des listes triées (pas utilisé ici)
import random                               # Module pour la génération de nombres aléatoires (pas utilisé ici)

# Fonction pour lire une ligne de l'entrée standard, la découper par espaces et convertir chaque morceau en entier
def LI():
    # sys.stdin.readline() lit une ligne de texte sur l'entrée standard (console ou fichier redirigé)
    # .split() divise la ligne en sous-chaînes en utilisant les espaces (par défaut)
    # [int(x) for x in ...] convertit chaque élément en entier
    return [int(x) for x in sys.stdin.readline().split()]

# Fonction pour lire une seule ligne et la convertir en entier
def I():
    # sys.stdin.readline() lit une ligne, int() la convertit en entier
    return int(sys.stdin.readline())

# Fonction pour lire une ligne de chaîne(s) de caractères, divisée selon les espaces, chaque chaîne convertie en liste de caractères
def LS():
    # sys.stdin.readline().split() divise la ligne selon les espaces
    # [list(x) for x in ...] transforme chaque élément x en une liste de ses caractères
    return [list(x) for x in sys.stdin.readline().split()]

# Fonction pour lire une ligne sous forme de liste de caractères, supprimant un éventuel retour à la ligne
def S():
    # sys.stdin.readline() lit la ligne comme une chaîne
    res = list(sys.stdin.readline())
    # la dernière position contient "\n" ? On l'enlève alors
    if res[-1] == "\n":
        return res[:-1]
    return res

# Fonction pour lire n entiers, chaque entier sur une ligne différente
def IR(n):
    # Pour chaque i dans range(n) (de 0 à n-1), appeler I() pour lire un entier
    return [I() for i in range(n)]

# Fonction pour lire n lignes de plusieurs entiers, chaque ligne transformée en liste d'entiers
def LIR(n):
    # Pour chaque i, appeler LI() pour lire une liste d'entiers sur une ligne
    return [LI() for i in range(n)]

# Fonction pour lire n lignes, chacune convertie en liste de caractères (avec S())
def SR(n):
    # Pour chaque i, appliquer S() pour obtenir la ligne en liste de caractères
    return [S() for i in range(n)]

# Fonction pour lire n lignes, chaque ligne traitée par LS()
def LSR(n):
    # Pour chaque i, appliquer LS() pour obtenir la ligne sous forme de liste de listes de caractères
    return [LS() for i in range(n)]

# Changer la limite de récursion pour autoriser une profondeur plus grande de récursion (utile dans certains algorithmes)
sys.setrecursionlimit(1000000)  # Définit la limite à un million

# Définition d'une constante pour la valeur du module (très courante pour les problèmes de calculs avec très grands nombres)
mod = 1000000007

# Définition de la fonction principale de résolution du problème
def solve():
    # Lecture de deux entiers N et M sur une même ligne
    N, M = LI()  # N et M représentent probablement le nombre de lignes et de colonnes d'une matrice
    
    # Lecture de N lignes, chaque ligne étant stockée comme liste de caractères (SR retourne une liste de listes)
    # Cela signifie que A est une liste de N sous-listes (une par ligne)
    A = SR(N)
    # Idem pour B, une autre matrice/list de N lignes (de caractères)
    B = SR(N)
    
    # Initialisation du compteur de différences à 0
    ans = 0
    
    # Boucle sur toutes les lignes (i de 0 à N-1)
    for i in range(N):
        # Boucle sur toutes les colonnes (j de 0 à M-1)
        for j in range(M):
            # Si la lettre/caractère dans la matrice A à la position (i,j) est différente de celle dans B à la même position
            if A[i][j] != B[i][j]:
                # On incrémente le compteur, car il y a une différence à cette position
                ans += 1
    # Affiche le nombre total de différences trouvées
    print(ans)
    return

# Bloc qui vérifie si ce fichier est exécuté comme programme principal
if __name__ == "__main__":
    # Appel de la fonction solve pour exécuter la logique principale
    solve()