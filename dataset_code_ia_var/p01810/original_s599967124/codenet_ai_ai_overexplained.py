import math  # Module pour les fonctions mathématiques de base (par exemple racine carrée, sinus, etc.)
import string  # Module pour les opérations relatives aux chaînes de caractères (par ex. alphabet, chiffres, etc.)
import itertools  # Module contenant des outils permettant de manipuler des itérateurs, notamment pour les combinaisons, permutations...
import fractions  # Module pour gérer les nombres rationnels, c'est-à-dire fractions (peu utilisé)
import heapq  # Module pour les files de priorité (tas ou "heap" en anglais)
import collections  # Module fournissant des structures de données alternatives (deque, Counter, etc.)
import re  # Module pour les expressions régulières (pattern matching avancé dans les chaînes de caractères)
import array  # Module pour les tableaux efficaces en mémoire (similaires aux listes mais typés)
import bisect  # Module pour effectuer des recherches et insertions binaires dans des listes triées
import sys  # Module système pour interagir avec l’interpréteur Python et le flux d'entrée/sortie
import random  # Module pour générer des nombres aléatoires ou utiliser d’autres fonctions de hasard
import time  # Module pour gérer le temps et les minuteries
import copy  # Module pour effectuer des copies (profondes ou peu profondes) d’objets Python
import functools  # Module fournissant des fonctions utilitaires pour la programmation fonctionnelle (comme reduce, lru_cache, etc.)

# Augmente la limite maximale de récursion du programme.
# Par défaut, un programme Python ne peut pas effectuer une profondeur de récursion trop élevée sous peine d’erreur.
# On augmente donc cette limite à 10^7 pour éviter ces erreurs lors d’appels récursifs profonds.
sys.setrecursionlimit(10**7)

# Initialise une variable appelée 'inf', représentant une valeur très grande pouvant servir de «infini».
# Elle vaut 10 puissance 20.
inf = 10**20

# Initialise une variable 'eps', qui représente une valeur très petite, utilisée pour des comparaisons avec des flottants.
# Ici, eps est défini comme 1 divisé par 10 puissance 10, soit 1e-10.
eps = 1.0 / 10**10

# Initialise le modulo 'mod', couramment utilisé pour limiter la valeur des entiers afin d’éviter le dépassement de capacité.
# C’est ici un nombre premier assez grand, souvent rencontré dans les problèmes de programmation compétitive.
mod = 10**9+7

# Liste nommée 'dd' des déplacements adjacents dans une grille à quatre directions (haut, droite, bas, gauche).
# Chaque tuple représente une variation sur les coordonnées (dx, dy) d’une cellule.
# Par exemple, (0,-1) signifie "vers le haut".
dd = [(0,-1), (1,0), (0,1), (-1,0)]

# Liste 'ddn' des déplacements dans une grille à huit directions (tous les voisins, diagonales comprises).
# Cela inclut les 4 directions cardinales et les 4 diagonales.
ddn = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,-1), (-1,0), (-1,1)]

# Définition d’une fonction utilitaire LI (List Input) :
# Lit une ligne depuis l'entrée standard (clavier, ou fichier redirigé),
# divise la chaîne obtenue à chaque espace en éléments,
# convertit ces éléments en entiers,
# et retourne le tout comme une liste d’entiers.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Définition de la fonction utilitaire LI_ (List Input with Decrement):
# Fait la même chose que LI(), mais diminue chaque entier lu par 1.
# Cela est utilisé lorsque les indices dans les données d’entrée commencent à 1,
# mais doivent être manipulés comme des indices commençant à 0 dans le code.
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Fonction utilitaire LF (List Float):
# Lit une ligne de l'entrée standard, la découpe en morceaux,
# convertit chaque morceau en flottant,
# retourne une liste de ces flottants.
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Fonction utilitaire LS (List String):
# Lit une ligne de l’entrée standard et la découpe en une liste de chaînes,
# en gardant chaque mot (élément entre espaces) comme un élément de la liste de chaînes de caractères.
def LS():
    return sys.stdin.readline().split()

# Fonction utilitaire I (Input Int):
# Lit une ligne complète sur l’entrée standard,
# convertit cette ligne en un entier,
# et le retourne.
def I():
    return int(sys.stdin.readline())

# Fonction utilitaire F (Input Float):
# Pareil que 'I', mais convertit la ligne en flottant.
def F():
    return float(sys.stdin.readline())

# Fonction utilitaire S (String Input):
# Lit une ligne depuis l’entrée standard à l'aide de la fonction 'input'.
# Renvoie la chaîne de caractères saisie.
def S():
    return input()

# Fonction utilitaire pf (print flush):
# Affiche une chaîne ou valeur 's' sur la sortie standard (écran).
# Utilise flush=True pour forcer l’affichage immédiat, ce qui peut être utile en contexte interactif ou compétitif.
def pf(s):
    return print(s, flush=True)

# Définition de la fonction principale du programme (point de départ)
def main():
    # Lis deux entiers sur une seule ligne depuis l’entrée standard et les place dans n et k.
    n, k = LI()

    # Déclare une variable entière 't' initialisée à 0.
    t = 0

    # Cette boucle for s’exécute exactement (n-1) fois.
    # À chaque itération, on met à jour la valeur de t en réalisant une opération :
    # On multiplie la valeur courante de t par k, on divise le résultat (division entière) par (k-1),
    # puis on ajoute 1 au résultat.
    # Cette opération est probablement liée à une formule récurrente ou à un process itératif à base de lots.
    for _ in range(n-1):  # _ signifie que la variable d’itération n’est pas utilisée.
        t = t * k // (k-1) + 1

    # Lorsque la boucle est terminée, on renvoie la valeur finale atteinte par t.
    return t

# Ceci exécute la fonction main, affiche la valeur qu’elle retourne.
# La valeur de retour de main() correspond à la solution attendue selon la logique du problème traité.
print(main())