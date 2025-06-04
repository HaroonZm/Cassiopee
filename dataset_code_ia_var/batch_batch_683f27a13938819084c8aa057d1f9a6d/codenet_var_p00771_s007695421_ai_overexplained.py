# Importation de nombreux modules standards de la bibliothèque Python.
# Ces modules fournissent diverses fonctionnalités, souvent utilisées dans de nombreux programmes.
import math         # Pour les fonctions mathématiques comme sqrt, sin, cos etc.
import string       # Pour les opérations de manipulation de chaînes de caractères.
import itertools    # Pour les fonctions qui créent et utilisent des itérateurs (ex: permutations, combinations).
import fractions    # Pour les nombres rationnels (fractions).
import heapq        # Pour la manipulation de tas/queues de priorité.
import collections  # Pour des structures de données alternatives (deque, Counter, etc).
import re           # Pour les expressions régulières (pattern matching sur les chaînes).
import array        # Pour des tableaux de haute performance c-typed.
import bisect       # Pour les recherches et insertions dans des listes triées.
import sys          # Pour l'accès à des variables ou fonctions système, ici pour la lecture stdin et d'autres fonctions système.
import random       # Pour générer des nombres aléatoires.
import time         # Pour gérer le temps, mesurer des intervalles, etc.
import copy         # Pour réaliser des copies superficielles et profondes d'objets.
import functools    # Pour des outils de programmation fonctionnelle.

# Définit la profondeur maximale de récursion autorisée. Utile pour éviter le dépassement si les fonctions récursives sont appelées sur de grandes profondeurs.
sys.setrecursionlimit(10**7)

# Définit une constante 'inf' représentant un "très grand nombre", utilisé comme valeur d'infini.
inf = 10**20

# Définit une petite valeur epsilon, utilisée pour la comparaison de flottants, pour lutter contre les imprécisions d'arrondi.
eps = 1.0 / 10**13

# Définit un modulo utilisé fréquemment dans les problèmes d'arithmétique modulaire.
mod = 10**9+7

# Définit dd comme une liste de 4 tuples, représentant les 4 directions cardinales (haut, droite, bas, gauche) dans une grille (utilisées dans les parcours sur une grille 2D).
dd = [(-1,0),(0,1),(1,0),(0,-1)]

# Définit ddn comme les 8 directions (cardinales + diagonales) sur une grille.
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Fonction utilitaire pour lire une ligne de l'entrée standard, couper par défaut par les espaces, convertir chaque morceau en entier, puis retourner la liste des entiers.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Identique à la précédente, mais décrémente chaque entier lu (utile pour passer de 1-indexé à 0-indexé).
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Même chose, mais pour les flottants.
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Lit une ligne, sépare les éléments et retourne les chaînes, utile pour lire une liste de chaînes.
def LS():
    return sys.stdin.readline().split()

# Lit une ligne de l'entrée standard, la convertit en entier et retourne ce nombre.
def I():
    return int(sys.stdin.readline())

# Pareil, mais convertit en flottant.
def F():
    return float(sys.stdin.readline())

# Lit toute une ligne de l'entrée standard (attention, garde souvent le '\n' final!).
def S():
    return input()

# Fonction raccourcie permettant d'afficher une valeur et de forcer le flush (vidage) du tampon de sortie immédiatement.
def pf(s):
    return print(s, flush=True)

# Redéfinit une petite valeur epsilon pour la convergence des calculs en virgule flottante.
eps = 1e-7

# Fonction pour effectuer une recherche par interpolation (dite "ternaire" ou "ternary search") sur les réels.
# f: la fonction à optimiser (min ou max)
# mi: borne inférieure de recherche
# ma: borne supérieure de recherche
def bs(f, mi, ma):
    mm = -1  # Initialisation possible mais 'mm' n'est pas utilisé dans le reste du code
    # Continue tant que la distance entre les bornes est supérieure à epsilon, garantissant une précision suffisante
    while ma > mi + eps:
        # Division de l'intervalle en 3 parties égales
        m1 = (mi*2+ma) / 3.0  # Premier point à 1/3 de l'intervalle
        m2 = (mi+ma*2) / 3.0  # Deuxième point à 2/3 de l'intervalle
        # Évalue la fonction aux deux points
        r1 = f(m1)
        r2 = f(m2)
        # Selon que r1 < r2 (optimisation), ajuste les bornes mi et ma
        if r1 < r2:
            mi = m1  # Si r1 est plus petit, on cherche du côté droit
        else:
            ma = m2  # Sinon, on cherche à gauche
    # Retourne la valeur optimale, évaluée au milieu du dernier intervalle réduit
    return f((ma+mi)/2.0)

# Début du corps principal du programme sous forme de fonction
def main():
    # Initialise une liste vide pour stocker les résultats de chaque cas de test
    rr = []

    # Définition de la fonction principale de traitement pour un cas de test donné, avec n entrées
    def f(n):
        # Lit n lignes de la saisie standard, chaque ligne étant une liste de 3 entiers (par exemple px, py, l)
        a = [LI() for _ in range(n)]

        # Fonction auxiliaire _f qui calcule, pour des coordonnées (x, y), la plus petite différence entre l^2 et la distance euclidienne carrée à chaque point du tableau
        def _f(x, y):
            # Initialise le résultat à "infini" (très grand nombre)
            r = inf
            # Parcourt chaque point (px, py) et l associé dans la liste 'a'
            for px, py, l in a:
                # Calcule pour chaque point la valeur suivante: l^2 - (distance euclidienne au carré entre (x, y) et (px, py))
                r = min(r, l ** 2 - (x - px) ** 2 - (y - py) ** 2)
            # Retourne la valeur minimale obtenue après avoir examiné tous les points
            return r

        # Fonction intermédiaire servant à fixer la valeur y et à maximiser/minimiser selon x, en effectuant une recherche binaire (ternaire)
        def _fy(y):
            # Fonction intermédiaire qui ne prend qu'un seul argument x et transmet x, y à _f
            def _ff(x):
                return _f(x, y)
            # Recherche par interpolation sur x (de -100 à 100) pour la valeur optimale avec y fixé
            return bs(_ff, -100, 100)

        # Recherche par interpolation sur y (de -100 à 100), pour maximiser/minimiser sur y avec x optimal pour chaque y fixé
        r = bs(_fy, -100, 100)

        # Formate la valeur obtenue (r), transforme r en racine carrée (puisque r représente un carré), et formate le résultat à 7 chiffres après la virgule comme chaîne de caractères
        return "{:0.7f}".format(r ** 0.5)

    # Boucle d'exécution principale, lit les données jusqu'à rencontrer la valeur 0
    while 1:
        # Lit un entier représentant le nombre de points à traiter pour le cas de test courant
        n = I()
        # Si la valeur lue est 0, cela signifie la fin de la saisie, on quitte la boucle
        if n == 0:
            break
        # Sinon, appelle la fonction f(n) pour résoudre le cas présent, ajoute le résultat à la liste rr
        rr.append(f(n))

    # À la fin, joint tous les résultats séparés par une nouvelle ligne et retourne la chaîne finale
    return '\n'.join(map(str, rr))

# Point d'entrée du script. Appelle main() et affiche son résultat à la sortie standard.
print(main())