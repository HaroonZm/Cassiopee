import math     # Importe le module math, qui fournit des fonctions mathématiques standard
import string   # Importe le module string, utile pour manipuler des chaînes et constantes de caractères
import itertools # Importe le module itertools, pour créer des itérateurs combinatoires
import fractions # Importe le module fractions, pour effectuer des calculs sur des fractions rationnelles
import heapq     # Importe le module heapq, qui fournit une implémentation de file de priorité (heap)
import collections # Importe le module collections, pour des structures de données avancées comme deque ou Counter
import re         # Importe le module re, qui permet de manipuler des expressions régulières
import array      # Importe le module array, pour manipuler des tableaux efficaces de type numérique
import bisect     # Importe le module bisect, pour l’insertion dans des listes triées
import sys        # Importe le module sys, qui fournit l’accès à des variables et fonctions système
import copy       # Importe le module copy, pour faire des copies superficielles ou profondes d’objets
import functools  # Importe le module functools, pour fonctions utilitaires sur d’autres fonctions

# On pourrait également importer d'autres modules comme time, random, resource (commentés ici)

# Définit la profondeur maximale de récursion ; en Python par défaut c'est 1000, ici élevé pour des appels récursifs profonds
sys.setrecursionlimit(10**7)

# La variable 'inf' représente une valeur numérique très grande que l'on utilisera comme un infini
inf = 10**20

# La variable 'eps' représente une très petite valeur (epsilon), utile pour comparer des nombres à virgule flottante
eps = 1.0 / 10**10

# 'mod' est un grand nombre premier servant typiquement de module pour les opérations en arithmétique modulaire
mod = 10**9 + 7

# 'mod2' est une autre valeur de module populaire dans les concours de programmation
mod2 = 998244353

# 'dd' représente les 4 directions cardinales en coordonnées (haut, droite, bas, gauche)
dd = [(-1,0), (0,1), (1,0), (0,-1)]

# 'ddn' décrit les 8 directions d'un quadrillage (y compris les diagonales, donc N, NE, E, SE, S, SO, O, NO)
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

# Définition de fonctions utilitaires pour simplifier la lecture des entrées :

def LI():
    # Lis une ligne depuis l'entrée standard, supprime l'espace de fin, sépare en morceaux puis convertit chaque morceau en entier
    return list(map(int, sys.stdin.readline().split()))

def LLI():
    # Lis toutes les lignes de l’entrée standard, puis pour chaque ligne,
    # sépare en entiers, convertit chaque ligne en liste d’entiers
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]

def LI_():
    # Lis une ligne depuis l'entrée standard, sépare en entiers,
    # puis retire 1 à chaque entier (utile pour convertir des indices 1-based en 0-based)
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    # Lis une ligne, sépare les morceaux et les convertit en flottants
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    # Lis une ligne et la sépare en chaînes (morceaux séparés par espace)
    return sys.stdin.readline().split()

def I():
    # Lis une ligne, enlève les espaces, puis convertit en entier
    return int(sys.stdin.readline())

def F():
    # Lis une ligne, enlève les espaces, puis convertit en nombre flottant
    return float(sys.stdin.readline())

def S():
    # Utilise la fonction input() pour lire une ligne depuis l'entrée standard comme chaîne de caractères
    # (différent de sys.stdin.readline pour permettre une compatibilité accrue)
    return input()

def pf(s):
    # Affiche la variable s sur la sortie standard puis force l’affichage immédiat
    return print(s, flush=True)

def pe(s):
    # Affiche la variable s (convertie en chaîne) sur la sortie d'erreur standard (stderr)
    return print(str(s), file=sys.stderr)

def JA(a, sep):
    # Prend une liste a et la convertit en une seule chaîne, avec les éléments séparés par la chaîne sep
    # Conversion de chaque élément en chaîne si besoin
    return sep.join(map(str, a))

def JAA(a, s, t):
    # Prend une liste de listes a, convertit chaque sous-liste en chaîne avec séparateur t,
    # puis joint toutes ces chaînes avec séparateur s
    return s.join(t.join(map(str, b)) for b in a)

def IF(c, t, f):
    # Simule une expression ternaire : si la condition c est vraie, retourne t, sinon retourne f
    return t if c else f

# Fonction floor_sum, qui calcule la somme des valeurs entières de (a*i + b) // m pour i de 0 à n-1
def floor_sum(n, m, a, b):
    # Initialise la variable de réponse à 0
    ans = 0

    # Si a est supérieur ou égal à m, on simplifie en utilisant la propriété distributive de la division entière
    if a >= m:
        # Calcule la contribution de a // m au total pour tous les i, c’est-à-dire
        # chaque i contribue d'autant d'entiers division par m
        ans += (n - 1) * n * (a // m) // 2
        # Garde uniquement le reste de a modulo m pour la suite du calcul
        a %= m

    # Si b est supérieur ou égal à m, on peut aussi pré-calculer sa contribution
    if b >= m:
        # Chaque i contribue b // m à la somme totale
        ans += n * (b // m)
        # Garde uniquement le reste de b modulo m pour la suite
        b %= m

    # Calcule le plus grand entier y tel que (a * n + b) // m = y_max
    y_max = (a * n + b) // m
    # Calcule la valeur de x où l’expression atteint la borne supérieure
    x_max = (y_max * m - b)

    # Si le maximum de y vaut 0, il n’y a plus rien à ajouter
    if y_max == 0:
        return ans # Retourne directement la réponse accumulée

    # Ajoute la partie qui peut être calculée directement
    ans += (n - (x_max + a - 1) // a) * y_max
    # Appel récursif avec de nouveaux paramètres ajustés
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return ans

# Fonction principale du programme
def main():
    # Lit un entier t, qui représente le nombre de cas ou de requêtes
    t = I()

    # Pour chaque requête, on lit une liste d'entiers (chaque ligne entrée contient n, m, a, b)
    qa = [LI() for _ in range(t)]

    # Initialise une liste vide pour stocker les résultats
    r = []
    # Pour chaque jeu d’arguments n, m, a, b dans chaque requête
    for n, m, a, b in qa:
        # On appelle la fonction floor_sum et on stocke le résultat dans la liste r
        r.append(floor_sum(n, m, a, b))

    # Retourne l'ensemble des résultats, converti en une seule chaîne de caractères avec chaque résultat sur une ligne
    return JA(r, "\n")

# Appelle la fonction main et affiche son résultat sur la sortie standard
print(main())