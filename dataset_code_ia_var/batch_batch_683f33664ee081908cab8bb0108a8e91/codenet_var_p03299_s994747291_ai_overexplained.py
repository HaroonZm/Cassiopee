# Importation de modules standards et utilitaires externes
# Ces modules fournissent des structures de données et fonctions utiles pour divers besoins.

from collections import defaultdict, deque, Counter # defaultdict, deque (file double extrémité), Counter pour compter
from heapq import heappush, heappop, heapify       # file de priorité/min-heap : ajout, extraction, transformation liste/propriété heap
import math                                        # bibliothèque mathématique, racines, puissances, etc.
import bisect                                      # insertion, recherche binaire sur listes triées
import random                                      # générateur aléatoire divers
from itertools import permutations, accumulate, combinations, product # outils itératifs : permutations, cumuls, combinaisons, produit cartésien
import sys                                         # accès stdin, stdout, et autres fonctionnalités système
import string                                      # constantes chaînes de caractères, etc.
from bisect import bisect_left, bisect_right       # fonctions bisect spécialisées (recherche position d'insertion à gauche/droite)
from math import factorial, ceil, floor            # factorielle, plafond, plancher d'un flottant
from operator import mul                           # opérateur multiplication
from functools import reduce                       # appliquer une fonction cumulativement à une séquence

# Définir la limite maximale de récursion à un très grand nombre pour éviter les erreurs de récursion profonde
sys.setrecursionlimit(2147483647)

# Déclaration d'une très grande constante pour représenter l'infini (valeur plus grande que toutes les valeurs de données typiques)
INF = 10 ** 13

# Définitions de fonctions utilitaires pour lire l'entrée rapidement et de différentes manières

# LI : Lit une ligne d'entrée standard, la découpe en parties séparées par espace, convertit chaque partie en entier et renvoie une liste d'entiers
def LI(): return list(map(int, sys.stdin.readline().split()))

# I : Lit une ligne entière, la convertit en entier et la renvoie
def I(): return int(sys.stdin.readline())

# LS : Lit une ligne (buffer) jusqu'à la nouvelle ligne, enlève le saut de ligne et la décode (utf-8), puis la découpe sur les espaces
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()

# S : Lit une ligne (buffer) et la renvoie comme chaîne (sans découpage)
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')

# IR(n) : Lit n lignes de l'entrée standard, chaque ligne convertie en entier, retourne la liste résultante
def IR(n): return [I() for i in range(n)]

# LIR(n) : Lit n lignes de l'entrée standard, chaque ligne découpée en entiers (liste d'entiers pour chaque ligne)
def LIR(n): return [LI() for i in range(n)]

# SR(n) : Lit n lignes (buffer) en chaînes décodées, chacune renvoyée sans découpage/retraitement
def SR(n): return [S() for i in range(n)]

# LSR(n) : Pour n lignes, lit chaque ligne, la décode et la découpe sur les espaces, retourne une liste de listes de chaînes
def LSR(n): return [LS() for i in range(n)]

# SRL(n) : Pour n lignes, lit chaque ligne et retourne une liste de caractères (chaîne vers liste de caractères)
def SRL(n): return [list(S()) for i in range(n)]

# MSRL(n) : Pour n lignes, lit chaque ligne, convertit chaque caractère de la ligne en entier et retourne la liste de résultats
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]

# mod : une grande constante première pour effectuer des opérations modulo (très utilisée dans les problèmes de combinatoire/modularité)
mod = 10 ** 9 + 7

# Lecture du nombre d'éléments à traiter depuis l'entrée (en général, cela correspondra à la taille d'une séquence ou d'une structure de données)
n = I()

# Lecture d'une liste d'entiers H venant de l'entrée. Puis on ajoute 1 à la fin de cette liste pour fonctionner sur n+1 éléments (probablement une sentinelle)
H = LI() + [1]

# Initialisation du tableau dp (programmation dynamique)
# dp : liste de n+1 éléments, chacun initialisé à 1.
# Ce tableau stocke à chaque indice l'état courant des sous-résultats dynamiques pour l'itération actuelle.
dp = [1] * (n + 1)

# Boucle principale de traitement dynamique - pour chaque position k de 0 à n-1 incluse
for k in range(n):
    # Création d'un nouveau tableau new_dp de longueur n+1, initialement rempli de zéros
    # Il servira à calculer les nouveaux états dp basés sur les états précédents.
    new_dp = [0] * (n + 1)
    # On parcourt chaque indice i de 0 à n inclus (soit n+1 au total)
    for i in range(n + 1):
        # PREMIER CAS: si la valeur H[i] est strictement supérieure à H[k]
        if H[i] > H[k]:
            # On multiplie l'état courant dp[k] par 2 et affecte le résultat à new_dp[i]
            # Cela correspond à un doublement du nombre de façons/scénarios compatibles à cet état.
            new_dp[i] = dp[k] * 2
        # DEUXIEME CAS: sinon, si la valeur précédente H[k-1] (à gauche) est inférieure ou égale à H[i]
        elif H[k - 1] <= H[i]:
            # On multiplie l'état courant dp[i] par 2, puis par 2 à la puissance (H[k] - H[i]),
            # le tout modulo la constante mod (pour éviter les débordements)
            new_dp[i] = dp[i] * 2 * pow(2, H[k] - H[i], mod)
        # TROISIEME CAS: sinon, si la valeur précédente H[k-1] est strictement supérieure à la valeur courante H[k]
        elif H[k - 1] > H[k]:
            # On soustrait dp[k] de dp[i], puis on ajoute dp[k] * 2, pour combiner/mélanger différentes transitions possibles
            new_dp[i] = dp[i] - dp[k] + dp[k] * 2
        # QUATRIEME CAS: tous les autres cas (le else attrape tout ce qui n'est pas couvert ci-dessus)
        else:
            # On soustrait dp[k-1] de dp[i], puis on ajoute dp[k-1] * 2. Le tout est multiplié par 2^(H[k] - H[k-1]) modulo mod.
            new_dp[i] = (dp[i] - dp[k - 1] + dp[k - 1] * 2) * pow(2, H[k] - H[k - 1], mod)
        # A chaque itération, on applique le modulo (reste de la division euclidienne) sur la valeur new_dp[i].
        # Cela est crucial pour éviter les dépassements d'entiers et respecter les contraintes du problème.
        new_dp[i] %= mod
    # Après avoir rempli new_dp pour tous les i, on le recopie dans dp pour la prochaine itération k.
    dp = new_dp

# Finalement, on affiche la dernière valeur du tableau dp (dp[-1]), c'est-à-dire la dernière cellule calculée.
# Cela représente typiquement le résultat final combinant toutes les possibilités/scénarios du problème traité.
print(dp[-1])