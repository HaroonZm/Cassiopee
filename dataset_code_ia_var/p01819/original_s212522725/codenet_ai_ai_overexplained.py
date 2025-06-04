# Importation de plusieurs modules standards, qui fournissent diverses fonctionnalités
import math          # Fournit des fonctions mathématiques (racine carrée, sinus, cosinus, etc.)
import string        # Accès à l'ensemble des caractères alphabétiques et utilitaires associés
import itertools     # Outils pour la manipulation efficace d'itérateurs (combinatoire, produits cartésiens, etc.)
import fractions     # Pour travailler avec des fractions rationnelles (i.e., 1/3, 5/7, etc.)
import heapq         # Module pour travailler avec des files à priorité (tas binaire/min-heap)
import collections   # Fournit des types conteneurs spécialisés (deque, Counter, etc.)
import re            # Pour faire des recherches, extractions, et substitutions par expressions régulières
import array         # Offre un type de tableau performant de valeurs de base
import bisect        # Pour chercher ou insérer efficacement dans des listes triées
import sys           # Accès à des variables et fonctions propres à l'interpréteur Python (stdin, sortie, gestion de récursion, etc.)
import random        # Génère des nombres pseudo-aléatoires et effectue des choix aléatoires
import time          # Gérer le temps, mesurer des durées ou attendre des secondes
import copy          # Fournit les fonctions pour copier des objets (shallow et deep copy)
import functools     # Fournit des outils pour la programmation fonctionnelle (partiel, réduction, cache, etc.)

# Définit la limite maximale de récursion pour éviter les erreurs de récursion profonde
sys.setrecursionlimit(10**7)    # Place la limite de récursion à 10 millions pour permettre de la récursion profonde sans erreurs

# Déclare quelques constantes utilisées dans le code
inf = 10**20                    # Définit une "valeur d'infini" très grande pour l'initialisation
eps = 1.0 / 10**10              # Définit une petite valeur epsilon pour la comparaison de flottants
mod = 998244353                 # Un grand nombre premier, souvent utilisé comme modulo dans les problèmes compétitifs

# Déclarations de coordonnées directionnelles utilisées pour le déplacement 
dd = [(0, -1), (1, 0), (0, 1), (-1, 0)]                               # Déplacements orthogonaux (gauche, bas, droite, haut)
ddn = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]  # Déplacements dans les 8 directions possibles

# Définitions de fonctions utilitaires pour lecture d'entrée et autres opérations courantes :
def LI():
    # Lit une ligne depuis l'entrée standard, la découpe via split() (donc par espace par défaut), 
    # convertit chaque élément en entier, et retourne la liste de ces entiers.
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    # Comme la fonction précédente, mais décrémente chaque entier lu de 1 (pour indexation 0-based)
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    # Lit une ligne de l'entrée standard, découpe la ligne en éléments séparés par des espaces,
    # convertit chaque élément en flottant, et retourne la liste de ces flottants.
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    # Lit une ligne, puis découpe la ligne en mots (séparés par espace) et retourne la liste des mots.
    return sys.stdin.readline().split()

def I():
    # Lit une ligne de l'entrée standard, la convertit en entier et le retourne
    return int(sys.stdin.readline())

def F():
    # Lit une ligne de l'entrée standard, la convertit en float et la retourne
    return float(sys.stdin.readline())

def S():
    # Lit une ligne de l'entrée standard via la fonction input() (qui lit jusqu'au prochain saut de ligne)
    # et retourne la chaîne saisie.
    return input()

def pf(s):
    # Affiche la valeur de s en la forçant à être imprimée immédiatement grâce à flush=True,
    # ce qui est utile dans des contextes interactifs ou compétitifs.
    return print(s, flush=True)

# --- Début de la fonction principale ---
def main():
    # Lecture des deux entiers n et m, qui représentent probablement la largeur et la hauteur d'une grille
    n, m = LI()
    
    # On crée une liste (a) de m chaînes de caractères, chaque chaîne étant lue via S() (input()),
    # ce qui représente probablement les lignes ou colonnes d'une grille.
    a = [S() for _ in range(m)]
    
    # On crée deux tableaux b et c de longueur n+1 remplis de zéros.
    # b: stockera probablement le nombre de caractères "W" ("white" ?) dans chaque colonne/ligne
    # c: stockera probablement le nombre d'autres caractères dans chaque colonne/ligne
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    
    # Double boucle imbriquée pour parcourir chaque élément de la grille
    for i in range(n):             # Parcourt les indices de 0 à n-1 (colonnes ou lignes)
        for j in range(m):         # Parcourt de 0 à m-1 (lignes ou colonnes)
            # Si le caractère à la position (j, i) de la grille vaut 'W'
            if a[j][i] == 'W':
                # Incrémente le compteur b à la position i (compte les 'W')
                b[i] += 1
            else:
                # Sinon, incrémente le compteur c à la position i (compte les autres)
                c[i] += 1
    
    # On crée un préfixe cumulé sur le tableau c. Pour chaque i de 0 à n-1,
    # c[i+1] prend la valeur de c[i+1] + c[i] (nombre cumulé des non-'W')
    for i in range(n):
        c[i + 1] += c[i]
    
    # On fait un suffixe cumulé sur b, mais dans l'autre sens (de n-2 vers 0).
    # Pour chaque i, b[i] prend la valeur b[i] + b[i+1] (nombre cumulé des 'W' à/droite de i)
    for i in range(n - 2, -1, -1):
        b[i] += b[i + 1]
    
    # La variable m est initialisée à b[0], c'est-à-dire le total des 'W' à partir de la première colonne/ligne
    m = b[0]
    r = 0 # Cette variable retiendra probablement le meilleur index, selon un certain critère d'optimisation
    
    # On parcourt chaque colonne/ligne pour trouver un seuil optimal
    for i in range(n):
        # Calcule une "somme de coût" temporaire : 
        # b[i+1] : total des 'W' à droite du point i (exclu)
        # c[i]   : nombre cumulé des non-'W' à gauche du point i (inclus)
        tm = b[i + 1] + c[i]
        # Si la valeur minimale m est supérieure à la valeur temporaire tm, on met à jour le meilleur seuil
        if m > tm:
            r = i + 1  # r reçoit l'index suivant, car on a trouvé une valeur meilleure
            m = tm     # m est mis à jour avec la nouvelle valeur plus petite
    
    # Retourne la solution recherchée, sous forme d'une chaîne avec deux entiers séparés par un espace
    # r et r+1 représentent probablement l'indice de coupure optimal et le suivant
    return '{} {}'.format(r, r + 1)

# Appelle la fonction main() et affiche ce que retourne main()
print(main())